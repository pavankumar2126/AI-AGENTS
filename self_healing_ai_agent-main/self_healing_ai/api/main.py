from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

from app.graph.workflow import build_graph


# =====================================================
# FASTAPI APP
# =====================================================

app = FastAPI()


# =====================================================
# BUILD WORKFLOW
# =====================================================

workflow = build_graph()


# =====================================================
# REQUEST MODEL
# =====================================================

class AgentRequest(BaseModel):

    task: str
    logs: str

    # 🔥 OPTIONAL IMAGE
    image: Optional[str] = None


# =====================================================
# HOME ROUTE
# =====================================================

@app.get("/")
def home():

    return {
        "message": "🚀 Self-Healing AI Running"
    }


# =====================================================
# MAIN ROUTE
# =====================================================

@app.post("/run")
def run_agent(request: AgentRequest):

    result = workflow.invoke({

        "task": request.task,

        "logs": request.logs,

        # 🔥 IMAGE SUPPORT
        "image": request.image,

        "analysis": "",
        "output": "",
        "status": "",

        "iterations": 0,

        "history": []
    })

    return {

        "output": result["output"],

        "status": result["status"],

        "analysis": result["analysis"],

        "history": result["history"]
    }