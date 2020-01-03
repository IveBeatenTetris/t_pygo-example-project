import t_pygo as go
import pygame as pg
# test functions
def call_popup():
	print("popup called.")
def printSomething():
	print("hello world")
def printArg(arg):
	print(arg)
def printKWArg(kwargs):
	"""."""
	for k, v in kwargs.items():
		print(k, v)
def testFunction():
	print("test succeed")
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
menu = go.Menu({
	"name": "right_click",
	#"background": (45, 45, 55),
	"options": [
		{
			"name": "Print something",
			"call": printSomething
		},
		{
			"name": "Print argument",
			"call": printArg,
			"args": "I have been printed."
		}
	]
})
menu.rect.topleft = (400, 360)
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
