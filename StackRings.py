def hanoi(n, source, helper, target):
    if n > 0:
        hanoi(n - 1, source, target, helper)
        print (source[0])
        if source[0]:
            disk = source[0].pop()
            target[0].append(disk)
            print ("Pole status:")
            print(source[0])
            print(target[0])
            print(helper[0])
        hanoi(n - 1, helper, source, target)


source = ([4, 3, 2, 1], "source")
target = ([], "target")
helper = ([], "helper")
hanoi(len(source[0]), source, helper, target)

