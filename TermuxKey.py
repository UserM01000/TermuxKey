#!/usr/bin env python3
from threading import Thread
import subprocess

# colores
yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
white='\033[97m'

logo = red+"""

 _____                              _  __          
|_   _|__ _ __ _ __ ___  _   ___  _| |/ /___ _   _ 
  | |/ _ \ '__| '_ ` _ \| | | \ \/ / ' // _ \ | | |
  | |  __/ |  | | | | | | |_| |>  <| . \  __/ |_| |
  |_|\___|_|  |_| |_| |_|\__,_/_/\_\_|\_\___|\__, |
     Developer ---> https://t.me/HackForAll1 |___/ 
"""

def banner():
  subprocess.run(['clear'])
  print(logo)

def init():

  try:
    subprocess.run(['mkdir','-p','.termux'])
  except:
    pass
  keys = '''extra-keys = [ \\
    ['ESC', 'CTRL', 'ALT', '-', {key: KEYBOARD, popup: DRAWER}, 'HOME', 'UP', 'END', '""'], \\
    ['TAB', '()', '[]', '{}', 'BACKSLASH', 'LEFT', 'DOWN', 'RIGHT', '/'] \\
]'''
  
  open('/data/data/com.termux/files/home/.termux/termux.properties','w').write(keys)
  subprocess.run(['termux-reload-settings'])

if __name__ == '__main__':

  banner()
  thread = Thread(target=init)
  thread.start()
  print(white+"Agregando teclas Extras...")
  subprocess.run(['sleep', '4'])
  banner()
  print(white+"Teclas agregadas correctamente :D")
  print(white+"Errores? ----> https://t.me/HackForAll1")
  subprocess.run(['rm','-rf','TermuxKey.py'])
