def converts_temperature(value, unit):
    if unit == "C":
        return (value * 9/5) + 32
    elif unit == "F":
        return (value - 32) * 5/9
    else:
        print("Tidak ada unit")

input_value = int(input("Masukkan value: "))
input_unit = input("Masukkan unit (C/F): ")

konversi = converts_temperature(input_value, input_unit)
print(f"Hasil konversi: {konversi}")
