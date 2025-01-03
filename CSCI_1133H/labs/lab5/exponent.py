# Lab 5
# exponent.py


def expo(base, exponent):
    answer = 1
    for i in range(exponent):
        temp = 0
        for j in range(base):
            temp += answer
        answer = temp

    return answer

print(expo(3, 2))   # 9
print(expo(2, 5))   # 32
print(expo(10, 3))  # 1000
