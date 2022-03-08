"""
sources:
Question 1: https://www.tutorialspoint.com/python/python_command_line_arguments.htm
Question 2: https://stackoverflow.com/questions/67821084/create-a-decorator-in-python-which-remembers-last-output-of-the-function
Question 3:
"""


# Question 2
def lastcall(func):
    def innerfunction(arg):
        with open('last_call.txt', "r") as f:
            try:
                previous_outputs = f.readlines()
            except:
                previous_outputs = []
        result = func(arg)
        if not previous_outputs:
            print(result)
        if previous_outputs:
            for last_line in previous_outputs:
                pass
            func_name, arg_name, output = last_line.split(" ")
            if func_name == func.__name__ and arg_name == str(arg):
                print(f"I already told you that the answer is {result}!")
                return result
            else:
                print(result)

        with open('last_call.txt', 'a') as f:
            f.write(f"{func.__name__} {arg} {func(arg)}\n")
        return result

    return innerfunction


if __name__ == '__main__':
    @lastcall
    def f(x: int):
        return x ** 2


    @lastcall
    def g(x: int):
        return x ** 2

    @lastcall
    def j(x: int):
        return x + x

    @lastcall
    def p(x: int):
        return x ** 3


    f(2)
    f(2)
    f(2)
    f(3)
    f(3)
    g(3)
    f(3)
    f(3)
    j(10)
    j(11)
    j(11)
    p(2)
    p(2)
    p(2)
    p(2)
    p(3)
    p(3)
    p(4)
    p(4)
