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
elements["panel"] = go.Panel(
		background = (50, 50, 60),
		size = (app.rect.width, 100),
		position = (0, app.rect.bottom - 100)
	)
elements["table"] = go.Table(
		rows = 3, cols = 2,
		size = (150, 50), position = (margin, margin),
		border = True, border_color = (180, 180, 190),
	)
elements["button"] = go.Button(
		text =	"New Button",
		position = (
			elements["table"].rect.right + margin,
			elements["table"].rect.top
		),
		border = True,
		background = (40, 45, 35),
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
		wrap = 200,
		#background = (0, 10, 20)
	)
elements["text_input"] = go.TextInput(
		position = (
			elements["text"].rect.right + margin,
			elements["text"].rect.top
		)
	)

app.draw_list.add(
	elements["panel"],
	elements["table"],
	elements["button"],
	elements["text"],
	elements["text_input"]
)
# main loop
def main():
	while True:
		# -------------------------------------------------------------------- #
		print(app.fps)
		if app.resized:
			elements["panel"].rect.bottomright = app.rect.bottomright
		# drawing information to panel
		for name, elem in elements.items():
			if elem.hover:
				text = go.Text(
					text = str(elem),
					font_size =	13,
					#wrap = 200,
					#background = (0, 10, 20)
				)
				panel = elements["panel"]
				panel.draw(panel.background, text.rect)
				panel.draw(text)
		# -------------------------------------------------------------------- #
		# events
		if "esc" in app.keys:
			app.quit()
		# drawing

		# updating
		app.update()

if __name__ == '__main__':
    main()
