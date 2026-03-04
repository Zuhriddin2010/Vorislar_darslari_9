# def sum(a,b):
#     return (a + b)

# a = int(input("Enter 1st number >>>"))
# b = int(input("Enter 2st number >>>"))

# print(f"sum of {a} and {b} is {sum(a,b)}")

# def daraja_oshirish(son,son1):
#     print(f"{son} ** {son1} = {son**son1}")
# daraja_oshirish(2,3)

# def summa(*sonlar):
#     """kiritilgan sonni hisoblavchi funksiya"""
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return yigindi
# print(summa(2))

# def malumotlar(ism,familiya,*ixtiyoriy):
#     ism = input("ismingiz nima >>>")
#     familiya = ("familiyachi >>>")

#     for matn in ixtiyoriy:
#         natija += matn
#     return f"{ism.title()} {familiya.title()} {natija}"
# print(malumotlar("bobur","isgandarov","23-yoshda","uylanmagan"))

# def avto_info(kampaniya,moder,**malumotlar):
#     malumotlar["kampaniya"] = kampaniya
#     malumotlar["model"] = Model
#     return malumotlar

# moshinalar = avto_info("GM","sedan",yili = "2000",rangi = "oq")
# print(moshinalar)
