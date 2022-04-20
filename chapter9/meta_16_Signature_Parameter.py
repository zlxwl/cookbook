from inspect import Signature, Parameter


params = [Parameter('x', Parameter.POSITIONAL_OR_KEYWORD),
          Parameter('y', Parameter.POSITIONAL_OR_KEYWORD, default=42),
          Parameter('z', Parameter.KEYWORD_ONLY, default=None)]
sig = Signature(params)
print(sig)


def func(*args, **kwargs):
    bound_values = sig.bind(*args, **kwargs)
    print(bound_values)
    print(bound_values.arguments)
    for name, value in bound_values.arguments.items():
        print(name, value)


if __name__ == '__main__':
    func(1, y=4)