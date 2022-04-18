from inspect import signature
from functools import wraps


def typeassert(*tr_args, **tr_kwargs):
    def decorate(func):
        if not __debug__:
            return func

        sig = signature(func)
        bound_types = sig.bind_partial(*tr_args, **tr_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs).arguments
            for key, value in bound_values.items():
                if key in bound_types.keys():
                    if not isinstance(value, bound_types[key]):
                        raise TypeError('Arguments {} must be {}'.format(key, bound_types[key]))
            return func(*args, **kwargs)
        return wrapper
    return decorate


@typeassert(int, z=int)
def spam(x, y, z=42):
    print(x, y, z)


@typeassert(int, int)
def add(x, y):
    return x, y


if __name__ == '__main__':
    # sig = signature(spam)
    # print(sig)
    # print(sig.parameters)
    # print(sig.parameters['z'].name)
    # print(sig.parameters['z'].default)
    # print(sig.parameters['z'].kind)
    # bound_types = sig.bind_partial(int, z=int)
    # bound_values = sig.bind(1, 2, 3)
    # print(bound_types)
    # print(bound_types.arguments)
    # print(bound_values)
    # print(bound_values.arguments.items())
    # print(bound_types.arguments['x'])
    # print(bound_types.arguments)
    # print('x' in bound_types.arguments.keys())
    spam(1, 2, 3)
    spam(1, 'hello', 3)
    spam(1, 'hello', 'world')
