import t_pygo as go
import pygame as pg

# assignments
app = go.Window({
	"title": "interface_tests",
	"resizable": True,
	"size": go.getMachineResolution(),
	#"background": (25, 25, 35)
	"backgroundrepeat": "xy"
})
gui = go.Interface("app_test1")
menu_file = go.DropDownMenu({
	"rect": pg.Rect(400, 400, 150, 200),
	"background": (55, 55, 65)
})
mousepos = go.Text({
	"font": "ebrima",
	"fontsize": 14,
	"text": "mouse position",
	"antialias": True,
	"color": (150, 150, 150)
})
appsize = go.Text({
	"font": "ebrima",
	"fontsize": 14,
	"text": "window size",
	"antialias": True,
	"color": (150, 150, 150)
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
		for elem in gui.elements:
			if elem.name == "menu_main":
				for e in elem.elements:
					if e.leftClick(events):
						print("click")
		# drawing
		for elem in gui.elements:
			if elem.name == "info_bar":
				go.draw(mousepos, gui, (
					elem.rect.left + 5,
					elem.rect.top + 2
				))
				go.draw(appsize, gui, (
					160,
					elem.rect.top + 2
				))
		go.draw(menu_file, gui, menu_file.rect)
		app.draw(gui)
		# updating
		mousepos.update({
			"text":
				"Cursor: x" +
				str(go.getMouse()[0]) +
				" y" +
				str(go.getMouse()[1])
		})
		appsize.update({
			"text":
				"App: w" +
				str(app.size[0]) +
				" h" +
				str(app.size[1])
		})
		gui.update()
		app.update()

if __name__ == '__main__':
    main()
