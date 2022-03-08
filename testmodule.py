"""
thit is a test module for Question 1
this module contains 5 functions
"""


def func1(param1: int, param2: dict[str, int]):
    """
    This function has two parameters
    (hint 2: you can read this comment using: `homeworkmodule.func1.__doc__`)
    (hint 3: you can read the annotations using: `homeworkmodule.func1.__annotations__`)
    """
    print("Hello")


def func2() -> list:
    """
    This function has no parameters and a return value.
    """
    return [1, 2, 3]


def func3(a: int, b: float, c, d: int) -> float:
    """
    This function has four parameters and a return value type float
    """
    return a + b + c + d


def func4(param1: list, param2: dict):
    """
    This function has two parameters
    """
    print("Func4")


def func5() -> dict:
    """
    This function has no parameters and a return value.
    """
    return {"a": 1, "b": 2, "c": 3}
