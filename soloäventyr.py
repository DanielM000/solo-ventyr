import random
import time

# VARIABLER I SPELET
# rum håller reda på vilket rum som spelaren är i
# spelet starta i cellen
rum = "meny"
letråd_1 = False
letråd_2 = False
letråd_3 = False

def slow_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

def mellansekvens_1():
    slow_print("Du befinner dig själv inne i en cell med en säng, en papperskorg, ett fönster\noch en sink, dörren är låst men den har ett nyckelhål, hitta ett sätt att fly.")

def mellansekvens_2():
    slow_print("Du smyger framåt tills du närmar en korridor, plötsligt ser du en vakt och\ndu kan inte gå förbi utan att bli upptäckt.")

def mellansekvens_3():
    slow_print("Du fortsätter smygga fram i korridoren tills du ser två vägar, en till vänster\noch en till höger.")

def mellansekvens_4():
    slow_print("Du närmar dig ett rum men plötsligt ser du en hund som vaktar en dörr,\ndu kan inte gå förbi utan att bli upptäckt.")

def mellansekvens_5():
    slow_print("Du närmar dig ett rum med en dörr men dörren är låst, du behöver skriva \nin rätt tre siffrig kod, annars så går alarmet efter tre fel försök.")

# RUM 1
def cell(rum):
    spel = True
    nyckel = False
    mellansekvens_1()
    
    while spel:
        cell_val = input("1. Kolla under sängen\n2. Kolla in i papperskorgen\n3. Kolla på fönstret\n4. Kolla in i sinken\n5. Öppna dörren\nVad vill du göra: ")
        if cell_val == "1" or cell_val == "3":
            slow_print("Du hittar inget.")
        elif cell_val == "2" and letråd_1 == False:
            slow_print("Du hittar ett papper, det står: Hur många färger har en regnbåge?")
            letråd_1 = True
        elif cell_val == "2" and letråd_1 == True:
            slow_print("Du hittar inget.")
        elif cell_val == "4" and nyckel == False:
            slow_print("Du hittar en nyckel.")
            nyckel = True
        elif cell_val == "4" and nyckel == True:
            slow_print("Du hittar inget.")
        elif cell_val == "5" and nyckel == False:
            slow_print("Dörren är låst.")
        elif cell_val == "5" and nyckel == True:
            slow_print("Du öppnar dörren med nyckeln och smiter förbi...")
            rum = "korridor"
            return rum
        else:
            slow_print("Ogiltigt, försök igen.")
            continue

# RUM 2
def korridor(rum):
    spel = True
    vakt_borta = False
    distraktion = False
    mellansekvens_2()

    while spel:
        korridor_val = input("1. Smyg förbi\n2. Leta efter något i marken\n3. Distrahera vakten\nVad vill du göra: ")
        if korridor_val == "1" and vakt_borta == False:
            slow_print("Vakten ser dig och fångar dig, han drar dig tillbaka till din cell...")
            rum = "cell"
            return rum
        elif korridor_val == "1" and vakt_borta == True:
            slow_print("Du smitter genom korridoren...")
            rum = "vägar"
            return rum
        elif korridor_val == "2" and distraktion == False:
            slow_print("Du hittar en sten.")
            distraktion = True
        elif korridor_val == "2" and distraktion == True and letråd_2 == False:
            slow_print("Du hittar ett papper, det står: Hur många ben har en spindel?")
            letråd_2 = True
        elif korridor_val == "2" and distraktion == True and letråd_2 == True:
            slow_print("Du hittar inget.")
        elif korridor_val == "3" and distraktion == False and vakt_borta == False:
            slow_print("Du har ingeting att distrahera med.")
        elif korridor_val == "3" and distraktion == True and vakt_borta == False:
            slow_print("Du kastar stenen bakom dig och gömmer dig vid en hörn, vakten går mot ljudet utan att se dig.")
            vakt_borta = True
        elif korridor_val == "3" and distraktion == True and vakt_borta == True:
            slow_print("Vakten är redan borta.")
        else:
            slow_print("Ogiltigt, försök igen.")
            continue

# RUM 3
def vägar(rum):
    spel = True
    mellansekvens_3()

    while spel:
        vägar_val = input("1. Gå vänster\n2. Gå höger\nVad vill du göra: ")
        if vägar_val == "1":
            slow_print("Du går vänster...")
            rum = "kod"
            return rum
        elif vägar_val == "2":
            slow_print("Du går höger...")
            rum = "hund"
            return rum
        else:
            slow_print("Ogiltigt, försök igen.")
            continue

