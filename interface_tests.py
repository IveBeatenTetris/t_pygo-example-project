import t_pygo as go
import pygame as pg
# test functions
def call_popup():
	print("this is where to call a new window object.")
def printSomething():
	print("hello world")
def printArg(arg):
	print(arg)
def printKWArg(kwargs):
	"""."""
	for k, v in kwargs.items():
		print(k, v)
# assignments
app = go.App({
	"title": "interface_tests",
	"resizable": True,
	"size": go.getMachineResolution(),
	#"background": (25, 25, 35),
	"backgroundrepeat": "xy",
	"fps": 120
})
gui = go.Interface("app_test3")
menu = go.Menu2({
	"name": "right_click",
	#"background": (45, 45, 55),
	#"fontsize": 13,
	#"rect": [450, 360, 85, 150],
	"options": [
		{
			"name": "Print something",
			"call": printSomething
		},
		{
			"name": "Print argument",
			"call": printArg,
			"args": "I have been printed."
		},
		{
			"name": "Print Keyword Args",
			"call": printKWArg,
			"args": {
				"test_arg": 5.67
			}
		},
	]
})
menu.rect.topleft = (450, 360)
popup1 = go.Window({
	"background": (85, 85, 95),
	"rect": [300, 400, 300, 400]
})
# main loop
def main():
	while True:
		# events
		events = app.events()
		if app.keys()["esc"]:
			app.quit()
		if app.resize():
			gui.resize(app.size)
		# drawing
		gui.draw(menu, menu.rect)
		app.draw(gui, gui.rect)
		# updating
		menu.update()
		gui.update()
		app.update()

if __name__ == '__main__':
    main()
