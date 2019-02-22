from typing import List
from pygame import Surface
from fighting_game.helpers.image import Image
from fighting_game.helpers.colors import BLACK
import os


class SpriteSheet:

    def __init__(self, base_sprite_path: str, frames: int):
        self.base_sprite_path: str = base_sprite_path
        self.frames: int = frames
        self.key_name: str = None
        self.base_file_name: str = None
        self.images: List[Surface] = []

    def load_images(self):
        if not (self.key_name and self.base_file_name):
            raise ValueError('key_name or base_file_name not set')

        if not self.images:
            self.images = []

        for frame in range(self.frames):
            file_format = "{} ({}).png".format(self.base_file_name, frame + 1)

            image = Image.load(os.path.join(self.base_sprite_path, file_format))
            image.set_colorkey(BLACK)
            self.images.append(image)


