import math
import pygame as py
import time
import os


def scroll(background):
    py.init()

    clock = py.time.Clock()

    frame_height = 600
    frame_width = 1200

    # Pygame frame window
    py.display.set_caption("Endless Scrolling in pygame")
    screen = py.display.set_mode((frame_width, frame_height))

    # Load background image
    bg = py.image.load(os.path.join("images", background))

    # Define main variables in scrolling
    scrolling = 0

    # Fix potential buffering issues
    tiles = math.ceil(frame_width / bg.get_width()) + 1

    # Set time to 0
    seconds = 0
    # Run for 60 seconds
    while seconds < 60:
        # Manage speed of scrolling
        clock.tick(33)

        # Append the image to the back of the same image
        i = 0
        while i < tiles:
            screen.blit(bg, (bg.get_width() * i + scrolling, 0))
            i += 1
        # Frame for scrolling
        scrolling -= 6

        # Reset scroll frame
        if abs(scrolling) > bg.get_width():
            scrolling = 0
        # Close frame of scrolling
        for event in py.event.get():
            if event.type == py.QUIT:
                quit()

        py.display.update()
        time.sleep(0.01)
        seconds += 1

    py.quit()
