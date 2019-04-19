from pygame.locals import *
import os
import pygame
import random
import pygameMenu
from pygameMenu.locals import *
from super import *

ABOUT = ['Mady by : ',
         '________201601364 Park Joo Young',
         '________201700124 Ishanga Vidusha',
         '________201503164 Jeong Hee Won']
HOWTOPLAY = ['',
             'MOVE :',
             'JUMP_is_KEY-UP_or_SPACE',
             'SLIDING_is_KEY-DOWN']
BACKGROUND = pygame.image.load('gameBg/gameBg1.png')
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_BLUE = (0, 0, 255)
WINDOW_SIZE = (800, 400)
W, H = 800, 400
gameSpeed = 7
gameSpeed2 = 13
gameSpeed3 = 17
clockSpeed = 30
DIFFICULTY = ['EASY']

# -----------------------------------------------------------------------------
# Init pygame
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Create pygame screen and objects
win = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('cookie run')
pygame.mixer.music.load('sound/bgm.mp3')
pygame.mixer.music.play(-1)
clock = pygame.time.Clock()


runingFroward = [pygame.image.load('boyData/1.png'), pygame.image.load('boyData/2.png'),
                 pygame.image.load('boyData/3.png'), pygame.image.load('boyData/4.png'),
                 pygame.image.load('boyData/5.png'), pygame.image.load('boyData/6.png'),
                 pygame.image.load('boyData/7.png'), pygame.image.load('boyData/8.png'),
                 pygame.image.load('boyData/9.png'), pygame.image.load('boyData/10.png')]

attack_list = [pygame.image.load('boyData/j_a1.png'), pygame.image.load('boyData/j_a2.png'),
               pygame.image.load('boyData/j_a3.png'), pygame.image.load('boyData/j_a4.png'),
               pygame.image.load('boyData/j_a5.png'), pygame.image.load('boyData/j_a6.png'),
               pygame.image.load('boyData/j_a7.png'), pygame.image.load('boyData/j_a8.png'),
               pygame.image.load('boyData/j_a9.png'), pygame.image.load('boyData/j_a10.png')]

jump_list = [pygame.image.load('boyData/j1.png'), pygame.image.load('boyData/j2.png'),
             pygame.image.load('boyData/j3.png'), pygame.image.load('boyData/j4.png'),
             pygame.image.load('boyData/j5.png'), pygame.image.load('boyData/j6.png'),
             pygame.image.load('boyData/j7.png'), pygame.image.load('boyData/j8.png'),
             pygame.image.load('boyData/j9.png'), pygame.image.load('boyData/j10.png')]

slid_list = [pygame.image.load('boyData/s1.png'), pygame.image.load('boyData/s2.png'),
             pygame.image.load('boyData/s3.png'), pygame.image.load('boyData/s4.png'),
             pygame.image.load('boyData/s5.png'), pygame.image.load('boyData/s6.png'),
             pygame.image.load('boyData/s7.png'), pygame.image.load('boyData/s8.png'),
             pygame.image.load('boyData/s9.png'), pygame.image.load('boyData/s10.png')]

bomb_list = [pygame.image.load('otherData/ob1.png'), pygame.image.load('otherData/ob2.png'),
             pygame.image.load('otherData/ob3.png'), pygame.image.load('otherData/ob4.png'),
             pygame.image.load('otherData/ob5.png'), pygame.image.load('otherData/ob6.png'),
             pygame.image.load('otherData/ob7.png'), pygame.image.load('otherData/ob8.png'),
             pygame.image.load('otherData/ob9.png'), pygame.image.load('otherData/ob10.png'),
             pygame.image.load('otherData/ob11.png')]

dead_list = [pygame.image.load('boyData/d1.png'), pygame.image.load('boyData/d2.png'),
             pygame.image.load('boyData/d3.png'), pygame.image.load('boyData/d4.png'),
             pygame.image.load('boyData/d5.png'), pygame.image.load('boyData/d6.png'),
             pygame.image.load('boyData/d7.png'), pygame.image.load('boyData/d8.png'),
             pygame.image.load('boyData/d9.png'), pygame.image.load('boyData/d10.png')]
bg = [pygame.image.load('gameBg/bg1.png'), pygame.image.load('gameBg/bg2.png')]


# -----------------------------------------------------------------------------

