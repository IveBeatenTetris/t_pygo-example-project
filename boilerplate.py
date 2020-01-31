# dependencies
import t_pygo as go
import pygame as pg
# assignments
app = go.App()
elements = {}
app.queue(elements)
# main loop
def main():
    while True:
        # events
        if "esc" in app.keys:
            app.quit()
        # updating
        app.update()

if __name__ == '__main__':
    main()
