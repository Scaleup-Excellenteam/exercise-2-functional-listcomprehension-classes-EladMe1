import functools


class TypeErrorWithMessage(TypeError):
    pass


def type_check(type_arg):
    def decorator(func):
        @functools.wraps(func)
        def warrper(arg):
            #check if the args not match for the type of args
            if not isinstance(arg, type_arg):
                raise TypeErrorWithMessage(f"Expected argument of type {type_arg.__name__}, but got {type(arg).__name__}")
            return func(arg)

        return warrper
    return decorator


@type_check(int)
def times2(num):
    return num*2


if __name__ == "__main__":
    try:
        print(times2(9))
        print(times2("9"))
    except TypeErrorWithMessage as e:
        print(e)