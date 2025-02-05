import random
import time

# VARIABLER I SPELET
# rum håller reda på vilket rum som spelaren är i
# spelet starta i meny
rum = "meny"
letråd_1 = False
letråd_2 = False
letråd_3 = False

# Slow print
def slow_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

# Mellansekvenser
def mellansekvens_1():
    slow_print("Du befinner dig själv inne i en cell med en säng, en papperskorg, ett fönster\noch en sink, dörren är låst men den har ett nyckelhål, hitta ett sätt att fly.\n")

def mellansekvens_2():
    slow_print("Du smyger framåt tills du närmar en korridor, plötsligt ser du en vakt och\ndu kan inte gå förbi utan att bli upptäckt.\n")

def mellansekvens_3():
    slow_print("Du fortsätter smygga fram i korridoren tills du ser två vägar, en till vänster\noch en till höger.\n")

def mellansekvens_4():
    slow_print("Du närmar dig ett rum men plötsligt ser du en hund som vaktar en dörr,\ndu kan inte gå förbi utan att bli upptäckt.\n")

def mellansekvens_5():
    slow_print("Du närmar dig ett rum med en dörr men dörren är låst, du behöver skriva \nin rätt tre siffrig kod, annars så går alarmet efter tre fel försök.\n")

# RUM 1
def cell(rum, letråd_1, letråd_2, letråd_3):
    spel = True
    nyckel = False
    mellansekvens_1()
    
    while spel:
        cell_val = input("1. Kolla under sängen\n2. Kolla in i papperskorgen\n3. Kolla på fönstret\n4. Kolla in i sinken\n5. Öppna dörren\nVad vill du göra:\n")
        if cell_val == "1" or cell_val == "3":
            slow_print("Du hittar inget.\n")
        elif cell_val == "2" and letråd_1 == False:
            slow_print("Du hittar ett papper, det står: Hur många färger har en regnbåge?\n")
            letråd_1 = True
        elif cell_val == "2" and letråd_1 == True:
            slow_print("Du hittar inget.\n")
        elif cell_val == "4" and nyckel == False:
            slow_print("Du hittar en nyckel.\n")
            nyckel = True
        elif cell_val == "4" and nyckel == True:
            slow_print("Du hittar inget.\n")
        elif cell_val == "5" and nyckel == False:
            slow_print("Dörren är låst.\n")
        elif cell_val == "5" and nyckel == True:
            slow_print("Du öppnar dörren med nyckeln och smiter förbi...\n")
            rum = "korridor"
            break
        else:
            slow_print("Ogiltigt, försök igen.\n")
            continue
    return rum, letråd_1, letråd_2, letråd_3

# RUM 2
def korridor(rum, letråd_1, letråd_2, letråd_3):
    spel = True
    vakt_borta = False
    distraktion = False
    mellansekvens_2()

    while spel:
        korridor_val = input("1. Smyg förbi\n2. Leta efter något i marken\n3. Distrahera vakten\n4. Gå tillbaka\nVad vill du göra:\n")
        if korridor_val == "1" and vakt_borta == False:
            slow_print("Vakten ser dig och fångar dig, han drar dig tillbaka till din cell...\n")
            rum = "cell"
            break
        elif korridor_val == "1" and vakt_borta == True:
            slow_print("Du smitter genom korridoren...\n")
            rum = "vägar"
            break
        elif korridor_val == "2" and distraktion == False:
            slow_print("Du hittar en sten.\n")
            distraktion = True
        elif korridor_val == "2" and distraktion == True and letråd_2 == False:
            slow_print("Du hittar ett papper, det står: Hur många ben har en spindel?\n")
            letråd_2 = True
        elif korridor_val == "2" and distraktion == True and letråd_2 == True:
            slow_print("Du hittar inget.\n")
        elif korridor_val == "3" and distraktion == False and vakt_borta == False:
            slow_print("Du har ingeting att distrahera med.\n")
        elif korridor_val == "3" and distraktion == True and vakt_borta == False:
            slow_print("Du kastar stenen bakom dig och gömmer dig vid en hörn, vakten går mot ljudet utan att se dig.\n")
            vakt_borta = True
        elif korridor_val == "3" and distraktion == True and vakt_borta == True:
            slow_print("Vakten är redan borta.\n")
        elif korridor_val == "4":
            slow_print("Du går tillbaka till förra rummet...\n")
            rum = "cell"
            break
        else:
            slow_print("Ogiltigt, försök igen.\n")
            continue
    return rum, letråd_1, letråd_2, letråd_3

# RUM 3
def vägar(rum, letråd_1, letråd_2, letråd_3):
    spel = True
    mellansekvens_3()

    while spel:
        vägar_val = input("1. Gå vänster\n2. Gå höger\n3. Gå tillbaka\nVad vill du göra:\n")
        if vägar_val == "1":
            slow_print("Du går vänster...\n")
            rum = "kod"
            break
        elif vägar_val == "2":
            slow_print("Du går höger...\n")
            rum = "hund"
            break
        elif vägar_val == "3":
            slow_print("Du går tillbaka till förra rummet...\n")
            rum = "korridor"
            break
        else:
            slow_print("Ogiltigt, försök igen.\n")
            continue
    return rum, letråd_1, letråd_2, letråd_3

