import one
print("top level in two.py")

one.func()
if __name__=="__main__":
    print("two is being run directly")
else:
    print("two is being imported")