import sys
def create_sqrA(n):
    result=[]

    for x1 in range(n):
        result.append(x1**2)
    return result
print(create_sqrA(10))
print(sys.getsizeof(create_sqrA(1000000)))

print('x'*20)

def create_sqrG(n):                    # using generator
    for x2 in range(n):
        yield x2**2
for x in create_sqrG(10):
    print(x)
print(sys.getsizeof(create_sqrG(1000000000)))