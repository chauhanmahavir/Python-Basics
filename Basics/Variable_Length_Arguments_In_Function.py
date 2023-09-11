def func_args(arg1, arg2, *args):
    print('arg1: ', arg1)
    print('args1_Type:', type(arg1))
    print('arg2: ', arg2)
    print('args2_Type:', type(arg2))
    print('args: ', args)
    print('args_Type:', type(args))

#func_args(arg1=0, arg2=1, *args=(2,3,4))
func_args(0, 1, 2, 3, 4)
