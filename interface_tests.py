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
gui = go.Interface2("app_test2")

# main loop
def main():
	while True:
		# events
		events = app.events()
		if app.keys()["esc"]:
			app.quit()
		if app.resize():
			gui.resize(app.size)
		#menu1 = gui.menus["menu_main_file"]
		#print(menu1.active)
		#print(menu1.config)
		print(gui.leftClick())
		# drawing
		app.draw(gui)
		# updating
		"""gui.elements["info_bar"].info = {
			"Mouse": go.getMouse(),
			"AppSize": app.size,
			"FPS": app.fps
		}"""
		#gui.update(events)
		app.update()

if __name__ == '__main__':
    main()
