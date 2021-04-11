import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Canvas
from kivy.graphics import Color
from kivy.graphics import Line
from kivy.graphics import Rectangle

class Paint(Widget):
	def __init__(self, **kwargs):
		super(Paint, self).__init__(**kwargs)
		self.m = 0
		self.color = (0, 1, 0, 1)
		
		with self.canvas:
			#white board
			Color(rgba=(1, 1, 1, 1))
			Rectangle(size=(720, 1440))

			Color(rgba=self.color)
			Rectangle(pos=(300, 1300), size=(140, 70))
		
	def on_touch_down(self, touch):
		self.x1 = touch.pos[0]
		self.y1 = touch.pos[1]
		self.conx = self.x1
		self.cony = self.y1
		
		if self.x1 >= 300 and self.y1 >= 1300 and self.x1 <= 440 and self.y1 <= 1370:
			if self.color == (0, 1, 0, 1):
				self.color = (1, 0, 0, 1)
			elif self.color == (1, 0, 0, 1):
				self.color = (0, 0, 1, 1)
			elif self.color == (0, 0, 1, 1):
				self.color = (1, 1, 0, 1)
			elif self.color == (1, 1, 0, 1):
				self.color = (0, 1, 1, 1)
			elif self.color == (0, 1, 1, 1):
				self.color = (1, 0, 1, 1)
			elif self.color == (1, 0, 1, 1):
				self.color = (0, 0, 0, 1)
			elif self.color == (0, 0, 0, 1):
				self.color = (0, 1, 0, 1)
			
			with self.canvas:
				Color(rgba=self.color)
				Rectangle(pos=(300, 1300), size=(140, 70))
		
		
	def on_touch_move(self, touch):
		self.x2 = touch.pos[0]
		self.y2 = touch.pos[1]
		try:
			self.newm = (self.y2-self.y1)/(self.x2-self.x1)
		except ZeroDivisionError:
			self.newm = "Straight up"
			
		if self.m != self.newm:
			self.x1 = self.conx
			self.y1 = self.cony

		with self.canvas:
			Color(rgba=self.color)
			Line(width=7, points=(self.x1,self.y1, self.x2, self.y2))
		try:
			self.m = (self.y2-self.y1)/(self.x2-self.x1)
		except ZeroDivisionError:
			self.m = "Straight up"
		self.conx = self.x2
		self.cony = self.y2

class MyApp(App):
	def build(self):
		return Paint()
	
if __name__=="__main__":
	MyApp().run()
