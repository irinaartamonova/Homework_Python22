from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy S11", "+79001004567"),
    Smartphone("Apple", "iPhone 22", "+79007654421"),
    Smartphone("Xiaomi", "Mi 31", "+79012349978"),
    Smartphone("Nokia", "310", "+79098885432"),
    Smartphone("Google", "Pixel 2", "+75211223344")
]

for smartphone in catalog:
    print (f"{smartphone.brand} - {smartphone.model}. {smartphone.phone_number})