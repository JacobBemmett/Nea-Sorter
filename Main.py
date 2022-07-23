import pygame
import random

BookTitles=["Bank", "Char", "Blink", "Ahead", "Chair","Chain","Storage","Flow","Plump","Low","Pump","Car"]

print(BookTitles)

def quicksort(array,pos,high):
  if pos<high:
    low=pos
    afterlastlow=low
    while pos<high:
      if array[pos]<array[high]:
          temp=array[afterlastlow]
          array[afterlastlow]=array[pos]
          array[pos]=temp     
          afterlastlow=afterlastlow+1
          pos=pos+1
      else:
        pos=pos+1 
    temp=array[afterlastlow]
    array[afterlastlow]=array[high]
    array[high]=temp
    quicksort(array,low,afterlastlow-1)
    quicksort(array,afterlastlow+1,high)

quicksort(BookTitles,0,(len(BookTitles)-1))
print(BookTitles)



pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((300,400),0,700)
pygame.display.set_caption("Game")
x,y = 200,130
sprite = pygame.image.load("Book_Resized.png")
sprite_rect= sprite.get_rect()

Loop = True
screen.fill((120,120,120))
#pygame..set_visible(False)
LastPos=35,235
screen.blit(sprite,(LastPos))
sprite_rect= sprite.get_rect(topleft=LastPos)
pygame.display.flip()

while Loop:
  for event in pygame.event.get():
    screen.fill((120,120,120))
    ButtonOne,ButtonTwo,ButtonThree=pygame.mouse.get_pressed()
    if ButtonOne:
      if event.type == pygame.MOUSEMOTION:
        if sprite_rect.collidepoint(pygame.mouse.get_pos()):
          screen.fill((120,120,120))
          pygame.display.flip()
          pos = pygame.mouse.get_pos()
          sprite_rect = sprite.get_rect(center=(pos))
          loc= x,y=sprite_rect.x,sprite_rect.y
          screen.blit(sprite,(loc))
          pygame.display.flip()
          print(loc)
    if event.type == pygame.MOUSEBUTTONUP:
      screen.fill((120,120,120))
      LastPos=pygame.mouse.get_pos()



