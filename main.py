from manim import *

class Benzol(Scene):
    def construct(self):
        radius = 2
        vector = UP * radius
        points = np.empty(6, np.ndarray)
        lines = np.empty(3, np.ndarray)
        for i in range(len(points)):
            vector = rotate_vector(vector, PI / 3)
            points[i] = vector
        for i in range(len(lines)):
            lines[i] = Line(points[i * 2] * .8, points[i * 2 + 1] * .8)
        self.add(Polygon(*points), *lines)
