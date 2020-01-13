import pygame
from pygame import display, draw as pd, key
import sys
import datetime
from collections import defaultdict
import math
from shutil import copyfile
import configparser
import os


class Game:
    def __init__(self,
                 width,
                 height,
                 timings,
                 time_to_show, startCile, startPlayer, timeStart=0):
        # self.background_image = pygame.image.load(back_image_filename)
        #self.frame_rate = frame_rate
        self.game_over = False
        self.timeStart = timeStart
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.init()
        pygame.font.init()
        self.myfont = pygame.font.SysFont('serif', 30)
        self.res = (width, height)
        self.safeTime = 500
        self.surface = display.set_mode((width, height))
        display.set_caption("Destroy the flower!")

        ##########ICON##########
        ico = "flower.png"
        if not os.path.exists(ico):
            ico = "main/flower.png"
        gameIcon = pygame.image.load(ico)
        display.set_icon(gameIcon)
        ##############
        self.clock = pygame.time.Clock()
        self.keydown_handlers = defaultdict(list)
        self.keyup_handlers = defaultdict(list)
        self.mouse_handlers = []
        self.curTime = 0
        self.showTime = time_to_show
        self.ct = datetime.datetime.now  # ().time
        self.skip = 0
        self.timings = timings
        self.half = startCile
        self.halfINT = (int(startCile[0]), int(startCile[1]))
        self.isStart = False

        temp = (startPlayer[0] - startCile[0], startPlayer[1] - startCile[1])
        self.startPlayer = startPlayer
        self.distantion = math.sqrt(temp[0]*temp[0] + temp[1]*temp[1])  # S1

        # time =  self.showTime# T = t1+t2

        self.speed = (self.distantion / (self.showTime))  # u1 = s1/t1

        self.size = int(self.safeTime * self.speed/2.0)  # r radius
       # self.speed += self.size/self.showTime/2

        self.isPause = False
        self.pauseDate = None
        self.prerar = 255*2/self.safeTime
        self.closeZone = int(self.safeTime/2)
        self.timeOffset = 0
        self.fps_pos = width-100
        self.lCicle = int(self.size/2.5)
        #(255, 233, 38),
        self.colors = [(255, 0, 0),
                       (255, 165, 0),
                       (255, 128, 128),
                       (0, 255, 0),
                       (0, 255, 255),
                       (0, 0, 255),
                       (255, 0, 255),
                       (163, 54, 81),
                       (77, 190, 111),
                       (182, 33, 196),
                       (87, 177, 255),
                       (145, 196, 5),
                       (159, 12, 196),
                       (14, 48, 240),
                       (22, 150, 11)]
        self.clrPointer = 0

        #self.hidePos = -self.closeZone
        #self.hidePos = 0
        self.hidePos = -self.lCicle

        pass

    def handle_events(self):
        """events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                write_timings(self.timings, self.timeOffset)
                exit()
                # sys.exit()
                return

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not self.isStart:
                        self.start()
                    elif self.isPause:
                        self.resume()
                    else:
                        self.pause()

                if event.key == pygame.K_r:
                    self.stop()

                if key.get_mods() & pygame.KMOD_CTRL:  # & for mask working
                    if self.skip >= len(self.timings):  # current
                        return
                    if event.key == pygame.K_RIGHT:
                        self.timings[self.skip] -= 50
                    elif event.key == pygame.K_LEFT:
                        self.timings[self.skip] += 50

                    elif event.key == pygame.K_DOWN:
                        self.start_dt -= datetime.timedelta(milliseconds=50)
                    elif event.key == pygame.K_UP:
                        self.start_dt += datetime.timedelta(milliseconds=50)

                elif key.get_mods() & pygame.KMOD_SHIFT:
                    if event.key == pygame.K_RIGHT:
                        self.start_dt -= datetime.timedelta(milliseconds=50)
                        self.timeOffset -= 50
                    elif event.key == pygame.K_LEFT:
                        self.start_dt += datetime.timedelta(milliseconds=50)
                        self.timeOffset += 50

                else:  # prev
                    if self.skip <= 0:
                        return

                    if event.key == pygame.K_RIGHT:
                        self.timings[self.skip-1] -= 50
                    elif event.key == pygame.K_LEFT:
                        self.timings[self.skip-1] += 50

                    elif event.key == pygame.K_y:
                        self.timings.pop(self.skip)

        if not key.get_mods() & pygame.KMOD_CTRL:
            keys = key.get_pressed()
            if keys[pygame.K_DOWN]:
                self.start_dt -= datetime.timedelta(milliseconds=3)

            elif keys[pygame.K_UP]:
                self.start_dt += datetime.timedelta(milliseconds=2)
                for i in range(self.skip-1, -1, -1):  # -1 not incl
                    temp = self.timings[i] - \
                        self.tempTime.total_seconds()*1000.0
                    if temp > self.hidePos and temp < self.showTime:
                        self.skip -= 1
                    else:
                        break
                    # for handler in self.keydown_handlers[event.key]:
                #    handler(event.key)

            #     for handler in self.keydown_handlers[event.key]:
            #         handler(event.key)
            # elif event.type in (pygame.MOUSEBUTTONDOWN,
            #                     pygame.MOUSEBUTTONUP,
            #                     pygame.MOUSEMOTION):
            #     for handler in self.mouse_handlers:
            #         handler(event.type, event.pos)

    def update(self):
        """pause sattus and """
        # for o in self.objects:
        #     o.update()
        if self.isPause:
            curt = self.ct()
            self.start_dt += curt-self.pauseDate
            self.pauseDate = curt
        if self.skip == len(self.timings)+1:
            self.pause()

    def draw(self):
        self.surface.fill((255, 255, 255))

        pd.circle(self.surface, (0, 0, 0),
                  (self.startPlayer), int(self.size), 1)

        pd.circle(self.surface, (0, 128, 0),
                  (self.startPlayer), self.lCicle, 1)

        # ltc
        pd.line(self.surface, (0, 0, 0),
                (self.startPlayer[0]-self.size + 1, self.startPlayer[1]), (self.startPlayer[0]-self.lCicle, self.startPlayer[1]), 2)
        # ctr
        pd.line(self.surface, (0, 0, 0),
                (self.startPlayer[0]+self.lCicle, self.startPlayer[1]), (self.startPlayer[0]+self.size, self.startPlayer[1]), 2)

        # dtc
        pd.line(self.surface, (0, 0, 0),
                (self.startPlayer[0], self.startPlayer[1]+self.size), (self.startPlayer[0], self.startPlayer[1]+self.lCicle), 2)

        if not self.isStart:
            return
        # tempTime = 0
        i = (self.skip) % len(self.colors)
        for _time in self.timings[self.skip:]:
           # ct =  self.ct()
            # + (self.isPause if ct -self.pauseDate else 0)   # сколько прошло
            self.tempTime = self.ct() - self.start_dt
            temp = self.tempTime.total_seconds() * 1000.0  # сколько прошло мс
            dif = _time - temp  # Время относительно начала ноты
            if dif <= self.showTime:  # dif уменьшается. От n до -n
                if dif <= self.hidePos:
                    self.skip += 1
                    continue
                pd.circle(self.surface, (self.colors[i] if dif > 0 else (-int(self.prerar*dif), 255 + int(self.prerar*dif), 10)), self.halfINT, max(
                    round((self.showTime - dif) * self.speed), 1), 1)
            # self.showTime - dif: 5000 -5000, 5000 -4999, ..., 5000-0 ||| coof -- speed=  distantion/showTime = 360/5000 |||  dist = showTime*coof

                if self.lCicle >= dif*self.speed and dif*self.speed >= -self.lCicle:
                    textsurface = self.myfont.render(
                        "Press!!!", False, (0, 0, 0))
                    self.surface.blit(
                        textsurface, (self.halfINT[0]-30, self.res[1]-30))

            i = (i+1 if i < len(self.colors)-1 else 0)
            pass

        textsurface = self.myfont.render((str(self.skip)), False, (0, 0, 0))
        # tempTime = timedelta(seconds = tempTime.total_seconds())f'{tempTime.hour}:{tempTime.minute}:{tempTime.second}:{tempTime.microsecond}
        self.surface.blit(textsurface, (0, 30))

        textsurface = self.myfont.render(str(self.tempTime), False, (0, 0, 0))
        self.surface.blit(textsurface, (0, 0))

    def run(self):

        # last_delta = self.ct()
        # last_fps = "0"
        # couner = 6

        while not self.game_over:
            # self.surface.blit(self.background_image, (0, 0))
            self.handle_events()
            self.update()
            self.draw()

            #################FPS########################
            #ct = self.ct()
            # if couner == 6:
            #     last_fps = str(int(1000.0/(ct-last_delta).total_seconds()))
            #     couner = 0
            # textsurface = self.myfont.render(last_fps, False, (0, 0, 0))
            # self.surface.blit(textsurface, (self.fps_pos, 0))
            #couner += 1
            #last_delta = ct
            # or
            # self.clock.tick(self.frame_rate)
            ############################################
            display.update()

    def start(self):
        self.start_dt = self.ct() - datetime.timedelta(milliseconds=self.timeStart)
        self.curTime = 0
        self.skip = 0
        self.isStart = True
        self.isPause = False
        self.pauseDate = None
        pass

    def stop(self):
        self.isStart = False
        pass

    def pause(self):
        self.pauseDate = self.ct()
        self.isPause = True

    def resume(self):
        self.isPause = False


timings = []


def write_timings(_times, offset):
    global timePath

    copyfile(timePath, timePath + '.bak')
    with open(timePath, 'w') as file:  # Use file to refer to the file object
        for time in _times:
            file.write(str(time+offset))
            file.write("\n")
            # times.append(float(line.replace('\n', '').replace(',', '.')))
    pass


def read_timings():
    global timePath
    global timings

    with open(timePath, 'r') as file:  # Use file to refer to the file object
        for line in file:
            timings.append(float(line.replace('\n', '').replace(',', '.')))
    pass


def split(st) -> list:
    st = st.replace(" ", "")
    st = st.split(",")
    res = []
    for s in st:
        res.append(int(s))
    return res


path = "main/config.ini"
timePath = "timings/timings"


if __name__ == "__main__":
    read_timings()
    print("starting...")
    ################CONFIG########
    if not os.path.exists(path):
        path = "config.ini"

    if not os.path.exists(timePath):
        timePath = "main/timings/timings"

    cof = configparser.ConfigParser()
    cof.read(path)

    wid = cof.getint("Settings", "width")

    hei = cof.getint("Settings", "height")

    nst = cof.getint("Settings", "noteShowTime")

    nsp = split(cof.get("Settings", "noteStartPos"))

    psp = split(cof.get("Settings", "playerStartPos"))

    st = split(cof.get("Settings", "startTime"))

    ##############################
    print("1/3...")

    time = datetime.timedelta(minutes=st[0], seconds=st[1], milliseconds=st[2])

    game = Game(wid, hei, timings, nst, (nsp[0], nsp[1]),
                (psp[0], psp[1]), time.total_seconds()*1000.0)

    #game = Game(800, 700, 2000, (400, 100), (400, 600), time.total_seconds()*1000.0)

    game.run() 
    #input("Press enter to continue...")
