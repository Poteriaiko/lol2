import pygame
pygame.init()


back = (200, 255, 255)
mw = pygame.display.set_mode((500, 500))
mw.fill(back)
clock = pygame.time.Clock()
dx = 3
dy = 3


platform_x = 200
platform_y = 330
move_right = False
move_left = False
game_over = False


class Area():
  def __init__(self, x=0, y=0, width=10, height=10, color=None):
      self.rect = pygame.Rect(x, y, width, height)
      self.fill_color = back
      if color:
          self.fill_color = color
  def color(self, new_color):
      self.fill_color = new_color
  def fill(self):
      pygame.draw.rect(mw, self.fill_color, self.rect)
  def collidepoint(self, x, y):
      return self.rect.collidepoint(x, y)      
  def colliderect(self, rect):
      return self.rect.colliderect(rect)


class Label(Area):
  def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
      self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)
  def draw(self, shift_x=0, shift_y=0):
      self.fill()
      mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


class Picture(Area):
  def __init__(self, filename, x=0, y=0, width=10, height=10):
      Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
      self.image = pygame.image.load(filename)
    
  def draw(self):
      mw.blit(self.image, (self.rect.x, self.rect.y))


ball = Picture('1.jpg', 160, 200, 50, 50)
platform = Picture('2.png', platform_x, platform_y, 250, 70)
platform2 = Picture('3.png', platform_x, 20, 100, 30)
start_x = 5
start_y = 5
count = 9



move_left2=False
move_right2=False

while not game_over:
  ball.fill()
  platform.fill()
  platform2.fill()
    
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          game_over = True
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RIGHT:
              move_right = True
          if event.key == pygame.K_LEFT:
              move_left = True
          if event.key == pygame.K_a:
            move_left2=True
          if event.key == pygame.K_d:
            move_right2=True

      elif event.type == pygame.KEYUP:
          if event.key == pygame.K_RIGHT:
              move_right = False
          if event.key == pygame.K_LEFT:
              move_left = False
          if event.key == pygame.K_a:
            move_left2=False
          if event.key == pygame.K_d:
            move_right2=False
  if move_right:
      platform.rect.x +=3
  if move_left:
      platform.rect.x -=3
  if move_right2:
      platform2.rect.x +=3
  if move_left2:
      platform2.rect.x -=3
  ball.rect.x += dx
  ball.rect.y += dy

  if ball.rect.x > 450 or ball.rect.x < 0:
      dx *= -1
  if ball.rect.y > 350:
      time_text = Label(150,150,50,50,back)
      time_text.set_text('YOU LOSE',60, (255,0,0))
      time_text.draw(10, 10)
      game_over = True
  if ball.rect.y < -50:
      time_text = Label(150,150,50,50,back)
      time_text.set_text('YOU LOSE',60, (255,0,0))
      time_text.draw(10, 10)
      game_over = True
#   if len(monsters) == 0:
#       time_text = Label(150,150,50,50,back)
#       time_text.set_text('YOU WIN',60, (0,200,0))
#       time_text.draw(10, 10)
#       game_over = True
  if ball.rect.colliderect(platform.rect):
      dy *= -1
  if ball.rect.colliderect(platform2.rect):
      dy *= -1

  platform.draw()
  ball.draw()
  platform2.draw()
  pygame.display.update()
  clock.tick(40)
