import pygame
import math as m


class CannonBall:
    global screen
    global height
    global width

    def __init__(self, color, rad, speed, mass, wind):
        self.color = color
        self.coords = [0, height]
        self.sin_a = m.sin(m.radians(rad))
        self.cos_a = m.cos(m.radians(rad))
        self.time = 0
        self.speed = speed
        self.mass = mass
        self.wind = wind

    def draw(self):
        pygame.draw.circle(screen, self.color, self.coords, 20)

    def move(self):
        self.time += 0.1
        if self.wind == 0:
            self.coords[0] = self.speed * self.cos_a * self.time
            self.coords[1] = height - self.speed * self.sin_a * self.time + 9.8 * self.mass * (self.time**2) / 2
        else:
            self.coords[0] = self.speed * self.cos_a * self.mass / self.wind * (1 - m.exp(- self.wind * self.time / self.mass))
            self.coords[1] = height - (self.speed * self.sin_a * self.mass / self.wind + (self.mass**2) * 9.8 / (self.wind**2)) * (1 - m.exp(- self.wind * self.time / self.mass)) + self.mass * 9.8 * self.time / self.wind


class Trajectory:
    global screen
    global rad
    global speed
    global height
    global width

    def __init__(self, color, mass, wind):
        self.color = color
        self.time = 0
        self.mass = mass
        self.wind = wind

    def draw(self):
        i = 1
        x = 0
        y = height
        while x < width and height >= y:
            cos_a = m.cos(m.radians(rad))
            sin_a = m.sin(m.radians(rad))
            if self.wind == 0:
                x = speed * cos_a * i
                y = height - speed * sin_a * i + 9.8 * self.mass * (i**2) / 2
            else:
                x = speed * cos_a * self.mass / self.wind * (1 - m.exp(- self.wind * i / self.mass))
                y = height - (speed * sin_a * self.mass / self.wind + (self.mass**2) * 9.8 / (self.wind**2)) * (1 - m.exp(- self.wind * i / self.mass)) + self.mass * 9.8 * i / self.wind
            pygame.draw.circle(screen, self.color, (x, y), 2)
            i += 1


black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

width = 720
height = 480
fps = 60
stack = []
speed = 0
rad = 0

wind = float(input("Укажите значение сопротивления воздуха: "))
mass = float(input("Укажите значение массы снаряда: "))

pygame.init()
screen = pygame.display.set_mode((width, height))
bg_c = black
pygame.display.set_caption("Cannon")
clock = pygame.time.Clock()
traj = Trajectory(red, mass, wind)

running = True
while running:
    clock.tick(fps)

    screen.fill(bg_c)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                stack.append(CannonBall(blue, rad, speed, mass, wind))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and rad <= 89:
        rad += 1
    if keys[pygame.K_RIGHT] and rad >= 1:
        rad -= 1
    if keys[pygame.K_UP]:
        speed += 1
    if keys[pygame.K_DOWN] and speed >= 1:
        speed -= 1

    i = 0
    while i < len(stack):
        stack[i].draw()
        stack[i].move()
        if stack[i].coords[0] > width or stack[i].coords[1] > height:
            del stack[i]
        else:
            i += 1
    traj.draw()
    pygame.display.flip()
