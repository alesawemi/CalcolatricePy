while True:
    print(hello_message)

    action = input("Inserisci il numero corrispondete all'operazione da effettuare: ")

    if action == "1":
        print("\nHai scelto: Addizione\n")
        a = float(input("Inserisci il Primo Numero -> "))
        b = float(input("Inserisci il Secondo Numero -> "))
        print("Il risultato dell'Addizione è: ", str(a + b))
    elif action == "2":
        print("\nHai scelto: Sottrazione\n")
        a = float(input("Inserisci il Primo Numero -> "))
        b = float(input("Inserisci il Secondo Numero -> "))
        print("Il risultato dell'Sottrazione è: ", str(a - b))
    elif action == "3":
        print("\nHai scelto: Moltiplicazione\n")
        a = float(input("Inserisci il Primo Numero -> "))
        b = float(input("Inserisci il Secondo Numero -> "))
        print("Il risultato dell'Moltiplicazione è: ", str(a * b))
    elif action == "4":
        print("\nHai scelto: Divisione\n")
        a = float(input("Inserisci il Primo Numero -> "))
        b = float(input("Inserisci il Secondo Numero -> "))
        print("Il risultato dell'Divisione è: ", str(a / b))
    elif action == "5":
        print("\nHai scelto: Calcolo Esponenziale\n")
        a = float(input("Inserisci la Base -> "))
        b = float(input("Inserisci l'Esponente -> "))
        print("Il risultato del Calcolo Esponenziale è: ", str(a ** b))
    elif action == "6":
        print("\nHai scelto: Radice Quadrata\n")
        a = float(input("Inserisci il Numero -> "))
        print("Il risultato dell'operazione è: ", str(sqrt(a)))
    elif action == "ESC":
        print("\nL'Applicazione verrà chiusa!\n")
        break
