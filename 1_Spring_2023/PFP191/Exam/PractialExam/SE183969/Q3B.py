'''
Cho chuỗi s gồm các từ được phân cách với nhau bằng
khoảng trắng.
1 - 1đ: Viết chương trình đếm tần suất xuất hiện của các từ
(không phân biệt hoa thường) dưới dạng dictionary
2 - 1đ: Sắp xếp dictionary trên theo tần suất từ
cao đến thấp thành list và in ra màn hình

Ví dụ:
s = "I am a student A good Student"

dic = {"i": 1, "am": 1, "a": 2, "student": 2, "good": 1}
sau khi sắp xếp

result = [('a', 2), ('student', 2), ('i', 1), ('am', 1), ('good', 1)]


'''
def getFrequency(s: str) -> dict:
    result = {}
    string_list = s.split(" ")
    for string in string_list:
        if string.lower() not in result:
            result[string.lower()] = 1
        else:
            result[string.lower()] += 1

    return result



def sortDictionary(d: dict) -> dict:
    sorted_result = []
    result = {}
    for key in d:
        sorted_result.append((d[key], key))
    sorted_result.sort(reverse=True)

    for item in sorted_result:
        result[item[1]] = item[0]




    return result


if __name__ == '__main__':
    #  Phần 1
    s = "I am a student A good Student"
    freq = getFrequency(s)
    sortedFreq = sortDictionary(freq)

    print(sortedFreq)
