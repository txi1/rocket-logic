import pygame

def initialize():
    screen = initialize_pygame()
    return initialize_data(screen)

def initialize_data(screen):
    game_data = {"screen": screen, 
                "entities":[],
                "is_open": True}
    return game_data
def initialize_pygame():
    pygame.init()
    pygame.key.set_repeat(1, 1)
    return pygame.display.set_mode((800, 800))

def handle_input(game_data):

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            game_data["is_open"] = False

def main():
    game_data = initialize()

    while game_data["is_open"]:
        handle_input(game_data)

if __name__ == "__main__":
    main()