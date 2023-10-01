def f(a, *args, **key_args):
    print(a, args, key_args)


f(1, 3, 4, 5, x=10, y=20)
