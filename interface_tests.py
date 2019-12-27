import t_pygo as go
import pygame as pg

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
	#"hover": (35, 35, 45),
	"fontsize": 13,
	"rect": [450, 360, 85, 150],
	"options": [
		{
			"name": "abc",
			#"background": (45, 45, 55),
			#"hover": (35, 35, 45),
			"textposition": (10, 0)
		}
	]
})
popup1 = go.Window({
	"background": (85, 85, 95),
	"rect": [300, 400, 300, 400]
})

def call_popup():
	print("called")
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
