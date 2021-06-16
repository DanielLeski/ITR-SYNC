"""
This is the script for the new chromebooks
"""

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

"""
Start your cursor on the ITR label
"""
def main():
    t.sleep(10)
    i = 0
    while i < 600:
        #waiting for ITR add item to load
        copy()
        t.sleep(1)
        #switch over to the ITR screen
        press_command_once()
        t.sleep(1)
        if i == 0:
            press_tab() 
        t.sleep(1)
        #select everything thats in the field
        selectAll_and_delete()
        t.sleep(1)
        #paste
        paste()
        t.sleep(1)
        #press tab
        press_tab()
        t.sleep(1)
        #switch over to the Excel screen
        press_command_once()
        t.sleep(1)
        #move to the Serial tab
        kb.press(Key.right)
        t.sleep(1)
        #copy the serial tab
        copy()
        t.sleep(1)
        #switch over to the ITR screen
        press_command_once()
        t.sleep(1)
        #paste the Serial number into the Serial field
        paste()
        t.sleep(1)
        #press tab to go to the location
        press_tab()
        t.sleep(1)
        #go back to the Excel screen
        press_command_once()
        t.sleep(1)
        #go to the Student ID
        kb.press(Key.left)
        t.sleep(1)
        kb.press(Key.left)
        t.sleep(1)
        #copy the student ID for the location
        copy()
        t.sleep(1)
        #go to the next ITR Field
        kb.press(Key.right)
        t.sleep(1)
        kb.press(Key.down)
        t.sleep(1)
        #go back to the ITR screen
        press_command_once()
        t.sleep(1)
        #paste the Student ID in the location Field 
        paste()
        t.sleep(1)
        #skip over the Status 
        press_tab()
        t.sleep(1)
        press_tab()
        t.sleep(1)
        #select "Use case" 
        if i == 0:
            enter_press()
            t.sleep(1)
            #scroll down to the "Intructional Classroom" option
            kb.press(Key.down)
            t.sleep(1)
            kb.press(Key.down)
            t.sleep(1)
            kb.press(Key.down)
            t.sleep(1)
            enter_press()
        t.sleep(1)
        # tabs to get to the add item
        press_tab()
        t.sleep(1)
        press_tab()
        t.sleep(1)
        press_tab()
        t.sleep(1)
        press_tab()
        t.sleep(1)
        press_tab()
        t.sleep(1)
        enter_press()
        t.sleep(1)
        press_command_once()
        i = i + 1

if __name__ == '__main__':	
    main()
