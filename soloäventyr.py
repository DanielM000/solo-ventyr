import random
import time

# VARIABLER I SPELET
# rum håller reda på vilket rum som spelaren är i
# spelet starta i cellen
rum = "cellen"

def slow_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()
menu = True
mellansekvens_1 = False
spelet_körs = False




while menu:
    slow_print("1. Starta spelet\n2. Avsluta")
    menu_val = input("Vad vill du göra: ")
    if menu_val == "1":
        slow_print("Startar spelet...")
        mellansekvens_1 = True
        menu = False
    elif menu_val == "2":
        slow_print("Lämnar spelet...")
        menu = False
    else:
        slow_print("Ogiltigt, försök igen.")
        continue

while mellansekvens_1:
    slow_print("Du hittar dig själv inne i en cell med en säng, en papperskorg, ett fönster\noch en sink, dörren är låst men den har ett nyckelhål, hitta ett sätt att fly.")
    spelet_körs = True
    mellansekvens_1 = False


def mellansekvens_den_andra():
    slow_print("Du smyger framåt tills du närmar en korridor, plötsligt ser du en vakt och \ndu kan inte gå förbi utan att bli upptäckt.")

mellansekvens_den_andra()

# RUM 1
def cell(rum):
    spel = True
    nyckel = False
    
    while spel:
        slow_print("1. Kolla under sängen\n2. Kolla in i papperskorgen\n3. Kolla på fönstret\n4. Kolla in i sinken\n5. Öppna dörren")
        cell_val = input("Vad vill du göra: ")
        if cell_val == "1" or cell_val == "2" or cell_val == "3":
            slow_print("Du hittar inget.")
        elif cell_val == "4":
            slow_print("Du hittar en nyckel.")
            nyckel = True
        elif cell_val == "5" and nyckel == False:
            slow_print("Dörren är låst.")
        elif cell_val == "5" and nyckel == True:
            slow_print("Du öppnar dörren med nyckeln och smitter förbi...")
            rum = "korridor"
            
            return rum
        else:
            slow_print("Ogiltigt, försök igen.")
            continue

# RUM 2
def korridor(rum):
    print("Du är i rum 2")
    rum = "slut"
    return rum

# Spel loop
while (spelet_körs == True):
    if (rum == "cellen"):
       rum = cell(rum)
    elif (rum == "korridor"):
       rum = korridor(rum)
    elif (rum == "slut"):
        break