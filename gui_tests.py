import t_pygo as go
import pygame as pg

app = go.Window({
	"title": "gui_tests",
	"fps": 70
})
map = go.Map("test_map")
player = go.Player("hero")
camera = go.Camera({
	"size": (320*2, 240*2),
	"tracking": player,
	"zoom": 2
})
text = go.Text({
	"font": "Verdana",
	"size": 20,
	"text": "fps",
	"color": (255, 255, 255)
})
controller = app.controller

# gui stuff
pause_background = go.Overlay({
	"background": (0, 0, 0),
	"size": camera.size,
	"opacity": 200
})
pause_button_continue = go.Button({
	"size": (160, 50),
	"background": (75, 75, 75),
	"hoverbackground": (100, 100, 100),
	"textcolor": (200, 200, 200),
	"text": "Continue",
	"fontsize": 22,
	"bold": True,
	"position": (camera.anchors["middle"], 160)
})
pause_button_exit = go.Button({
	"size": (160, 50),
	"background": (75, 75, 75),
	"hoverbackground": (100, 100, 100),
	"textcolor": (200, 200, 200),
	"text": "Exit Game",
	"fontsize": 22,
	"bold": True,
	"position": (camera.anchors["middle"], 240)
})

def setup():
	"""pre-setup for the game before entering the main-loop."""
	app.resize(camera.size)
	player.knownblocks = map.blocks
	if map.playerstart:
	    player.position(map.playerstart)

def handlingInput():
	"""handles keyboard and controller input."""
	events = app.events()
	keys = app.pressedKeys()
	# ESCAPE KEY
	if app.keys()["esc"]:
		app.pause()
	# PAUSE MENU
	if app.paused:
		if pause_button_continue.leftClick(events):
			app.pause()
		elif pause_button_exit.leftClick(events):
			app.quit()
	# START / STOP
	if controller.buttons["select"]:
		app.quit()
	if controller.buttons["start"]:
		app.pause()
		controller.stop("start")
	# MOVING PLAYER
	if not app.paused:
		if keys[pg.K_w] or controller.sticks[0]["up"]:
			player.move((0, -player.speed))
		elif keys[pg.K_s] or controller.sticks[0]["down"]:
			player.move((0, player.speed))
		if keys[pg.K_a] or controller.sticks[0]["left"]:
			player.move((-player.speed, 0))
		elif keys[pg.K_d] or controller.sticks[0]["right"]:
			player.move((player.speed, 0))
def drawing():
	"""keeping the main loop clean."""
	screen = pg.Surface(camera.size, pg.SRCALPHA)
	go.draw((90, 86, 99), screen)
	go.draw(map.preview, screen, camera)
	go.draw(player, screen, "center")
	if camera.zoomfactor > 1:
		screen = go.scale(screen, camera.zoomfactor)
	app.draw(screen, "center")
	# drawing gui when paused
	if app.paused:
		# drawing this first to create illusion of frozen game
		app.draw(app.screenshot)
		# then darken the screen
		app.draw(pause_background)
		app.draw(pause_button_continue, pause_button_continue.rect)
		app.draw(pause_button_exit, pause_button_exit.rect)
	app.draw(text)
def updating():
	"""keeping the main loop clean."""
	text.update({
		"text": "quacks: {0}".format(app.fps)
	})
	camera.update()
	player.update()
	app.update()

def main():
	"""main loop."""
	while True:
		handlingInput()
		drawing()
		updating()

if __name__ == '__main__':
    setup()
    main()
