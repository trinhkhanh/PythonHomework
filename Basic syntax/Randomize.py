__author__ = 'trinhkhanh'

import random

squad = [['Marc-Andre ter Stegen', 'Claudio Bravo', 'Jordi Masip'],
         ['Douglas',  'Gerard Pique', 'Daniel Alves', 'Marc Bartra, Jordi Alba', 'Adriano', 'Thomas Vermaelen', 'Jeremy Mathieu', 'Martin Montoya'],
         ['Ivan Rakitic', 'Sergio Busquets', 'Andres Iniesta', 'Neymar', 'Rafinha', 'Javier Mascherano', 'Sergi Roberto', 'Denis Suarez'],
         ['Luis Suarez', 'Lionel Messi', 'Sandro', 'Munir', 'Cristian Tello']]

TM = random.sample(squad[0], 1)# TM: chon mot thu mon
HV = random.sample(squad[1], 4) # HV: Hau ve chon 2 tru - 2 bien
TV = random.sample(squad[2], 4) # TV: chon 4 tien ve
TD = random.sample(squad[3], 2) #TD: chon 2 tien dao

print('Doi hinh ra san gom: %s, %s, %s, %s'%(TM, HV, TV, TD))
