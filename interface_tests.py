import t_pygo as go
import pygame as pg

# assignments
app = go.Window({
	"title": "interface_tests",
	"resizable": True,
	"size": go.getMachineResolution(),
	"background": (25, 25, 35)
})
gui = go.Interface("app_test1")
mousepos = go.Text({
	"font": "Verdana",
	"fontsize": 14,
	"text": "mouse position",
	"antialias": True,
	"color": (150, 150, 150)
})
# main loop
def main():
	while True:
		# events
		app.events()
		if app.keys()["esc"]:
			app.quit()
		if app.resize():
			gui.resize(app.size)
		# drawing
		for elem in gui.elements:
			if elem.name == "info_bar":
				go.draw(mousepos, gui, (
					elem.rect.left + 5,
					elem.rect.top + 3
				))
		app.draw(gui)
		# updating
		mousepos.update({
			"text": "Cursor: x" + str(go.getMouse()[0]) + " y" + str(go.getMouse()[1])
		})
		gui.update()
		app.update()

if __name__ == '__main__':
    main()
