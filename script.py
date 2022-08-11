import os
import time
import random
from art import *

def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

def welcome_simon_game():
    tprint("Simon Game")
    tprint("by Sidiraos")
    time.sleep(5)
    clear_screen()
    for i in range (3) :
        tprint("are u ready ?" , font="small")
        tprint(str(i+1) , font="small")
        time.sleep(1)
        clear_screen()
    
    

def show_user_random_number(rand_str):
    print("Retenez la séquence")
    time.sleep(1)
    print(rand_str)
    time.sleep(3)
    return rand_str

def get_answer_from_user(rand_str):
    clear_screen()
    reponse_str = input("votre reponse : ")
    try:
        reponse_int = int (reponse_str)
    except:
        print("ERREUR : Vous devez rentrer un nombre , recommencez !")
        show_user_random_number(rand_str)
        return get_answer_from_user()
    
    return reponse_str

def verify_answer_of_user(reponse , rand):
    n = str(random.randint(0,9))
    global d
    global score
    d = rand
    if reponse == d:
        d += n
        score += 1
        print("votre score :", score )
        show_user_random_number(d)
        r = get_answer_from_user()
        verify_answer_of_user(r , d)
    return d
    

def show_score_user(a , score) :
    print(f"mauvaise reponse la séquence etait {a}")
    print(f"votre score finale est {score}")
    if score > 5 :
        print("Pas mal , vous ferez mieux la prochaine fois")
    elif score >= 10 :
        print("Vous avez une bonne memoire")
    elif score >= 15 :
        print("Vous etes exceptionnel")
    elif score > 20 :
        print("Vous avez une memoire d'un genie")
    elif score >= 50:
        print("Vous avez une memoire d'elephant")
    else :
        print("Vous n'avez pas une bonne mémoire")
        print("entrainez vous en jouant le jeu pour booster votre memoire")

def ask_user_to_try_again() :
    print("Voulez vous ressayer ?")
    answer = input("OUI ou NON\n--> ").lower()
    if answer == "oui":
        clear_screen()
        global score
        score = 0
        return play_game()
    elif answer == "non":
        clear_screen()
        print("Merci à la prochaine")
        return
    else:
        print("Veuillez entrer une réponse entre Oui et Non")

def play_game():
    rand_str    = str(random.randint(1000,9999))
    rand_number = show_user_random_number(rand_str)
    reponse_str = get_answer_from_user(rand_str)
    sequence    = verify_answer_of_user(reponse_str , rand_number)
    show_score_user(sequence , score)
    ask_user_to_try_again()

score = 0

#fonctions
welcome_simon_game()
play_game()


input()