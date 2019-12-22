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
		app.draw(gui, gui.rect)
		# updating
		gui.update()
		app.update()

if __name__ == '__main__':
    main()
