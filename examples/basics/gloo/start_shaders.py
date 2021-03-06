#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from vispy import gloo
from vispy import app
import numpy as np

VERT_SHADER = """
attribute vec2 a_position;
void main() {
    gl_Position = vec4(a_position, 0.0, 1.0);
    gl_PointSize = 10.0;
}
"""

FRAG_SHADER = """
void main() {
    gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0);
}
"""


class Canvas(app.Canvas):
    def __init__(self):
        app.Canvas.__init__(self, keys='interactive')
        self.program = gloo.Program(VERT_SHADER, FRAG_SHADER)
        data = np.random.uniform(-0.5, 0.5, size=(20, 2))
        self.program['a_position'] = data.astype(np.float32)

    def on_resize(self, event):
        width, height = event.size
        gloo.set_viewport(0, 0, width, height)

    def on_draw(self, event):
        gloo.clear('white')
        self.program.draw('points')

if __name__ == '__main__':
    c = Canvas()
    c.show()
    if sys.flags.interactive != 1:
        app.run()
