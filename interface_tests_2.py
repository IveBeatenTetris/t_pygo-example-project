import t_pygo as go
import pygame as pg
# assignments
app = go.App(
	size		=	(580, 650),
	#background = (35, 35, 45),
	resizable	=	True,
	fps			=	120
)
#gui = go.Interface("app_test4")
elem = go.GuiMaster(
	parent		=	app,
	#position = app.rect.center,
	#background_hover = (55, 55, 65),
	dragable	=	True,
	drag_area	=	[5, 5, 290, 25],
	resizable	=	"buttomleft"
)
layout = go.Layout(
	size		=	app.rect.size,
	background	=	(200, 200, 215)
)
# main loop
def main():
	while True:
		# -------------------------------------------------------------------- #
		print(app.fps)
		# -------------------------------------------------------------------- #
		# events
		if "esc" in app.keys:
			app.quit()
		if app.resize():
			layout.resize(app.rect.size)
		# updating elements
		elem.update()
		# drawing
		#app.draw(elem, elem.rect)
		app.draw(layout, layout.rect)
		# updating
		layout.update()
		app.update()

if __name__ == '__main__':
    main()
