n = int(input("Nhập số nguyên dương n: "))
tich = 1
for ch in str(n):
    tich *= int(ch)

print("Tích các chữ số =", tich)
if tich % 2 == 0 and tich > 20:
    print("Tích là số chẵn và lớn hơn 20")
else:
    print("Không thỏa mãn điều kiện")
