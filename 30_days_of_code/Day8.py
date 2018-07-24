#python3


a = [] #input
try:
    n = int(input())
    pass
except:
    n = 3

for _ in range(n):
    a.append(str(input()).split())
'''
test = [str(input()).split() for _ in range(n)] #one_line_code
print(test)
test = dict(test)
print(test)
'''


a = dict(a)

for _ in range(n):
    search = str(input())
    if search in a:
        print(search + "=" + a[search])
    else:
        print("Not found")
