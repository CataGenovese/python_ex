with open("didac.txt", 'r', encoding='utf-8') as f_noms:

    with open("frases.txt", 'r', encoding='utf-8') as f_cos:

        cos = f_cos.read()

        for nom in f_noms:
            missatge = "Hola " + nom.strip() + "\n" + cos # strip elimina els espais
            # escribim les dades a arxius individuals
            with open(nom.strip()+".txt", 'w', encoding='utf-8') as f_composicio:
                f_composicio.write(missatge)