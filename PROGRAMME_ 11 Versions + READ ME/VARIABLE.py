def indice_variable (mot):
    if mot == "Bruit":
        return 0
    elif mot == "température":
        return 1
    elif mot == "Humidité":
        return 2
    elif mot == "luminosité":
        return 3
    elif mot == "CO2":
        return 4 
    elif mot == "humidex":
        return 5
    else : 
        raise NameError ("Veuillez chosir entre c'est 6 variable: Bruit, Température, Humidité, Luminosité, CO2, Humidex")

print (indice_variable("CO2"))
