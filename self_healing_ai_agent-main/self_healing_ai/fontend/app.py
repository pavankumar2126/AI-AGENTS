import streamlit as st
import requests


# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Self-Healing AI",
    page_icon="🧠",
    layout="wide"
)


# =====================================================
# TITLE
# =====================================================

st.title("🧠 Self-Healing AI Agent System")

st.write(
    "AI-powered multi-agent workflow using LangGraph + FastAPI + Streamlit"
)


# =====================================================
# INPUT SECTION
# =====================================================

task = st.text_area(
    "📌 Enter Task",
    placeholder="Example: Write a Python function to divide two numbers safely"
)

logs = st.text_area(
    "📋 Enter Logs / Errors",
    placeholder="Example: ZeroDivisionError: division by zero"
)


# =====================================================
# IMAGE UPLOAD
# =====================================================

uploaded_file = st.file_uploader(
    "📷 Upload Error Screenshot",
    type=["png", "jpg", "jpeg"]
)

image_bytes = None

if uploaded_file:

    image_bytes = uploaded_file.read()

    st.image(
        uploaded_file,
        caption="Uploaded Screenshot",
        width="stretch"
    )


# =====================================================
# RUN BUTTON
# =====================================================

if st.button("🚀 Run AI Workflow"):

    # Empty input validation
    if not task or not logs:

        st.warning("⚠️ Please enter both task and logs.")

    else:

        # =====================================================
        # PAYLOAD
        # =====================================================

        payload = {

            "task": task,

            "logs": logs,

            # 🔥 IMAGE SUPPORT
            "image": image_bytes.decode("latin1") if image_bytes else None
        }

        # =====================================================
        # API REQUEST
        # =====================================================

        try:

            response = requests.post(
                "http://127.0.0.1:8000/run",
                json=payload
            )

            result = response.json()

            # =====================================================
            # STATUS
            # =====================================================

            st.subheader("✅ Status")

            st.success(result["status"])

            # =====================================================
            # ANALYSIS
            # =====================================================

            st.subheader("🧠 Analysis")

            st.write(result["analysis"])

            # =====================================================
            # GENERATED OUTPUT
            # =====================================================

            st.subheader("💻 Generated Output")

            st.code(
                result["output"],
                language="python"
            )

            # =====================================================
            # AGENT TIMELINE
            # =====================================================

            st.subheader("🧠 Agent Timeline")

            for step in result["history"]:

                st.write(step)

        # =====================================================
        # CONNECTION ERROR
        # =====================================================

        except Exception as e:

            st.error(
                f"❌ Backend connection failed: {e}"
            )