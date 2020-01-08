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
				#size			=	app.rect.size,
				border			=	True,
				border_color	=	(150, 150, 175),
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
	#resizable	=	"buttomleft"
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
		# drawing
		#app.draw(elem, elem.rect)
		app.draw(table, table.rect)
		for each in table.columns:
			app.display.fill(
				(10, 20, 250),
				[
					each.left + 5,
					each.top + 5,
					25,
					25
				]
			)
		# updating
		table.update()
		app.update()
		#elem.update()

if __name__ == '__main__':
    main()
