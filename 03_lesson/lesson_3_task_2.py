from smartphone import Smartphone

phone_1 = Smartphone('Samsung', "S2", "+7928" )
phone_2 = Smartphone('Nokia', "N3", "+7952" )
phone_3 = Smartphone('Siemens', "Sm5", "+7909" )
phone_4 = Smartphone('iPhone', "12mini", "+7922" )
phone_5 = Smartphone('Redmee', "R9", "+7931" )
catalog = [phone_1, phone_2, phone_3, phone_4, phone_5]

for element in catalog:
    print(f"{element.brand}-{element.model}, {element.number}")