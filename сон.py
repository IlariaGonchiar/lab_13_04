text = input("Скільки ви сьогодні спали?").split()
a = int(text[0])
if a < 8:
    print("Ви сонні")
if a > 8:
    print("Ви голодні")
if a > 10:
    print("Ви щасливі")
    

    
