import pygame
from pygame.locals import *
import sys
import random
from super import *
import json

pygame.init()

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_BLUE = (0, 0, 255)
COLOR_RED = (255, 0, 0)
W, H = 800, 400
FPS = 30
win = pygame.display.set_mode((W, H))
pygame.display.set_caption("MAPLE DEFENCE")
walkRight = [pygame.image.load('boyData/RunRight1.png'), pygame.image.load('boyData/RunRight2.png'),
             pygame.image.load('boyData/RunRight3.png'), pygame.image.load('boyData/RunRight4.png'),
             pygame.image.load('boyData/RunRight5.png'), pygame.image.load('boyData/RunRight6.png'),
             pygame.image.load('boyData/RunRight7.png'), pygame.image.load('boyData/RunRight8.png'),
             pygame.image.load('boyData/RunRight9.png'), pygame.image.load('boyData/RunRight10.png')]
walkLeft = [pygame.image.load('boyData/RunLeft1.png'), pygame.image.load('boyData/RunLeft2.png'),
            pygame.image.load('boyData/RunLeft3.png'), pygame.image.load('boyData/RunLeft4.png'),
            pygame.image.load('boyData/RunLeft5.png'), pygame.image.load('boyData/RunLeft6.png'),
            pygame.image.load('boyData/RunLeft7.png'), pygame.image.load('boyData/RunLeft8.png'),
            pygame.image.load('boyData/RunLeft9.png'), pygame.image.load('boyData/RunLeft10.png')]
menubg = pygame.image.load('gameBg/bg.png')
gamebg = pygame.image.load('gameBg/gameBg2.png')
pygame.mixer.music.load('sound/bgmm.mp3')
pygame.mixer.music.play(-1)
fenceimg = pygame.image.load('otherData2/fence.png')
healthbar_img = pygame.image.load("otherData2/healthbar.png")
health_img = pygame.image.load("otherData2/health.png")
my_font = pygame.font.Font('menuData/Bubblegum.ttf', 30)
bitter = pygame.font.Font('menuData/Bitter-Regular.ttf', 20)
buttonImage = [pygame.image.load('menuData/blue_button00.png'), pygame.image.load('menuData/yellow_button00.png'),
               pygame.image.load('menuData/grey_button00.png'), pygame.image.load('menuData/green_button00.png')]
badplayer_list= [pygame.image.load('girlData/Run__001.png'), pygame.image.load('girlData/Run__002.png'),
             pygame.image.load('girlData/Run__003.png'), pygame.image.load('girlData/Run__004.png'),
             pygame.image.load('girlData/Run__005.png'), pygame.image.load('girlData/Run__006.png'),
             pygame.image.load('girlData/Run__007.png'), pygame.image.load('girlData/Run__008.png'),
             pygame.image.load('girlData/Run__009.png'), pygame.image.load('girlData/Run__010.png')]
badplayer2_list= [pygame.image.load('girlData/leftRun__001.png'), pygame.image.load('girlData/leftRun__002.png'),
             pygame.image.load('girlData/leftRun__003.png'), pygame.image.load('girlData/leftRun__004.png'),
             pygame.image.load('girlData/leftRun__005.png'), pygame.image.load('girlData/leftRun__006.png'),
             pygame.image.load('girlData/leftRun__007.png'), pygame.image.load('girlData/leftRun__008.png'),
             pygame.image.load('girlData/leftRun__009.png'), pygame.image.load('girlData/leftRun__010.png')]
bullet_list = [pygame.image.load('otherData2/0.png'), pygame.image.load('otherData2/1.png'),
               pygame.image.load('otherData2/2.png'),pygame.image.load('otherData2/2.png'),
               pygame.image.load('otherData2/3.png'), pygame.image.load('otherData2/4.png'),
               pygame.image.load('otherData2/5.png'), pygame.image.load('otherData2/6.png'),
               pygame.image.load('otherData2/6.png'), pygame.image.load('otherData2/7.png')]
char1 = pygame.image.load('boyData/boy.png')
char2 = pygame.image.load('boyData/boy1.png')
clock = pygame.time.Clock()
gameSpeed = 4
pygame.mixer.init()

usersDict = {}
with open('data.txt') as json_file:
    usersDict = json.load(json_file)

class User(object):
    def __init__(self):
        self.idInput = ''
        self.passwordInput = ''
        self.userId = ''
        self.password = ''
        self.login = True

    def loginPass(self):
        if self.idInput in usersDict:
            self.password = usersDict[self.idInput]
            if self.password == self.passwordInput:
                print('PW Match')
                return True
            else:
                print('PW Not Match')
                return False
        else:
            print('ID Not Match')
            return False

    def registerPass(self):
        if self.idInput in usersDict:
            print('ID Not Registered')
            return False
        else:
            usersDict[self.idInput] = self.passwordInput
            print('Registered')
            return True


