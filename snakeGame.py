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
game_mode = False  # False for easy mode and True for hard mode

# Score window and text
def textWindow(text, color, x, y, size):
    font = pygame.font.SysFont(None, size)
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

# Snake length and specifications
def plotSnake(gameWindow, color, snakeList, snakeSize):
    for x, y in snakeList:
        pygame.draw.rect(gameWindow, color, [x, y, snakeSize, snakeSize])


# Game Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

# Game clock
clock = pygame.time.Clock()

# Game window initialization
gameWindow = pygame.display.set_mode(
    (screen_width, screen_height))  # set width and height
pygame.display.set_caption('Snake Game')
pygame.display.update()

# Welcome screen
def welcome():
    global game_mode
    exit_game = False
    gameWindow.fill(black)
    textWindow("Welcome to Snakes", white, 100, 200, 50)
    textWindow('Please select game mode', white, 150, 250, 25)
    textWindow('• Easy "E"', white, 150, 275, 25)
    textWindow('• Hard "H"', white, 150, 300, 25)

    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    gameWindow.fill(black)
                    textWindow("Welcome to Snakes", white, 100, 200, 50)
                    textWindow('Press "SpaceBar" to Play', white, 150, 270, 25)

                    game_mode = False
                if event.key == pygame.K_h:
                    gameWindow.fill(black)
                    textWindow("Welcome to Snakes", white, 100, 200, 50)
                    textWindow('Press "SpaceBar" to Play', white, 150, 270, 25)
                    game_mode = True
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
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    while not exit_game:
        # Game over criteria
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(black)
            textWindow(f'Game Over!!!', (255, 0, 0),
                       (screen_width/2)-125, (screen_height/2)-50, 50)
            textWindow(f'Your score was {score}', (255, 0, 0),
                       (screen_width/2)-85, (screen_height/2)-10, 25)
            textWindow("Press Enter to continue...", (0, 255, 0),
                       (screen_width/2)-110, screen_height-20, 25)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            # In-game movement
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocityX = initVelocity
                        velocityY = 0

                    if event.key == pygame.K_LEFT:
                        velocityX = - 1 * initVelocity
                        velocityY = 0

                    if event.key == pygame.K_UP:
                        velocityY = - 1 * initVelocity
                        velocityX = 0

                    if event.key == pygame.K_DOWN:
                        velocityY = initVelocity
                        velocityX = 0

            snakeY += velocityY
            snakeX += velocityX

            # Food position and length,score update
            if snakeX == foodX and snakeY == foodY:
                score += 10
                snakeLen += 3
                foodX = grid_size*random.randint(1, (screen_width/grid_size)-1)
                foodY = grid_size * \
                    random.randint(10, (screen_height/grid_size)-1)
                if score > int(hiscore):
                    hiscore = score
            gameWindow.fill(black)
            textWindow(f"Current Score:{score}", white, 5, 10, 25)
            textWindow(f"High Score:{hiscore}", red, 380, 10, 25)

            head = []
            head.append(snakeX)
            head.append(snakeY)
            snakeList.append(head)

            if len(snakeList) > snakeLen:
                del snakeList[0]

            # Snake overlapping on itself(Game Over)
            if head in snakeList[:-1]:
                game_over = True
            if game_mode == False:  # Easy Mode
                # Snake Moving out of screen
                if snakeX < 0:
                    snakeX = (screen_width + snakeX) + grid_size
                    snakeY = snakeY

                if snakeX > screen_width:
                    snakeX = (snakeX - screen_width) - 2*grid_size
                    snakeY = snakeY

                if snakeY < 0:
                    snakeY = (screen_width + snakeY) + grid_size
                    snakeX = snakeX

                if snakeY > screen_height:
                    snakeY = (snakeY - screen_width) - 2*grid_size
                    snakeX = snakeX

            elif game_mode == True:  # Hard Mode
                if snakeX <= 0 or snakeX >= screen_width or snakeY <= 0 or snakeY >= screen_height:
                    game_over = True
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
