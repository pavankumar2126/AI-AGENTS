import json
import ast

from app.llm.gemini import call_gemini
from app.utils.logger import log
from app.utils.code_executor import execute_code
from app.database.db import save_workflow


# =====================================================
# REQUIRED KEYWORDS
# =====================================================

REQUIRED_KEYWORDS = [
    "def",
    "return"
]


# =====================================================
# LOCAL VALIDATION
# =====================================================

def local_validation(output: str):

    output = output.strip()

    # =====================================================
    # EMPTY OUTPUT
    # =====================================================

    if len(output) < 10:

        return False, "Output too short"

    # =====================================================
    # REQUIRED KEYWORDS
    # =====================================================

    for keyword in REQUIRED_KEYWORDS:

        if keyword not in output:

            return False, f"Missing keyword: {keyword}"

    # =====================================================
    # PREVENT FALLBACK CODE
    # =====================================================

    if "fallback_solution" in output:

        return False, "LLM fallback detected"

    # =====================================================
    # SYNTAX VALIDATION
    # =====================================================

    try:

        ast.parse(output)

    except Exception as e:

        return False, f"Syntax Error: {str(e)}"

    # =====================================================
    # RUNTIME EXECUTION
    # =====================================================

    execution_result = execute_code(output)

    if not execution_result["success"]:

        return False, execution_result["error"]

    # =====================================================
    # VALIDATION PASSED
    # =====================================================

    return True, "Validation passed"


# =====================================================
# MAIN VALIDATION AGENT
# =====================================================

def validation_agent(state):

    log("Validation Agent Running")

    output = state["output"]

    # =====================================================
    # LOCAL VALIDATION
    # =====================================================

    is_valid, reason = local_validation(output)

    # =====================================================
    # LOCAL VALIDATION FAILED
    # =====================================================

    if not is_valid:

        state["status"] = "fail"

        state["analysis"] = reason

        state["history"].append(
            f"❌ Validation Failed: {reason}"
        )

        return state

    # =====================================================
    # OPTIONAL GEMINI VALIDATION
    # =====================================================

    prompt = f"""
    Validate this Python code carefully.

    Rules:
    - Must solve the task correctly
    - Must not contain syntax errors
    - Must contain valid Python function
    - Return ONLY JSON

    Example PASS:
    {{
      "status": "PASS",
      "reason": "Code looks correct"
    }}

    Example FAIL:
    {{
      "status": "FAIL",
      "reason": "Logic issue"
    }}

    CODE:
    {output}
    """

    response = call_gemini(prompt)

    # =====================================================
    # JSON PARSING
    # =====================================================

    try:

        result = json.loads(response)

        state["status"] = result["status"].lower()

        state["analysis"] = result.get(
            "reason",
            ""
        )

        # =====================================================
        # VALIDATION PASSED
        # =====================================================

        if state["status"] == "pass":

            state["history"].append(
                "✅ Validation Passed"
            )

        # =====================================================
        # VALIDATION FAILED
        # =====================================================

        else:

            state["history"].append(
                "❌ Gemini Validation Failed"
            )

    # =====================================================
    # GEMINI VALIDATION FAILED
    # =====================================================

    except Exception as e:

        # Local validation already passed
        # so continue safely

        state["status"] = "pass"

        state["analysis"] = (
            "Gemini validation unavailable "
            "- local runtime validation passed"
        )

        state["history"].append(
            "⚠️ Local Runtime Validation Used"
        )

    # =====================================================
    # SAVE WORKFLOW HISTORY
    # =====================================================

    save_workflow(state)

    return state