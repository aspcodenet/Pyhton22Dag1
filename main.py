# print("Hello world")
# print("Då")
# print("2022-12-24")
# print(2022-12-24)


# namn = input("vad heter du:")   #Stefan
# resultatet = namn + namn + namn + namn + namn # StefanStefanStefanStefanStefan
# resultatet = namn*5 # StefanStefanStefanStefanStefan

#Skriv ett program som tar ett TAL (int) som input. Det ska skriva ut 
# False om talet 
# är mindre än 100 och True om det är större eller lika med 100, 
#OBS: Utan If-satser. (skriv direkt ut resultat från jämförelsen)
# ´



from unittest.mock import PropertyMock


age = int(input("Hur gammal är du?"))
location = input("Var är du") # K eller S
promilleHalt = float(input("Din promillehalt")) # flyttal

# if promilleHalt < 1.0:
#     if age >= 18 and location == "K":
#         print("Japp du får köpa")
#     elif age >= 20 and location == "S":
#         print("Japp du får köpa")
#     else:
#         print("Nope ingen öl")        
# else:
#     print("Nope ingen öl")        

# if promilleHalt >= 1.0:
#     print("Nope ingen öl")
# elif age >= 18 and location == "K":
#     print("Japp du får köpa")
# elif age >= 20 and location == "S":
#     print("Japp du får köpa")
# else:
#     print("Nope ingen öl")    

if age >= 18 and location == "K" and promilleHalt < 1.0:
    print("Japp du får köpa")
elif age >= 20 and location == "S" and promilleHalt < 1.0:
    print("Japp du får köpa")
else:    
    print("Nope ingen öl")






age = int(input("Hur gammal är du?"))
namn = input("Vad heter du")
if age > 49:
    print("Du är gammal")
elif namn == "Kalle":
    print("Du är gammal")
else:    
    print("Du är ung")



age = int(input("Hur gammal är du?"))
if age < 18:
    print("Du är omyndig")    
    yearsToEighteen = 18 - age
    print("Du får vänta " , yearsToEighteen , " tills du är myndig")
else:
    print("Du är myndig")    
print("Klart")    
    



n = int(input("Skriv in ett tal:")) 
#res = True
#res = n >= 100
#print(res)
print(n >= 100)




tal1 = int(input("Mata in tal 1"))
tal2 = int(input("Mata in tal 2"))
resultat = tal1 ** tal2
print(resultat)
print(tal1 ** tal2)


e = "Holmberg"
a = "Stefan"
print(e+ ", " + a) # Holmberg, Stefan
total = e+a


print("Du heter " + e + "," + a)
print("Du heter " ,e,a)

Age = 50
print("Vad heter du?")
namnet = input("")
print("Ok...")
print("Hejsan ", namnet)
yearsToAdd = input("Hur många år till du lägga till")
Age = Age + int(yearsToAdd)
print(Age)
