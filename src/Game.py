import pygame 
from src.Config import Config
from src.Snake import Snake

class Game:
    def __init__(self, display):
        self.display = display
        
    def loop(self):
        clock = pygame.time.Clock()
        snake = Snake(self.display)
        x_change = 0
        y_change = 0
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            
                
                # print(event)
            snake.draw()
            
            pygame.display.update()
        clock.tick(Config['game']['fps'])