#Dictionary
student1 = {"Nama" : "Ahmad", "asal" : "Samarinda", "Nilai" : 90} 
student2 = {"Nama" : "Bambang", "asal" : "Bontang", "Nilai" : 75}
student3 = {"Nama" : "Cecep", "asal" : "Cimahi", "Nilai" : 60}

#list  of Dictionary
students = [student1, student2, student3,]
Sum = 0

for i in range(len(students)):
    print("Siswa ke-" ,i + 1, ":", students [i] ["Nama"])
    Sum = Sum + students[i]["Nilai"]

print("Total seluruh nilai adalah: ", Sum)

ratarata = Sum / len(students)
print("Nilai rata-rata: ", ratarata)

Nama = str(input("Masukan Nama: "))
asal = str(input("Asal: "))
Nilai = int(input("Nilai: ")) #casting

student4 = {"Nama" : Nama, "Asal" : asal, "Nilai" : Nilai}

sum = 0

students.append(student4)

for i in range(len(students)):
    print("Siswa ke-",i + 1, ":", students [i]["Nama"])
    sum = sum + students[i]["Nilai"]

print("Total Nilai: ", sum)
print("Nilai Rata Rata:",  ratarata)

# CRUD - read 

print("No\tNama\tasal\tNilai")
for i in range(len(students)):
    print(i + 1, "\t", students[i]["Nama"], "\t", students[i]["asal"], "\t", students[i]["Nilai"])

print("Nama\tasal\tNilai")
for s in students:
    print(s["Nama"], "\t", s["asal"], "\t", s["Nilai"])