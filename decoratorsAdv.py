def checking_that_arg_is(predicate, error_message):
    def wrapper(function):
        def inner(arg):
            if not predicate(arg):
                raise ValueError(error_message)
            return function(arg)
        return inner
    return wrapper

def greater_than(value):
    def predicate(arg):
        return arg > value
    return predicate

@checking_that_arg_is(greater_than(10), 'Non-positive integer')
def foo(arg):
    return arg

print(foo(5))