def change_difficulty(d):
    print('Selected difficulty: {0}'.format(d))
    DIFFICULTY[0] = d


class player(player1):
    def __init__(self, x, y, width, height, vel):
        player1.__init__(self, x, y, width, height, vel)
        self.vel = vel
        self.isJump = False
        self.sliding = False
        self.isAttack = False
        self.dead = False
        self.slidCount = 30
        self.attackCount = 30
        self.jumpCount = 10
        self.hitbox = (x, y, width, height)

    def draw(self, win):
        if self.walkCount + 1 >= 30:
            self.walkCount = 0
        if self.dead:
            win.blit(dead_list[9], (self.x, self.y))
            self.walkCount += 1
        elif self.isJump:
            win.blit(jump_list[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
            self.hitbox = (self.x + 10, self.y + 5, self.width - 20, self.height - 5)
            # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        elif self.sliding:
            win.blit(slid_list[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
            self.hitbox = (self.x + 5, self.y + 5, self.width - 5, self.height - 5)
            # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        elif self.isAttack:
            win.blit(attack_list[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
            self.hitbox = (self.x + 10, self.y + 5, self.width - 20, self.height - 5)
            # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        else:
            win.blit(runingFroward[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
            self.hitbox = (self.x + 10, self.y + 5, self.width - 20, self.height - 5)
            # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


class bomber(player1):
    def __init__(self, x, y, width, height, vel):
        player1.__init__(self, x, y, width, height, vel)
        self.rotateCount = 0
        self.hitbox = (x, y, width, height)

    def draw(self, win):
        if self.rotateCount + 1 >= 30:
            self.rotateCount = 0
        self.hitbox = (self.x + 5, self.y + 20, self.width - 20, self.height - 5)
        win.blit(bomb_list[self.rotateCount // 3], (self.x, self.y))
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        self.rotateCount += 1

    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False


class spike(bomber):
    img = pygame.image.load(os.path.join('otherData', 'spike2.png'))

    def draw(self, win):
        self.hitbox = (self.x - 10, self.y + 5, self.width - 18, self.height - 10)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        win.blit(self.img, (self.x, self.y))

    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] < self.hitbox[3]:
                return True
        return False

class coin(bomber):
    img = pygame.image.load(os.path.join('otherData','coin1.png'))

    def draw(self, win):
        self.hitbox = (self.x -5, self.y -5, self.width - 5, self.height - 5)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        win.blit(self.img, (self.x, self.y))

    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False

class background(background1):
    def __init__(self, x, y, vel, index):
        background1.__init__(self, x, y, vel, index)

    def draw(self, win):
        win.blit(bg[self.index], (self.x, self.y))
        if self.x < -800:
            self.x = 800


def updateFile():
    f = open('scores.txt', 'r')  # opens the file in read mode
    file = f.readlines()  # reads all the lines in as a list
    last = int(file[0])  # gets the first line of the file

    if last < int(score):  # sees if the current score is greater than the previous best
        f.close()  # closes/saves the file
        file = open('scores.txt', 'w')  # reopens it in write mode
        file.write(str(score))  # writes the best score
        file.close()  # closes/saves the file

        return score

    return last

def endScreen():
    global pause, score, clockSpeed, bombs, spikes, run,deadsound
    pause = 0
    clockSpeed = 30
    bombs = []
    spikes = []
    deadsound=pygame.mixer.Sound('sound/dead.wav')
    pygame.mixer.Sound.play(deadsound)
    end = pygame.image.load(os.path.join('otherData', 'Result.png'))
    run_end = True
    while run_end:
        pygame.time.delay(100)

        playevents = pygame.event.get()
        for e in playevents:
            if e.type == QUIT:
                exit()
                run = False
            elif e.type == KEYDOWN:
                if e.key == K_ESCAPE and main_menu.is_disabled():
                    main_menu.enable()
                    run = False
                    player_one.dead = False
                    score = 0
                    # Quit this function, then skip to loop of main-menu on line 217
                    return

        win.blit(bg[0], (0, 0))
        largeFont = pygame.font.SysFont('comicsans', 40)
        lastScore = largeFont.render('Best Score: ' + str(updateFile()), 1, (0, 0, 0))
        currentScore = largeFont.render(str(score), 1, (0, 0, 0))
        press = largeFont.render('want to again game , press "esc" key ',1,(0,0,0))
        win.blit(end,(250,100))
        win.blit(lastScore, (W / 2 - lastScore.get_width() / 2 -20, 220))
        win.blit(currentScore, (W / 2 - currentScore.get_width() / 2 , 165))
        win.blit(press, (W /2-lastScore.get_width() / 2 - 140, 330))

        pygame.display.update()

    main_menu.mainloop(playevents)


def redrawGameWindow():
    largeFont = pygame.font.SysFont('comicsans', 30)  # Font object
    bg_one.draw(win)
    bg_two.draw(win)
    text = largeFont.render('Score: ' + str(score), 1, COLOR_WHITE)  # create our text
    player_one.draw(win)
    for bomb in bombs:
        bomb.draw(win)
    for spikee in spikes:
        spikee.draw(win)
    for coinn in coins:
        coinn.draw(win)
    win.blit(text, (685, 10))
    pygame.display.update()

def redrawGameWindowHARD():
    largeFont = pygame.font.SysFont('comicsans', 30)  # Font object
    bg_one_H.draw(win)
    bg_two_H.draw(win)
    text = largeFont.render('Score: ' + str(score), 1, COLOR_WHITE)  # create our text
    player_one.draw(win)
    for bomb in bombs:
        bomb.draw(win)
    for spikee in spikes:
        spikee.draw(win)
    for coinn in coins:
        coinn.draw(win)
    win.blit(text, (685, 10))
    pygame.display.update()


pygame.time.set_timer(USEREVENT + 2, random.randrange(2000, 2500))

if __name__ == "__main__":
    player_one = player(160, 318, 64, 64, gameSpeed)
    bg_one = background(0, 0, gameSpeed, 0)
    bg_two = background(800, 0, gameSpeed, 1)
    bg_one_H = background(0, 0, gameSpeed3, 0)
    bg_two_H = background(800, 0, gameSpeed3, 1)
    bombs = []
    spikes = []
    coins = []
    pause = 0
    fallSpeed = 0
    score = 0
run = True



def play_function(difficulty):
    global run, score, fallSpeed, pause, bombs, bg_one, bg_two, player_one,jumpsound,slidesound,coinsound
    coinsound = pygame.mixer.Sound('sound/coin.wav')
    jumpsound = pygame.mixer.Sound('sound/jump.wav')
    slidesound = pygame.mixer.Sound('sound/slide.wav')
    main_menu.disable()
    main_menu.reset(1)

    difficulty = difficulty[0]
    assert isinstance(difficulty, str)

    run = True
    if difficulty == 'EASY':
        while run:
            clock.tick(clockSpeed)
            score += 1
            if pause > 0:
                pause += 1
                if pause == fallSpeed:
                    endScreen()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == USEREVENT + 2:
                    r = random.randrange(0, 2)
                    r2 = random.randrange(600,700)
                    r3 = random.randrange(850,1000)
                    coins.append(coin(r2, 318, 50, 50, gameSpeed))
                    coins.append(coin(r3, 318, 50, 50, gameSpeed))
                    if r == 0:
                        bombs.append(bomber(800, 318, 64, 64, gameSpeed))
                    elif r == 1:
                        spikes.append(spike(800, 0, 80, 340, gameSpeed))

            keys = pygame.key.get_pressed()

            for bomb in bombs:
                if bomb.collide(player_one.hitbox):
                    player_one.dead = True
                    if pause == 0:
                        pause = 1
                        fallSpeed = 20
                bomb.x -= bomb.vel
                if bomb.x < 0:
                    bombs.pop(bombs.index(bomb))
            for spikee in spikes:
                if spikee.collide(player_one.hitbox):
                    player_one.dead = True
                    if pause == 0:
                        pause = 1
                        fallSpeed = 20
                spikee.x -= spikee.vel
                if spikee.x < 0:
                    spikes.pop(spikes.index(spikee))
            for coinn in coins:
                if coinn.collide(player_one.hitbox):
                    pygame.mixer.Sound.play(coinsound)
                    score += 400
                    coins.pop(coins.index(coinn))
                coinn.x -= coinn.vel

            if not player_one.dead:
                if not player_one.isJump:
                    if not player_one.sliding:
                        if not player_one.isAttack:
                            if keys[pygame.K_UP]:
                                pygame.mixer.Sound.play(jumpsound)
                                player_one.isJump = True
                                player_one.walkCount = 0
                            elif keys[pygame.K_DOWN]:
                                pygame.mixer.Sound.play(slidesound)
                                player_one.sliding = True
                                player_one.walkCount = 0
                            elif keys[pygame.K_SPACE]:
                                pygame.mixer.Sound.play(jumpsound)
                                player_one.isAttack = True
                                player_one.walkCount = 0
                        else:
                            if player_one.jumpCount >= -10:
                                neg = 1
                                if player_one.jumpCount < 0:
                                    neg = -1
                                player_one.y -= (player_one.jumpCount ** 2) * 0.5 * neg
                                player_one.jumpCount -= 1
                            else:
                                player_one.isAttack = False
                                player_one.jumpCount = 10
                    else:
                        if player_one.slidCount >= 0:
                            player_one.y = 350
                            player_one.slidCount -= 1
                        else:
                            player_one.sliding = False
                            player_one.y = 318
                            player_one.slidCount = 30
                else:
                    if player_one.jumpCount >= -10:
                        neg = 1
                        if player_one.jumpCount < 0:
                            neg = -1
                        player_one.y -= (player_one.jumpCount ** 2) * 0.5 * neg
                        player_one.jumpCount -= 1
                    else:
                        player_one.isJump = False
                        player_one.jumpCount = 10
            bg_one.x -= bg_one.vel
            bg_two.x -= bg_two.vel
            redrawGameWindow()
    elif difficulty == 'MEDIUM':
        while run:
            clock.tick(clockSpeed)
            score += 1
            if pause > 0:
                pause += 1
                if pause == fallSpeed:
                    endScreen()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == USEREVENT + 2:
                    r = random.randrange(0, 2)
                    r2 = random.randrange(500,700)
                    r3 = random.randrange(850,1000)
                    coins.append(coin(r2, 318, 40, 40, gameSpeed2))
                    coins.append(coin(r3, 318, 40, 40, gameSpeed2))
                    if r == 0:
                        bombs.append(bomber(800, 318, 64, 64, gameSpeed2))
                    elif r == 1:
                        spikes.append(spike(800, 0, 80, 340, gameSpeed2))

            keys = pygame.key.get_pressed()
            for bomb in bombs:
                if bomb.collide(player_one.hitbox):
                    player_one.dead = True
                    if pause == 0:
                        pause = 1
                        fallSpeed = 20
                bomb.x -= bomb.vel
                if bomb.x < 0:
                    bombs.pop(bombs.index(bomb))
            for spikee in spikes:
                if spikee.collide(player_one.hitbox):
                    player_one.dead = True
                    if pause == 0:
                        pause = 1
                        fallSpeed = 20
                spikee.x -= spikee.vel
                if spikee.x < 0:
                    spikes.pop(spikes.index(spikee))
            for coinn in coins:
                if coinn.collide(player_one.hitbox):
                    pygame.mixer.Sound.play(coinsound)
                    score += 400
                    coins.pop(coins.index(coinn))
                coinn.x -= coinn.vel
            if not player_one.dead:
                if not player_one.isJump:
                    if not player_one.sliding:
                        if not player_one.isAttack:
                            if keys[pygame.K_UP]:
                                pygame.mixer.Sound.play(jumpsound)
                                player_one.isJump = True
                                player_one.walkCount = 0
                            elif keys[pygame.K_DOWN]:
                                pygame.mixer.Sound.play(slidesound)
                                player_one.sliding = True
                                player_one.walkCount = 0
                            elif keys[pygame.K_SPACE]:
                                pygame.mixer.Sound.play(jumpsound)
                                player_one.isAttack = True
                                player_one.walkCount = 0
                        else:
                            if player_one.jumpCount >= -10:
                                neg = 1
                                if player_one.jumpCount < 0:
                                    neg = -1
                                player_one.y -= (player_one.jumpCount ** 2) * 0.5 * neg
                                player_one.jumpCount -= 1
                            else:
                                player_one.isAttack = False
                                player_one.jumpCount = 10
                    else:
                        if player_one.slidCount >= 0:
                            player_one.y = 338
                            player_one.slidCount -= 1
                        else:
                            player_one.sliding = False
                            player_one.y = 318
                            player_one.slidCount = 30
                else:
                    if player_one.jumpCount >= -10:
                        neg = 1
                        if player_one.jumpCount < 0:
                            neg = -1
                        player_one.y -= (player_one.jumpCount ** 2) * 0.5 * neg
                        player_one.jumpCount -= 1
                    else:
                        player_one.isJump = False
                        player_one.jumpCount = 10
            bg_one.x -= bg_one.vel
            bg_two.x -= bg_two.vel
            redrawGameWindow()
    elif difficulty == 'HARD':
        while run:
            clock.tick(clockSpeed)
            score += 1
            if pause > 0:
                pause += 1
                if pause == fallSpeed:
                    endScreen()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == USEREVENT + 2:
                    r = random.randrange(0, 2)
                    r2 = random.randrange(500,700)
                    r3 = random.randrange(850,1000)
                    coins.append(coin(r2, 318, 40, 40, gameSpeed3))
                    coins.append(coin(r3, 318, 40, 40, gameSpeed3))
                    if r == 0:
                        spikes.append(spike(800, 0, 80, 340, gameSpeed + 2))
                        bombs.append(bomber(800, 318, 64, 64, gameSpeed3 - 2))
                    elif r == 1:
                        spikes.append(spike(800, 0, 80, 340, gameSpeed3 - 2))
                        bombs.append(bomber(800, 318, 64, 64, gameSpeed + 2))
            keys = pygame.key.get_pressed()

            for bomb in bombs:
                if bomb.collide(player_one.hitbox):
                    player_one.dead = True
                    if pause == 0:
                        pause = 1
                        fallSpeed = 20
                bomb.x -= bomb.vel
                if bomb.x < 0:
                    bombs.pop(bombs.index(bomb))
            for spikee in spikes:
                if spikee.collide(player_one.hitbox):
                    player_one.dead = True
                    if pause == 0:
                        pause = 1
                        fallSpeed = 20
                spikee.x -= spikee.vel
                if spikee.x < 0:
                    spikes.pop(spikes.index(spikee))
            for coinn in coins:
                if coinn.collide(player_one.hitbox):
                    pygame.mixer.Sound.play(coinsound)
                    score += 400
                    coins.pop(coins.index(coinn))
                coinn.x -= coinn.vel
            if not player_one.dead:
                if not player_one.isJump:
                    if not player_one.sliding:
                        if not player_one.isAttack:
                            if keys[pygame.K_UP]:
                                pygame.mixer.Sound.play(jumpsound)
                                player_one.isJump = True
                                player_one.walkCount = 0
                            elif keys[pygame.K_DOWN]:
                                pygame.mixer.Sound.play(slidesound)
                                player_one.sliding = True
                                player_one.walkCount = 0
                            elif keys[pygame.K_SPACE]:
                                pygame.mixer.Sound.play(jumpsound)
                                player_one.isAttack = True
                                player_one.walkCount = 0
                        else:
                            if player_one.jumpCount >= -10:
                                neg = 1
                                if player_one.jumpCount < 0:
                                    neg = -1
                                player_one.y -= (player_one.jumpCount ** 2) * 0.5 * neg
                                player_one.jumpCount -= 1
                            else:
                                player_one.isAttack = False
                                player_one.jumpCount = 10
                    else:
                        if player_one.slidCount >= 0:
                            player_one.y = 338
                            player_one.slidCount -= 1
                        else:
                            player_one.sliding = False
                            player_one.y = 318
                            player_one.slidCount = 30
                else:
                    if player_one.jumpCount >= -10:
                        neg = 1
                        if player_one.jumpCount < 0:
                            neg = -1
                        player_one.y -= (player_one.jumpCount ** 2) * 0.5 * neg
                        player_one.jumpCount -= 1
                    else:
                        player_one.isJump = False
                        player_one.jumpCount = 10
            bg_one_H.x -= bg_one_H.vel
            bg_two_H.x -= bg_two_H.vel
            redrawGameWindowHARD()
    else:
        raise Exception('Unknown difficulty {0}'.format(difficulty))


def main_background():
    win.blit(BACKGROUND, (0, 0))


# -----------------------------------------------------------------------------
# PLAY MENU
play_menu = pygameMenu.Menu(win,
                            bgfun=main_background,
                            color_selected=COLOR_BLUE,
                            font=pygameMenu.fonts.FONT_BEBAS,
                            font_color=COLOR_BLACK,
                            font_size=30,
                            menu_alpha=70,
                            menu_color=COLOR_WHITE,
                            menu_color_title=COLOR_WHITE,
                            font_title=pygameMenu.fonts.FONT_8BIT,
                            menu_height=int(WINDOW_SIZE[1] * 0.6),
                            menu_width=int(WINDOW_SIZE[0] * 0.6),
                            onclose=PYGAME_MENU_DISABLE_CLOSE,
                            option_shadow=False,
                            title='Play',
                            window_height=WINDOW_SIZE[1],
                            window_width=WINDOW_SIZE[0]
                            )
play_menu.add_option('Start', play_function, DIFFICULTY)
play_menu.add_selector('Select difficulty', [('Easy', 'EASY'),
                                             ('Medium', 'MEDIUM'),
                                             ('Hard', 'HARD')],
                       onreturn=None,
                       onchange=change_difficulty)
play_menu.add_option('Return to main menu', PYGAME_MENU_BACK)

# ABOUT MENU
about_menu = pygameMenu.TextMenu(win,
                                 bgfun=main_background,
                                 color_selected=COLOR_BLUE,
                                 font=pygameMenu.fonts.FONT_BEBAS,
                                 font_color=COLOR_BLACK,
                                 font_size_title=30,
                                 menu_alpha=70,
                                 font_title=pygameMenu.fonts.FONT_8BIT,
                                 menu_color=COLOR_WHITE,
                                 menu_color_title=COLOR_WHITE,
                                 menu_height=int(WINDOW_SIZE[1] * 0.6),
                                 menu_width=int(WINDOW_SIZE[0] * 0.6),
                                 onclose=PYGAME_MENU_DISABLE_CLOSE,
                                 option_shadow=False,
                                 text_color=COLOR_BLACK,
                                 text_fontsize=20,
                                 title='About',
                                 window_height=WINDOW_SIZE[1],
                                 window_width=WINDOW_SIZE[0]
                                 )
for m in ABOUT:
    about_menu.add_line(m)
about_menu.add_option('Return to menu', PYGAME_MENU_BACK)

# HOWTO MENU
howto_menu = pygameMenu.TextMenu(win,
                                 bgfun=main_background,
                                 color_selected=COLOR_BLUE,
                                 font=pygameMenu.fonts.FONT_BEBAS,
                                 font_color=COLOR_BLACK,
                                 font_size_title=30,
                                 menu_alpha=70,
                                 font_title=pygameMenu.fonts.FONT_8BIT,
                                 menu_color=COLOR_WHITE,
                                 menu_color_title=COLOR_WHITE,
                                 menu_height=int(WINDOW_SIZE[1] * 0.6),
                                 menu_width=int(WINDOW_SIZE[0] * 0.6),
                                 onclose=PYGAME_MENU_DISABLE_CLOSE,
                                 option_shadow=False,
                                 text_color=COLOR_BLACK,
                                 text_fontsize=20,
                                 title='HOWTOPLAY',
                                 window_height=WINDOW_SIZE[1],
                                 window_width=WINDOW_SIZE[0]
                                 )
for m in HOWTOPLAY:
    howto_menu.add_line(m)
howto_menu.add_option('Return to menu', PYGAME_MENU_BACK)

# MAIN MENU
main_menu = pygameMenu.Menu(win,
                            bgfun=main_background,
                            color_selected=COLOR_BLUE,
                            font=pygameMenu.fonts.FONT_BEBAS,
                            font_color=COLOR_BLACK,
                            font_size=30,
                            menu_alpha=0,
                            menu_height=int(WINDOW_SIZE[1] * 2.5),
                            menu_width=int(WINDOW_SIZE[0] * 0.6),
                            onclose=PYGAME_MENU_DISABLE_CLOSE,
                            option_shadow=False,
                            title='',
                            window_height=WINDOW_SIZE[1],
                            window_width=WINDOW_SIZE[0]
                            )
main_menu.add_option('Play', play_menu)
main_menu.add_option('About', about_menu)
main_menu.add_option('How To Play', howto_menu)
main_menu.add_option('Quit', PYGAME_MENU_EXIT)

# -----------------------------------------------------------------------------
# Main loop
while True:

    clock.tick(60)

    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            exit()

    main_menu.mainloop(events)



# -----------------------------------------------------------------------------
