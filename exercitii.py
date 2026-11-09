# Exercițiul 1 + 5 + 2

#inceput

print("=== Bun venit la aplicație! ===")
nume = input("Cum te cheamă? ")
print(f"Salut, {nume}!")

#numaratoare plus desen

print("\nNumărătoare:")
for i in range(10, 0, -1):
    print(f"{i}")
print("Start!")

print("\nChenar:")
latime = 20
inaltime = 6

#partea de sus
print("-" * latime) 
for _ in range(inaltime - 2):
    print("|" + " "* (latime - 2) + "|")

#partea de jos
print("-" * latime) 

#calculul varstei peste 5 ani, daca e par sau impar.
varsta = int(f"{input('\nCâți ani ai? ')}")
print(f"Peste 5 ani vei avea {varsta + 5} ani.")
if varsta % 2 == 0:
    print("Vârsta ta este un număr par. Ce să vezi, ești norocos!")
else:
    print("Vârsta ta este un număr impar. Ia te uită! Tare, nu?")
print("Îți mulțumim pentru utilizarea aplicației!")
if varsta < 22:
    print("Ai o vârstă frumoasă! Bucură-te de viață!")
if varsta >= 22 and varsta < 70:
    print("Deja...viața devine serioasă. Ai grijă de tine!")
if varsta >= 70:
    print("Ai o experiență de viață bogată! Sau..minți.. tu sa-mi spui ce simți!")

raspuns = input("\nMinti sau nu? (da/nu): ")
if raspuns == "da":
    print("Aha! Am intuit eu că minți! Nu-i nimic, ești un om deosebit!")
else:
    print("Mă bucur că ești sincer! Ești un om deosebit!")