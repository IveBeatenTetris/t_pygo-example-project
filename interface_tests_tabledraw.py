import t_pygo as go
import pygame as pg
# assignments
app	= go.App(
	title =	"Testing Table-drawing",
	#size = go.getMachineResolution(),
	#size = (600, 400),
	size = (600, 400),
	background = (35, 35, 45),
	resizable =	True,
	fps = 120
)
elements = {}
elements["text_test"] = go.Text(text="my new text")
elements["panel_drag"] = go.Panel(
	size = (200, 300),
	background = (50, 50, 60),
	dragable = True,
	drag_area = [5, 5, 190, 25],
	drag_area_background = (70, 70, 80)
)
elements["panel_drag"].rect.center = app.rect.center
elements["table_info"] = go.Table(
	background = (15, 15, 20),
	border = True,
	border_color = (200, 200, 210),
	size = (app.rect.width, 150),
	rows = (
		#("Object", elements["text_test"]),
		("Type", str(type(elements["text_test"]))),
		("Rect", str(elements["text_test"].rect)),
		("Test", "Test")
	)
)
elements["table_info"].rect.bottomleft = app.rect.bottomleft
app.draw_list.add(*[e for _, e in elements.items()])
# main loop
def main():
	while True:
		# -------------------------------------------------------------------- #
		if app.resized:
			elements["table_info"].resize((app.rect.width, 150))
			elements["table_info"].rect.bottomleft = app.rect.bottomleft
		# -------------------------------------------------------------------- #
		# events
		if "esc" in app.keys:
			app.quit()
		# drawing
		# updating
		app.update()
if __name__ == '__main__':
    main()
