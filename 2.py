def bigger_price(son, mahsulotlar):

    sorted_mahsulotlar = sorted(mahsulotlar, key=lambda x: x['price'], reverse=True)
    return sorted_mahsulotlar[:son]


son = int(input("Nechta eng qimmat mahsulotni ko'rmoqchisiz --> "))

mahsulotlar = []
n = int(input("Mahsulotlar sonini kiriting --> "))

for i in range(n):
    nomi = input(f"{i+1}-mahsulotning nomini kiriting -->  ")
    narxi = float(input(f"{nomi}ning narxini kiriting --> "))
    mahsulotlar.append({"name": nomi, "price": narxi})

natija = bigger_price(son, mahsulotlar)
print("Eng qimmat mahsulotlar:")
for item in natija:
    print(item)
