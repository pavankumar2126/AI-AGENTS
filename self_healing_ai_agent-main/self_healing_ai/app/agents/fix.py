from app.llm.gemini import call_gemini
from app.utils.logger import log


def fix_agent(state):
    log("Fix Agent Running")

    prompt = f"""
    Fix this code issue.

    Problem:
    {state['analysis']}

    Current Code:
    {state['output']}

    Rules:
    - Return ONLY corrected function
    - No explanation
    - No comments
    - No examples
    """

    state["output"] = call_gemini(prompt)

    state["iterations"] += 1

    # 🔥 TIMELINE
    state["history"].append("🔄 Fix Agent Retrying")

    return state