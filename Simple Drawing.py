import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import *

class Paint(Widget):
	def __init__(self, **kwargs):
		super(Paint, self).__init__(**kwargs)
		self.m = 0
		self.color = (0, 1, 0, 1)
		
		with self.canvas:
			#white board
			Color(rgba=(1, 1, 1, 1))
			Rectangle(size=(720, 1440))

			#colour selector
			Color(rgba=(0, 0, 0, 1))
			Rectangle(pos=(297.5, 1297.5), size=(145, 75))
			
			Color(rgba=self.color)
			Rectangle(pos=(300, 1300), size=(140, 70))
			
			#size selector
			self.currentSize = 10
			j = 5
			x = 50
			y = 1200
			c = 42
			self.sizeBtn = []
			self.sizes = []
			for i in range(10):
				Color(rgba=(.1, .1, .1, .1))
				self.sizeBtn.append(Rectangle(pos=(5, y-c), size=(95, 95)))
				self.sizes.append(j)
				Color(rgba=(0, 0, 0, 1))
				Ellipse(pos=(x, y), size=(j, j))
				j += 5
				x -= 2.5
				y -= 100
				c -= 2.5
				
				#border
				Line(points=[118, 1278, 118, 0], width=2)
				Line(points=[118, 1278, 720, 1278], width=2)
		
	def on_touch_down(self, touch):
		#touch coordinates
		self.x1 = touch.pos[0]
		self.y1 = touch.pos[1]
		self.conx = self.x1
		self.cony = self.y1
		
		#size update
		for i in range(10):
			if self.x1 >= self.sizeBtn[i].pos[0] and self.x1 <= self.sizeBtn[i].pos[0]+95 and self.y1 >= self.sizeBtn[i].pos[1] and self.y1 <= self.sizeBtn[i].pos[1]+95:
				self.currentSize = self.sizes[i]
		
		#colour update
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
				self.color = (1, 1, 1, 1)
			elif self.color == (1, 1, 1, 1):
				self.color = (0, 1, 0, 1)
		
		#colour update and draw circle on touch		
		with self.canvas:
			Color(rgba=self.color)
			Rectangle(pos=(300, 1300), size=(140, 70))
			
			if self.x1 >= 120 and self.y1 <= 1280:
				Ellipse(pos=(touch.pos[0]-(self.currentSize/2), touch.pos[1]-(self.currentSize/2)), size=(self.currentSize, self.currentSize))
		
	def on_touch_move(self, touch):
		#check if within limits
		temp = True
		if touch.pos[0] < 120 or touch.pos[1] > 1280:
			temp = False
		
		#draw	
		if temp == True:
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
				Line(width=self.currentSize/2, points=(self.x1,self.y1, self.x2, self.y2))
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
