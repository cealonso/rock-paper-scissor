import random
f = open('puntaje.txt','a',encoding='utf8')
for i in range(1,4):
     user_action=input("Seleccione (piedra-papel-tijera)")
     possible_actions = ["piedra", "papel", "tijera"]
     computer_action=random.choice(possible_actions)
    #  print(computer_action)
     print("\nTú elegiste", user_action, " , la computadora eligió ",computer_action,"\n")
     if user_action == computer_action:
        f.write("Empate. \n")
        print("Empate !" ,user_action, ". Ambos Ganaron !")
     elif user_action=="piedra" and computer_action=="papel":
        f.write("Empate. \n")
        print ("Ganó la computadora . \n")
     elif user_action=="piedra" and computer_action=="tijera":
        print ("Ganó el usuario .\n")
        f.write("Ganó el Usuario. \n")
     elif user_action=="papel" and computer_action=="piedra":
        f.write("Ganó el usuario .\n")
        print ("Ganó el usuario .\n") 
     elif user_action=="papel" and computer_action=="tijera":
        f.write("Ganó la computadora .\n")
        print ("Ganó la computadora .\n")
     elif user_action=="tijera" and computer_action=="piedra":
        f.write("Ganó la computadora .\n")
        print ("Ganó la computadora .\n")
     elif user_action=="tijera" and computer_action=="papel":
        f.write("Ganó el usuario .\n")
        print ("Ganó el usuario .\n")
     else:
        print("Error seleccione bien !")

