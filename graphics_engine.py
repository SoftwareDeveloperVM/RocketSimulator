import pygame as graphic
import sys as system
import json

graphic.init()

width, height, loop = 700, 700, True
screen = graphic.display.set_mode((width, height))
graphic.display.set_caption("Rocket Simulator")
clock = graphic.time.Clock()

with open("config file/colors.json", "r") as file:
    colors = json.load(file)

with open("config file/initial.json", "r") as file:
    initial = json.load(file)

while loop:
    for event in graphic.event.get():
        if event.type == graphic.QUIT:
            loop = False
    screen.fill(colors["colors"]["white"])
    graphic.display.flip()
    clock.tick(initial["environment"]["fps"])
graphic.quit()
system.exit()
