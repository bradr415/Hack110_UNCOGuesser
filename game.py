import sys, pygame

# screen size
size = width, height = 640, 480

# constants
RED = (240, 20, 20)
LIGHT_BLUE = (51, 153, 255)
GOLD = (255, 204, 0)
DARK_PINK = (102, 0, 51)
PINK = (255, 51, 153)
# screen and clock objects
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# ball rectangle object
ball: pygame.Rect = pygame.Rect(5, height/2, 50, 50)


# obstacle rectangle objects
obstacle_top: pygame.Rect = pygame.Rect(0, -25, width, height/2)
obstacle_bottom: pygame.Rect = pygame.Rect(0, height - 175, width, height/2)
obstacle_list: list[pygame.Rect] = [obstacle_top, obstacle_bottom]

# goal rectangle object
goal: pygame.Rect = pygame.Rect(width-75, height/2, 50, 50)

def main():
    # starts pygame window and systems
    pygame.init()

    # fill background with Location
    background_image = pygame.image.load("image.jpg").convert()
    background_image = pygame.transform.scale(background_image, (640, 480))
    screen.blit(background_image, (0, 0))





    # place mouse in right place and make it invisible
    pygame.mouse.set_pos(15, (height+40)/2)
    pygame.mouse.set_visible(False)
    while 1:
        # Sets frame rate
        time_delta = clock.tick(60)/1000.0

        # draw obstacles
        pygame.draw.rect(screen, RED, obstacle_top)
        pygame.draw.rect(screen, RED, obstacle_bottom)

        # draw goal
        pygame.draw.circle(screen, GOLD, (goal.centerx, goal.centery), goal.width / 2)

        # pygame boilerplate for handling keyboard and mouse inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): sys.exit()

        # allow movement if player has reset
        (ball.centerx, ball.centery) = pygame.mouse.get_pos()

        # check collisions with obstacles, reset ball if it touches wall
        for obstacle in obstacle_list:
            if ball.colliderect(obstacle):
                pygame.mouse.set_pos(15, (height+40)/2)

        # check win condition
        if ball.colliderect(goal):
            print("You Won!")
            sys.exit()

        # draw ball and it's collision rectangle
        pygame.draw.rect(screen, DARK_PINK, ball)
        pygame.draw.circle(screen, PINK, (ball.centerx, ball.centery), ball.width / 2)


        # after all our drawing is done, "flip" the new frame onto the screen
        pygame.display.flip()


if __name__ == '__main__':
    main()

#add score on bottom
    import pygame

pygame.init()

# Set up the display
box = pygame.display.set_mode((800, 200))
pygame.display.set_caption(point_total)
# Set up the font
font = pygame.font.Font(None, 36)
# Create the text surface
text_surface = font.render(f"Score: {point_total}", True, LIGHT_BLUE)
# Get the rectangle of the text surface
text_rect = text_surface.get_rect()
# Center the text on the screen
text_rect.center = (0, 600)
# Fill the screen with black color
box.fill((0, 0, 0))
# Draw the text surface onto the screen
screen.blit(text_surface, text_rect)
# Update the display
pygame.display.update()

pygame.draw.line()