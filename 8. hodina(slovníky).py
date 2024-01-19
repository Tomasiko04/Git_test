# zamestnanec1 = ["Petr", "Novák", "Olomouc", 779 00, True]
# zamestnanec2 = ["Petr", "Malý", "Prostějov", 775 44, True]
# zamestnanec3 = ["Jan", "Velký", "Přerov", False]

# print(zamestnanec1[1])
# print(zamestnanec1[3])
# print(zamestnanec3[3])

# zamestnaneci=[zamestnanec1,zamestnanec2,zamestnanec3]

# for zamestnanec in zamestnaneci:
#     print(zamestnanec[1])


#klíč:hodnota keys: value Neni možnost duplicita klíčů

zamestnanec1 = {"name": "Jon", "age": 30, "city":"NY" }
print(zamestnanec1)

#lepší zápis přehlednost
zamestnanec2={
    "name": "Marry",
    "age": 30,
    "city": "Paris",
}
#print(zamestnanec2)


#založení slovníku
muj_novy_slovnik={}
muuj_novy_slovnik_2=dict()
#založení množiny
moje_mnozina= set()

print(muj_novy_slovnik)
muj_novy_slovnik["jmeno"]="Lukas"
print(muj_novy_slovnik)
muj_novy_slovnik["ridicak"]=True
muj_novy_slovnik["hobby"]=("fotbal", "hry", "zahálka", "spánek")
muj_novy_slovnik["vek"]=22
muj_novy_slovnik["jmeno"]="Matej"

print(muj_novy_slovnik)

print(muj_novy_slovnik["jmeno"])
print(muj_novy_slovnik["hobby"])
print(muj_novy_slovnik["hobby"][0])


#ZÁKLADNÍ METODY
print(muj_novy_slovnik.keys())
print(muj_novy_slovnik.values())
print(muj_novy_slovnik.items())

student={
    "name": "John",
    "age": 25,
    "courses": ["Math", "CompSci"]       
    }

for value in student.values():
    print(value)
