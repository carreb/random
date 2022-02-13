from lifxlan import *
from random import randint, betavariate
from time import sleep
import keyboard

blue = (43072, 65535, 65535, 3500)
def main():
    running = True
    lan = LifxLAN()
    light = lan.get_lights()[0]
    tilechain_lights = lan.get_tilechain_lights()
    if len(tilechain_lights) != 0:
        t = lan.get_tilechain_lights()[0] #grab the first tilechain
        print("Selected TileChain light: {}".format(t.get_label()))
        original_colors = t.get_tilechain_colors()
        (cols, rows) = t.get_canvas_dimensions()
        hue = 0
        rainbow_colors = []
        for row in range(rows):
            color_row = []
            for col in range(cols):
                color_row.append((hue, 65535, 65535, 4500))
                hue += int(65535.0/(cols*rows))
            rainbow_colors.append(color_row)

        t.project_matrix(rainbow_colors)

        duration_ms = 100

        try:
            while running == True:
                rainbow_colors = cycle_row(rainbow_colors)
                t.project_matrix(rainbow_colors, duration_ms, rapid=True)
                sleep(max(duration_ms/2000.0, 0.05))
                if keyboard.is_pressed('q'):
                    running = False
                    light.set_color(blue, duration=150)
                    sleep(0.1)
                    running = True
                if keyboard.is_pressed('w'):
                    running = False
                    light.set_color(blue, duration=150)
                    keyboard.wait('e')
                    running = True
                if keyboard.is_pressed('r'):
                    running = False
                    light.set_color(blue, duration=3000)
                    keyboard.wait('e')
                    running = True
        except KeyboardInterrupt:
            t.set_tilechain_colors(original_colors)
            print("Done.")
        while running == True:
            if keyboard.is_pressed('q'):
              t.set_tilechain_colors(original_colors)
              print("Done.")
    else:
        print("No TileChain lights found.")

def cycle_row(matrix):
    new_matrix = [matrix[-1]]
    for row in matrix[:-1]:
        new_matrix.append(row)
    return new_matrix

def bluetest():
    while True:
        if keyboard.is_pressed('q'):
            global running
            running = False
            light.set_color(blue, duration=300)
            sleep(0.3)
            light.set_color(returnclr, duration=300)


if __name__=="__main__":
    main()