import traceback


def execute_code(code: str):

    try:

        # Safe execution scope
        local_scope = {}

        exec(code, {}, local_scope)

        return {
            "success": True,
            "error": None
        }

    except Exception as e:

        return {
            "success": False,
            "error": traceback.format_exc()
        }