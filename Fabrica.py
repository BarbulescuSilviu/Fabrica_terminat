import json



menu1 = ["1.Lista angajati","2.Adaugare angajati", "3.Eliminare angajati", "4.Modificare calificari angajati",
                 "0.Iesire"]
menu2 = ["1.Lista angajati", "2.Produse create in fabrica ", "0.Iesire"]
menu3 = ["1.Adauga accesorii:","2.Schimba stoc accesorii:","3.Adauga produse noi:","4.Schimba stoc produse:"
                 ,"0.Iesire"]

class Operator:

    def __init__(self, functie, id_unic, nume, prenume, calificare):
        self.functie = functie
        self.id_unic = id_unic
        self.nume = nume
        self.prenume = prenume
        self.calificare = calificare


    def oper_lista_operatori(self):
        print(30 * "*")
        print("Lista de angajati:")
        print(30 * "*")
        file = open("angajati.json", "r")
        anga222 = json.load(file)
        file.close()
        for aa4 in anga222:
            print(f'{aa4}. {anga222[aa4][0]} {anga222[aa4][1]} {anga222[aa4][4]}')


    def produse_fabrica(self):
        file = open("produse.json", "r")
        qwe = json.load(file)
        file.close()
        for e in qwe:
            print(f"{e}. {qwe[e][0]}")





class Manager(Operator):
    def __init__(self, functie, id_unic, nume, prenume, calificare):
        super().__init__(functie, id_unic, nume, prenume, calificare)

    def lista_angajati(self):
            print("Lista angajati")
            file = open("angajati.json", "r")
            anga22 = json.load(file)
            for aaa in anga22:
                print(f'{aaa}. {anga22[aaa][0]} {anga22[aaa][1]} {anga22[aaa][4]}')
            file.close()


    def adaugare_angajat(self):
        print("Adauga un angajat:")
        nume = input("Nume:\n>")
        prenume = input("Prenume:\n>")
        idd = int(input("Id:\n>"))
        functie = input("Functie")
        calificare = input("Calificare:\n>")
        new_user = [nume, prenume, idd, functie, calificare]
        file = open("angajati.json", "r")
        angajati = json.load(file)
        file.close()
        angajati[len(angajati) + 1] = new_user
        file = open("angajati.json", "w")
        file.write(json.dumps(angajati, indent=4))
        file.close()
        print("Ai adaugat un angajat!")

    def stergere_angajat(self):
        print("Ai ales sa stergi un angajat!")
        file = open("angajati.json", "r")
        ang = json.load(file)
        file.close()
        for w in ang:
            print(f"{w}.{ang[w][0]} {ang[w][1]}")
        print("0.Exit")
        delete_user = input()
        if delete_user == 0:
            return False
        update_ang = ang.copy()
        for del_user in ang:
            if del_user == delete_user:
                update_ang.pop(del_user)
        file_ang = open("angajati.json", "w")
        file_ang.write(json.dumps(update_ang, indent=2))
        file_ang.close()

        print(30 * "*")
        print("Angajatul a fost sters")
        print(30 * "*")
        file = open("angajati.json", "r")
        anga2 = json.load(file)
        file.close()
        for aa in anga2:
            print(f'{aa}. {anga2[aa][0]} {anga2[aa][1]} {anga2[aa][4]}')

    def schimbare_calificare(self):
        print("Schimbare calificare:")
        file = open("angajati.json", "r")
        anga = json.load(file)
        file.close()

        for a in anga:
            if anga[a][3] == "operator" or "gestionar":
                print(f'{a}. {anga[a][0]} {anga[a][1]} {anga[a][4]}')
        user_calificare = input("\n>")
        for ang in anga:
            if ang == user_calificare:
                calificare_noua = input("Noua calificare:[Electrician, Electronist, Pirotehnist, Designer]\n>")
                anga[a][4] = calificare_noua

        file_ang2 = open("angajati.json", "w")
        file_ang2.write(json.dumps(anga, indent=4))
        file_ang2.close()
        print(40 * "*")
        print("Calificarea a fost schimbata!")
        print(40 * "*")


