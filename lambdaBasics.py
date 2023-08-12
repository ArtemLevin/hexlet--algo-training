def make_module(step = 1):
    return {'inc': lambda arg: arg + step, 'dec': lambda arg: arg - step}

m = make_module()
print(m['inc'](5))