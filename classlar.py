# # class Davlatlar:
# #     def __init__(self, nomi, poytaxti, aholisi, jaylshuvi, maydoni,tili):
# #         self.nomi = nomi
# #         self.poytaxti = poytaxti
# #         self.aholisi = aholisi
# #         self.jaylshuvi = jaylshuvi
# #         self.maydoni = maydoni
# #         self.tili = tili
# #     def get_nomi(self):
# #         return f"{self.nomi.title()}"
# #     def Info(self):
# #         return f"{self.nomi.title()} Davlatining poytaxti {self.poytaxti} shaxri {self.aholisi}"
# #     def get_joylashuv(self):
# #         return f"{self.nomi.title() } davlati {self.joylashuv} da joylashgan"
# #     def get_maydoni(self):
# #         return f"{self.nomi.title ()} ning maydoni {self.maydoni} km kvga teng"
# #     def get_tili(self):
# #         return f"{self.nomi.title()} ning davlat tili {self.tili} tili hisoblanadi."
    
# # Uzb = Davlatlar('uzb',"Toshkent",38000000,'Markaziy osiyo',448978)

# # Rus = Davlatlar('Rassiya','Moskva', 14000000,'Yevro osiyo',17089242)

# # print(Uzb.Info())
    
# class Shaxs:
#     def __init__(self,Ism,Familiya,tyil):
#         self.name = Ism
#         self.surname = Familiya
#         self.age = tyil
#     def get_name(self):
#         return f"{self.name.title()}"
#     def get_surname(self):
#         return f"{self.surname.title()}"
#     def get_age(self):
#         return f"{self.age}"
    
# class Talaba(Shaxs):
#     def __init__(self, Ism, Familiya, tyil, bosqich):
#         super().__init__(Ism, Familiya, tyil)
#         self.bosqich = bosqich
#     def get_bosqich(self):
#         return f"{self.bosqich}"
# # t = Talaba("Ali","Valiyev",2000,3)
# # print(t.get_bosqich())

# class Fanlar(Talaba):
#     def __init__(self, ism,familiya, tyil, bosqich, fan, ustoz):
#         super().__init__(ism, familiya, tyil, bosqich)
#         self.fan = fan
#         self.ustoz = ustoz
#     def get_fan(self):
#         return f"{self.fan.title()}"
#     def get_ustoz(self):
#         return f"{self.ustoz.title()}"
# f = Fanlar("Ali","Valiyev",2000,3,"Matematika","Olim")
# print(f.get_fan())
# print(f.get_ustoz())





class Hodimlar:
    def __init__(self, ism, lavozim, tajriba, maosh):
        self.ism = ism
        self.lavozim = lavozim
        self.tajriba = tajriba
        self.maosh = maosh
    def get_name(self):
        return f"{self.ism.title()}"
    def get_lavozim(self):
        return f"{self.lavozim.title()}"
    def get_tajriba(self):
        return f"{self.tajriba}"
    def get_maosh(self):
        return f"{self.maosh}"
    def get_info(self):
        return f"{self.ism.title()} {self.lavozim.title()} lavozimida ishlaydi, tajribasi {self.tajriba} yil, maoshi {self.maosh} so'm"
    
# hodim1 = Hodimlar("Ali","Dasturchi",5,5000)
# print(hodim1.get_name())
# print(hodim1.get_lavozim())
# print(hodim1.get_tajriba())
# print(hodim1.get_maosh())

class Magazin(Hodimlar):
    def __init__(self, ism, lavozim, tajriba, maosh, maxsulot_turi):
        super().__init__(ism, lavozim, tajriba, maosh)
        self.maxsulot_turi = maxsulot_turi
    def get_maxsulot_turi(self):
        return f"{self.maxsulot_turi.title()}"
    def get_info(self):
        return f"{self.ism.title()} {self.lavozim.title()} lavozimida ishlaydi, tajribasi {self.tajriba} yil, maoshi {self.maosh} so'm, maxsulot turi {self.maxsulot_turi.title()}"
magazin1 = Magazin("Ixtiyor","Dasturchi",5,5000,)
print(magazin1.get_info())
