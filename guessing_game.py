"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random
import time

number_attempts = 1
record_attempts = 0 

def random_num():
    list_num  = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
    ]    
    return random.choice(list_num)

number_solution = random_num()

def start_game(number_solution, number_attempts, record_attempts):

    print("\n>>-------------------+-------------------<<")
    time.sleep(.5)
    print("!!  Welcome to the number guessing game  !!")
    time.sleep(.5)
    print(">>-------------------+-------------------<<")

    name = input("\nPlease enter your name: ")

    if record_attempts == 0:
        print("\nHi {}, there is no High score set yet - let's see what you can do!".format(name)) 

    while True:
        try:
            number_guess = int(input("\nGuess a number from 1 to 10: "))
        except ValueError:
            print("Only use whole numbers between 1 and 10...try again")         
            continue

        if number_guess > 10 or number_guess < 1:
            print("Only use whole numbers between 1 and 10...try again")
            continue
        else:   
            if number_guess == number_solution:
                print("\nGreat Job {}!!!".format(name.upper()))
                print("You have guessed in {} attempt(s)!".format(number_attempts))
                
                play_again = input("\nWould you like to play again [Y]es/[N]o? ")

                while True:
                    if play_again.lower() == "y" or play_again.lower() == "n":
                        break    
                    else:
                        time.sleep(.5)
                        print("\n{} that is not a valid answer..try again!".format(name))
                        time.sleep(.5)
                        play_again = input("\nWould you like to play again [Y]es/[N]o? Please only use [Y] or [N] ")                        

                if play_again.lower() == "y":
                    if record_attempts > number_attempts or record_attempts == 0:
                        record_attempts = number_attempts
                        number_attempts = 1
                        number_solution = random_num()
                        print("\nThe current record is {} attempt(s)".format(record_attempts))
                        continue
                    else:
                        print("\nThe current record is {} attempt(s)".format(record_attempts))                        
                        number_attempts = 1
                        number_solution = random_num()
                        continue
                elif play_again.lower() == "n":
                    time.sleep(.5)
                    print("\nThank you for playing {}!".format(name))
                    time.sleep(.5)
                    break              
            else:
                if number_guess > number_solution:
                    print("It is Lower")
                    number_attempts += 1
                elif number_guess < number_solution:
                    print("It is Higher")
                    number_attempts += 1

if __name__ == '__main__':
    start_game(number_solution, number_attempts, record_attempts) 
