
import pygame
from pygame.locals import *
from pygamehelper import *
from vec2d import *
from blocks import *
from random import randrange


class Block:
    def __init__(self, x, y, w, config):
        self.x, self.y, self.w, self.config = x, y, w, config
        self.r = 0
        self.color = self.config[4]

    def rotate(self):
        self.r = (self.r + 1) if self.r < 3 else 0

    def draw(self, screen):
        ix, iy = self.w * self.x, self.w * self.y
        for x, y, b in self.config[self.r]:
            if not b: continue

            xywh = (ix + (x * self.w), iy + (y * self.w), self.w, self.w)
            border = tuple([x * 0.75 for x in self.color])
            pygame.draw.rect(screen, self.color, xywh)
            pygame.draw.rect(screen, border, xywh, 2)


class Tetris(PygameHelper):
    def __init__(self):
        self.w, self.h = 360, 540
        PygameHelper.__init__(self, size=(self.w, self.h))

        self.block_width = 20
        self.grid = Matrix(self.w / self.block_width,
                           self.h / self.block_width)
        self.blocks = []
        self.interval = 10
        self.frame = 0
        self.new_block()
        self.empty_grid()

    def keyDown(self, key):
        if key == 32:
            while not self.at_lowest_point():
                self.current_block.y += 1

        if key == 276 and self.current_block.x > 0:
            self.current_block.x -= 1

        limit = self.grid.w - self.current_block.config[self.current_block.r].w
        if key == 275 and self.current_block.x < limit:
            self.current_block.x += 1

        if key == 273:
            self.current_block.rotate()

    def update(self):
        self.frame += 1
        if (self.frame % self.interval) == 0:
            self.tick()

    def new_block(self):
        config = blocks[randrange(0, len(blocks))]
        self.current_block = Block(self.grid.w / 2, -(config[0].h),
                                   self.block_width, config)

    def empty_grid(self):
        for x in range(self.grid.w):
            for y in range(self.grid.h):
                self.grid.set(x, y, 0)

    def populate_grid(self):
        self.empty_grid()

        for b in self.blocks:
            config = b.config[b.r]
            for x, y, s in config:
                if s: self.grid.set(b.x + x, b.y + y, s)

    def at_lowest_point(self):
        config = self.current_block.config[self.current_block.r]
        dist = self.grid.h - self.current_block.y
        if dist <= config.h:
            return True

        config = [(x, y, s) for x, y, s in config if s]
        for x, y, s in config:
            ay = self.current_block.y + y
            ax = self.current_block.x + x
            if ay < 0: continue
            if self.grid.get(ax, ay + 1):
                return True

        return False

    def chop_row(self, row):
        chopped = {}
        for i, b in enumerate(self.blocks):
            dist = row - b.y
            config = b.config[b.r]
            if dist >= 0 and dist < config.h:
                chopped[i] = b

        for k, b in chopped.items():
            r = row - b.y
            config = b.config[b.r]
            if r >= 0 and r < config.h:
                m = Matrix(config.as_2d_list()[:r])
                b.config = [m, m, m, m, b.config[4]]
                self.blocks[k] = b
                if not r == (config.h - 1):
                    m2 = Matrix(config.as_2d_list()[(r + 1):])
                    b2 = Block(b.x, row + 1, self.block_width,
                               [m2, m2, m2, m2, b.config[4]])

                    self.blocks.append(b2)

        shifted = [b for b in self.blocks if b.y < row]
        for b in shifted:
            b.y += 1

    def tick(self):
        if self.at_lowest_point():
            self.blocks.append(self.current_block)
            self.populate_grid()
            self.new_block()
        else:
            self.current_block.y += 1

        for i, row in enumerate(self.grid.as_2d_list()):
            if sum([r or 0 for r in row]) == self.grid.w:
                self.chop_row(i)

        self.populate_grid()

    def draw(self):
        self.screen.fill((0, 0, 0))

        self.current_block.draw(self.screen)

        for b in self.blocks:
            b.draw(self.screen)

        pygame.display.update()

t = Tetris()
t.mainLoop(60)
