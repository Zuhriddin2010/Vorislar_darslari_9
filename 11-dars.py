# ro`yhatlar

# ismlar = ["elbek", "ixtiyor"]  # oddiy ro`yhat                                      
# familiyalar = ("karimboyev", "abdullayev")  # ozgarmas royhat

# print("oddiy royhat",ismlar)                       
# print("ozgarmas royhat",familiyalar)

# ismlar.append("sardor")
# print(ismlar)

# #familiyalar.append("teshaboyev")        # xatolik beradi, type ga ya`ni element qo`lish bo`lmaydi
# #print(familiyalar)
                                  
# o_familiyalar = list(familiyalar)
# print(o_familiyalar)  # typeni listga o`tiramiz

# o_familiyalar.append("teshaboyev")
# print(o_familiyalar) # endi element qo`sh

# familiyalar = tuple(o_familiyalar)  # listni yana tuple ga aylantiramiz
# print(familiyalar)

davlatlar = ["amerika","aqsh","qozoqiston","kareya","uzb"]
print(len(davlatlar))

sorted(davlatlar)
print(davlatlar)

davlatlar.reverse() # ro`yhatni ortidan boshlab chiqaradi
print(davlatlar)

print(davlatlar) #asl royhatni boshqatdan chiqaradi

print(f"davlatlarning teskari tartiblanganini chiqradi : {sorted(davlatlar, reverse = True)}") # royhatni teskari tartibda chiqaradi
