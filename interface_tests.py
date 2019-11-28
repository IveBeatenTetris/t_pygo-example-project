# dependencies
import t_pygo as go
import pygame as pg

# class assignments
app = go.Window({
	"title": "item_tests",
	"fps": 70,
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
moneycount = go.Text({
	"font": "Verdana",
	"size": 14,
	"text": "moneycount",
	"color": (255, 255, 255),
	"bold": True
})
interface = go.Interface("testinterface1", size=camera.size)

# session assignments
money = 10000

# functions
def setup():
	"""pre-setup for the game before entering the main-loop."""
	# resizing app relative to camera size
	app.resize(camera.size)
	# player has to know the active maps blocking elements
	player.knownblocks = map.blocks
	# placing player on the map
	if map.playerstart:
	    player.position(map.playerstart)
def handlingInput():
	"""handles keyboard and controller input."""
	events = app.events()
	keys = app.pressedKeys()
	# EXIT GAME
	if app.keys()["esc"]:
		app.quit()
	# MOVING PLAYER
	if keys[pg.K_w]:
		player.move((0, -player.speed))
	elif keys[pg.K_s]:
		player.move((0, player.speed))
	if keys[pg.K_a]:
		player.move((-player.speed, 0))
	elif keys[pg.K_d]:
		player.move((player.speed, 0))
	# LEFT SHIFT
	for event in events:
		# makes the player move faster
		if event.type is pg.KEYDOWN and event.key == pg.K_LSHIFT:
			player.setAnimationSpeed(20)
			player.speed = player.config["speed"] * 1.6
		# makes the player move slow again
		elif event.type is pg.KEYUP and event.key == pg.K_LSHIFT:
			player.setAnimationSpeed(30)
			player.speed = player.config["speed"]
def drawing():
	"""keeping the main loop clean."""
	# drawing everything to a temporary surface
	screen = pg.Surface(camera.size, pg.SRCALPHA)
	# black background
	go.draw((90, 86, 99), screen)
	# layers of the map
	go.draw(map.preview, screen, camera)
	# player
	go.draw(player, screen, "center")
	# scaling display if zoomed
	if camera.zoomfactor > 1:
		screen = go.scale(screen, camera.zoomfactor)
	# finally drawing screen to app
	app.draw(screen, "center")
	# drawing money panel to interface
	interface.panels["money"].draw(moneycount, (32, -3))
	# drawing gui to window
	app.draw(interface)
	# text directly drawn to window
	app.draw(text, (0, camera.height - text.rect.height))
def updating():
	"""keeping the main loop clean."""
	# frames per second
	text.update({
		"text": "quacks: {0}".format(app.fps)
	})
	# money count
	moneycount.update({
		"text": money
	})
	# rebuilding interface with updated information
	interface.update()
	# camera recalculatings
	camera.update()
	# animations and idle images
	player.update()
	# pygames display and event updates
	app.update()
def main():
	"""main loop."""
	while True:
		# --------------------------- events ---------------------------- #
		handlingInput()
		# ------------------------ game routines ------------------------ #

		# --------------------------- drawing --------------------------- #
		drawing()
		# -------------------------- updating --------------------------- #
		updating()

# begin game-routines
if __name__ == '__main__':
    setup()
    main()
