# =====================================================
# LANGSMITH TRACING
# =====================================================

import os

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "self-healing-ai"


# =====================================================
# START PROJECT
# =====================================================

print("🚀 STARTING SELF-HEALING AI SYSTEM")


# =====================================================
# IMPORT WORKFLOW
# =====================================================

from app.graph.workflow import build_graph


# =====================================================
# BUILD WORKFLOW
# =====================================================

app = build_graph()


# =====================================================
# RUN WORKFLOW
# =====================================================

result = app.invoke({

    "task": "Write a Python function to divide two numbers safely",

    "logs": "ZeroDivisionError: division by zero",

    "image": None,

    "analysis": "",
    "output": "",
    "status": "",

    "iterations": 0,

    # 🔥 TIMELINE
    "history": []
})


# =====================================================
# FINAL OUTPUT
# =====================================================

print("\n✅ FINAL OUTPUT:\n")

print(result["output"])


# =====================================================
# AGENT TIMELINE
# =====================================================

print("\n🧠 AGENT TIMELINE:\n")

for step in result["history"]:

    print(step)