class Button(object):
    def __init__(self, x, y, width, height, text=''):
        self.width = width
        self.height = height
        self.x = (W / 2 - self.width / 2)
        self.y = y
        self.text = text
        self.drawButton = True
        self.clickButton = False
        self.hoverButton = False

    def eventHandler(self, event):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.mouseCollision(mouse_x, mouse_y):
            self.hoverButton = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.clickButton = True
            else:
                self.clickButton = False
        else:
            self.hoverButton = False

    def draw(self, win):
        if self.drawButton:
            if self.hoverButton:
                win.blit(buttonImage[0], (self.x, self.y))
            else:
                win.blit(buttonImage[1], (self.x, self.y))
            if self.text != '':
                text_surface = my_font.render(self.text, 1, COLOR_BLACK)
                win.blit(text_surface, (self.x + (self.width / 2 - text_surface.get_width() / 2),
                                        self.y + (self.height / 2 - text_surface.get_height() / 2)))

    def mouseCollision(self, mouse_x, mouse_y):
        if self.x < mouse_x < self.x + self.width:
            if self.y < mouse_y < self.y + self.height:
                return True
        else:
            return False


class textInputBox(object):
    def __init__(self, x, y, width, height, lable=''):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.lable = lable
        self.starMod = True
        self.text = ''
        self.userInput = ''
        self.hoverTextBox = False
        self.activeTextBox = False
        self.drawTextBox = False

    def mouseCollision(self, mouse_x, mouse_y):
        if self.x < mouse_x < self.x + self.width:
            if self.y < mouse_y < self.y + self.height:
                return True
        else:
            return False

    def eventHandler(self, event):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.mouseCollision(mouse_x, mouse_y) and event.type == pygame.MOUSEBUTTONDOWN:
            self.activeTextBox = True
            self.text = ''
        if not (self.mouseCollision(mouse_x, mouse_y)) and event.type == pygame.MOUSEBUTTONDOWN:
            self.activeTextBox = False
        if event.type == pygame.KEYDOWN:
            if self.activeTextBox:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.userInput = self.text
                    self.activeTextBox = False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def draw(self, win):
        if self.drawTextBox:
            if self.activeTextBox:
                win.blit(buttonImage[3], (self.x, self.y))
            else:
                win.blit(buttonImage[2], (self.x, self.y))
            if self.starMod:
                text_surface = bitter.render(self.text, 1, COLOR_BLUE)
            else:
                temptext = ''
                for i in self.text:
                    temptext += '*'
                text_surface = bitter.render(temptext, 1, COLOR_BLUE)
            win.blit(text_surface, (self.x + (self.width / 2 - text_surface.get_width() / 2),
                                    self.y + (self.height / 2 - text_surface.get_height() / 2)))
            text_lable = bitter.render(self.lable, 1, COLOR_WHITE)
            win.blit(text_lable,
                     (self.x - (text_lable.get_width() + 50), self.y + (self.height / 2 - text_lable.get_height() / 2)))
class background(background1):
    def __init__(self, x, y, vel, index):
        background1.__init__(self, x, y, vel, index)
    def draw(self, win):
        win.blit(menubg[self.index], (self.x, self.y))
        if self.x < -800:
            self.x = 800
# ---------------------------------------------------------------
class player2(player1):
    def __init__(self, x, y, width, height,vel):
        player1.__init__(self, x, y, width, height, vel)
        self.vel = 5
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = False

    def draw(self, win):
        if self.walkCount + 1 >= 30:
            self.walkCount = 0
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(char1, (self.x, self.y))
            else:
                win.blit(char2, (self.x, self.y))

