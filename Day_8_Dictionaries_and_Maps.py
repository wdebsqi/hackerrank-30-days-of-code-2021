# Enter your code here. Read input from STDIN. Print output to STDOUT
length = int(input())
phone_book = {}

for i in range(length):
    key, value = input().strip().split(' ')
    phone_book[key] = value
    
try:
    for i in range(length):
        name = input()
        if name not in phone_book:
            print('Not found')
        else:
            print(str(name) + '=' + str(phone_book[name]))
except EOFError:
    pass
