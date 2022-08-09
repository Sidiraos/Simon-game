import os
import time
import random

def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

def show_user_random_number(rand_str):
    print("Retenez la séquence")
    time.sleep(1)
    print(rand_str)
    time.sleep(3)
    return rand_str

def get_answer_from_user():
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


score = 0
rand_str    = str(random.randint(1000,9999))
#fonctions

rand_number = show_user_random_number(rand_str)
reponse_str = get_answer_from_user()
sequence    = verify_answer_of_user(reponse_str , rand_number)
show_score_user(sequence , score)