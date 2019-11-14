# dependencies
import t_pygo as go
import pygame as pg

# assignments
app = go.Window({
	"title": "merely something 0.1",
	"zoom": 1,
	"fps": 70
})
map = go.Map("test_map")
player = go.Player("hero")
camera = go.Camera({
	"size": (640, 480),
	"tracking": player
})
text = go.Text({
	"font": "Verdana",
	"size": 20,
	"text": "fps",
	"color": (255, 255, 255)
})

# gui
pause_background = go.Overlay({
	"background": (0, 0, 0),
	"size": camera.rect.size,
	"opacity": 200
})
pause_button_continue = go.Button({
	"size": (160, 50),
	"background": (75, 75, 75),
	"textcolor": (200, 200, 200),
	"text": "Continue",
	"fontsize": 22,
	"bold": True,
	"position": (camera.anchors["middle"], 160)
})
pause_button_exit = go.Button({
	"size": (160, 50),
	"background": (75, 75, 75),
	"textcolor": (200, 200, 200),
	"text": "Exit Game",
	"fontsize": 22,
	"bold": True,
	"position": (camera.anchors["middle"], 240)
})

# functions
def setup():
	"""pre-setup for the game before entering the main-loop."""
	# resizing app relative to camera size
	app.resize(camera.rect.size)
	# player has to know the active maps blocking elements
	player.knownblocks = map.blocks
	# placing player on the map
	if map.playerstart:
	    player.position(map.playerstart)
def drawing():
	"""keeping the main loop clean."""
	# drawing everything to the camera
	camera.draw((0, 0, 0))
	camera.draw(map.preview, camera.rect)
	camera.draw(player, "center")
	camera.draw(
		go.drawBorder(camera, camera.rect, (3, 'solid', (255, 0, 0)))
	)
	camera.draw(text)
	# finally drawing camera to app
	app.draw(camera)
	# drawing gui when paused
	if app.paused:
		app.draw(pause_background)
		app.draw(pause_button_continue, pause_button_continue.rect)
		app.draw(pause_button_exit, pause_button_exit.rect)
def eventChecking():
	"""keeping the main loop clean."""
	events = app.events()
	# ESCAPE KEY
	if app.keys()["esc"]:
		app.pause()
	# MOUSE WHEEL
	if app.mouseWheel() == "up":
		print("mouse wheel up")
	elif app.mouseWheel() == "down":
		print("mouse wheel down")
	# PAUSE MENU
	if app.paused:
		if pause_button_continue.leftClick(events):
			app.pause()
		elif pause_button_exit.leftClick(events):
			app.quit()
	# GAME PAD
	if app.controller:
		c = app.controller
		# left stick
		if c.sticks[0]["down"]:
			print("left stick down")
		elif c.sticks[0]["up"]:
			print("left stick up")
		if c.sticks[0]["left"]:
			print("left stick left")
		elif c.sticks[0]["right"]:
			print("left stick right")
		# right stick
		if c.sticks[1]["down"]:
			print("right stick down")
		elif c.sticks[1]["up"]:
			print("right stick up")
		if c.sticks[1]["left"]:
			print("right stick left")
		elif c.sticks[1]["right"]:
			print("right stick right")
		# buttons
		if c.buttons["select"]:
			app.quit()
		if c.buttons["start"]:
			c.stop("start")
			app.pause()
		if c.buttons["lb"]:
			print("button 'lb' pressed")
		if c.buttons["lt"]:
			print("button 'lt' pressed")
		if c.buttons["rb"]:
			print("button 'rb' pressed")
		if c.buttons["rt"]:
			print("button 'rt' pressed")
		if c.buttons["l3"]:
			print("left stick click")
		if c.buttons["r3"]:
			print("right stick click")
		if c.buttons["a"]:
			print("button 'a' pressed")
		if c.buttons["b"]:
			print("button 'b' pressed")
		if c.buttons["x"]:
			print("button 'x' pressed")
		if c.buttons["y"]:
			print("button 'y' pressed")
		if c.buttons["dup"]:
			print("button 'up' pressed")
		elif c.buttons["ddown"]:
			print("button 'down' pressed")
		if c.buttons["dleft"]:
			print("button 'left' pressed")
		elif c.buttons["dright"]:
			print("button 'right' pressed")
def updating():
	"""keeping the main loop clean."""
	# frames per second
	text.update({
		"text": "quacks: {0}".format(app.fps)
	})
	# camera recalculatings
	camera.update()
	# pygames display and event updates
	app.update()
def main():
	"""main loop."""
	while True:
		# --------------------------- events ---------------------------- #
		eventChecking()
		# ------------------------ game routines ------------------------ #
		# try to move the player
		if not app.paused:
			player.move()
		# --------------------------- drawing --------------------------- #
		drawing()
		# -------------------------- updating --------------------------- #
		updating()

# begin game-routines
if __name__ == '__main__':
    setup()
    main()
