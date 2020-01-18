import t_pygo as go
import pygame as pg
# assignments
app	= go.App(
	title =	"Test Project 0.1",
	resizable =	True,
	fps = 120,
	size = go.getMachineResolution(),
	background_color = (35, 35, 45)
)

margin = 10
elements = {}
elements["panel"] = go.Panel(
	background_color = (50, 55, 10),
	size = (175, 200),
	position = (margin, margin),
	dragable = True,
	drag_area = [5, 5, 165, 25],
	drag_area_background = (10, 10, 20)
)
app.draw_list.add(*[e for _, e in elements.items()])
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
