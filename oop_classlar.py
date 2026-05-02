# class Talaba:
#     def __init__(self, ism, familiya, otasining_ismi, tyil):
#        self.name = ism 
#        self.familya = familiya
#        self.tyil = tyil
#        self.ochestvo = otasining_ismi
#     def FIO(self):
#         return f"{self.familya} {self.name} {self.ochestvo}"
#     def yosh(self):
#         return f"{2026-self.tyil} yoshda"
    
# t1  = Talaba ('kamolbek', 'ruzmamatov', 'Vohidjonivich',2010)
# t2 = Talaba ('aziz', 'karimov', 'Salimovich', 2005)
# t3 = Talaba ('sardor', 'murodov', 'Abdullayevich', 2000)
# print(t1.FIO(), t2.FIO(), t3.FIO())
# print(t1.yosh(), t2.yosh(), t3.yosh())
# print(t1.name, t1.familya, t1.ochestvo, t1.tyil)
# print(t2.name, t2.familya, t2.ochestvo, t2.tyil)
# print(t3.name, t3.familya, t3.ochestvo, t3.tyil)

# class Kitob:
#     def __init__(self, nomi, muallif, nashr_yili):
#         self.nomi = nomi
#         self.muallif = muallif
#         self.nashr_yili = nashr_yili
#     def get_info(self):
#         return f"{self.nomi} kitobi {self.muallif} tomonidan {self.nashr_yili}-yilda nashr etilgan."
# k1 = Kitob("O'tgan kunlar", "Abdulla Qodiriy", 1922)
# k2 = Kitob("Kecha va kunduz", "Abdulhamid Cho‘lpon", 1930)
# k3 = Kitob("Shum bola", "G'afur G'ulom", 1936)
# k4 = Kitob("Dunyoning ishlari", "O'tkir Hoshimov", 1982)
# print(k1.get_info())
# print(k2.get_info())
# print(k3.get_info())
# print(k4.get_info())




import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class ZamonaviyDastur(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Zamonaviy Python Dasturi")
        self.geometry("400x500")

        self.label = ctk.CTkLabel(self, text="Mening Rejalarim", font=("Helvetica", 24, "bold"))
        self.label.pack(pady=20)

        # Matn kiritish maydoni
        self.entry = ctk.CTkEntry(self, placeholder_text="Yangi vazifa kiriting...", width=300, height=40)
        self.entry.pack(pady=10)
        
        # --- MUHIM QISMI: Enter tugmasini ulaymiz ---
        self.entry.bind("<Return>", lambda event: self.vazifa_qoshish())

        self.add_button = ctk.CTkButton(self, text="Qo'shish", command=self.vazifa_qoshish, corner_radius=10)
        self.add_button.pack(pady=10)

        self.scrollable_frame = ctk.CTkScrollableFrame(self, width=350, height=250, label_text="Vazifalar ro'yxati")
        self.scrollable_frame.pack(pady=20, padx=10)

    def vazifa_qoshish(self):
        vazifa = self.entry.get()
        if vazifa.strip(): # Bo'sh matn qo'shilib ketmasligi uchun .strip() qo'shdik
            vazifa_label = ctk.CTkCheckBox(self.scrollable_frame, text=vazifa)
            vazifa_label.pack(pady=5, anchor="w")
            self.entry.delete(0, 'end')

if __name__ == "__main__":
    app = ZamonaviyDastur()
    app.mainloop()