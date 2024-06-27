def pascal(num: int) -> None:
    pascal_list = [[0, 1, 0]]
    k = 1
    while k < num:
        curr = pascal_list[-1]
        next = [0]
        for i in range(len(curr) - 1):
            next.append(curr[i] + curr[i+1])
        next.append(0)
        pascal_list.append(next)
        k+=1
    for pas in pascal_list:
        for p in pas:
            if p != 0:
                print(p, end=" ")
        print()
    return pascal_list

pascal(1)
print("--------------")
pascal(4)