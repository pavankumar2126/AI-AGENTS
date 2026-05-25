from app.llm.gemini import call_gemini
from app.utils.logger import log
from app.utils.cleaner import clean_output


# =====================================================
# EXECUTION AGENT
# =====================================================

def execution_agent(state):

    log("Execution Agent Running")

    prompt = f"""
You are an expert Python engineer.

TASK:
{state['task']}

ERROR LOGS:
{state['logs']}

ANALYSIS:
{state['analysis']}

STRICT RULES:
1. Return ONLY executable Python code
2. NO explanations
3. NO markdown
4. NO comments
5. NO examples
6. Output must contain exactly ONE function
7. Keep code concise and clean

Generate final corrected Python code.
"""

    # =====================================================
    # LLM RESPONSE
    # =====================================================

    response = call_gemini(prompt)

    # =====================================================
    # CLEAN OUTPUT
    # =====================================================

    state["output"] = clean_output(response)

    # =====================================================
    # TIMELINE
    # =====================================================

    state["history"].append(
        "✅ Execution Agent Completed"
    )

    return state