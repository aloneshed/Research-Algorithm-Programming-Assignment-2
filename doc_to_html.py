import sys
import importlib

module_name = sys.argv[1][0:-3]
html_file_name = sys.argv[2]
module = importlib.import_module(module_name)


def dummy():
    pass


html_string = "<html>\n<head>\n<title>\nDoc\n</title>\n</head>\n<body>\n"
html_string += f"<h1>Module {module_name}:</h1>\n"
html_string += module.__doc__ + "\n"
my_list = [(name, type(getattr(module, name))) for name in dir(module)]
func_list = []
for tup in my_list:
    if tup[1] == type(dummy):
        func_list.append(tup[0])

for i in func_list:
    func = getattr(module, i)
    html_string += f"<h1>Function {i}:</h1>\n"
    html_string += func.__doc__ + "\n"
    html_string += "<h3>Annotations:</h3>\n"
    html_string += str(func.__annotations__) + "\n"

html_string += "</body>\n</html>"

with open(html_file_name, "x") as f:
    f.write(html_string)
