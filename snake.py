# credits naar programmersplace voor de tutorial
# https://www.youtube.com/@programmersplace6203
import pygame
import random


def snakeGame():
    height, width = 1000, 1000
    pygame.init()

    screen = pygame.display.set_mode((height, width))
    clock = pygame.time.Clock()
    running = True
    gameOver = False

    gameSpeed = 10

    # snake
    snakePositionY, snakePositionX = height / 2, width / 2
    directionY, directionX = 0, 0
    snakeLength = [(snakePositionX, snakePositionY)]

    # place first fruit
    fruitPositionY, fruitPositionX = random.randrange(0, width)//25*25, random.randrange(0, height)//25*25

    def gameOverScreen():
        font = pygame.font.Font(None, 100)
        gameOverText = font.render("Game Over", True, (255, 0, 0))

        screen.fill((0, 0, 0))
        screen.blit(gameOverText, (width / 3, height / 2))

        pygame.display.update()

        # Wait for quit event
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN or event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
                    quit()

    def snake():
        nonlocal snakePositionY, snakePositionX, fruitPositionY, fruitPositionX, gameOver, gameSpeed

        blockWidth, blockHeight = 25, 25
        snakeHeadColor = (4, 89, 49)
        snakeBodyColor = (57, 138, 55)
        fruitColor = (255, 0, 0)
        backgroundColor = (0, 0, 0)

        # Update snake's position
        snakePositionX += directionX
        snakePositionY += directionY

        # check if snake is hitting the wall
        if snakePositionX < 0 or snakePositionX >= width or snakePositionY < 0 or snakePositionY >= height:
            gameOver = True
            return

        # check if snake is hitting itself
        if(snakePositionX, snakePositionY) in snakeLength[:-1]:
            # print(f"collition {snakePositionX, snakePositionY}")
            gameOver = True
            return

        # Add new head position to snake
        snakeLength.append((snakePositionX, snakePositionY))

        # Check if snake ate the fruit
        if fruitPositionX == snakePositionX and fruitPositionY == snakePositionY:
            while (fruitPositionX, fruitPositionY) in snakeLength:
                fruitPositionX, fruitPositionY = random.randrange(0, width) // 25 * 25, random.randrange(0,height) // 25 * 25
        else:
            del snakeLength[0]

        # Redraw screen
        screen.fill(backgroundColor)
        pygame.draw.rect(screen, fruitColor, [fruitPositionX, fruitPositionY, blockWidth, blockHeight])

        # draw whole snake
        for i, j in snakeLength:
            pygame.draw.rect(screen, snakeBodyColor, [i, j, blockWidth, blockHeight])
        # give the head a different color
        pygame.draw.rect(screen, snakeHeadColor, [snakeLength[-1][0], snakeLength[-1][1], blockWidth, blockHeight])

        pygame.display.update()



    while running:
        # get all events
        events = pygame.event.get()

        if gameOver == True:
            gameOverScreen()
            pygame.quit()
            quit()


        for event in events:
            # check for quit event
            if event.type == pygame.QUIT:
                running = False

            # movement
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_LEFT or event.key == pygame.K_a):
                    if(directionX != 25):
                        directionX = -25
                        directionY = 0
                elif(event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                    if (directionX != -25):
                        directionX = 25
                        directionY = 0
                elif(event.key == pygame.K_UP or event.key == pygame.K_w):
                    if (directionY != 25):
                        directionY = -25
                        directionX = 0
                elif(event.key == pygame.K_DOWN or event.key == pygame.K_s):
                    if (directionY != -25):
                        directionY = 25
                        directionX = 0

        snake()

        clock.tick(gameSpeed)

    pygame.quit()
