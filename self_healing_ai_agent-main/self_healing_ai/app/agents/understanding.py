from app.llm.gemini import call_gemini
from app.llm.prompts import UNDERSTANDING_PROMPT
from app.utils.logger import log


def understanding_agent(state):
    log("Understanding Agent Running")

    prompt = f"""
    Analyze the problem carefully.

    Task:
    {state['task']}

    Logs:
    {state['logs']}

    Also analyze the uploaded screenshot if available.
    """

    state["analysis"] = call_gemini(prompt)

    # 🔥 Timeline
    state["history"].append("✅ Understanding Agent Completed")

    return state