from collections.abc import Callable

# -------------------------------------------------------------------------------------------------
# All "move effect" functions

def no_effect_function():
    pass

# -------------------------------------------------------------------------------------------------

def get_function_from_code(code:str)->Callable:
    return no_effect_function
