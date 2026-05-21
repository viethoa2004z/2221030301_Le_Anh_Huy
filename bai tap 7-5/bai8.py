x = int(input("Nhap x: "))
y = int(input("Nhap y: "))
z = int(input("Nhap z: "))

tich = x * y * z

print("Tich =", tich)

so_chu_so = len(str(tich))

print("So chu so cua tich:", so_chu_so)

lon_nhat = 0

for ch in str(tich):
    if int(ch) > lon_nhat:
        lon_nhat = int(ch)

print("Chu so lon nhat la:", lon_nhat)