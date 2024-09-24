""" 

Todo listi
    - Save
    - Load
    - Quit
    - Coins/Points
    - Search?
    - High Score System

"""

import json
import os

def read_file(fileName):
    with open(f"./saves/{fileName}", "r") as game_save:
        data = json.load(game_save)
        return data
    
def show_available_loads():
    available_loads = os.listdir("./saves/")
    print("Available loads:")
    print(available_loads)

def find_available_directions(currentPos):
    # find available directions
    availableDir = tileMap[str(currentPos)][1]
    directions = ''
    
    if 'n' in availableDir:
        directions += '(N)orth '
    if 'e' in availableDir:
        directions += '(E)ast '
    if 's' in availableDir:
        directions += '(S)outh '
    if 'w' in availableDir:
        directions += '(W)est '

    directions = directions[:-1]
    directions = directions.replace(' ', ' or ')

    return availableDir, directions

def move_character(dir, currentPos):
    if dir == 'n':
        currentPos += 1
    elif dir == 'w':
        currentPos -= 10
    elif dir == 's':
        currentPos -= 1
    elif dir == 'e':
        currentPos += 10
    
    return currentPos

def save_game(curr_tile_map, curr_location, curr_coins):
    file_name = input("Enter your file name: ")
    current_game_state = {}
    current_game_state["tileMap"] = curr_tile_map
    current_game_state["location"] = curr_location
    current_game_state["coins"] = curr_coins

    with open(f"./saves/{file_name}", "w") as game_save:
        json.dump(current_game_state, game_save)
    
def set_game_variables(game_state):
    tile_map = gameState["tileMap"]
    location = int(gameState["location"])
    coins = int(gameState["coins"])

    return tile_map, location, coins


def load_save():
    show_available_loads()
    load_save_file_name = input("What is the name of your save: ")
    new_game_state = read_file(load_save_file_name)

    tile_map = new_game_state["tileMap"]
    location = new_game_state["location"]
    coins = new_game_state["coins"]

    return tile_map, location, coins

def pickup_coin(curr_coins_amount, position, tile_map):
    curr_coins_amount += int(tile_map[str(position)][0])
    tile_map[str(position)][0] = "0"
    return curr_coins_amount




gameState = read_file("defaultGame.json")

tileMap, location, coins = set_game_variables(gameState)

while location != 31:
    availableDir, directions_string = find_available_directions(location)

    # print available directions 
    print('You can travel: ', end='')
    print(directions_string + '.')

    # see if desire direction is avaiable and go that direction if available.
    print(f"Current Coins: {coins}")
    option = input('Direction: ').lower()
    if option in availableDir:
        location = move_character(option, location)
        coins = pickup_coin(coins, location, tileMap)
    elif option == "save":
        save_game(tileMap, location, coins)
    elif option == "load":
        tileMap, location, coins = load_save()
    elif option == "quit":
        break
    else:
        print('Not a valid Direction!')

    if location == 31:
        print("Victory!")


    
