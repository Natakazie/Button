from pynput import mouse, keyboard
from pynput.mouse import Button
from screeninfo import get_monitors

print("DO NOT TAB IN THE TERMINAL WHILE USING THIS SCRIPT!")
    
screens = get_monitors()
screen = screens[0]
width = screen.width
height = screen.height
running = True
mouse = mouse.Controller()

def on_press(key):
    try:
        if key == keyboard.Key.esc:
            running = False
            print(running)
            return False
        if str(key) == "'x'":
            print(str(key) + " 'x'")
            mouse.position = (width*0.5, height*0.3)
            mouse.click(Button.left)
            mouse.position = (width, height*0.55) 
            print("Mouse press simulated")
            print("mouse moved")
        return True
           
        
    except AttributeError:
        print("error on step " + str(steps))

def on_release(key): 
        
    if key == keyboard.Key.esc:
        return False

# Collect events until released

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)

listener.start()

while running == True:
    continue
exit()
