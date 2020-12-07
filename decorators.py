def cheeseandbuns(myfunc):
    def wrap():
        print("this is upper bread")
        myfunc()
        print("this is lower bread")

    return wrap
@cheeseandbuns # decorator
def chicken():
    print('i am roasted chicken')

chicken()

