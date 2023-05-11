'''
Download zip
unzip file
type'cmd' in directory
type'python main.py' in command prompt

'''
import pygame
from pygame import mixer
import sys
pygame.init()
mixer.init()
display = pygame.display.set_mode((800,800))

mixer.music.set_volume(1)
pygame.mixer.set_num_channels(13)



'''Hello'''
'''Boken code'''

def play_note(note_name, channel_number, note_file):
  pygame.mixer.Channel(channel_number).play(pygame.mixer.Sound(f'{note_file}'))

octave = 4
loop = True

while loop:
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


        
