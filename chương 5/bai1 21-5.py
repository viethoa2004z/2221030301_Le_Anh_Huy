n = int(input("Mời nhập số lượng phần tử n: "))
a = []
for i in range(n):
    x = float(input("Nhập phần tử thứ " + str(i+1) + ": "))
    a.append(x)

tong = 0
dem = 0
for x in a:
    if x > 0 and x < 1000:
        tong += x
        dem += 1

if dem > 0:
    print("Trung bình cộng =", tong/dem)
else:
    print("Không có phần tử thỏa mãn")
