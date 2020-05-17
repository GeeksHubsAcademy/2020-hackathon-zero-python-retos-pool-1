import pygame, sys, time, random
from pygame.locals import *

class Snake():
    position = [100,50]
    body = [[100,50], [90,50],[80,50]]
    direction = "RIGHT"
    change = direction
    speed = 10

    VALID_DIRECTIONS = {
        'RIGHT': ['UP', 'DOWN'],
        'LEFT': ['UP', 'DOWN'],
        'UP': ['RIGHT', 'LEFT'],
        'DOWN': ['RIGHT', 'LEFT'],
    }
    
    def controller(self, event, pygame):
        movement_key_map = {
            pygame.K_RIGHT: 'RIGHT',
            pygame.K_LEFT: 'LEFT',
            pygame.K_UP: 'UP',
            pygame.K_DOWN: 'DOWN',
        }

        if event.type == pygame.KEYDOWN:
            if event.key in movement_key_map:
                self.change = movement_key_map[event.key] 
        
    def changeDirection(self):
        if self.change in self.VALID_DIRECTIONS[self.direction]:
            self.direction = self.change

        if self.direction == 'RIGHT':
            self.position[0] += self.speed 
        if self.direction == 'LEFT':
            self.position[0] -= self.speed
        if self.direction == 'UP':
            self.position[1] -= self.speed
        if self.direction == 'DOWN':
            self.position[1] += self.speed

        self.body.insert(0, list(self.position))

class Game():
    run = True
    food_pos = 0
    score = 0

    def __init__(self):
        self.food_spawn()

    # función de salida
    def exit(self, event, pygame):
        pass
        #
        #
    
    def food_spawn(self): 
        new_x = random.choice(range(0, 49)) * 10
        new_y = random.choice(range(0, 49)) * 10
        
        self.food_pos = [new_x, new_y]

    def eat(self, snake):
        if snake.position == self.food_pos:
            self.food_spawn()
            self.score += 1
        else:
            snake.body.pop()
        
    def dead(self, snake):
        is_in_playground =  0 < snake.position[0] < 500 and 0 < snake.position[1] < 500
        is_self_collision = snake.position in snake.body[2:]
        if not is_in_playground or is_self_collision:
            Game.run = False
        else:
            Game.run = True

def main():
    # Descomentar para lanzar el juego en local
    # Comentar para validar con el oráculo
    # pygame.init()
    # play_surface = pygame.display.set_mode((500, 500))
    # fps = pygame.time.Clock()
    

    snake = Snake()
    game = Game()

    while game.run:
        for event in pygame.event.get():
            game.exit(event, pygame)
            snake.controller(event, pygame)
        
        snake.changeDirection()

        game.eat(snake)

        play_surface.fill((0,0,0))
        for pos in snake.body:
            pygame.draw.rect(play_surface, (200,200,200), pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(play_surface, (255,160,60), pygame.Rect(game.food_pos[0], game.food_pos[1], 10, 10))

        game.dead(snake)

        pygame.display.flip()
        fps.tick(60)

        
# Comienza la aventura!!!!
# Descomentar para lanzar el juego en local
# Comentar para validar con el oráculo
# main()
# pygame.quit()
