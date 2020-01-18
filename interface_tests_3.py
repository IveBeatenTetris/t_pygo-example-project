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
elements["table"] = go.Table(
		size = (150, 50),
		position = (
			elements["panel"].rect.right + margin,
			elements["panel"].rect.top
		),
		border = True,
		border_color = (180, 180, 190),
		rows = (
			("Key1", "Value1"),
			("Key2", "Value2"),
			("Key3", "Value3")
		)
	)
elements["text"] = go.Text(
		text = "Lorem Ipsum dolor sit amet.",
		position = (
			elements["table"].rect.right + margin,
			elements["table"].rect.top
		),
		font_size =	20,
		wrap = 200,
		#background_color = (0, 10, 20),
		#background_hover = (20, 30, 40),
	)
elements["button"] = go.Button(
		#text =	"New Button",
		position = (
			elements["text"].rect.right + margin,
			elements["text"].rect.top
		),
		#border = True,
		background_color = (0, 100, 120),
		background_hover = (120, 120, 140),
		padding = 10,
		font_size =	20,
	)
app.draw_list.add(*[e for _, e in elements.items()])
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

		# updating
		app.update()

if __name__ == '__main__':
    main()
