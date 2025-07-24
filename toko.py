item1 = {"barang" : "Jaket", "stok" : 12, "harga" : 100000}
item2 = {"barang" : "Baju", "stok" : 20, "harga" : 80000}
item3 = {"barang" : "Celana", "stok" : 54, "harga" : 40000}
item4 = {"barang" : "celana dalam", "stok" : 71, "harga" : 20000}
item5 = {"barang" : "kemeja", "stok" : 34, "harga" : 400000}

items = [item1, item2, item3, item4, item5]
sum = 0


for i in range (len(items)):
    print(i + 1, ("Nama Item: "), items[i]["barang"])
    sum = sum + items[i]["harga"]

print("Total harga masing-masing 1 barang: ", sum)

#total harga per-1 barang di kali dengan jumlah stok

totalHargaStok = sum * items[i]["stok"]
print("total Harga Keseluruhan: ", totalHargaStok)

barang = (input("Masukan Barang Baru: "))
stok = (input("Masukan Jumlah Stok: "))
harga = int(input("Masukan Harga Barang: "))

item6 = {"barang" : barang, "stok" : stok, "harga" : harga}

sum = 0

items.append(item6)

for i in range (len(items)):
    print(i + 1, ("Nama Item: "), items [i]["barang"])
    sum = sum + items[i]["harga"]

print("Total harga masing-masing 1 barang: ", sum)
