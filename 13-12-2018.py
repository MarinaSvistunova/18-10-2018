"""
  Заставить код работать и протестировать программу на вычисление дискриминанта и функции для вычисления корней.
"""

def foo(op1, op2):
    return op1 + op2

def test_assert(*args):
    """
        args = (func, *operands, exp_value, "Failed assertion message")
    """
    func, *operands, exp_value = args[0], *args[1:-1], args[-1]
    try:
        assert func(*operands)==exp_value ,f"Failed assertion message with func {func}{operands}, exp value is {exp_value}"
    except AssertionError as e:
        print(e)

test_assert(foo,2,3,5)