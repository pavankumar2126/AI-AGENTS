from typing import TypedDict, Optional, List


class AgentState(TypedDict):

    # INPUTS
    task: str
    logs: str

    # 🔥 IMAGE SUPPORT
    image: Optional[str] = None

    # WORKFLOW STATE
    analysis: str
    output: str
    status: str

    # RETRY COUNT
    iterations: int

    # TIMELINE
    history: List[str]