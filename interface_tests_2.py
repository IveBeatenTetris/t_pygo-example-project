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
layout = go.Layout(
	size		=	app.rect.size,
	rows		=	[
						{
							"size"	: (100, 50),
							"cols"	:	[
								{
									"content": None
								}
							]
						}
					]
)
elem = go.GuiMaster(
	parent		=	app,
	#position = app.rect.center,
	background = (35, 35, 45),
	#background_hover = (55, 55, 65),
	dragable	=	True,
	drag_area	=	[5, 5, 290, 25],
	resizable	=	"buttomleft"
)
# main loop
def main():
	redraw_layout = True
	while True:
		# -------------------------------------------------------------------- #
		print(app.fps)
		# -------------------------------------------------------------------- #
		# updating
		layout.update()
		app.update()
		# events
		if "esc" in app.keys:
			app.quit()
		if app.resized:
			layout.resize(app.rect.size)
			redraw_layout = True
		# updating elements
		#elem.update()
		# drawing
		if redraw_layout:
			app.draw(layout, layout.rect)
			redraw_layout = False
		#app.draw(elem, elem.rect)

if __name__ == '__main__':
    main()
