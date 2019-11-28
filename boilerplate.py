# dependencies
import t_pygo as go
import pygame as pg
# assignments
app = go.Window()
# main loop
def main():
	while True:
		# events
		events = app.events()
		# updating
		app.update()

if __name__ == '__main__':
    main()
