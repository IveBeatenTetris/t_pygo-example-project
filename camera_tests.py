import t_pygo as go
import pygame as pg

app = go.Window({
	"title": "camera_tests",
	"size": (320*2, 240*2),
	"zoom": 1,
	"fps": 70
})
map = go.Map("test_map")
player = go.Player("hero")
camera = go.Camera({
	"size": app.size,
	"tracking": player
})
text = go.Text({
	"font": "Verdana",
	"size": 20,
	"text": "fps",
	"color": (255, 255, 255)
})

def main():
	"""main function."""
	player.knownblocks = map.blocks
	if map.playerstart:
	    player.position(map.playerstart)
	# main loop
	while True:
		# events
		app.events()
		keys = app.pressedKeys()
		# moving
		if keys[pg.K_w]:
			player.move((0, -player.speed))
		elif keys[pg.K_s]:
			player.move((0, player.speed))
		if keys[pg.K_a]:
			player.move((-player.speed, 0))
		elif keys[pg.K_d]:
			player.move((player.speed, 0))
		# zooming
		if app.mouseWheel() == "up":
			camera.zoom(1)
		elif app.mouseWheel() == "down":
			camera.zoom(-1)
		# drawing
		screen = pg.Surface(camera.size)
		go.draw(map.preview, screen, camera)
		go.draw(player, screen, "center")
		if camera.zoomfactor > 1:
			screen = go.scale(screen, camera.zoomfactor)
		app.draw(screen, "center")
		app.draw(text)
		# frames per second
		text.update({
			"text": "quacks: {0}".format(app.fps)
		})
		# updating
		player.update()
		camera.update()
		app.update()
if __name__ == '__main__':
    main()
