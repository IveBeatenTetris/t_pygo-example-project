# dependencies
import t_pygo as go
import pygame as pg
# assignments
app	= go.App(
	title =	"Bar-Elements Tests",
	size =	(980, 550),
	background_color = (35, 35, 45),
	resizable =	True,
	fps = 120
)
el = {}
el["bar"] = go.Panel()
el["bar"].shift(app.rect.center, "center")
el["menu_bar"] = go.MenuBar(
    size = (app.rect.width, 30)
)
el["info_bar"] = go.InfoBar(
    size = (app.rect.width, 30)
)
el["info_bar"].shift(app.rect.bottomleft, "bottomleft")
app.draw_list.add(*[e for _, e in el.items()])
# main loop
def main():
    while True:
        # events
        if app.resized:
            el["bar"].shift(app.rect.center, "center")
            el["menu_bar"].resize((app.rect.width, 30))
            el["info_bar"].resize((app.rect.width, 30))
            el["info_bar"].shift(app.rect.bottomleft, "bottomleft")
        # updating
        app.update()

if __name__ == '__main__':
    main()
