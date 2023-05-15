import pygame
from pygame import mixer
import sys
import time
import random
pygame.init()
mixer.init()
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
mixer.music.set_volume(1)
pygame.mixer.set_num_channels(13)
octave = 4
playing_notes = True
c1_key = pygame.Rect(4, 600, 96, 300)
d_key = pygame.Rect(104, 600, 96, 300)
e_key = pygame.Rect(204, 600, 96, 300)
f_key = pygame.Rect(304, 600, 96, 300)
g_key = pygame.Rect(404, 600, 96, 300)
a_key = pygame.Rect(504, 600, 96, 300)
b_key = pygame.Rect(604, 600, 96, 300)
c2_key = pygame.Rect(704, 600, 96, 300)
cs_key = pygame.Rect(70, 600, 70, 150)
ds_key = pygame.Rect(170, 600, 70, 150)
fs_key = pygame.Rect(370, 600, 70, 150)
gs_key = pygame.Rect(470, 600, 70, 150)
as_key = pygame.Rect(570, 600, 70, 150)
keys = [c1_key, d_key, e_key, f_key, g_key, a_key, b_key, c2_key, cs_key, ds_key, fs_key, gs_key, as_key,]
x_list = [4, 104, 204, 304, 404, 504, 604, 704]
x = random.choice(x_list)
y = 200
width = 96
height = 200
velocity = 10
score = 4
tiles_fallen = 0
velocity_increase = 0
lives = 5

win_img = pygame.image.load("win_screen.png")
win_img = pygame.transform.scale(win_img,(screen_width, screen_height))
lose_img = pygame.image.load("lose_screen.png")
lose_img = pygame.transform.scale(lose_img,(screen_width, screen_height))

screen.fill((128,128,128))



def play_note(note_name, channel_number, note_file, note, score):
  pygame.draw.rect(screen, (100,100,100), note)
  pygame.mixer.Channel(channel_number).play(pygame.mixer.Sound(f'{note_file}'))
  if note_name == good_note:
    print("Good Note Hit")
    hit = True
    return hit
  else:
    hit = False
  

key_is_falling = True
hit = False

while playing_notes:

  while key_is_falling:

    if score == 100 or lives == 0:
      if score == 100:
        game_verdict = 'win'
      elif lives == 0:
        game_verdict = 'lose'
      key_is_falling = False
      playing_notes = False


    if (tiles_fallen % 8) == 0 and tiles_fallen != 0:
      velocity_increase += 2
      velocity += velocity_increase
      tiles_fallen += 1
    print("Speed is currently", velocity)
    print(tiles_fallen, 'tiles fallen')

    if y >= 400:
      print("Failed Note Hit")
      lives = lives - 1
      velocity = 10
      print("New lives:", lives)
      x = random.choice(x_list)
      y = 100
    else:
      for i in keys:
        if i != cs_key and i != ds_key and i != fs_key and i != gs_key and i != as_key:
          pygame.draw.rect(screen, (255,255,255), i)
        else:
          pygame.draw.rect(screen, (0,0,0), i)
      pygame.display.flip()

      screen.fill((182, 212, 206))
      pygame.time.delay(100)
      y += velocity
      pygame.draw.rect(screen, (6, 87, 79), (x, y, width, height))
      pygame.display.flip()

      for i in keys:
        if i != cs_key and i != ds_key and i != fs_key and i != gs_key and i != as_key:
          pygame.draw.rect(screen, (255,255,255), i)
        else:
          pygame.draw.rect(screen, (0,0,0), i)
      pygame.display.flip()

      if x == 4:
        good_note = 'C1'
      elif x == 104:
        good_note = 'D'
      elif x == 204:
        good_note = 'E'
      elif x == 304:
        good_note = 'F'
      elif x == 404:
        good_note = 'G'
      elif x == 504:
        good_note = 'A'
      elif x == 604:
        good_note = 'B'
      elif x == 704:
        good_note = 'C2'

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_z:
            if octave == 3:
              print("The piano doesn't have any lower keys!")
            else:
              octave = octave - 1
              print(f"Now in octave {octave}")
          if event.key == pygame.K_x:
            if octave == 5:
              print("The piano doesn't have any higher keys!")
            else:
              octave = octave + 1
              print(f"Now in octave {octave}")
              
          if event.key == pygame.K_a:
            hit = play_note("C1", 0, f'./Octave {octave} Notes/c{octave}.mp3', c1_key, score)

          if event.key == pygame.K_w:
            hit = play_note("C#", 1, f'./Octave {octave} Notes/c-{octave}.mp3', cs_key, score)
          
          if event.key == pygame.K_s:
            hit = play_note("D", 2, f'./Octave {octave} Notes/d{octave}.mp3', d_key, score)
          
          if event.key == pygame.K_e:
            hit = play_note("D#", 3, f'./Octave {octave} Notes/d-{octave}.mp3', ds_key, score)
          
          if event.key == pygame.K_d:
            hit = play_note("E", 4, f'./Octave {octave} Notes/e{octave}.mp3', e_key, score)
          
          if event.key == pygame.K_f:
            hit = play_note("F", 5, f'./Octave {octave} Notes/f{octave}.mp3', f_key, score)
          
          if event.key == pygame.K_t:
            hit = play_note("F#", 6, f'./Octave {octave} Notes/f-{octave}.mp3', fs_key, score)
          
          if event.key == pygame.K_g:
            hit = play_note("G", 7, f'./Octave {octave} Notes/g{octave}.mp3', g_key, score)
          
          if event.key == pygame.K_y:
            hit = play_note("G#", 8, f'./Octave {octave} Notes/g-{octave}.mp3', gs_key, score)
          
          if event.key == pygame.K_h:
            hit = play_note("A", 9, f'./Octave {octave} Notes/a{octave}.mp3', a_key, score)
          
          if event.key == pygame.K_u:
            hit = play_note("A#", 10, f'./Octave {octave} Notes/a-{octave}.mp3', as_key, score)
          
          if event.key == pygame.K_j:
            hit = play_note("B", 12, f'./Octave {octave} Notes/b{octave}.mp3', b_key, score)
            
          if event.key == pygame.K_k:
            high_c = octave + 1
            hit = play_note("C2", 12, f'./Octave {octave} Notes/c{high_c}.mp3', c2_key, score)
      if hit:
        score += 1
        tiles_fallen += 1
        print(score, 'score')
        print("next key...")
        x = random.choice(x_list)
        y = 100
        hit = False

  if game_verdict == 'lose':
    screen.blit(lose_img, (0, 0))
    pygame.display.flip()
  elif game_verdict == 'win':
    screen.blit(win_img, (0, 0))
    pygame.display.flip()

  play_again_loop = True
  while play_again_loop:
    play_again = input("Do you want to play again? ('y' or 'n'): ")
    if play_again == 'y':
      print("Refresh the page lmao")
      play_again_loop = False
      playing_notes = False
    elif play_again == 'n':
      print("Goodbye!")
      play_again_loop = False
      playing_notes = False
    else:
      print("Invalid answer")
print("All loops ended")
