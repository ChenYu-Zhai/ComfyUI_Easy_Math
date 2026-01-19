import math

class EasyMath:
    """
    A simple math node for ComfyUI that performs various mathematical operations.
    """
    
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "op": ([
                    "Add (加)", 
                    "Subtract (减)", 
                    "Multiply (乘)", 
                    "Divide (除)", 
                    "Power (幂)", 
                    "Logarithm (对数)", 
                    "Square Root (平方根)", 
                    "Inverse Square Root (平方根倒数)", 
                    "Absolute (绝对值)", 
                    "Exponent (指数)"
                ],),
                "a": ("*", {"default": 0.0}),
                "b": ("*", {"default": 0.0}),
            },
            "optional": {
            }
        }

    RETURN_TYPES = ("FLOAT", "INT")
    RETURN_NAMES = ("float", "int")
    FUNCTION = "do_math"
    CATEGORY = "EasyMath"

    def do_math(self, op, a, b):
        result = 0.0
        
        # Ensure inputs are treated as floats for calculation
        # Since we use wildcard "*", inputs could be anything, so we try to cast to float.
        try:
            a = float(a)
        except (ValueError, TypeError):
            print(f"Warning: Input 'a' in EasyMath node is not a valid number ({a}). Using 0.0.")
            a = 0.0

        try:
            b = float(b)
        except (ValueError, TypeError):
            print(f"Warning: Input 'b' in EasyMath node is not a valid number ({b}). Using 0.0.")
            b = 0.0

        try:
            if op == "Add (加)":
                result = a + b
            elif op == "Subtract (减)":
                result = a - b
            elif op == "Multiply (乘)":
                result = a * b
            elif op == "Divide (除)":
                if b == 0:
                    print(f"Warning: Division by zero in EasyMath node. Returning 0.0.")
                    result = 0.0
                else:
                    result = a / b
            elif op == "Power (幂)":
                # Handle potential complex numbers or overflow
                try:
                    result = math.pow(a, b)
                except ValueError:
                    print(f"Warning: Invalid input for Power in EasyMath node (e.g. negative base with fractional exponent). Returning 0.0.")
                    result = 0.0
                except OverflowError:
                    print(f"Warning: Overflow in Power in EasyMath node. Returning 0.0.")
                    result = 0.0
            elif op == "Logarithm (对数)":
                # Logarithm of a to base b: log(a, b) = ln(a) / ln(b)
                if a <= 0 or b <= 0 or b == 1:
                    print(f"Warning: Invalid input for Logarithm in EasyMath node (a<=0, b<=0 or b=1). Returning 0.0.")
                    result = 0.0
                else:
                    result = math.log(a, b)
            elif op == "Square Root (平方根)":
                if a < 0:
                    print(f"Warning: Negative input for Square Root in EasyMath node. Returning 0.0.")
                    result = 0.0
                else:
                    result = math.sqrt(a)
            elif op == "Inverse Square Root (平方根倒数)":
                if a <= 0:
                    print(f"Warning: Invalid input for Inverse Square Root in EasyMath node (<=0). Returning 0.0.")
                    result = 0.0
                else:
                    result = 1.0 / math.sqrt(a)
            elif op == "Absolute (绝对值)":
                result = abs(a)
            elif op == "Exponent (指数)":
                try:
                    result = math.exp(a)
                except OverflowError:
                    print(f"Warning: Overflow in Exponent in EasyMath node. Returning 0.0.")
                    result = 0.0
            
        except Exception as e:
            print(f"Error in EasyMath node: {e}. Returning 0.0.")
            result = 0.0

        return (result, int(result))