class Gestionar(Manager):
    def __init__(self, functie, id_unic, nume, prenume, calificare, cartuse, praf_de_pusca, luneta,incarcator):
        super().__init__(functie, id_unic, nume, prenume, calificare)
        self.cartuse = cartuse
        self.praf_de_pusca = praf_de_pusca
        self.luneta = luneta
        self.incarcator = incarcator


    def adauga_accesorii(self):
        print("Adauga accesorii:")
        nume = input("Nume:\n>")
        cantitate = input("Cantitate:\n>")
        fabr = [nume, cantitate]

        file = open("materie_prima.json", "r")
        er = json.load(file)
        file.close()
        er[len(er)+1] = fabr
        file = open("materie_prima.json", "w")
        file.write(json.dumps(er, indent=4))
        file.close()
        print("*** Ati introdus un accesoriu nou! ***")

        for oo in er:
            print(f"{oo} - {er[oo][0]} - {er[oo][1]}")

    def schimbare_stoc_accesorii(self):
        files1 = open("materie_prima.json", "r")
        mmp = json.load(files1)
        files1.close()

        print("*** Alege produsul caruia doresti sa-i schimbi valoarea: ***")
        for pp in mmp:
            print(f"{pp}.{mmp[pp][0]} - {mmp[pp][1]}")
        materie_prima = input("\n>")
        for www in mmp:
            if www == materie_prima:
                new_materie = int(input("Cantitate noua:\n>"))
                mmp[www][1] = new_materie


        files1 = open("materie_prima.json", "w")
        files1.write(json.dumps(mmp))
        files1.close()
        print("*** Cantitate schimbata! ***")

        files1 = open("materie_prima.json", "r")
        verific = json.load(files1)
        files1.close()
        for r in verific:
            print(f"{r} - {verific[r][0]} - {verific[r][1]}")

    def adauga_produse(self):
        files = open("produse.json", "r")
        produse = json.load(files)
        files.close()
        print("*** Adauga produs nou! ***:")
        nume = input("Nume:\n>")
        cantitate = input("Cantitate:\n>")
        pro = [nume, cantitate]

        file = open("produse.json", "r")
        era = json.load(file)
        file.close()
        era[len(era) + 1] = pro

        file = open("produse.json", "w")
        file.write(json.dumps(era, indent=4))
        file.close()

        print("*** Ati introdus un produs nou! ***")
        file = open("produse.json", "r")
        eraq = json.load(file)
        file.close()
        for oo1 in eraq:
            print(f"{oo1} - {eraq[oo1][0]} - {eraq[oo1][1]}")


    def schimbare_stoc_produse(self):
        files = open("produse.json", "r")
        produse1 = json.load(files)
        files.close()

        print("*** Alege produsul caruia doresti sa-i schimbi valoarea: ***")
        for ppp in produse1:
            print(f"{ppp}.{produse1[ppp][0]} - {produse1[ppp][1]}")

        produs = input("Alege produs:\n>")
        for wq in produse1:
            if wq == produs:
                prod_nou = int(input("Cantitate noua:\n>"))
                produse1[wq][1] = prod_nou
        files1 = open("produse.json", "w")
        files1.write(json.dumps(produse1, indent=4))
        files1.close()
        print("*** Cantitate schimbata! ***")

        files1 = open("produse.json", "r")
        verific2 = json.load(files1)
        files1.close()

        for r in verific2:
            print(f"{r}. {verific2[r][0]} - {verific2[r][1]}")




# '''De aici se ruleaza programul'''
    def log__in(self):
        while True:
            log = int(input("Logheaza-te\n>"))
            fila = open("angajati.json", "r")
            angajati1 = json.load(fila)
            fila.close()
            for i in angajati1:
                if log == angajati1[i][2] and angajati1[i][3] == "manager":
                    print("***Esti manager!***")
                    while True:
                        for c in menu1:
                            print(c)
                        option = input()
                        if option == "1":
                            1 == Manager.lista_angajati(self)
                            print("0.Exit")
                            b = input(">")
                            if b == "0":
                                continue

                        elif option == "2":
                            2 == Manager.adaugare_angajat(self)
                            print("0.Exit")
                            b = input(">")
                            if b == "0":
                                continue
                        elif option == "3":
                            3 == Manager.stergere_angajat(self)
                            print("0.Exit")
                            b = input(">")
                            if b == "0":
                                continue
                        elif option == "4":
                            4 == Manager.schimbare_calificare(self)
                            print("0.Exit")
                            b = input(">")
                            if b == "0":
                                continue
                        elif option == "0":
                            break



                elif log == angajati1[i][2] and angajati1[i][3] == "operator":
                    print("***  Esti operator!  ***")
                    for r in menu2:
                        print(r)
                    option2 = input()
                    if option2 == "1":
                        1 == Operator.oper_lista_operatori(self)
                        print("0.Exit")
                        b = input(">")
                        if b == "0":
                            continue
                    elif option2 == "2":
                        2 == Operator.produse_fabrica(self)
                        print("0.Exit")
                        b = input(">")
                        if b == "0":
                            continue
                    elif option2 == "0":
                        break
                elif log == angajati1[i][2] and angajati1[i][3] == "gestionar":
                    print("*** Esti gestionar! ***")
                    while True:
                        for t in menu3:
                            print(t)
                        option3 = input()
                        if option3 == "1":
                            1 == Gestionar.adauga_accesorii(self)
                            print("0.Exit")
                            b = input(">")
                            if b == "0":
                                continue
                        if option3 == "2":
                            2 == Gestionar.schimbare_stoc_accesorii(self)
                            print("0.Exit")
                            b = input(">")
                            if b == "0":
                                continue
                        if option3 == "3":
                            3 == Gestionar.adauga_produse(self)
                            print("0.Exit")
                            b = input(">")
                            if b == "0":
                                continue
                        if option3 == "4":
                            4 == Gestionar.schimbare_stoc_produse(self)
                            print("0.Exit")
                            b = input(">")
                            if b == "0":
                                continue
                        if option3 == "0":
                            return False







a = Gestionar("functie", "id_unic", "nume", "prenume", "calificare","cartuse", "praf_de_pusca", "luneta","incarcator")


a.log__in()

