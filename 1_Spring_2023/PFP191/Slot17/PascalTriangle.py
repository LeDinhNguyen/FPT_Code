def Pascal(num: int) -> list:
    result = [[1], [1, 1]]
    while len(result) < num:
        layer = []
        a = result[-1]
        for i in range(len(a)):
            if i == 0:
                layer.append(a[i])
            else:
                layer.append(a[i] + a[i - 1])
            if i == len(a) - 1:
                layer.append(a[i])

        result.append(layer)
    for num_list in result:
        for p in num_list:
            print(p, end=" ")
        print(" ")
    return result
Pascal(4)
