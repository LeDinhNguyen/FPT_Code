def splitList(num_list: list) -> bool:
    for i in range(len(num_list)):
        if sum(num_list[0:i+1]) == sum(num_list[i+1::]):
            return True

print(splitList([1, 2, 3, 5, 1]))
