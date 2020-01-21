import t_pygo as go
import pygame as pg
# assignments
app	= go.App(
	title =	"Test Project 0.1",
	#size =	(580, 650),
	size = go.getMachineResolution(),
	background_color = (35, 35, 45),
	resizable =	True,
	fps = 60
)

margin = 10
elements = {}
elements["panel"] = go.Panel(
		background = (50, 50, 60),
		size = (150, 200),
		position = (margin, margin),
		dragable = True,
		drag_area = [5, 5, 140, 25],
		drag_area_background = (70, 70, 80)
	)
elements["table"] = go.Table(
		size = (150, 50),
		position = (
			elements["panel"].rect.right + margin,
			elements["panel"].rect.top
		),
		border = True,
		#border_color = (180, 180, 190),
		rows = (
			("Key1", "Value1"),
			("Key2", "Value2"),
			("Key3", "Value3")
		),
		#text_size = 16
	)
elements["button"] = go.Button(
		text =	"New Button",
		position = (
			elements["table"].rect.right + margin,
			elements["table"].rect.top
		),
		border = True,
		#background = (40, 45, 35),
		#background_hover = (50, 55, 45),
		padding = 10,
		font_size =	20,
	)
elements["text"] = go.Text(
		text = "Lorem Ipsum dolor sit amet.",
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
elements["slider"] = go.Slider(
	#size = (200, 50),
	position = (
		elements["text_input"].rect.right + margin,
		elements["text_input"].rect.top
	)
)
elements["slot"] = go.Slot(
	background_color = (20, 20, 30),
	position = (
		elements["slider"].rect.right + margin,
		elements["slider"].rect.top
	)
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
