
import pygame
from pygame import mixer
import sys
pygame.init()
mixer.init()
screen = pygame.display.set_mode((800,800))

mixer.music.set_volume(1)
pygame.mixer.set_num_channels(13)

def play_note(note_name, channel_number, note_file):
  pygame.mixer.Channel(channel_number).play(pygame.mixer.Sound(f'{note_file}'))
  print(f"Pressed {note_name} Key")

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


cs_key = pygame.Rect(90, 600, 70, 150)
ds_key = pygame.Rect(190, 600, 70, 150)
fs_key = pygame.Rect(390, 600, 70, 150)
gs_key = pygame.Rect(490, 600, 70, 150)
as_key = pygame.Rect(590, 600, 70, 150)


keys = [c1_key, d_key, e_key, f_key, g_key, a_key, b_key, c2_key, cs_key, ds_key, fs_key, gs_key, as_key,]






while playing_notes:

  screen.fill((128,128,128))
  for i in keys:
    if i != cs_key and i != ds_key and i != fs_key and i != gs_key and i != as_key:
      pygame.draw.rect(screen, (255,255,255), i)
    else:
      pygame.draw.rect(screen, (0,0,0), i)
  pygame.display.flip()

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
        play_note("C1", 0, f'./Octave {octave} Notes/c{octave}.mp3')

      if event.key == pygame.K_w:
        play_note("C#", 1, f'./Octave {octave} Notes/c-{octave}.mp3')
      
      if event.key == pygame.K_s:
        play_note("D", 2, f'./Octave {octave} Notes/d{octave}.mp3')
      
      if event.key == pygame.K_e:
        play_note("D#", 3, f'./Octave {octave} Notes/d-{octave}.mp3')
      
      if event.key == pygame.K_d:
        play_note("E", 4, f'./Octave {octave} Notes/e{octave}.mp3')
      
      if event.key == pygame.K_f:
        play_note("F", 5, f'./Octave {octave} Notes/f{octave}.mp3')
      
      if event.key == pygame.K_t:
        play_note("F#", 6, f'./Octave {octave} Notes/f-{octave}.mp3')
      
      if event.key == pygame.K_g:
        play_note("G", 7, f'./Octave {octave} Notes/g{octave}.mp3')
      
      if event.key == pygame.K_y:
        play_note("G#", 8, f'./Octave {octave} Notes/g-{octave}.mp3')
      
      if event.key == pygame.K_h:
        play_note("A", 9, f'./Octave {octave} Notes/a{octave}.mp3')
      
      if event.key == pygame.K_u:
        play_note("A#", 10, f'./Octave {octave} Notes/a-{octave}.mp3')
      
      if event.key == pygame.K_j:
        play_note("B", 12, f'./Octave {octave} Notes/b{octave}.mp3')
        
      if event.key == pygame.K_k:
        high_c = octave + 1
        play_note("C2", 12, f'./Octave {octave} Notes/c{high_c}.mp3')


        
