file=open('c:\\users\\anand\\desktop\\string python.txt')
print(file.read())
file.seek(0)
print(file.read())
print('x'*50)
file.seek(0)
with open('xyz.txt',mode='w') as file_one:
    file_one.write("this is file i created using pycharm ")
with open('lo.txt', mode='w') as file_two:
    file_two.write("hehe i created another file using pycharm")