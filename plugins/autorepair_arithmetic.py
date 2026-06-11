<think>We need to write a plugin that handles simple arithmetic queries like "Was ist 2+2?" The plugin should be a ROUTER plugin that triggers on such requests. The trigger phrase could be something like "was ist" or "was ist" with numbers and operators. But we need to detect arithmetic expressions. We can use regex to parse simple expressions like "2+2", "3*4", "5-1", "10/2". The plugin should evaluate and return result. Use safe eval or parse manually. Use context["print_fn"] to show progress. Should return string result.

We need to set PLUGIN_NAME, PLUGIN_VERSION, PLUGIN_DESCRIPTION, PLUGIN_AUTHOR, PLUGIN_ENABLED, PLUGIN_TYPE, PLUGIN_TRIGGERS, PLUGIN_ROUTE_TOKEN, PLUGIN_COMMANDS maybe. The plugin file will be named autorepair_<token_lowercase>.py. Token should not clash. Let's choose "ARITHMETIC". So file name autorepair_arithmetic.py. PLUGIN_ROUTE_TOKEN = "ARITHMETIC". PLUGIN_TRIGGERS maybe ["was ist", "was ist", "was ist"] but we can use regex? The router triggers match exact strings? It says triggers match. So we need to match phrase like "was ist 2+2". We can set trigger "was ist" and then parse rest. But if user says "Was ist 2+2?" with capital W, maybe case-insensitive? Not sure. We can set triggers ["was ist", "was ist"] but maybe better to set triggers ["was ist"] and rely on router to match. But the router might match only if the prompt starts with trigger? The spec says triggers match. Might be substring? Not sure. But we can set triggers ["was ist"].

Also we can set PLUGIN_COMMANDS = ["/arithmetic"] maybe.

Implement run(prompt, context). Use regex to find expression after "was ist". We can use re.search(r'was ist\s+(.+)', prompt, re.IGNORECASE). Then extract expression. Clean punctuation. Evaluate safely: allow digits, + - * / parentheses. Use eval with restricted globals. Or use ast.parse to evaluate. Let's implement safe eval using ast.

Define function safe_eval(expr). Use ast.parse, walk nodes, allow only BinOp, UnaryOp, Num, Expression, etc. Only operators + - * / // % **. Then evaluate.

Return result string: f"{expr} = {result}". Use context["print_fn"] to show "Evaluating: {expr}". Then return.

Wrap in try/except. If fails, return empty? But must return non-empty string on success. If fails, maybe return error message.

Also need PLUGIN_REQUIRES maybe none. But we can use re and ast which are stdlib.

Implement plugin.

Let's write code.</think>
import re
import ast
import operator

PLUGIN_NAME        = "Arithmetic Helper"
PLUGIN_VERSION     = "1.0.0"
PLUGIN_DESCRIPTION = "Evaluates simple arithmetic expressions in German queries"
PLUGIN_AUTHOR      = "Electra Plugin Forge"
PLUGIN_ENABLED     = True
PLUGIN_TYPE        = "ROUTER"
PLUGIN_TRIGGERS    = ["was ist"]
PLUGIN_ROUTE_TOKEN = "ARITHMETIC"
PLUGIN_COMMANDS    = ["/arithmetic"]

# No external dependencies
PLUGIN_REQUIRES    = []

# Mapping of AST operator nodes to actual functions
_ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}

def _safe_eval(node):
    """
    Recursively evaluate an AST node containing a simple arithmetic expression.
    Only allows numbers and basic arithmetic operators.
    """
    if isinstance(node, ast.Expression):
        return _safe_eval(node.body)
    elif isinstance(node, ast.BinOp):
        left = _safe_eval(node.left)
        right = _safe_eval(node.right)
        op_type = type(node.op)
        if op_type not in _ALLOWED_OPERATORS:
            raise ValueError(f"Unsupported operator: {op_type}")
        return _ALLOWED_OPERATORS[op_type](left, right)
    elif isinstance(node, ast.UnaryOp):
        operand = _safe_eval(node.operand)
        op_type = type(node.op)
        if op_type not in _ALLOWED_OPERATORS:
            raise ValueError(f"Unsupported unary operator: {op_type}")
        return _ALLOWED_OPERATORS[op_type](operand)
    elif isinstance(node, ast.Num):  # Python <3.8
        return node.n
    elif isinstance(node, ast.Constant):  # Python 3.8+
        if isinstance(node.value, (int, float)):
            return node.value
        else:
            raise ValueError(f"Unsupported constant type: {type(node.value)}")
    elif isinstance(node, ast.Paren):
        return _safe_eval(node.value)
    else:
        raise ValueError(f"Unsupported expression: {ast.dump(node)}")

def run(prompt: str, context: dict) -> str:
    """
    Detects and evaluates simple arithmetic expressions in German queries.
    Example: "Was ist 2+2?" -> "2+2 = 4"
    """
    try:
        # Normalize prompt to lowercase for trigger matching
        lower_prompt = prompt.lower()
        # Find the expression after "was ist"
        match = re.search(r'was ist\s+(.+)', lower_prompt, re.IGNORECASE)
        if not match:
            return ""

        expr = match.group(1).strip()
        # Remove trailing punctuation like '?' or '!'
        expr = re.sub(r'[?!.]$', '', expr)

        if not expr:
            return ""

        context["print_fn"](f"Evaluating expression: {expr}")

        # Parse expression safely
        parsed = ast.parse(expr, mode='eval')
        result = _safe_eval(parsed)

        # Format result
        return f"{expr} = {result}"
    except Exception as e:
        # Log error via print_fn and return a friendly message
        context["print_fn"](f"Error evaluating expression: {e}")
        return "Entschuldigung, ich konnte die Rechnung nicht ausführen."