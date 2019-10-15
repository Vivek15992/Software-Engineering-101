def Tower(n, source, inter, target):
    if n > 0:
        # move tower of size n - 1 to helper:
        Tower(n - 1, source, target, inter)
        # move disk from source peg to target peg
        print (source[0])
        if source[0]:
            disk = source[0].pop()
            print ("moving " + str(disk) + " from " + source[1] + " to " + target[1])
            target[0].append(disk)
        # move tower of size n-1 from helper to target
        Tower(n - 1, inter, source, target)


source = ([4, 3, 2, 1], "source")
target = ([], "target")
inter = ([], "helper")
Tower(len(source[0]), source, inter, target)

print (source, inter, target)