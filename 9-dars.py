def main():
    # Foydalanuvchidan son kiritishni so'raymiz
    son = int(input("Iltimos, biror butun son kiriting: "))
    
    # Sonning juft yoki toqligini tekshiramiz
    if son % 2 == 0:
        print(f"{son} juft son.")
    else:
        print(f"{son} toql son.")      

if __name__ == "__main__":      
    main() 
