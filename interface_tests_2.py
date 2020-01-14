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
		size = (150, 200),
		position = (margin, margin),
		dragable = True
	)
elements["table"] = go.Table(
		rows = 3,
		cols = 2,
		size = (150, 50),
		position = (
			elements["panel"].rect.right + margin,
			elements["panel"].rect.top
		),
		border = True,
		border_color = (180, 180, 190),
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
elements["text_input"] = go.TextField(
		position = (
			elements["text"].rect.right + margin,
			elements["text"].rect.top
		)
	)
elements["info_panel"] = go.Table(
	rows = 2,
	cols = 4,
	size = (app.rect.width, 50),
	border = True,
	background = (50, 50, 60)
)
elements["info_panel"].rect.bottomleft = app.rect.bottomleft
app.draw_list.add(*[e for _, e in elements.items()])
# main loop
def main():
	while True:
		# -------------------------------------------------------------------- #
		#print(app.fps)
		if app.resized:
			elements["info_panel"].rect.size = (app.rect.width, 50)
			elements["info_panel"].rect.bottomleft = app.rect.bottomleft
		# drawing information to panel
		for name, elem in elements.items():
			if elem.hover:
				panel = elements["info_panel"]
				info_text = [
					str(type(elem)),
					str(elem.rect)
				]
				for i in range(len(info_text)):
					text = go.Text(
						text = info_text[i],
						font_size =	13
					)
					panel.draw(panel.background, panel.columns[i])
					panel.draw(text, panel.columns[i])
		# -------------------------------------------------------------------- #
		# events
		if "esc" in app.keys:
			app.quit()
		# drawing

		# updating
		app.update()

if __name__ == '__main__':
    main()
