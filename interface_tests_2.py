import t_pygo as go
import pygame as pg
# assignments
app	= go.App(
	size		=	(580, 650),
	background	= 	(35, 35, 45),
	resizable	=	True,
	fps			=	120
)
text = go.Text(
	text		=	"In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since. 'Whenever you feel like criticizing anyone,' he told me, 'just remember that all the people in this world haven't had the advantages that you've had.'",
	#background	=	(20, 25, 50),
	font_size	=	20,
	wrap		=	500
)
text.rect.center = app.rect.center
# main loop
def main():
	while True:
		# -------------------------------------------------------------------- #
		print(app.fps)
		# -------------------------------------------------------------------- #
		# events
		if "esc" in app.keys:
			app.quit()
		if app.resized:
			text.rect.center = app.rect.center
		# drawing
		app.draw(text, text.rect)
		# updating
		app.update()

if __name__ == '__main__':
    main()
