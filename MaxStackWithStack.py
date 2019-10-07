def push(newvalue, stackname):
    stackname.append(newvalue)
    if len(maxstack) == 0:
        maxstack.append(newvalue)
    elif len(maxstack) > 0:
        if max(maxstack) < newvalue:
            maxstack.append(newvalue)

def pop(stackname):
    if stackname[len(stackname)-1] > maxstack[len(maxstack)-1]:
        maxstack.pop()
        stackname.pop()
    else:
        stackname.pop()




stack = []
maxstack = []


push(20, stack)

print ("Stack")
print(stack)
print ("Max Stack")
print(maxstack)

push(10, stack)
print ("Stack")
print(stack)
print ("Max Stack")
print(maxstack)

push(100, stack)
print ("Stack")
print(stack)
print ("Max Stack")
print(maxstack)


push(50, stack)
print ("Stack")
print(stack)
print ("Max Stack")
print(maxstack)


pop(stack)
print ("Stack")
print(stack)
print ("Max Stack")
print(maxstack)