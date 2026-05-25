import sqlite3


# =====================================================
# CONNECT DATABASE
# =====================================================

conn = sqlite3.connect(
    "app/database/history.db",
    check_same_thread=False
)

cursor = conn.cursor()


# =====================================================
# CREATE TABLE
# =====================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS workflow_history (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    task TEXT,

    logs TEXT,

    output TEXT,

    status TEXT,

    analysis TEXT,

    iterations INTEGER,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()


# =====================================================
# SAVE WORKFLOW
# =====================================================

def save_workflow(state):

    cursor.execute("""

    INSERT INTO workflow_history (

        task,
        logs,
        output,
        status,
        analysis,
        iterations

    ) VALUES (?, ?, ?, ?, ?, ?)

    """, (

        state["task"],
        state["logs"],
        state["output"],
        state["status"],
        state["analysis"],
        state["iterations"]
    ))

    conn.commit()