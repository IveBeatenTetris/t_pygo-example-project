import t_pygo as go
import pygame as pg
# assignments
app	= go.App(
	title =	"Test Project 0.1",
	#size =	(580, 650),
	size = go.getMachineResolution(),
	background = (35, 35, 45),
	resizable =	True,
	fps = 120
)

margin = 10
elements = {}
elements["guimaster"] = go.GuiMaster(

)
app.draw_list.add(*[e for _, e in elements.items()])
# main loop
def main():
	while True:
		# -------------------------------------------------------------------- #
		#print(app.fps)
		# -------------------------------------------------------------------- #
		# events
		if "esc" in app.keys:
			app.quit()
		# drawing

		# updating
		app.update()

if __name__ == '__main__':
    main()
