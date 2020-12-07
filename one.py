def func():
    print("this function is in one.py")

print("this is global print in one.py")


if __name__=="__main__":

    print("one.py is being directly called")
else:
    print("one.py is being imported ")


