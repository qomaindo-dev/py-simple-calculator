#---------------------------#
#SIMPEL CALCULATOR IN PYTHON#
#---------------------------#

import numpy as np
from collections import Counter

print("-------------------------------------")
print("Operasi Matematika ")
print("-------------------------------------")
list_operator = "[+] Tambah\n[-] Kurang\n[*] Kali\n[/] Bagi"
print(list_operator)
print("-------------------------------------\n")
pilihan = input("Silahkan pilih Operator:")

if pilihan == "+" or pilihan == "-" or pilihan == "*" or pilihan == "/":
  jmlValue = int(input("\nJumlah nilai perhitungan: "))

  hasil = 0
  hasilKali = 1
  nilai = []

  for i in range(jmlValue):
    ipnilai = 0
    inilai = i+1
    print(f'Nilai ke-{inilai}')
    ipnilai = int(input(""))

    nilai.append(ipnilai)

  arr = Counter(nilai)

  for key, value in arr.items():
    if pilihan == "+":
      hasil += key * value

    elif pilihan == "-":
      if nilai[0] == key:
        hasil = key
      else:
        hasil = hasil - key
    elif pilihan == "*":
      hasilKali *= key
    else :
      if nilai[0] == key:
        hasil = key
      else:
        hasil = hasil / key
      print("Key: ", key)
      print("hasil", hasil)

  if pilihan == "*":
    hasil = hasilKali

  print(f'Hasil: {hasil}')
else:
    print(f'Pilihan operator {pilihan} tidak tersedia!!!')
