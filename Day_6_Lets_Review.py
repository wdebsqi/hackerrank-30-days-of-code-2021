# Enter your code here. Read input from STDIN. Print output to STDOUT
def myFunc(s):
    even = ''
    odd = ''
    for i in range(len(s)):
        if (i % 2 == 0):
            even += s[i]
        else:
            odd += s[i]

    result = even + ' ' + odd
    print(result)

t = int(input())
for i in range(t):
    s = input().strip()
    myFunc(s)
