import t_pygo as go
import pygame as pg

# assignments
app = go.Window({
	"title": "interface_tests",
	"resizable": True,
	"size": go.getMachineResolution(),
	#"background": (25, 25, 35)
	"backgroundrepeat": "xy",
	"fps": 100
})
gui = go.Interface("app_test1")
fpstxt = go.Text({
	"font": "ebrima",
	"fontsize": 14,
	"text": "frames per second",
	"antialias": True,
	"color": (150, 150, 150)
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

		# drawing on infobar
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
				go.draw(fpstxt, gui, (
					200 + appsize.rect.width,
					elem.rect.top + 2
				))
		app.draw(gui)

		# updating
		fpstxt.update({
			"text": "FPS: {0}".format(app.fps)
		})
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
		gui.update(events)
		app.update()

if __name__ == '__main__':
    main()
