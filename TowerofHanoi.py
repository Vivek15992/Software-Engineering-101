def shift():
    stack2.append(stack1[-1])
    stack1.pop()
    stack3.append(stack1[-1])
    stack1.pop()
    print(stack1)
    print(stack2)
    print(stack3)
    while len(stack1) != 0 and len(stack3) != 0:
        try:
            if stack1[-1] < stack2[-1]:
                stack2.append(stack1[-1])
                stack1.pop()
                print("loop1")
        except:
            stack2.append(stack1[-1])
            stack1.pop()
        try:
            if stack1[-1] < stack3[-1]:
                stack3.append(stack1[-1])
                stack1.pop()
                print("loop1")
        except:
            stack3.append(stack1[-1])
            stack1.pop()
        try:
            if stack2[-1] < stack3[-1]:
                stack3.append(stack2[-1])
                stack2.pop()
        except:
            stack3.append(stack2[-1])
            stack2.pop()
        try:
            if stack2[-1] < stack1[-1]:
                stack1.append(stack2[-1])
                stack2.pop()
        except:
            stack3.append(stack2[-1])
            stack2.pop()
        try:
            if stack3[-1] < stack1[-1]:
                stack1.append(stack3[-1])
                stack3.pop()
                print("loop3")
        except:
            stack1.append(stack3[-1])
            stack3.pop()
            print("loop3")
        try:
            if stack3[-1] < stack2[-1]:
                stack2.append(stack3[-1])
                stack3.pop()
                print("loop3")
        except:
            stack2.append(stack3[-1])
            stack3.pop()
            print("loop3")

        print(stack1)
        print(stack2)
        print(stack3)



stack1 = ([50, 30, 10,5,2,1])
stack2 = []
stack3 = []

shift()

print (stack1)
print (stack2)
print (stack3)




