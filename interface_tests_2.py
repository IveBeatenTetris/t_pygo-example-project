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
				rows		=	3,
				cols		=	3
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
"""layout = go.Layout2(
	size		=	app.rect.size,
	rows		=	[
						{
							#"size"	: (100, 50),
							"border":	(1, app.background),
							"cols"	:	[
								{
									"border":	(1, app.background),
									"content"	:	None
								}
							]
						},
						{
							"border":	(1, app.background),
							"cols"	:	[
								{"content"	:	None}
							]
						},
						{
							"border":	(1, app.background),
							"cols"	:	[
								{"content"	:	None}
							]
						}
					]
				)"""
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
		app.draw(table, table.rect)
		#app.draw(elem, elem.rect)
		# updating
		app.update()
		table.update()
		#elem.update()

if __name__ == '__main__':
    main()
