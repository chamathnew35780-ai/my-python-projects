import keyboard

print("press arrow keys (up, down, left, right) to see their actions. Press 'esc' to exit.")

while True:
    if keyboard.is_pressed('up'):
        print(f"\rCommand : Move Up          ", end="")
        while keyboard.is_pressed('up'):
            pass  
    elif keyboard.is_pressed('down'):
        print(f"\rCommand : Move Down          ", end="")

        while keyboard.is_pressed('down'):
            pass
    elif keyboard.is_pressed('left'):
        print(f"\rCommand : Move Left          ", end="")
        while keyboard.is_pressed('left'):
            pass
    elif keyboard.is_pressed('right'):
        print(f"\rCommand : Move Right         ", end="")
        while keyboard.is_pressed('right'):
            pass
    elif keyboard.is_pressed('esc'):
        print("Exiting...")
        break
