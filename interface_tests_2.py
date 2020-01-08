import t_pygo as go
import pygame as pg
# assignments
app		=	go.App(
				size		=	(580, 650),
				background	= 	(35, 35, 45),
				resizable	=	True,
				fps			=	120
			)
table	=	go.Table(
				rows			=	5,
				cols			=	2,
				size			=	app.rect.size,
				border			=	True,
				#border_color	=	(25, 80, 50),
				#border_size		=	5,
				background		=	(200, 200, 215),
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
	while True:
		# -------------------------------------------------------------------- #
		#print(app.fps)
		# -------------------------------------------------------------------- #

		# events
		if "esc" in app.keys:
			app.quit()
		if app.resized:
			table.resize(app.rect.size)
		# drawing
		#app.draw(elem, elem.rect)
		app.draw(table, table.rect)
		# updating
		table.update()
		app.update()
		#elem.update()

if __name__ == '__main__':
    main()
