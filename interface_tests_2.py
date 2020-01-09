import t_pygo as go
import pygame as pg
# assignments
app	= go.App(
	title =	"Test Project 0.1",
	#size =	(580, 650),
	size = go.getMachineResolution(),
	background = (35, 35, 45),
	resizable =	True,
	fps = 120
)

margin = 10
elements = {}

elements["table"] = go.Table(
	rows = 3, cols = 2,
	size = (150, 50), position = (margin, margin),
	border = True, border_color = (180, 160, 170),
)
elements["button"] = go.Button(
	text =	"New Button",
	position = (
		elements["table"].rect.right + margin,
		elements["table"].rect.top
	),
	border = True,
	#background = (40, 45, 35),
	background_hover = (50, 55, 45),
	padding = 10,
	font_size =	20,
)
elements["text"] = go.Text(
	text = "Lorem Ipsum dolor set amet.",
	position = (
		elements["button"].rect.right + margin,
		elements["button"].rect.top
	),
	font_size =	20,
	wrap = 200
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
		# drawing
		for _, elem in elements.items():
			app.draw(elem, elem.rect)
		# updating
		for _, elem in elements.items():
			elem.update()
		app.update()

if __name__ == '__main__':
    main()
