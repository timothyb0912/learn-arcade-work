"""
This is my drawing for Lab 02.

For this lab, I will focus on a drawing that is practically useful to me
at the moment: an image of a person.

A person image is generically useful, and I plan to use it in causal diagrams.

Inspiration: https://thenounproject.com/search/?q=afro&i=2643409
"""
from typing import Tuple

import arcade
import attr


@attr.s
class Afro:
    center_x: int = attr.ib(default=300)
    center_y: int = attr.ib(default=300)
    outer_radius: int = attr.ib(default=100)
    inner_radius: int = attr.ib(default=60)
    inner_y_offset: int = attr.ib(default=-20)
    hair_color: Tuple[int] = attr.ib(default=arcade.csscolor.BLACK)

    def _draw_outer_circle(self):
        arcade.draw_circle_outline(
            center_x=self.center_x,
            center_y=self.center_y,
            radius=self.outer_radius,
            color=self.hair_color,
        )

    def _draw_inner_circle(self):
        arcade.draw_circle_outline(
            center_x=self.center_x,
            center_y=self.center_y + self.inner_y_offset,
            radius=self.inner_radius,
            color=self.hair_color,
        )

    def _draw_hair_outer(self):
        pass

    def _draw_hair_inner(self):
        pass

    def draw(self):
        self._draw_outer_circle()
        self._draw_inner_circle()
        self._draw_hair_outer()
        self._draw_hair_inner()


@attr.s
class Face:
    def draw(self):
        pass


@attr.s
class Body:
    def draw(self):
        pass


@attr.s
class Avatar:
    afro: Afro = attr.ib()
    face: Face = attr.ib()
    body: Body = attr.ib()

    def draw(self):
        afro.draw()
        face.draw()
        body.draw()


def make_drawing(
    avatar: Avatar,
    window_width: int = 600,
    window_height: int = 600,
    background_color: Tuple[int] = arcade.color.EARTH_YELLOW,
    title: str = "Afro-Avatar",
) -> None:
    arcade.open_window(window_width, window_height, title)

    # Set the background color
    arcade.set_background_color(background_color)

    # Begin drawing
    arcade.start_render()

    avatar.draw()

    # Finish drawing
    arcade.finish_render()

    # Run the commands and keep the window open.
    arcade.run()

    return


if __name__ == "__main__":

    afro = Afro()
    face = Face()
    body = Body()
    avatar = Avatar(afro=afro, face=face, body=body)
    make_drawing(avatar)
