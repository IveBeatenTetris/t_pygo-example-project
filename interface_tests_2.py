import t_pygo as go
import pygame as pg
# assignments
app	= go.App(
	size		=	(580, 650),
	background	= 	(35, 35, 45),
	resizable	=	True,
	fps			=	120
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

		# updating
		app.update()

if __name__ == '__main__':
    main()
