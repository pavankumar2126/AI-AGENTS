from langgraph.graph import StateGraph, END
from app.graph.state import AgentState

from app.agents.understanding import understanding_agent
from app.agents.execution import execution_agent
from app.agents.validation import validation_agent
from app.agents.fix import fix_agent


def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("understanding", understanding_agent)
    graph.add_node("execution", execution_agent)
    graph.add_node("validation", validation_agent)
    graph.add_node("fix", fix_agent)

    graph.set_entry_point("understanding")

    graph.add_edge("understanding", "execution")
    graph.add_edge("execution", "validation")

    # 🔥 OPTIMIZED ROUTE
    def route(state):
        if state["status"] == "fail" and state["iterations"] < 1:
            return "fix"
        return END

    graph.add_conditional_edges("validation", route)

    graph.add_edge("fix", "execution")

    return graph.compile()