import t_pygo as go
import pygame as pg
# assignments
app	= go.App(
	title =	"Testing Table-drawing",
	size = go.getMachineResolution(),
	background = (35, 35, 45),
	resizable =	True,
	fps = 120
)

elements = {}
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
