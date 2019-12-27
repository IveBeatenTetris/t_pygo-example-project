import t_pygo as go
import pygame as pg
# overal functions
def call_popup():
	gui.draw(popup1, popup1.rect)
def helloWorld2():
	print("called")
def helloWorld():
	print("hello world")
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
	"background": (45, 45, 55),
	"fontsize": 13,
	"rect": [450, 360, 85, 150],
	"options": [
		{
			"name": "abc",
			"call": helloWorld
		},
		{
			"name": "test_func",
			"call": helloWorld2
		},
	]
})
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
		# drawing menus
		for e in events:
			if e.type is pg.MOUSEBUTTONDOWN:
				if e.button == 3:
					gui.blit(gui.static, menu.rect.topleft, menu.rect)
					menu.rect.topleft = app.mouse.pos
					menu.visible = True
				elif menu.visible:
					gui.blit(gui.static, menu.rect.topleft, menu.rect)
					menu.visible = False
			if menu.visible:
				gui.draw(menu, menu.rect)

		app.draw(gui, gui.rect)
		# updating
		menu.update()
		gui.update()
		app.update()

if __name__ == '__main__':
    main()
