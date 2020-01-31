import t_pygo as go
import pygame as pg
# functions
def resize_window():
	app.resize((
		el["slider_h"].rect.right + margin[1],
		el["chart"].rect.bottom + margin[0]
	))
	el["menu_bar"].resize((app.rect.width, 30))
	el["info_bar"].resize((app.rect.width, 30))
	el["info_bar"].shift(app.rect.bottomleft, "bottomleft")
# assignments
app	= go.App(
	title =	"UI Demonstration",
	#size =	(580, 650),
	size = go.getMachineResolution(),
	background_color = (35, 35, 45),
	resizable =	True,
	fps = 120
)
margin = (40, 10)
el = {}

el["panel"] = go.Panel(
		#background_color = (50, 50, 60),
		#background_hover = (60, 60, 70),
		size = (150, 200),
		position = (margin[1], margin[0]),
		#dragable = True,
		#drag_area = [5, 5, 140, 25],
		#drag_area_background = (70, 70, 80)
	)
el["table"] = go.Table(
		size = (200, 100),
		position = (
			el["panel"].rect.right + margin[1],
			el["panel"].rect.top
		),
		background_color = (50, 50, 60),
		#border = True,
		#border_color = (180, 180, 190),
		rows = (
			("Key1", "Value1"),
			("Key2", "Value2"),
			("Key3", "Value3"),
			("Mouse Location:", "mouseLoc")
		),
		#text_size = 16
		#text_position = "center"
	)
el["text"] = go.Text(
		text = "Lorem Ipsum dolor sit amet.",
		position = (
			el["table"].rect.right + margin[1],
			el["table"].rect.top
		),
		font_size =	20,
		wrap = 200,
		#background = (0, 10, 20),
		#bold = True
		italic = True
	)
el["button"] = go.Button(
	text =	"New Button",
	position = (
		el["text"].rect.left,
		el["text"].rect.bottom + margin[1]
	),
	#border = True,
	#background_color = (40, 45, 35),
	#background_hover = (50, 55, 45),
	padding = [10, 10, 6, 10],
	font_size =	20,
)
el["text_input"] = go.TextField(
	position = (
		el["text"].rect.right + margin[1],
		el["text"].rect.top
	)
)
"""el["slot"] = go.Slot(
	size = (40, 32),
	position = (
		el["text_input"].rect.left,
		el["text_input"].rect.bottom + margin[1]
	),
	border_color = (15, 15, 25)
)"""
el["slider_h"] = go.Slider(
	#size = (200, 50),
	position = (
		el["text_input"].rect.right + margin[1],
		el["text_input"].rect.top
	)
)
el["slider_v"] = go.Slider(
	alignment = "vertical",
	position = (
		el["slider_h"].rect.left,
		el["slider_h"].rect.bottom + margin[1]
	)
)
el["popup"] = go.Window(
	#border = True,
	position = (
		el["panel"].rect.left,
		el["panel"].rect.bottom + margin[1]
	),
)
el["chart"] = go.Graph(
	size = (300, 120),
	position = (
		el["popup"].rect.left,
		el["popup"].rect.bottom + margin[1]
	),
	text = "FPS"
)
el["menu"] = go.Menu(
	position = (
		el["popup"].rect.right + margin[1],
		el["popup"].rect.top
	),
	options = [
		("Option 1", print, "Option1 has been clicked.", 1),
		("Option 2", print, "Option2 has been clicked.", 2),
		("Option 3", print, "Option3 has been clicked.", 3),
		("Another Test-Option", print, "Option4 has been clicked.", 4)
	]
)
el["drop_down"] = go.DropDown(
	position = (
		el["menu"].rect.left,
		el["menu"].rect.bottom + margin[1]
	),
	options = [
		("Option 1", 1),
		("Option 2", print, "Option2 has been clicked.", 2),
		("Option 3", print, "Option3 has been clicked.", 3),
		("Another Test-Option", print, "Option4 has been clicked.", 4)
	],
	border = True,
	border_color = (15, 15, 25)
)
el["menu_bar"] = go.MenuBar(
	size = (app.rect.width, 30)
)
el["info_bar"] = go.InfoBar(
	size = (app.rect.width, 30),
	position = (
		app.rect.left,
		app.rect.bottom,
		"bottomleft"
	)
)
app.draw_list.add(*[e for _, e in el.items()])
# resizing
resize_window()
# main loop
def main():
	while True:
		# -------------------------------------------------------------------- #
		#print(app.fps)
		el["chart"].inspect = app.fps
		# -------------------------------------------------------------------- #
		# events
		if "esc" in app.keys:
			app.quit()
		if app.resized:
			el["menu_bar"].resize((app.rect.width, 30))
			el["info_bar"].resize((app.rect.width, 30))
			el["info_bar"].shift(app.rect.bottomleft, "bottomleft")
		# drawing

		# updating
		app.update()

if __name__ == '__main__':
    main()
