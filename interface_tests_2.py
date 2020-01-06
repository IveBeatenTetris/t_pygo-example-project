import t_pygo as go
import pygame as pg
# assignments
app = go.App(
	size = (580, 650),
	#background = (35, 35, 45),
	resizable = True,
	fps = 60
)
#gui = go.Interface("app_test4")
gui = go.GuiMaster(
	position = app.rect.center,
	background_hover = (55, 55, 65),
	dragable = True
)
# main loop
def main():
	while True:
		# events
		if "esc" in app.keys:
			app.quit()
		if app.resize():
			gui.rect.center = app.rect.center
		# drawing
		app.draw(gui, gui.rect)
		# updating
		gui.update()
		app.update()

if __name__ == '__main__':
    main()