class badplayer(player1):
    def __init__(self, x, y, width, height,vel):
        player1.__init__(self, x, y, width, height, vel)
        self.rotateCount = 0
        self.hitbox = (x, y, width, height)

    def draw(self, win):
        if self.rotateCount + 1 >= 30:
            self.rotateCount = 0
        self.hitbox = (self.x + 5, self.y, self.width - 20, self.height - 5)
        win.blit(badplayer_list[self.rotateCount // 3], (self.x, self.y))
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        self.rotateCount += 1

    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1] and rect[1] < self.hitbox[1] + self.hitbox[3]:
                return True
        return False

class badplayer2(badplayer):
    def draw(self, win):
        if self.rotateCount + 1 >= 30:
            self.rotateCount = 0
        self.hitbox = (self.x + 5, self.y, self.width - 20, self.height - 5)
        win.blit(badplayer2_list[self.rotateCount // 3], (self.x, self.y))
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        self.rotateCount += 1

class fence(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (x, y, width, height)
    def draw(self, win):
        self.hitbox = (self.x + 10, self.y, self.width - 5, self.height)
        win.blit(fenceimg, (self.x, self.y))
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

class bullet_factory(object):
    def __init__(self, x, y, width, height, facing):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rotateCount = 0
        self.facing = facing
        self.vel = 8 * facing
        self.hitbox = (x, y, width, height)

    def draw(self, win):
        if self.rotateCount + 1 >= 30:
            self.rotateCount = 0
        self.hitbox = (self.x, self.y, self.width, self.height)
        win.blit(bullet_list[self.rotateCount // 3], (self.x, self.y))
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        self.rotateCount += 1
def updateFile():
    f = open('scores2.txt', 'r')  # opens the file in read mode
    file = f.readlines()  # reads all the lines in as a list
    last = int(file[0])  # gets the first line of the file

    if last < int(score):  # sees if the current score is greater than the previous best
        f.close()  # closes/saves the file
        file = open('scores2.txt', 'w')  # reopens it in write mode
        file.write(str(score))  # writes the best score
        file.close()  # closes/saves the file

        return score

    return last

def endScreen():
    global pause, score, clockSpeed, bombs, run, healthvalue
    pause = 0
    clockSpeed = 30
    bombs = []
    run = False
    healthvalue = 194

    run_end = True
    while run_end:
        run = True
        pygame.time.delay(150)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.K_ESCAPE:
                run = True
                score = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
                player_one.dead = False
            home_window()

        win.blit(menubg, (0,0))
        largeFont = pygame.font.SysFont('comicsans', 40)
        lastScore = largeFont.render('Best Score: ' + str(updateFile()), 1, (0, 0, 0))
        currentScore = largeFont.render('Score: '+ str(score),1,(0,0,0))
        win.blit(lastScore, (W / 2 - lastScore.get_width() / 2 - 20, 200))
        win.blit(currentScore, (W/2 - currentScore.get_width()/2, 240))
        pygame.display.update()
    score = 0

user_one = User()
button_list = []
textBox_list = []
warning = [0, '']
healthvalue = 194

def redrawMenuWindow():
    global warningCount, warningText
    win.blit(menubg, (0,0))
    for button in button_list:
        button.draw(win)
    for box in textBox_list:
        box.draw(win)
    if warning[0] > 0:
        text_surface = bitter.render(warning[1], 1, COLOR_RED)
        win.blit(text_surface, (int(W / 2 - text_surface.get_width() / 2), 20))
        warning[0] -= 1
    pygame.display.update()

def redrawGameWindow():
    global warningCount, warningText
    largeFont = pygame.font.SysFont('comicsans', 30)
    win.blit(gamebg, (0, 0))
    player_one.draw(win)
    fence_one.draw(win)
    fence_two.draw(win)
    text = largeFont.render('Score: ' + str(score), 1, (255, 255, 255))
    win.blit(healthbar_img, (5, 5))
    for health1 in range(healthvalue):
        win.blit(health_img, (health1 + 8, 8))
    for bullet in bullets:
        bullet.draw(win)
    for badplayerr in badplayerleft:
        badplayerr.draw(win)
    for badplayerr in badplayerright:
        badplayerr.draw(win)
    win.blit(text, (665, 20))
    if warning[0] > 0:
        text_surface = bitter.render(warning[1], 1, COLOR_RED)
        win.blit(text_surface, (int(W / 2 - text_surface.get_width() / 2), 20))
        warning[0] -= 1
    pygame.display.update()

run = True
if __name__ == "__main__":
    player_one = player2(390, 200, 64, 64, 5)
    fence_one = fence(285, 0, 40, 400)
    fence_two = fence(460, 0, 40, 400)
    bullets = []
    badplayerleft = []
    badplayerright = []
    score = 0
# user_one = User()
# button_list = []
# textBox_list = []
# warning = [0, '']
# healthvalue = 194
hit = pygame.mixer.Sound("sound/explode.wav")
shoot = pygame.mixer.Sound("sound/shoot.wav")
score = 0
pygame.time.set_timer(USEREVENT + 2, random.randrange(2000, 2500))

def game_window():
    global score, healthvalue,warningCount, warningText
    run = True
    while run:
        clock.tick(30)
        score += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == USEREVENT + 2:
                r = random.randrange(0, 330)
                badplayerleft.append(badplayer(-50, r, 64, 64, gameSpeed))
                r2 = random.randrange(0, 330)
                badplayerright.append(badplayer2(850, r2, 64, 64, gameSpeed))
        keys = pygame.key.get_pressed()
        for bullet in bullets:
            if bullet.x < 800 and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        for badplayerr in badplayerleft:
            if badplayerr.collide(fence_one.hitbox):
                hit.play()
                badplayerleft.pop(badplayerleft.index(badplayerr))
                healthvalue -= random.randint(10, 20)
            badplayerr.x += badplayerr.vel

            for bullet in bullets:
                if badplayerr.collide(bullet.hitbox):
                    score += 300
                    badplayerleft.pop(badplayerleft.index(badplayerr))
                    bullet.x += bullet.vel
                    bullets.pop(bullets.index(bullet))

        for badplayerr in badplayerright:
            if badplayerr.collide(fence_two.hitbox):
                hit.play()
                badplayerright.pop(badplayerright.index(badplayerr))
                healthvalue -= random.randint(10, 20)
            badplayerr.x -= badplayerr.vel

            for bullet in bullets:
                if badplayerr.collide(bullet.hitbox):
                    score += 300
                    badplayerright.pop(badplayerright.index(badplayerr))
                    bullet.x -= bullet.vel
                    bullets.pop(bullets.index(bullet))
        if keys[pygame.K_SPACE]:
            shoot.play()
            if player_one.left:
                facing = -1
            else:
                facing = 1
            if len(bullets) < 10:
                bullets.append(bullet_factory(round(player_one.x + player_one.width - 130 // 2), round(player_one.y + player_one.height - 100 // 2), 32, 32, facing))


        if keys[pygame.K_LEFT] and player_one.x > 330:
            player_one.x -= player_one.vel
            player_one.left = True
            player_one.right = False
            player_one.standing = False
        elif keys[pygame.K_RIGHT] and player_one.x < 435:
            player_one.x += player_one.vel
            player_one.right = True
            player_one.left = False
            player_one.standing = False
        else:
            player_one.standing = True
            player_one.walkCount = 0

        if keys[pygame.K_UP] and player_one.y > 20:
            player_one.y -= player_one.vel
        if keys[pygame.K_DOWN] and player_one.y < 380 - player_one.height:
            player_one.y += player_one.vel
        if healthvalue <= 0:
            endScreen()
        redrawGameWindow()
    main_window()

def home_window():
    button_list.append(Button(400, 250, 190, 49, 'LOGIN'))
    button_login = button_list[-1]
    button_login.drawButton = True
    button_list.append(Button(400, 320, 190, 49, 'REGISTER'))
    button_register = button_list[-1]
    button_register.drawButton = True
    run = True
    while run:
        clock.tick(FPS)
        key = pygame.key.get_pressed()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            for button in button_list:
                button.eventHandler(event)
        if button_login.clickButton:
            button_login.drawButton = False
            button_list.pop(button_list.index(button_login))
            button_register.drawButton = False
            button_list.pop(button_list.index(button_register))
            login_window()
        if button_register.clickButton:
            button_login.drawButton = False
            button_list.pop(button_list.index(button_login))
            button_register.drawButton = False
            button_list.pop(button_list.index(button_register))
            register_window()
        redrawMenuWindow()


def login_window():
    global warningCount, warningText
    button_list.append(Button(400, 320, 190, 49, 'LOGIN'))
    button_loginTwo = button_list[-1]
    button_loginTwo.drawButton = True
    textBox_list.append(textInputBox(420, 120, 190, 49, 'Loging ID : '))
    idTextBox = textBox_list[-1]
    idTextBox.drawTextBox = True
    textBox_list.append(textInputBox(420, 220, 190, 49, 'Loging PW : '))
    pwTextBox = textBox_list[-1]
    pwTextBox.drawTextBox = True
    pwTextBox.starMod = False
    run = True
    while run:
        clock.tick(FPS)
        key = pygame.key.get_pressed()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            for box in textBox_list:
                box.eventHandler(event)
            for button in button_list:
                button.eventHandler(event)
        if button_loginTwo.clickButton:
            if idTextBox.userInput != '' and pwTextBox.userInput != '':
                user_one.idInput = idTextBox.userInput
                user_one.passwordInput = pwTextBox.userInput
                if user_one.loginPass():
                    button_loginTwo.drawButton = False
                    button_list.pop(button_list.index(button_loginTwo))
                    idTextBox.drawTextBox = False
                    textBox_list.pop(textBox_list.index(idTextBox))
                    pwTextBox.drawTextBox = False
                    textBox_list.pop(textBox_list.index(pwTextBox))
                    warning[0], warning[1] = 60, 'Login Success'
                    main_window()
                else:
                    button_loginTwo.drawButton = False
                    button_list.pop(button_list.index(button_loginTwo))
                    idTextBox.drawTextBox = False
                    textBox_list.pop(textBox_list.index(idTextBox))
                    pwTextBox.drawTextBox = False
                    textBox_list.pop(textBox_list.index(pwTextBox))
                    warning[0], warning[1] = 60, 'Login Faild'
                    login_window()
            else:
                button_loginTwo.drawButton = False
                button_list.pop(button_list.index(button_loginTwo))
                idTextBox.drawTextBox = False
                textBox_list.pop(textBox_list.index(idTextBox))
                pwTextBox.drawTextBox = False
                textBox_list.pop(textBox_list.index(pwTextBox))
                warning[0], warning[1] = 60, 'Not Completed Enter Both Value'
                login_window()
        redrawMenuWindow()


def register_window():
    global warningCount, warningText
    button_list.append(Button(400, 320, 190, 49, 'REGISTER'))
    button_registerTwo = button_list[-1]
    button_registerTwo.drawButton = True
    textBox_list.append(textInputBox(420, 120, 190, 49, 'Register ID : '))
    idTextBox = textBox_list[-1]
    idTextBox.drawTextBox = True
    textBox_list.append(textInputBox(420, 220, 190, 49, 'Register PW : '))
    pwTextBox = textBox_list[-1]
    pwTextBox.drawTextBox = True
    pwTextBox.starMod = False
    run = True
    while run:
        clock.tick(FPS)
        key = pygame.key.get_pressed()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            for box in textBox_list:
                box.eventHandler(event)
            for button in button_list:
                button.eventHandler(event)
        if button_registerTwo.clickButton:
            if idTextBox.userInput != '' and pwTextBox.userInput != '':
                user_one.idInput = idTextBox.userInput
                user_one.passwordInput = pwTextBox.userInput
                if user_one.registerPass():
                    with open('data.txt', 'w+') as outfile:
                        json.dump(usersDict, outfile)
                    button_registerTwo.drawButton = False
                    button_list.pop(button_list.index(button_registerTwo))
                    idTextBox.drawTextBox = False
                    textBox_list.pop(textBox_list.index(idTextBox))
                    pwTextBox.drawTextBox = False
                    textBox_list.pop(textBox_list.index(pwTextBox))
                    warning[0], warning[1] = 60, 'Register Success'
                    login_window()
                else:
                    button_registerTwo.drawButton = False
                    button_list.pop(button_list.index(button_registerTwo))
                    idTextBox.drawTextBox = False
                    textBox_list.pop(textBox_list.index(idTextBox))
                    pwTextBox.drawTextBox = False
                    textBox_list.pop(textBox_list.index(pwTextBox))
                    warning[0], warning[1] = 60, 'Register Faild'
                    main_window()
            else:
                warning[0], warning[1] = 60, 'Not Completed Enter Both Value'
                button_registerTwo.drawButton = False
                button_list.pop(button_list.index(button_registerTwo))
                idTextBox.drawTextBox = False
                textBox_list.pop(textBox_list.index(idTextBox))
                pwTextBox.drawTextBox = False
                textBox_list.pop(textBox_list.index(pwTextBox))
                register_window()
        redrawMenuWindow()


def main_window():
    global warningCount, warningText
    button_list.append(Button(400, 180, 190, 49, 'PLAY'))
    button_play = button_list[-1]
    button_play.drawButton = True
    button_list.append(Button(400, 240, 190, 49, 'EXIT'))
    button_exit = button_list[-1]
    button_exit.drawButton = True
    run = True
    while run:
        clock.tick(FPS)
        key = pygame.key.get_pressed()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            for button in button_list:
                button.eventHandler(event)
        if button_play.clickButton:
            button_play.drawButton = False
            button_list.pop(button_list.index(button_play))
            button_exit.drawButton = False
            button_list.pop(button_list.index(button_exit))
            game_window()
        if button_exit.clickButton:
            button_play.drawButton = False
            button_list.pop(button_list.index(button_play))
            button_exit.drawButton = False
            button_list.pop(button_list.index(button_exit))
            pygame.quit()
            sys.exit()
        redrawMenuWindow()

home_window()

pygame.quit()
sys.exit()