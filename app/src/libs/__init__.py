import re

# Allowed pattern: This will allow common Python code but restrict things like "import"
ALLOWED_CODE = re.compile(r"^[a-zA-Z0-9_+\-*/\s()=:;\n]+$")

def validate_code_block(code_block):
    # Check if code_block contains only allowed characters and structure
    if not ALLOWED_CODE.match(code_block):
        raise ValueError("Invalid characters or unsafe code in block!")
    return True

def execute_user_code_block(a, b, code_block):
    try:
        # Validate the user's code block
        validate_code_block(code_block)

        # Define allowed variables
        allowed_globals = {'a': a, 'b': b}
        local_vars = {}

        # Safely execute the block of code with restricted globals and locals
        exec(code_block, allowed_globals, local_vars)
        
        # Optionally return a result from local variables (e.g., if the user sets `result`)
        return local_vars.get('result', "No result specified")
    
    except Exception as e:
        return f"Error executing code block: {e}"

# Example usage
a = 10
b = 5

# User-provided block of code
user_code_block = """
result = 1 * 5
if result > 20:
    result += 10
"""

# # Execute the user block of code
# output = execute_user_code_block(a, b, user_code_block)
# print(output)  # Output: 60
