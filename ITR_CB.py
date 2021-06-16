import pyautogui as p
import time as t 
import keyboard 
from pynput.keyboard import Key, Controller

kb = Controller()

def copy():
  p.keyDown('ctrl')
  p.press('c')
  p.keyUp('ctrl')

def paste():
  p.hotkey('ctrl','v')

def enter_press():
  p.press('enter')

def press_tab():
  p.press('tab')

def press_command():
  p.keyDown('alt')
  p.press('tab')
  p.press('tab')
  p.keyUp('alt')

def press_command_once():
  p.keyDown('alt')
  t.sleep(1)
  p.press('tab')
  p.keyUp('alt')

def selectAll_and_delete():
  p.hotkey('ctrl','a')
  p.press('backspace')

def right_key():
  p.press('right')

def down_key():
  p.press('down')

def shift_tab():
  p.hotkey('shift','tab')

def loop_tab():
  i = 0
  while i < 11:
    p.press('tab')
    t.sleep(2)
    i = i + 1

def loopy():
    i = 0
    while i < 8:
        p.press('tab')
        t.sleep(2)
        i = i + 1

def loopy_end():
    i = 0
    while i < 9:
        p.press('tab')
        t.sleep(2)
        i = i + 1


def main():
    t.sleep(10)
    i = 0
    while i < 200:
       copy()
       t.sleep(2)
       press_command_once()
       t.sleep(1)
       paste()
       t.sleep(1)
       press_tab()
       t.sleep(1)
       enter_press()
       t.sleep(1)
       loop_tab()
       t.sleep(1)
       enter_press()
       t.sleep(1)
       press_tab()
       t.sleep(1)
       press_tab()
       t.sleep(1)
       selectAll_and_delete()
       t.sleep(1)
       press_command_once()
       t.sleep(1)
       kb.press(Key.left)
       copy()
       t.sleep(1)
       press_command_once()
       t.sleep(1)
       paste()
       t.sleep(1)
       loopy()
       t.sleep(1)
       enter_press()
       t.sleep(1)
       loopy_end()
       t.sleep(1)
       press_command_once()
       t.sleep(1)
       kb.press(Key.right)
       t.sleep(1)
       kb.press(Key.right)
       t.sleep(1)
       kb.type('done')
       down_key()
       kb.press(Key.left)
       i = i + 1


if __name__ == '__main__':
    main()
