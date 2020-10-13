import pygame
import random

# module initialized
pygame.init()

# Game specific variables
grid_size = 15
screen_width = 34*grid_size
screen_height = 34*grid_size

initVelocity = grid_size

snakeSize = grid_size

fps = 15


# Score window and text
def scoreWindow(text, color, x, y, size):
    font = pygame.font.SysFont(None, size)
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

#Snake length and specifications
def plotSnake(gameWindow, color, snakeList, snakeSize):
    for x, y in snakeList:
        pygame.draw.rect(gameWindow, color, [x, y, snakeSize, snakeSize])


# Game Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue=(0,0,255)

#Game clock
clock = pygame.time.Clock()

# Game window initialization
gameWindow = pygame.display.set_mode(
    (screen_width, screen_height))  # set width and height
pygame.display.set_caption('Snake Game')
pygame.display.update()

#Welcome screen
def welcome():
    exit_game=False
    while not exit_game:
        gameWindow.fill(black)
        scoreWindow("Welcome to Snakes",white,100,200,50)
        scoreWindow('Press "SpaceBar" to Play',white,150,270,25)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    exit_game = True
                    pygame.quit()
                    quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameLoop()
            pygame.display.update()
            clock.tick(fps)


# Game loop
def gameLoop():
    exit_game = False
    game_over = False

    snakeX = 2*grid_size
    snakeY = 2*grid_size

    foodX = grid_size*random.randint(1, (screen_width/grid_size)-1)
    foodY = grid_size*random.randint(1, (screen_height/grid_size)-1)

    velocityX = 0
    velocityY = 0

    snakeList = []
    snakeLen = 1

    score = 0

    while not exit_game:
        #Game over criteria
        if game_over:
            gameWindow.fill(black)
            scoreWindow(f'Game Over!!!', (255, 0, 0),
                        (screen_width/2)-125, (screen_height/2)-50, 50)
            scoreWindow(f'Your score was {score}', (255, 0, 0),
                        (screen_width/2)-85, (screen_height/2)-10, 25)
            scoreWindow("Press Enter to continue...", (0, 255, 0),
                        (screen_width/2)-110, screen_height-20, 25)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            #In-game movement
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        velocityX = initVelocity
                        velocityY = 0
                    if event.key == pygame.K_RIGHT:
                        velocityX = initVelocity
                        velocityY = 0

                    if event.key == pygame.K_a:
                        velocityX = - 1 * initVelocity
                        velocityY = 0
                    if event.key == pygame.K_LEFT:
                        velocityX = - 1 * initVelocity
                        velocityY = 0

                    if event.key == pygame.K_w:
                        velocityY = - 1 * initVelocity
                        velocityX = 0
                    if event.key == pygame.K_UP:
                        velocityY = - 1 * initVelocity
                        velocityX = 0

                    if event.key == pygame.K_s:
                        velocityY = initVelocity
                        velocityX = 0
                    if event.key == pygame.K_DOWN:
                        velocityY = initVelocity
                        velocityX = 0

            snakeY += velocityY
            snakeX += velocityX

            #Food position and length,score update
            if snakeX == foodX and snakeY == foodY:
                score += 1
                snakeLen += 1
                foodX = grid_size*random.randint(1, (screen_width/grid_size)-1)
                foodY = grid_size * \
                    random.randint(1, (screen_height/grid_size)-1)

            gameWindow.fill(black)
            scoreWindow(f"Score:{score}", white, 5, 5, 25)

            head = []
            head.append(snakeX)
            head.append(snakeY)
            snakeList.append(head)

            if len(snakeList) > snakeLen:
                del snakeList[0]

            #Snake overlapping on itself(Game Over)
            if head in snakeList[:-1]:
                game_over = True

            #Snake Moving out of screen (hard mode)
            if snakeX <= 0 or snakeX >= screen_width or snakeY <= 0 or snakeY >= screen_height:
               game_over =True


            # #Snake Moving out of screen (easy mode)
            # if snakeX < 0:
            #     snakeX = (screen_width + snakeX) + grid_size
            #     snakeY = snakeY

            # if snakeX > screen_width:
            #     snakeX = (snakeX - screen_width) - 2*grid_size
            #     snakeY = snakeY

            # if snakeY < 0:
            #     snakeY = (screen_width + snakeY) + grid_size
            #     snakeX = snakeX

            # if snakeY > screen_height:
            #     snakeY = (snakeY - screen_width) - 2*grid_size
            #     snakeX = snakeX



            # Position of snake
            plotSnake(gameWindow, white, snakeList, snakeSize)

            # Position of food
            pygame.draw.rect(gameWindow, red, [
                             foodX, foodY, snakeSize, snakeSize])

        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()


if __name__ == "__main__":
    welcome()
