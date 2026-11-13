def calculadora():
    print ("1 = +, 2 = -, 3 = *, 4 = /")
    print("Las operacions que son disponibles son +, -, * y /")
    operacio_ingresa_usuari = int(input("Que operacion desea usar? "))
    num_1 = int(input("Que primer numero desea usar? "))
    num_2 = int(input("Que segundo numero desea usar? "))
    if operacio_ingresa_usuari == 1:
        return num_1 + num_2
    elif operacio_ingresa_usuari == 2:
            return num_1 - num_2
    elif operacio_ingresa_usuari == 3:
            return num_1 * num_2
    elif operacio_ingresa_usuari == 4:
            return num_1 / num_2
    else:
          return "Esta operacion que has ingresado no esta disponible"
print(calculadora())