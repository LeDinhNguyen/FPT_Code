'''
1 - (1.5đ) Viết chương trình thực hiện việc nhập vào
thông tin của n sinh viên với n nhập từ bàn phím.
Mỗi sinh viên được biểu diễn dưới dạng dictionary
gồm tên, tuổi và điểm số với khóa là mã số sinh viên.

2 - (1đ) Sau đó, in ra thông tin của các sinh viên
đó theo thứ tự tăng dần của điểm số,
trong đó mỗi sinh viên được in ra tên,
tuổi và điểm số của họ.
'''
def input_students_info():
    students_info = {}
    n = int(input("Nhập số lượng sinh viên: "))
    for i in range(n):
        student_info = {}
        id = input("Nhập mã số sinh viên: ")
        name = input("Nhập tên sinh viên: ")
        age = int(input("Nhập tuổi sinh viên: "))
        score = float(input("Nhập điểm số sinh viên: "))
    ##### WRITE YOUR CODE HERE #######





    return students_info

def print_students_info_by_score(students_info):
    ###### WRITE YOUR CODE HERE ######
    ##### SORT YOUR DICTIONARY ######
    # sorted_students_info =
    ## sắp xếp danh sách và gán vào biến sau

    print("Thông tin sinh viên theo thứ tự tăng dần của điểm số:")

    ### in thông tin sinh viên theo mẫu được yêu cầu





if __name__ == '__main__':
    #  Phần 1
    students = input_students_info()
    print(students)
    # print_students_info_by_score(students)
