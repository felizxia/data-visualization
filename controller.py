import pygame
import view
import model
from button import Button
pygame.init()

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Election Data Viewer")
pygame.display.update()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
data = model.get_data()


bc1 = view.BarChart(rect=pygame.Rect(0, 50, 950, 700), ticks=5,max_val=10000000, plot_area_width_ratio=0.95,values=data)
# bc3 = view.BarChart(rect=pygame.Rect(0, 50, 950, 700), ticks=5,max_val=100, plot_area_width_ratio=0.95,values=data)

party="dem"
max_val=10000000
raw=True
sort_ascending=True
# de = None

class PartyButton(Button):
	def __init__ (self,text,rect,chart,demand):
		Button.__init__(self,text,rect)
		# self.default=True
		self.party=demand
		self.chart=chart

		# pygame.draw.rect(surface, RED, self.rect)
	def on_click(self,event):
		global party
		global raw
		global sort_ascending
		party=self.party
		data = model.get_data(party=party,raw=raw,sort_ascending=sort_ascending)
		self.chart.set_values(data)

		# global de
		# de = True
	def draw(self, surface):
		global party
		if party == self.party:
			color= RED

		else:
			color = GRAY
		pygame.draw.rect(surface, color, self.rect)
		font = pygame.font.Font(None, 36)
		label_view = font.render(self.text, False, BLACK)
		label_pos = label_view.get_rect()
		label_pos.centery = self.rect.centery
		label_pos.centerx = self.rect.centerx
		surface.blit(label_view, label_pos)

class UpdownButton(Button):
	def __init__ (self,text,rect,chart,demand):
		Button.__init__(self,text,rect)

		self.sort_ascending=demand
		self.chart=chart

	def on_click(self,event):
		global party
		global raw
		global sort_ascending
		sort_ascending=self.sort_ascending
		data = model.get_data(party=party,raw=raw,sort_ascending=sort_ascending)
		self.chart.set_values(data)
		# global de
		# de = True
	def draw(self, surface):
		global sort_ascending
		if sort_ascending == self.sort_ascending:
			color= RED

		else:
			color = GRAY
		pygame.draw.rect(surface, color, self.rect)
		font = pygame.font.Font(None, 36)
		label_view = font.render(self.text, False, BLACK)
		label_pos = label_view.get_rect()
		label_pos.centery = self.rect.centery
		label_pos.centerx = self.rect.centerx
		surface.blit(label_view, label_pos)

class RawButton(Button):
	def __init__ (self,text,rect,chart,demand):
		Button.__init__(self,text,rect)
		self.default=True
		self.raw=demand
		self.chart=chart

	def on_click(self, event):
		global party
		global raw
		global sort_ascending
		# global de
		# global max_val
		raw=self.raw
		data = model.get_data(party=party,raw=raw,sort_ascending=sort_ascending)
		if self.raw==True:
			self.chart.max_val=10000000
			self.chart.set_values(data)
		if self.raw== False:
			self.chart.max_val = 100
			self.chart.set_values(data)

	def draw(self, surface):
		global raw
		if raw == self.raw:
			color = RED

		else:
			color = GRAY
		pygame.draw.rect(surface, color, self.rect)
		font = pygame.font.Font(None, 36)
		label_view = font.render(self.text, False, BLACK)
		label_pos = label_view.get_rect()
		label_pos.centery = self.rect.centery
		label_pos.centerx = self.rect.centerx
		surface.blit(label_view, label_pos)
		# if self.chart== bc3:
		# 	de = False
		# else:
		# 	de = True
			#bc1.draw(screen)

button1= PartyButton("Dem",pygame.Rect(1000,  20, 100, 40),bc1,"dem")
button2 = PartyButton("Gop", pygame.Rect(1000,  60, 100, 40),bc1,"gop")
button3= UpdownButton("Up",pygame.Rect(1000,  120, 100, 40),bc1,True)
button4= UpdownButton("Down",pygame.Rect(1000,  160, 100, 40),bc1,False)
button5= RawButton("Raw",pygame.Rect(1000,  220, 100, 40),bc1,True)
button6= RawButton("%",pygame.Rect(1000,  260, 100, 40),bc1,False)

# display loop
done = False
while not done:
	screen.fill((0,0,0))
	button1.draw(screen)
	button2.draw(screen)
	button3.draw(screen)
	button4.draw(screen)
	button5.draw(screen)
	button6.draw(screen)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		else:
			button1.handle_event(event)
			button2.handle_event(event)
			button3.handle_event(event)
			button4.handle_event(event)
			button5.handle_event(event)
			button6.handle_event(event)

	# if de == False:
	# 	bc3.draw(screen)
	# else:
	bc1.draw(screen)



	pygame.display.update()

pygame.quit()


