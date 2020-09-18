a = input()
b = input()
temp = 0
head = 0
if len(a) > len(b):
    b = (len(a) - len(b)) * "0" + b
    head = len(a) % 4
    temp = len(a) // 4
else:
    a = (len(b) - len(a)) * "0" + a
    head = len(b) % 4
    temp = len(b) // 4

temp -= 1
carry = 0
sum_num = 0
sum_str = ""
while temp != -1:
    sum_num = int(a[head + temp * 4 : head + temp * 4 + 4]) + int(b[head + temp * 4 : head + temp * 4 + 4])
    if carry == 1:
        sum_num += 1
        carry = 0
    if sum_num > 9999:
        carry += 1
        sum_str = str(sum_num)[1:] + sum_str
    else:
        sum_str = str(sum_num) + sum_str
    temp -= 1


sum_num = int(a[:head]) + int(b[:head])
if carry == 1:
    sum_num += 1
    sum_str = str(sum_num) + sum_str
else:
    sum_str = str(sum_num) + sum_str
print("a + b = " + sum_str)
