import pygame
import sys

def initialize():
    screen = initialize_pygame()
    return initialize_data(screen)


def initialize_data(screen):

    game_data = {"screen":screen,
                "entities":[],
                "is_open": True}
    
    entities = []

    entities.append({
        "type": "rocket",
        "location" : [20, 225],
        "velocity": 1,
        "size": [50, 50],
        "color":(0, 0, 225),
        "current_action":'NA'
    })
    game_data["entities"] = entities
    return game_data

def initialize_pygame():
    pygame.init()
    pygame.key.set_repeat(1, 1)
    return pygame.display.set_mode((800, 500))

def handle_input(game_data):
    events = pygame.event.get()
    entity = game_data["entities"]
    for event in events:
        if event.type == pygame.QUIT:
            game_data["is_open"] = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                for entity in game_data["entities"]:
                    if entity['type'] == "rocket":
                        entity["current_action"] = 'Up'
            if event.key == pygame.K_DOWN:
                for entity in game_data["entities"]:
                    if entity['type'] == "rocket":
                        entity["current_action"] = 'Down'

def update(game_data):
    
    for entity in game_data["entities"]:
        if entity['type'] == 'rocket':
            update_rocket(entity)

def update_rocket(entity):
    if entity["current_action"] == "NA":
            return
    elif entity["current_action"] == "Up":
        entity["location"][1] = entity["location"][1] - entity["velocity"]
    elif entity["current_action"] == "Down":
        entity["location"][1] = entity["location"][1] + entity["velocity"]
    entity['current_action'] = "NA"

def render(game_data):
    game_data["screen"].fill([245, 245, 220])


    for entity in game_data["entities"]:
        if entity['type'] == "rocket":
            positions = (entity["location"][0], entity["location"][1], entity["size"][0], entity["size"][1])
            pygame.draw.rect(game_data["screen"], entity["color"], positions)
    pygame.display.update()
def main():
    game_data = initialize()
    while game_data["is_open"]:
        handle_input(game_data)
        update(game_data)
        render(game_data)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()