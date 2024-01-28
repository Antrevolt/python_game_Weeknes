import pygame as pg

clock = pg.time.Clock()

class objects:
    def __init__(self, caption, coord_x, coord_y):
        self.caption = pg.image.load(caption).convert_alpha()
        self.coord_x = weight + coord_x
        self.coord_y = coord_y
#Функция для сдвига объекта
def move_2(x,offset, l_side, start_x = 0):
    x -= offset
    if x <= - l_side:
        x = start_x
    return x
#Функция для Очка
def point(type,counter, player_x, player_y, enemy_x,point, border = 2):
    target_y = 0
    if type == 'task':
        target_y = 400
        if (enemy_x - border) <= player_x <= (enemy_x + border) and player_y <= target_y:
            return counter + point
        else:
            return counter
    elif type == 'enemy':
        target_y = 410
        if (enemy_x - border) <= player_x <= (enemy_x + border) and player_y >= target_y:
            return counter - point
        else:
            return counter
def count_fps(start,finish,fps):
    l = []
    i = 0
    while int(i/fps) <= finish:
        start = int(i/fps)
        print(start)
        l.append(start)
        i +=1
    print(*l)
    return l
    
    



pg.init()

#display 
weight = 741                                                                                   # display weight
haight = 545                                                                                   # display haight
screen = pg.display.set_mode((weight, haight))                                                 # set display size
icon = pg.image.load('images/1.png') .convert_alpha()                                                         # logo
myfront = pg.font.Font('fonts/Roboto/Roboto-Black.ttf', 60)                                    # font

pg.display.set_caption("Weekness. Kupcov Edition")                                             # set caption
pg.display.set_icon(icon)                                                                      # sel logo
                              
h_c = 9    
t_c = 0                          
text_surface = myfront.render(f'health: {h_c}', True, 'black')                                # use font

#objects

#Player
player = pg.image.load('images/main_run/run_0.png').convert_alpha()                                                  # Playr_icon

player_speed = 2
player_x = 100
player_y = 445
walk_right = [
    pg.image.load('images/main_run/run_0.png').convert_alpha(),
    pg.image.load('images/main_run/run_1.png').convert_alpha(),
    pg.image.load('images/main_run/run_2.png').convert_alpha(),
    pg.image.load('images/main_run/run_3.png').convert_alpha(),
    pg.image.load('images/main_run/run_4.png').convert_alpha(),
    pg.image.load('images/main_run/run_5.png').convert_alpha(),
    pg.image.load('images/main_run/run_6.png').convert_alpha(),
    pg.image.load('images/main_run/run_7.png').convert_alpha()
]
tt = count_fps(0, len(walk_right)-1,5)
player_aim_count = tt[0]

#Enemy
enemy = objects('images/enemy_1.png', 2, 470)
enemy_2 = objects('images/enemy_2.png', 10, 480)

#Task
task = objects('images/done.png', 10, 370)

#background
bg = pg.image.load('images/bg.png').convert()                                                            # background 
bg_x = 0                                                                                       # background xy_start

bg_sound = pg.mixer.Sound('sound/start_song.ogg')

#action_el

#jump
is_jump = False

jump_size = 7

#running
running = True

#main_game
i = 0
bg_sound.play()
while running:

#move background
    
    screen.blit(bg, (bg_x, 0))
    #screen.blit(bg, (bg_x + weight, 0))
    text_surface = myfront.render(f'health: {h_c}', True, 'black')
    text_task = myfront.render(f'task: {t_c}', True, 'black')

    player_rect = walk_right[0].get_rect(topleft=(player_x, player_y))
    enemy_rect = enemy.caption.get_rect(topleft=(enemy.coord_x,enemy.coord_y))
    enemy_2_rect = enemy_2.caption.get_rect(topleft=(enemy_2.coord_x,enemy_2.coord_y))
    task_rect = task.caption.get_rect(topleft=(task.coord_x,task.coord_y))
#add text
    screen.blit(text_surface,(0, 0))
    screen.blit(text_task,(0, 50))
#add player
    if i < len(tt):
        screen.blit(walk_right[tt[i]], (player_x, player_y))
        print(tt[i])
        i += +1
    else:
        i = 0
        

    
#add enemy
    screen.blit(enemy.caption, (enemy.coord_x, enemy.coord_y))
    screen.blit(enemy_2.caption, (enemy_2.coord_x, enemy_2.coord_y))
#add task
    screen.blit(task.caption, (task.coord_x, task.coord_y))

    pg.display.update()
    
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
        if jump_size >= -7:
            if jump_size > 0:
                player_y -= (jump_size ** 2) / 2
                player_x += 5
            else:
                player_y += jump_size ** 2 / 2
            jump_size -= 1
        else:
            is_jump = False
            jump_size = 7

    #Повторяем фон
    #bg_x = move_2(bg_x, 1, 741)    
    #двигаем первого врага
    enemy.coord_x = move_2(enemy.coord_x, 3, 741, weight + 2)
    #двигаем второго врага
    enemy_2.coord_x = move_2(enemy_2.coord_x, 2, 741, weight + 3)
    #двигаем таску 
    task.coord_x = move_2(task.coord_x, 5, 741, weight + 10)

    
    #играемся с жизнями
    #h_c = point('enemy', h_c,player_x,player_y,enemy.coord_x,2)
    #h_c = point('enemy', h_c,player_x,player_y,enemy_2.coord_x,2)
    #t_c = point('task', t_c,player_x,player_y,task.coord_x,1)
    if player_rect.colliderect(enemy_rect):
        h_c -= 1
        enemy.coord_x = -30
    elif player_rect.colliderect(enemy_2_rect):
        h_c -= 1
        enemy_2.coord_x = -30
    elif player_rect.colliderect(task_rect):
        t_c += 1
        task.coord_x = -30

    clock.tick(50)

    

                
