import t_pygo as go
import pygame as pg

# assignments
app = go.Window({
	"title": "window_tests",
	"resizable": True,
	"size": go.getMachineResolution(),
	"backgroundrepeat": "xy"
})
# main loop
def main():
	while True:
		# events
		events = app.events()
		if app.keys()["esc"]:
			app.quit()
		# drawing
		app.draw(gui)
		# updating
		app.update()

if __name__ == '__main__':
    main()
