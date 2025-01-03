# Primer on Python Decorators

This folder contains various Python scripts demonstrating the use of decorators.
You can find most decorators in the file `decorators.py`. The exceptions are those decorators that depend on the third-party packages ([Flask](http://flask.pocoo.org/) and [Pint](https://pint.readthedocs.io/)). These decorators are available in `secret_app.py`, `validate_input.py`, and `units.py`.

## Files

### `decorators.py`
Contains various decorator functions such as `do_twice`, `timer`, `debug`, `slow_down_one_second`, `register`, `repeat`, `count_calls`, `singleton`, and `cache`. These decorators provide functionalities like timing, debugging, repeating function calls, and caching results.

### `calculate_e.py`
This script uses a `debug` decorator to wrap the `math.factorial` function and defines a function to approximate the value of e using a series expansion.

### `class_decorators.py`
Demonstrates the use of decorators on classes and methods. It includes a `TimeWaster` class with a `debug` decorator on the constructor and a `timer` decorator on a method. It also shows a `TimeWaster2` class with a `timer` decorator applied to the entire class.

### `circle.py`
Defines a `Circle` class with properties for radius and area, and methods for calculating the volume of a cylinder and creating a unit circle. It also includes a static method for the value of π.

### `greeters.py`
Defines two greeting functions, `say_hello` and `be_awesome`, and a `greet_bob` function that takes a greeter function as an argument and applies it to the name "Bob".

### `hello_decorator.py`
Defines a simple decorator that prints messages before and after calling a function. It demonstrates the decorator with two functions, `say_whee` and `say_whee2`.

### `inner_functions.py`
Demonstrates the use of inner functions and returning functions from other functions. It includes a `parent` function with two inner functions and a `get_child` function that returns one of two inner functions based on an argument.

### `quiet_night.py`
Contains a decorator `not_during_the_night` that prevents a function from running during certain hours. It demonstrates this decorator with a `say_whee` function.

### `secret_app.py`
Uses the Flask web framework to create a simple web application with a `login_required` decorator that ensures a user is logged in before accessing a route.

### `units.py`
Demonstrates the use of the `pint` library for unit handling. It includes decorators `set_unit` and `use_unit` to register and use units with functions.

### `validate_input.py`
Uses the Flask web framework to create a web application with a `validate_json` decorator that ensures certain keys are present in the JSON request body before proceeding with a route handler.

## References
These scripts are based on examples from the [Primer on Python Decorators](https://realpython.com/primer-on-python-decorators/)
