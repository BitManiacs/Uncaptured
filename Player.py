import pygame, sys
from pygame.locals import *
import collisions

global game_engine

player_image = pygame.image.load( "img/bulbasaur.png" )
BLOCK_PIXELS = 32 #filler variable for the pixels of each square
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Player:

   """Initiates the Player"""
   #Using x,y,options(options comes from map file) as only parameters
   def __init__(self, x, y, options):
      self.x = x
      self.y = y
      self.image = player_image
      self.health = 10 #Health at 10, might change

   def draw(self,screen):
      screen.blit( self.image, ( self.x, self.y ) )

   def update(self):
      events = pygame.event.get()
      if ( len(events) != 0 ):
         keys = events[0].key
      else:
         keys = 0
      if ( keys == K_LEFT ):
         self.move( -BLOCK_PIXELS, 0 )
         self.xDelta = -BLOCK_PIXELS
         self.yDelta = 0
      elif ( keys == K_RIGHT ):
         self.move( BLOCK_PIXELS, 0 )
         self.xDelta = BLOCK_PIXELS
         self.yDelta = 0
      elif ( keys == K_DOWN ):
         self.move( 0, BLOCK_PIXELS )
         self.xDelta = 0
         self.yDelta = BLOCK_PIXELS
      elif ( keys == K_UP ):
         self.move( 0, -BLOCK_PIXELS )
         self.xDelta = 0
         self.yDelta = -BLOCK_PIXELS


   def move( self, xDelta, yDelta ):
      #new1 = self.x + self.image.get_width()
      #new2 = self.y + self.image.get_height()
      """Check if moving will move out of bounds of the screen"""
      if ( self.x + xDelta < SCREEN_WIDTH and
          self.x + xDelta >= 0 and
          self.y + yDelta < SCREEN_HEIGHT and
          self.y + yDelta >= 0 ):
         self.x += xDelta
         self.y += yDelta
         """
         coll = collisions.checkByType( self.x, self.y, "boulder" )
         if ( len(coll) != 0 ):
            self.x -= xDelta
            self.y -= yDelta
         """
         """
         newRect = self.image.get_rect().move( self.x, self.y )
         for object in game_engine.objectList['boulder']:
            if newRect.colliderect( object.image ):
               self.x -= xDelta
               self.y -= yDelta
               """

   def moveBack(self):
      self.move( -self.xDelta, -self.yDelta )

   def getX( self ):
      return self.x


   def getY( self ):
      return self.y
"""
#Using main.py to test instead
clock = pygame.time.Clock()
BLOCK_PIXELS = 50 #filler variable for the pixels of each square
def keycheck():
   return pressed
pygame.init()
screen = pygame.display.set_mode((640, 480))
player = Player( 200, 200, "cat.png", screen )
# Fill background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))
pygame.display.update()
screen.blit( background, (0,0 ) )

while ( True ):
   global pressed
   pressed = 0

   pos = player.image.get_rect()
   screen.blit( background, pos, pos )
   keys = pygame.key.get_pressed()
   if keys[K_LEFT]:
      pressed = K_LEFT
   elif keys[K_RIGHT]:
      pressed = K_RIGHT
   elif keys[K_UP]:
      pressed = K_UP
   elif keys[K_DOWN]:
      pressed = K_DOWN
   player.update()
   pygame.display.update()
   clock.tick( 10 )
   for event in pygame.event.get():
      if event.type == QUIT:
         pygame.quit()
         sys.exit()
      #if event.type == KEYDOWN:
       #  global pressed
        # pressed = event.key
        # player.update()
        # pygame.display.update()
"""
