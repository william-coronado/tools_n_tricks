from icecream import ic

# Simple variable inspection
x = 42
ic(x)  # ic| x: 42

# Expression evaluation
ic(x + 100)  # ic| x + 100: 142

# Function debugging
#@ic
def complex_calculation(a, b):
    result = a * b + sum([1, 2, 3])
    ic(result)
    return result

ic(complex_calculation(2, 3))
# Multiple variables
y = "test"
z = [1, 2, 3]
ic(x, y, z)  # ic| x: 42, y: 'test', z: [1, 2, 3]

# Conditional debugging
ic.configureOutput(includeContext=True)
ic.disable()  # Turn off debug prints
ic.enable()   # Turn them back on