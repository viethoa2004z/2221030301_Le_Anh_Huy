a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))

chuoi_b = str(b)
min_digit = int(min(chuoi_b))   # tìm chữ số nhỏ nhất

print("Chữ số nhỏ nhất của b là:", min_digit)
if min_digit != 0 and a % min_digit == 0:
    print(a, "chia hết cho", min_digit)
else:
    print(a, "không chia hết cho", min_digit)
