import pygame
class Ball:

    def __init__(self,posX,posY,radius):
        self.posX = posX
        self.posY = posY
        self.speedX = 0
        self.speedY = 0
        self.radius = radius

    def update(self):
        self.posX += self.speedX
        self.posY += self.speedY

    def render(self,screen):
        pygame.draw.circle(screen, (157, 87, 7), (self.posX, self.posY), self.radius)

class Paddle:

    def __init__(self,posX,posY):
        self.posX = posX
        self.posY = posY
        self.height = 100
        self.width = 10

    def moveUp (self):
        self.posY += 5

    def moveDown (self):
        self.posY -= 5

    def render(self, screen):
        pygame.draw.line(screen,(150,150,150),(self.posX,self.posY),(self.posX,self.posY + self.height),self.width)

    @classmethod
    def includes (cls, a, b, x):
        return x >= a and x <= b

    def collides(self, ball):
        return (Paddle.includes(self.posX,self.posX+self.width,ball.posX-ball.radius) or
                Paddle.includes(self.posX,self.posX+self.width,ball.posX+ball.radius)) and\
               ball.posY >= self.posY and ball.posY <= self.posY + self.height




class PingPong:

    def __init__(self):
        self.running = False
        self.screen = None
        self.clock = None
        self.ball = None
        self.lpaddle = None
        self.rpaddle = None

    def run(self):
        self.init()
        while (self.running):
            self.update()
            self.render()
        self.cleanUp()

    def init(self):
        self.screen = pygame.display.set_mode((700, 500))
        pygame.display.set_caption("Ping Pong")
        self.clock = pygame.time.Clock()
        self.running = True
        self.ball = Ball(250, 350, 50)
        self.ball.speedX = 4
        self.ball.speedY = 8
        self.lpaddle = Paddle(10, 240)
        self.rpaddle = Paddle(685, 350)


    def update(self):
        self.events()
        self.ball.update()
        r = self.ball.radius
        if self.lpaddle.collides(self.ball) or self.rpaddle.collides(self.ball):
            self.ball.speedX *= -1
        if self.ball.posY-r <= 50 or self.ball.posY+r >= 500:
            self.ball.speedY *= -1
        if self.ball.posX-r <= 0 or self.ball.posX+r >= 700:
            self.running = False

    def events(self):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                self.running = False

    def render(self):
        self.screen.fill((0, 0, 0))
        self.drawMenu()
        self.ball.render(self.screen)
        self.rpaddle.render(self.screen)
        self.lpaddle.render(self.screen)
        pygame.display.flip()
        self.clock.tick(60)

    def cleanUp(self):
        self.screen.fill((255,255,255))

    def drawMenu (self):
        pygame.draw.line(self.screen, pygame.Color("green"), [0, 45], [700, 45], 5)




if __name__ == '__main__':
    pingpong = PingPong()
    pingpong.run()










