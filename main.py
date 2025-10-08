import pygame

# Section 01: Pre-game setup
pygame.init()

monitor_display = (800, 600)

game_display = pygame.display.set_mode(monitor_display)

pygame.display.set_caption("Tank Domination")

system_clock = pygame.time.Clock()

game_tank_image = pygame.image.load("tank.png")

# Section 02: Game properties
game_properties = {
    "sky": {
        "color": (135, 206, 235)
    },
    "grass": {
        "color": (0, 255, 0),
        "position": { 
            "y": 0.8 * monitor_display[1]
        }
    },
    "player": {
        "name": "Player",
        "sprite": {
            "image": game_tank_image,
            "color": (92, 0, 0),
            "flipped": False
        },
        "position": {}
    },
"computer": {
        "name": "Computer",
        "sprite": {
            "image": game_tank_image,
            "color": (0, 0, 92),
            "flipped": True
        },
        "position": {}
    }
}

# Section 03: Reset game properties logic
def reset_game_properties():
    game_properties["player"]["position"]["x"] = 0.2 * monitor_display[0]
    game_properties["player"]["angle"] = 45
    game_properties["player"]["hp"] = 1

    game_properties["computer"]["position"]["x"] = 0.8 * monitor_display[0] - game_properties["computer"]["sprite"]["image"].get_width()
    game_properties["computer"]["angle"] = 45
    game_properties["computer"]["hp"] = 1 

# Section 04: Draw tank logic
def render_tank(tank_property):
    tank_sprite_copy = tank_property["sprite"]["image"].copy()

    tank_sprite_copy.fill((0, 0, 0, 255), None, pygame.BLEND_RGBA_MULT)
    tank_sprite_copy.fill(tank_property["sprite"]["color"][0:3] + (0,), None, pygame.BLEND_RGBA_ADD)

    if tank_property["sprite"]["flipped"]: 
        tank_sprite_copy = pygame.transform.flip(tank_sprite_copy, True, False)
    
    game_display.blit(tank_sprite_copy, (tank_property["position"]["x"], game_properties["grass"]["position"]["y"] - tank_sprite_copy.get_height()))

# Section 05: Draw heads up display logic 
def display_hud(tank_property, offset_left):
    offset = {
        "left": offset_left * monitor_display[0],
        "top": 0.05 * monitor_display[1]
    }

    size = { 
        "width": 0.5 * monitor_display[0],
        "height": 25
    }

    pygame.draw.rect(game_display, (127, 127, 127), pygame.Rect(offset["left"] + 0.1 * size["width"], offset["top"], 0.8 * size["width"], size["height"]))

# Section 06: Projectile shooting logic

# Section 07: Computer controls logic 

# Section 08: Game logic
game_running_flag = True

reset_game_properties()

while game_running_flag: 
    # Section 08A: Stopping the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running_flag = False
        
    if not game_running_flag: 
        pygame.quit()

        break

    # Section 08B: Detecting key presses and movements
    key_pressed = pygame.key.get_pressed()

    position_delta = 0

    if key_pressed[pygame.K_LEFT]:
        position_delta = -1
    elif key_pressed[pygame.K_RIGHT]:
        position_delta = 1
    
    position_delta *= 3

    if 0 <= game_properties["player"]["position"]["x"] + position_delta and \
    game_properties["player"]["position"]["x"] + position_delta + \
    game_properties["player"]["sprite"]["image"].get_width() <= \
    game_properties["computer"]["position"]["x"]:
        game_properties["player"]["position"]["x"] += position_delta

    # Section 08C: Rendering background graphics 
    game_display.fill(game_properties["sky"]["color"])

    pygame.draw.rect(game_display, game_properties["grass"]["color"], pygame.Rect(0, game_properties["grass"]["position"]["y"], monitor_display[0], monitor_display[1] - game_properties["grass"]["position"]["y"]))

    # Section 08D: Rendering tank graphics 
    render_tank(game_properties["player"])
    render_tank(game_properties["computer"])

    # Section 08E: Rendering the heads up display graphics 
    display_hud(game_properties["player"], 0)
    display_hud(game_properties["computer"], 0.5)

    # Section 08F: Refreshing game graphics
    pygame.display.update()

    system_clock.tick(30)