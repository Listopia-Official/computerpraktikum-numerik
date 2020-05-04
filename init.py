import pygame as pg

from cucker_smale import *

pg.font.init()  # Init font module so we can create a font here

# Image by https://pixabay.com/illustrations/clipart-fish-sea-water-swim-3418189/
fish_icon = pg.image.load('fish_icon.png')
fish_sprite = pg.image.load('fish_sprite.png')  # Scaled, and cut out

# General display properties
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

FPS_CAP = 60

REALTIME = True  # If false, the rendered frames will be saved and merged into a video with constant FPS_CAP framerate

EXPORTED_VIDEO_NAME = "rendered_scene.avi"

APP_ICON = fish_icon
APP_TITLE = "Flocking Simulation ({:}x{:})".format(SCREEN_WIDTH, SCREEN_HEIGHT)
APP_FONT = pg.font.SysFont('Comic Sans MS', 20)

BACKGROUND_COLOR = (255, 255, 255,)

# Fish-specific settings
FISH_WIDTH = 28
FISH_HEIGHT = 10

# Fish boundary colors
FISH_CENTER_POINT_COLOR = (255, 0, 0)
FISH_BOUNDING_BOX_COLOR = (0, 255, 0)

# Primitive fish rendering
FISH_COLOR = (84, 84, 84)
FISH_DIRECTION_COLOR = (0, 0, 255)

# Pretty fish rendering
FISH_SPRITE = pg.transform.smoothscale(fish_sprite, (FISH_WIDTH, FISH_HEIGHT))

# Flock settings
MOUSE_FISH = False  # makes the mouse cursor behave like a fish

flock = Flock(100)
flock.positions = np.random.normal((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), 50, (flock.population, 2))
flock.velocities = np.random.normal((0, 0), 100, (flock.population, 2))
flock.dimensions = (SCREEN_WIDTH, SCREEN_HEIGHT)
