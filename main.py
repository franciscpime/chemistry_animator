from manim import *

# manim -pql main.py NomeDaCena
class Chemistry_Animator(Scene):

    def construct(self):
        self.play(Write(self.equation))
        self.wait(2)