# RUM 4
def hund(rum, letråd_1, letråd_2, letråd_3):
    spel = True
    hund_borta = False
    distraktion = False
    mellansekvens_4()

    while spel:
        hund_val = input("1. Gå fram\n2. Leta efter något i marken\n3. Distrahera hunden\n4. Gå tillbaka\nVad vill du göra:\n")
        if hund_val == "1" and hund_borta == False:
            slow_print("Hunden ser dig och biter dig i benen, vakten kommer och han drar dig tillbaka till din cell...\n")
            rum = "cell"
            break
        elif hund_val == "1" and hund_borta == True:
            slow_print("Du går till dörren utan problem, du öppnar dörren...\n")
            rum = "slut_1"
            break
        elif hund_val == "2" and distraktion == False:
            slow_print("Du hittar en liten boll.\n")
            distraktion = True
        elif hund_val == "2" and distraktion == True and letråd_3 == False:
            slow_print("Du hittar ett papper, det står: Hur många hjärtan har en bläckfisk?\n")
            letråd_3 = True
        elif hund_val == "2" and distraktion == True and letråd_3 == True:
            slow_print("Du hittar inget.\n")
        elif hund_val == "3" and distraktion == False and hund_borta == False:
            slow_print("Du har ingeting att distrahera med.\n")
        elif hund_val == "3" and distraktion == True and hund_borta == False:
            boll_kast = input("1. Kasta bollen kort fram\n2. Kasta bollen långt fram\nVad vill du göra:\n")
            if boll_kast == "1":
                slow_print("Hunden går fram, tar bollen och går iväg med den.\n")
                hund_borta = True
            elif boll_kast == "2":
                slow_print ("Hunden går fram, tar bollen men går fram mot dig och ser dig, hunden biter dig i benen och vakten kommer, han drar dig tillbaka till din cell...\n")
                rum = "cell"
                break
            else:
                slow_print("Ogiltigt, försök igen.\n")
                continue
        elif hund_val == "3" and distraktion == True and hund_borta == True:
            slow_print("Hunden är redan borta.\n")
        elif hund_val == "4":
            slow_print("Du går tillbaka till förra rummet...\n")
            rum = "vägar"
            break
        else:
            slow_print("Ogiltigt, försök igen.\n")
            continue
    return rum, letråd_1, letråd_2, letråd_3

# RUM 5
def kod(rum, letråd_1, letråd_2, letråd_3):
    spel = True
    alarm = 0
    mellansekvens_5()

    while spel:
        kod_val = input("1. Skriv in koden\n2. Läs letrådarna\n3. Gå tillbaka\nVad vill du göra:\n")
        if kod_val == "1":
            skriv_kod = input("Skriv koden:\n")
            if skriv_kod == "783":
                slow_print("Du skriver rätt kod, du öppnar dörren...\n")
                rum = "slut_2"
                break
            else:
                slow_print("Du skriver fel kod.\n")
                alarm = alarm + 1
        elif kod_val == "2":
            if letråd_1 == True:
                slow_print("Hur många färger har en regnbåge?\n")
            if letråd_2 == True:
                slow_print("Hur många ben har en spindel?\n")
            if letråd_3 == True:
                slow_print("Hur många hjärtan har en bläckfisk?\n")
        elif kod_val == "3":
            slow_print("Du går tillbaka till förra rummet...\n")
            rum = "vägar"
            break
        if alarm == 3:
            slow_print("Alarmet går och vakten kommer, han drar dig tillbaka till din cell...\n")
            rum = "cell"
            break
        else:
            slow_print("Ogiltigt, försök igen.\n")
            continue
    return rum, letråd_1, letråd_2, letråd_3

# Spel loop
def spel_loop(rum, letråd_1, letråd_2, letråd_3):
    spelet_körs = True
    
    while (spelet_körs == True):
        if (rum == "cell"):
            rum, letråd_1, letråd_2, letråd_3 = cell(rum, letråd_1, letråd_2, letråd_3)
        elif (rum == "korridor"):
            rum, letråd_1, letråd_2, letråd_3 = korridor(rum, letråd_1, letråd_2, letråd_3)
        elif (rum == "vägar"):
            rum, letråd_1, letråd_2, letråd_3 = vägar(rum, letråd_1, letråd_2, letråd_3)
        elif (rum == "hund"):
            rum, letråd_1, letråd_2, letråd_3 = hund(rum, letråd_1, letråd_2, letråd_3)
        elif (rum == "kod"):
            rum, letråd_1, letråd_2, letråd_3 = kod(rum, letråd_1, letråd_2, letråd_3)
        elif (rum == "slut_1"):
            slow_print("Du är utanför fängelset nu och du springer så snabbt du kan men du blir träffad\nav en prickskytt, du ligger i marken och dör.\n \nSlut 1")
            spelet_körs = False
        elif (rum == "slut_2"):
            slow_print("Du är utanför fängelset nu, du hittar en öppen bil och gör iväg från fängelset\n \nSlut 2")
            spelet_körs = False
        elif (rum == "meny"):
            rum = meny(rum)

# Meny
def meny(rum):
    menu = True
    readme = open("soloäventyr/readme.txt", "r", encoding = "utf-8")
    while menu:
        menu_val = input("1. Starta spelet\n2. Avsluta\n3. Visa instruktioner\nVad vill du göra:\n")
        if menu_val == "1":
            slow_print("Startar spelet...\n")
            rum = "cell"
            return rum
        elif menu_val == "2":
            slow_print("Lämnar spelet...")
            menu = False
        elif menu_val == "3":
            print(readme.read())
        else:
            slow_print("Ogiltigt, försök igen.")
            continue

spel_loop(rum, letråd_1, letråd_2, letråd_3)