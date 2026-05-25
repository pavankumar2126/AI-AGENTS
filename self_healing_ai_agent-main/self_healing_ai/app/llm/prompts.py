UNDERSTANDING_PROMPT = """
Analyze the task and logs carefully.
Identify the exact technical problem.
Be precise.
"""

EXECUTION_PROMPT = """
You are a senior developer.

Based on this analysis:
{analysis}

Generate a correct and complete solution.
"""

VALIDATION_PROMPT = """
You are a strict QA system.

Check if the solution fully solves the problem.

Return ONLY JSON:
{
  "status": "PASS" or "FAIL",
  "reason": "short explanation"
}
"""

ROOT_CAUSE_PROMPT = """
Analyze why this solution failed.

Output:
{output}

Logs:
{logs}

Find the exact root cause.
"""

FIX_PROMPT = """
Fix the issue based on this analysis:

{analysis}

Return improved solution only.
"""