from functools import wraps
import inspect


# def optional_debug(func):
#     @wraps(func)
#     def wrapper(*args, debug=False, **kwargs):
#         if debug:
#             print('calling', func.__name__)
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @optional_debug
# def spam(a, b, c):
#     print(a, b, c)
def optional_debug(func):
    if 'debug' in inspect.getfullargspec(func).args:
        raise TypeError('debug argument already defined!')

    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('calling {}'.format(func.__name__))
        return func(*args, kwargs)
    parameters = list(inspect.signature(func).parameters.values())
    parameters.append(
        inspect.Parameter('debug',
                          inspect.Parameter.KEYWORD_ONLY,
                          default=False)
    )
    wrapper.__signature__ = inspect.signature(func).replace(parameters=parameters)
    return wrapper


@optional_debug
def a(x):
    pass


@optional_debug
def b(x, y, z):
    pass


@optional_debug
def c(x, y):
    pass


@optional_debug
def add(x, y):
    return x + y


if __name__ == '__main__':
    # spam(1, 2, 3)
    print(inspect.signature(add))