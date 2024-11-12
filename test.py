while True:
    print('Vítejte v aplikaci pro výpočet Hopkinsonovo zákona')
    print("1: Magnetomotorická síla (F)")
    print("2: Magnetický tok (Φ)")
    print("3: Magnetický odpor (R)")
    
    vyber = input("Vyberte si co budeme dnes počítat zadáním čísla 1-3 nebo napište 'konec' pro ukončení: ")
    
    if vyber.lower() == 'konec':
        print("Program končí.")
        break
    
    if vyber == "1":
        phi = float(input('Zadejte hodnotu magnetického toku (Φ): (ve webrech) '))
        r = float(input('Zadejte hodnotu magnetického odporu (R): (v ampérech na závit) '))
        
        if phi > 0 and r > 0:
            F = phi * r
            print(f"Φ = {phi} weberů")
            print(f"R = {r} ampérů na závit na weber")
            print("F = ? ampérů na závit")
            print(f"F = {phi} * {r}")
            print(f"Magnetomotorická síla (F) je: {F} ampérů na závit")
        else:
            print('Co pak to děláš? Ty troubo, zadal jsi záporné číslo!')
    
    elif vyber == "2":
        F = float(input("Zadejte hodnotu magnetomotorické síly (F) v ampérech na závit: "))
        r = float(input("Zadejte hodnotu magnetického odporu (R) v ampérech na závit na weber: "))
        
        if F > 0 and r > 0:
            phi = F / r
            print(f"F = {F} ampérů na závit")
            print(f"R = {r} ampérů na závit na weber")
            print("Φ = ? weberů")
            print(f"Φ = {F} / {r}")
            print(f"Magnetický tok (Φ) je: {phi} weberů")
        else:
            print('Co pak to děláš? Ty troubo, zadal jsi záporné číslo!')
    
    elif vyber == "3":
        F = float(input("Zadejte hodnotu magnetomotorické síly (F) v ampérech na závit: "))
        phi = float(input("Zadejte hodnotu magnetického toku (Φ) v weberech: "))
        
        if F > 0 and phi > 0:
            r = F / phi
            print(f"F = {F} ampérů na závit")
            print(f"Φ = {phi} weberů")
            print("R = ? ampérů na závit na weber")
            print(f"R = {F} / {phi}")
            print(f"Magnetický odpor (R) je: {r} ampérů na závit na weber")
        else:
            print('Co pak to děláš? Ty troubo, zadal jsi záporné číslo!')
    
    else:
        print("Nevybral sis žádnou z možností.")
    
    pokracovat = input("Chcete pokračovat? (ano/ne): ")
    if pokracovat.lower() != 'ano':
        print("Program končí.")
        break
