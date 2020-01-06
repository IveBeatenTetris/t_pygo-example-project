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
elem = go.GuiMaster(
	parent = app,
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
			elem.rect.center = app.rect.center
		# updating elements
		elem.update()
		# drawing
		app.draw(elem, elem.rect)
		# updating
		app.update()

if __name__ == '__main__':
    main()
