import t_pygo as go
import pygame as pg
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
elements = {}
elements["panel"] = go.Panel(
		background_color = (50, 50, 60),
		#background_hover = (60, 60, 70),
		size = (150, 200),
		position = (margin[1], margin[0]),
		#dragable = True,
		#drag_area = [5, 5, 140, 25],
		#drag_area_background = (70, 70, 80)
	)
elements["table"] = go.Table(
		size = (200, 100),
		position = (
			elements["panel"].rect.right + margin[1],
			elements["panel"].rect.top
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
elements["text"] = go.Text(
		text = "Lorem Ipsum dolor sit amet.",
		position = (
			elements["table"].rect.right + margin[1],
			elements["table"].rect.top
		),
		font_size =	20,
		wrap = 200,
		#background = (0, 10, 20)
	)
elements["button"] = go.Button(
	text =	"New Button",
	position = (
		elements["text"].rect.left,
		elements["text"].rect.bottom + margin[1]
	),
	border = True,
	#background = (40, 45, 35),
	#background_hover = (50, 55, 45),
	padding = [10, 10, 6, 10],
	font_size =	20,
)
elements["text_input"] = go.TextField(
	position = (
		elements["text"].rect.right + margin[1],
		elements["text"].rect.top
	)
)
elements["slot"] = go.Slot(
	size = (40, 32),
	position = (
		elements["text_input"].rect.left,
		elements["text_input"].rect.bottom + margin[1]
	),
	border_color = (15, 15, 25)
)
elements["slider_h"] = go.Slider(
	#size = (200, 50),
	position = (
		elements["text_input"].rect.right + margin[1],
		elements["text_input"].rect.top
	)
)
elements["slider_v"] = go.Slider(
	alignment = "vertical",
	position = (
		elements["slider_h"].rect.left,
		elements["slider_h"].rect.bottom + margin[1]
	)
)
elements["menu"] = go.Menu(
	position = (
		elements["slider_h"].rect.right + margin[1],
		elements["slider_h"].rect.top
	),
	options = [
		("Option 1", print, "Option1 has been clicked.", 1),
		("Option 2", print, "Option2 has been clicked.", 2),
		("Option 3", print, "Option3 has been clicked.", 3),
		("Another Test-Option", print, "Option4 has been clicked.", 4)
	]
)
elements["drop_down"] = go.DropDown(
	position = (
		elements["menu"].rect.left,
		elements["menu"].rect.bottom + margin[1]
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
elements["popup"] = go.Window(
	#border = True,
	position = (
		elements["panel"].rect.left,
		elements["panel"].rect.bottom + margin[1]
	),
)
elements["menu_bar"] = go.MenuBar(
	size = (app.rect.width, 30),
	#border = True,
	options = {
		"File": (
			("New", print, "Button 'New' was clicked"),
			("Open", print, "Button 'Open' was clicked"),
			("Exit", print, "Button 'Exit' was clicked"),
		),
		"Edit": (),
		"View": (),
		"Help": ()
	}
)
elements["info_bar"] = go.InfoBar(
	#text_size = 16
	#text_position = "bottomright"
	#border = True,
	border_color = (80, 80, 90)
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
		if app.resized:
			elements["menu_bar"].resize((app.rect.width, 30))
		# drawing

		# updating
		app.update()

if __name__ == '__main__':
    main()
