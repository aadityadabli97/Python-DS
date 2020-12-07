def name_fun(*args):
    print(args)
    return(sum(args))*0.1

result = name_fun(1,2,3,4,5,6,7,8,9)


print(result)

print("x"*20)
def new_fun(**kwargs):
    print(kwargs)
    if'mohsin' in kwargs:
        print('my code name is {}'.format(kwargs['john']))
    else:
        print("there is no code name")

new_fun(mohsin ='cat',john='dog')

def new_fun(*args,**kwargs):
    print(kwargs)
    if'mohsin' in kwargs:
        print('my code name is {} {}'.format(args[0],kwargs['john']))
    else:
        print("there is no code name")

new_fun(2,3,4,5,mohsin ='cat',john='dog')