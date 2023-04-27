""""Functions for our game"""

from classes import Location
import sys
import pygame
from math import sqrt
import random
from math import log

RED = (240, 20, 20)



#bell_tower: Location = Location()
old_well: Location = Location("ol_well (1).jpg", (1144, 146))
wilson: Location = Location("wilson.jpg", (1144, 240))
bell_tower: Location("bell_tower.jpg", (1000,500))
# bell_tower: Location(bell tower jpg, coordinates)
# kenan_stadium: Location(stadiumjpg, coordinates)
#sitterson_hall: Location = Location()
BORDER: int = 800
MAP_LENGTH: int = 640
WIDTH: int = BORDER + MAP_LENGTH
HEIGHT: int = 800
LIGHT_BLUE = (51, 153, 255)
size = width, height = BORDER + MAP_LENGTH, HEIGHT
screen = pygame.display.set_mode(size)
#size1 = width, height = BORDER, HEIGHT
#blue_map = pygame.display.set_mode(size1)
#blue_map.fill(LIGHT_BLUE)
point_total: int = 0

places: list[Location] = [old_well, wilson]



def points(actual_location: Location, input_location) -> int:
    length: int = (sqrt(((actual_location.location_place[0] - input_location[0])**2)+ ((actual_location.location_place[1] - input_location[1])**2)))
    score = 100 - ((length ** (1/2.3)) / 2)
    if score < 0:
        score = 0

    return score

which_image: int = random.randint(0, len(places))
    
def rand_image() -> Location:
    
    which_image: int = random.randint(0, len(places))
    image: Location = places[which_image]
    
    return image


    
def initialize_background(place: Location, score: int):
    global point_total
    size = width, height = WIDTH, HEIGHT
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # fill background with Location
    background_image = pygame.image.load(place.location_adress).convert()
    background_image = pygame.transform.scale(background_image, (BORDER, HEIGHT))
    screen.blit(background_image, (0, 0))
    
    #fill background with map
    background_image = pygame.image.load("bw_map_smaller_cropped.jpg").convert()
    background_image = pygame.transform.scale(background_image, (MAP_LENGTH, HEIGHT))
    screen.blit(background_image, (BORDER, 0))
    
    pygame.init()
    pygame.display.set_caption(f"Score:{score}")
    font = pygame.font.Font(None, 100) # Set up the font
    
    text_surface = font.render(f"Score: {point_total}", True, LIGHT_BLUE) # Create the text surface
    
    text_rect = text_surface.get_rect() # Get the rectangle of the text surface
    
    text_rect.center = (200, 700) # Center the text on the screen
    pygame.display.update()
    screen.blit(text_surface, text_rect)
pygame.init()

pygame.display.set_caption(f"") # Set up the display
    
font = pygame.font.Font(None, 100) # Set up the font
    
text_surface = font.render(f"", True, LIGHT_BLUE) # Create the text surface
    
text_rect = text_surface.get_rect() # Get the rectangle of the text surface
    
text_rect.center = (200, 700) # Center the text on the screen

# pygame.display.update
# pygame.time.delay(3000)

def main():
    # starts pygame window and system 
    pic:Location = wilson
    initialize_background(pic, 0)
    pygame.display.update()
    global point_total
    


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                point_total = int(points(pic, pos))

                RED = (240, 20, 20)
                initialize_background(pic, point_total)
                dot: pygame.Rect = pygame.Rect(pos[0]-7.5, pos[1]-7.5, 15, 15)

                correct_place: pygame.Rect = pygame.Rect(pic.location_place[0]-7.5, pic.location_place[1]-7.5, 15, 15)

                pygame.draw.rect(screen, RED, dot)
                pygame.draw.rect(screen, LIGHT_BLUE, correct_place)
                
                print(points(wilson, pos))
                print(pos)
                #pygame.display.set_caption(f"Score: {point_total}") # Set up the display
                #text_surface = font.render(f"Score: {point_total}", True, LIGHT_BLUE) # Create the text surface
                
                screen.blit(text_surface, text_rect)
                

                pygame.display.update()


if __name__ == '__main__':
    main()
