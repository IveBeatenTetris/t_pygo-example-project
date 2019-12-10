import t_pygo as go
import pygame as pg

# assignments
app = go.App({
	"title": "interface_tests",
	"resizable": True,
	"size": go.getMachineResolution(),
	#"background": (25, 25, 35)
	"backgroundrepeat": "xy",
	"fps": 100
})
gui = go.Interface("app_test1")

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
		app.draw(gui)
		# updating
		gui.elements["info_bar"].info = {
			"Mouse": go.getMouse(),
			"AppSize": app.size,
			"FPS": app.fps
		}
		gui.update(events)
		app.update()

if __name__ == '__main__':
    main()
