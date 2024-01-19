import pygame as pg

clock = pg.time.Clock()

class objects:
    def __init__(self, caption, coord_x, coord_y):
        self.caption = pg.image.load(caption) 
        self.coord_x = weight + coord_x
        self.coord_y = coord_y

pg.init()

#display 
weight = 741                                                                                   # display weight
haight = 545                                                                                   # display haight
screen = pg.display.set_mode((weight, haight))                                                 # set display size
icon = pg.image.load('images/1.png')                                                           # logo
myfront = pg.font.Font('fonts/Roboto/Roboto-Black.ttf', 60)                                    # font

pg.display.set_caption("Weekness. Kupcov Edition")                                             # set caption
pg.display.set_icon(icon)                                                                      # sel logo
                              
h_c = 9    
t_c = 0                          
text_surface = myfront.render(f'health: {h_c}', True, 'black')                                # use font

#objects

#Player
player = pg.image.load('images/frog.png')                                                      # Playr_icon

player_speed = 5
player_x = 100
player_y = 463

#Enemy
enemy = objects('images/enemy_1.png', 2, 470)
enemy_2 = objects('images/enemy_2.png', 10, 480)

#Task
task = objects('images/done.png', 10, 370)

#background
bg = pg.image.load('images/bg.png')                                                            # background 
bg_x = 0                                                                                       # background xy_start

#action_el

#jump
is_jump = False

jump_size = 10

#running
running = True

#main_game

while running:

#move background
    text_surface = myfront.render(f'health: {h_c}', True, 'black')
    text_task = myfront.render(f'task: {t_c}', True, 'black')
    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + weight, 0))
#add text
    screen.blit(text_surface,(0, 0))
    screen.blit(text_task,(0, 50))
#add player
    screen.blit(player, (player_x, player_y))
#add enemy
    screen.blit(enemy.caption, (enemy.coord_x, enemy.coord_y))
    screen.blit(enemy_2.caption, (enemy_2.coord_x, enemy_2.coord_y))
#add task
    screen.blit(task.caption, (task.coord_x, task.coord_y))
    
#button on
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

#key description
    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT] and player_x -player_speed >= 0:                                 #add borders
        player_x -=player_speed
    elif keys[pg.K_RIGHT] and player_x +player_speed < 700:                             #add borders
        player_x +=player_speed

    if not is_jump:
        if keys[pg.K_UP]:
            is_jump = True
    else:
        if jump_size >= -10:
            if jump_size > 0:
                player_y -= jump_size ** 2 / 2
            else:
                player_y += jump_size ** 2 / 2
            jump_size -= 2
        else:
            is_jump = False
            jump_size = 10

    bg_x -= 1
    if bg_x == -741:
        bg_x = 0
    enemy.coord_x -=3
    if enemy.coord_x <= -741:
        enemy.coord_x = weight + 2
    
    enemy_2.coord_x -=2
    if enemy_2.coord_x <= -741:
        enemy_2.coord_x = weight + 3

    task.coord_x -=5
    if task.coord_x <= -741:
        task.coord_x = weight + 10
    pg.display.update()
    if (player_x-2 <= enemy.coord_x and player_x+2 >= enemy.coord_x) and player_y >= 410:
        print(player_y)
        h_c -= 1
    if (player_x-2 <= enemy_2.coord_x and player_x+2 >= enemy_2.coord_x) and player_y >= 410:
        print(player_y)
        h_c -= 2
    if ((player_x-5 <= task.coord_x and player_x+5 >= task.coord_x) or player_x == task.coord_x) and player_y <= 400:
        print(player_y)
        t_c += 1
    
    clock.tick(60)
                
