import t_pygo as go
import pygame as pg

app = go.Window({
	"title": "camera_tests",
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

def testEvent():
	print("success")
def testEvent2():
	print("success again")
def input():
	"""handles all keyboard mouse and controller input."""
	# shift key is pressed
	for event in app.events():
		# makes the player move faster
		if event.type is pg.KEYDOWN and event.key == pg.K_LSHIFT:
			player.setAnimationSpeed(15)
			player.speed = 2
		# makes the player move slow again
		elif event.type is pg.KEYUP and event.key == pg.K_LSHIFT:
			player.setAnimationSpeed(30)
			player.speed = 1
	# pressed keys
	keys = app.pressedKeys()
	# keyboard moving
	if keys[pg.K_w]:
		player.move((0, -player.speed))
	elif keys[pg.K_s]:
		player.move((0, player.speed))
	if keys[pg.K_a]:
		player.move((-player.speed, 0))
	elif keys[pg.K_d]:
		player.move((player.speed, 0))
	# event areas
	for ea in map.layers["events"].objects:
		if player.collide(ea):
			if ea.trigger == "activate":
				if keys[pg.K_e]:
					if ea.state == "ready":
						# calling function
						globals()[ea.name]()
						# disable event
						ea.state = "done"
			elif ea.trigger == "touch":
				if ea.state == "ready":
					# calling function
					globals()[ea.name]()
					# disable event
					ea.state = "done"
def main():
	"""main function."""
	app.resize(camera.size)
	player.knownblocks = map.blocks
	if map.playerstart:
	    player.position(map.playerstart)
	# main loop
	while True:
		input()
		# drawing
		screen = pg.Surface(camera.size)
		go.draw(map.preview, screen, camera)
		go.draw(player, screen, "center")
		# scaling display if zoomed
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
