#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# Get random value from ['piedra', 'papel', 'tijera']
def get_random_value():
    import random
    values = ['piedra', 'papel', 'tijera']
    return random.choice(values)

# Get user value and validate
def get_user_value():
    user_value = input("Ingrese un valor: ").lower()
    while user_value not in ['piedra', 'papel', 'tijera']:
        user_value = input("Ingrese un valor valido: ").lower()
    return user_value

# Get winner in the game
def get_winner(user_value, random_value):
    if user_value == random_value:
        return 0
    elif user_value == 'piedra':
        if random_value == 'papel':
            return -1
        else:
            return 1
    elif user_value == 'papel':
        if random_value == 'tijera':
            return -1
        else:
            return 1
    elif user_value == 'tijera':
        if random_value == 'piedra':
            return -1
        else:
            return 1

def print_points(points, winner):
    if winner == 1:
        points += 1
    elif winner == -1:
        points -= 1
    print("Puntos: {}".format(points))

def play_again():
    play = input("Jugar de nuevo? (y/n): ").lower() == 'y'
    return play

def print_winner(winner):
    if winner == 0:
        print("Empate!")
    elif winner == 1:
        print("Ganaste!")
    else:
        print("Perdiste!")
    
# Main function
def main():
    while True:
        points = 0
        
        print("Piedra, papel o tijera?")
        
        random_value = get_random_value()
        user_value = get_user_value()
        winner = get_winner(user_value, random_value)
        
        print_winner(winner)
        print_points(points, winner)
        
        if not play_again():
            break
        


if __name__ == '__main__':
    main()
