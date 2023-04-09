import time
import board
import digitalio
import neopixel

led = digitalio.DigitalInOut(board.D13)
led.switch_to_output()

button1 = digitalio.DigitalInOut(board.BUTTON_A)
button1.switch_to_input(pull=digitalio.Pull.DOWN)

button2 = digitalio.DigitalInOut(board.BUTTON_B)
button2.switch_to_input(pull=digitalio.Pull.DOWN)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.2, auto_write=False)

number_of_pixels = 10

state = 0

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)


        
def color(color):
    for i in range(number_of_pixels):
        pixels[i] = color 
        pixels.show()
    print(color)
        


    

while True:
    print(str(state))
    if button1.value:  # button is pushed
        if state == 0:
            color(RED)
            #time in seconds 
            time.sleep(180)
            color(YELLOW)
            time.sleep(150)
            color(GREEN)
            state = 1
            print("state = " + str(state))
        elif state == 1:
            color(OFF)
            state = 0
            time.sleep(2)
    if button2.value:
        if state == 0:
            color(RED)
            #time in seconds 
            time.sleep(180)
            color(YELLOW)
            time.sleep(150)
            color(GREEN)
            state = 1
            print("state = " + str(state))
        elif state == 1:
            color(OFF)
            state = 0
            #if you dont' have some pause the button is read as both triggering OFF and restarting things
            time.sleep(2)
    else:
        pass

    time.sleep(0.05)

