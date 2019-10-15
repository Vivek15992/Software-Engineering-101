def shift()

    while len(stack1) > 0 and len(stack3) > 0:
        stack2.append(stack1[-1])
        stack1.pop()
        stack3.append(stack1[-1])
        stack1.pop()
        stack3.append(stack2[-1])
        stack2.pop()
        stack2.append(stack1[-1])
        stack1.pop()
        stack1.append(stack3[-1])
        stack3.pop()
        stack2.append((stack3[-1]))
        stack3.pop()
        stack2.append(stack1[-1])
        stack1.pop()








stack1 = [50, 30, 10]
stack2 = []
stack3 = []

shift()

print(stack1)
print(stack2)
print(stack3)


