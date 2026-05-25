'''from app.llm.gemini import call_gemini
from app.utils.logger import log


def root_cause_agent(state):
    log("Root Cause Agent Running")

    prompt = f"""
    The system says the solution FAILED.

    You MUST find a problem.

    Do NOT say solution is correct.

    Logs:
    {state["logs"]}

    Output:
    {state["output"]}

    Find exact technical issue.
    """

    state["analysis"] = call_gemini(prompt)
    return state'''