# RUM 4
def hund(rum):
    spel = True
    hund_borta = False
    distraktion = False
    mellansekvens_4()

    while spel:
        hund_val = input("1. Gå fram\n2. Leta efter något i marken\n3. Distrahera hunden\nVad vill du göra: ")
        if hund_val == "1" and hund_borta == False:
            slow_print("Hunden ser dig och biter dig i benen, vakten kommer och han drar dig tillbaka till din cell...")
            rum = "cell"
            return rum
        elif hund_val == "1" and hund_borta == True:
            slow_print("Du går till dörren utan problem, du öppnar dörren...")
            rum = "slut_1"
            return rum
        elif hund_val == "2" and distraktion == False:
            slow_print("Du hittar en liten boll.")
            distraktion = True
        elif hund_val == "2" and distraktion == True and letråd_3 == False:
            slow_print("Du hittar ett papper, det står: Hur många hjärtan har en bläckfisk?")
            letråd_3 = True
        elif hund_val == "2" and distraktion == True and letråd_3 == True:
            slow_print("Du hittar inget.")
        elif hund_val == "3" and distraktion == False and hund_borta == False:
            slow_print("Du har ingeting att distrahera med.")
        elif hund_val == "3" and distraktion == True and hund_borta == False:
            boll_kast = input("1. Kasta bollen kort fram\n2. Kasta bollen långt fram\nVad vill du göra: ")
            if boll_kast == "1":
                slow_print("Hunden går fram, tar bollen och går iväg med den.")
                hund_borta = True
            elif boll_kast == "2":
                slow_print ("Hunden går fram, tar bollen men går fram mot dig och ser dig, hunden biter dig i benen och vakten kommer, han drar dig tillbaka till din cell...")
                rum = "cell"
                return rum
            else:
                slow_print("Ogiltigt, försök igen.")
                continue
        elif hund_val == "3" and distraktion == True and hund_borta == True:
            slow_print("Hunden är redan borta.")
        else:
            slow_print("Ogiltigt, försök igen.")
            continue

# RUM 5
def kod(rum):
    spel = True
    alarm = 0
    mellansekvens_5()

    while spel:
        kod_val = input("1. Skriv in koden\n2. Läs letrådarna\n3. Gå tillbaka\nVad vill du göra: ")
        if kod_val == "1":
            skriv_kod == input("Skriv koden: ")
            if skriv_kod == "783":
                slow_print("Du skriver rätt kod, du öppnar dörren...")
                rum = "slut_2"
                return rum
            else:
                slow_print("Du skriver fel kod.")
                alarm += 1
        elif kod_val == "2":
            if letråd_1 == True:
                slow_print("Hur många färger har en regnbåge?")
            if letråd_2 == True:
                slow_print("Hur många ben har en spindel?")
            if letråd_3 == True:
                slow_print("Hur många hjärtan har en bläckfisk?")
        elif kod_val == "3":
            slow_print("Du går tillbaka till förra rummet...")
            rum = "vägar"
            return rum
        elif alarm == 3:
            slow_print("Alarmet går och vakten kommer, han drar dig tillbaka till din cell...")
            rum = "cell"
            return rum
        else:
            slow_print("Ogiltigt, försök igen.")
            continue

# Spel loop
def spel_loop(rum):
    spelet_körs = True
    
    while (spelet_körs == True):
        if (rum == "cell"):
            rum = cell(rum)
        elif (rum == "korridor"):
            rum = korridor(rum)
        elif (rum == "vägar"):
            rum = vägar(rum)
        elif (rum == "hund"):
            rum = hund(rum)
        elif (rum == "kod"):
            rum = kod(rum)
        elif (rum == "slut_1"):
            break
        elif (rum == "slut_2"):
            break
        elif (rum == "meny"):
            rum = meny(rum)

def meny(rum):
    menu = True
    while menu:
        slow_print("1. Starta spelet\n2. Avsluta\n3. Visa instruktioner")
        menu_val = input("Vad vill du göra: ")
        if menu_val == "1":
            slow_print("Startar spelet...")
            rum = "cell"
            return rum
            

        elif menu_val == "2":
            slow_print("Lämnar spelet...")
            menu = False
        elif menu_val == "3":
            print("\n")
            filnamn = "readme.txt"

            try:
                with open(filnamn, "r", encoding="utf-8") as fil:
                    innehål = fil.read()
                    print(innehål)
                    input("\nTryck på valfri tangent")
            except FileNotFoundError:
                print(f"Filen {filnamn} kunde inte hittas")
                input("\nTryck på valfri tangent")
            except Exception as e:
                print(f"Ett fel inträffade: {e}")
                input("\nTryck på valfri tangent")
        else:
            slow_print("Ogiltigt, försök igen.")
            continue

spel_loop(rum)