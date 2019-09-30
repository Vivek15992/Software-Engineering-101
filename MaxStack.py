
def push(x,y):
    y.append(x)

def pop(y):
    y.pop()

def max(y):
    maxval = 0
    for i in y:
        if i > maxval:
            maxval = i
    print (maxval)

stack = []

print ("Empty Stack")
print (stack)

print ("Push New elements")
push(20,stack)
push(50,stack)
push(70,stack)
push(10,stack)
push(5,stack)
push(50,stack)
push(7,stack)
push(59,stack)
push(67,stack)

print (stack)

print("Pop last element")
pop(stack)
print(stack)

print("Find max valuse in the stack")
max(stack)

