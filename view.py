import pygame

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)


# a class to display a horizontal bar chart in pygame
class Bar:
	def __init__(self, color, length, height, padding=0.1):
		self.length = length
		self.color = color
		self.height = height
		self.padding = padding

	# decide width of bars
	def draw(self, surface, x, y):
		padding_height = self.height * self.padding
		adjusted_height = self.height - 2 * padding_height
		pygame.draw.rect(surface, self.color, [x, y + padding_height, self.length, adjusted_height])


class BarChart:
	# rect: a pygame.rect encoding size and position
	def __init__(self, rect=pygame.Rect(0, 0, 600, 400), values=[], ticks=10,
				 plot_area_width_ratio=0.8, plot_area_height_ratio=0.8, color=GREEN,
				 max_val=15):
		self.rect = rect
		self.color = color
		self.background = BLACK
		self.label_color = WHITE

		# Constant ratios for portions of the display
		self.label_area_width_ratio = 0.2
		self.scale_area_height_ratio = 0.2
		self.plot_area_width_ratio = plot_area_width_ratio
		self.plot_area_height_ratio = plot_area_height_ratio
		self.ticks = ticks
		#assigned max_val
		self.max_val = max_val
		self.rect = rect
		self.scale_area = pygame.Rect(
			rect.x + rect.width * self.label_area_width_ratio,
			rect.y + rect.height * self.plot_area_height_ratio,
			rect.width * self.plot_area_width_ratio,
			rect.height * self.scale_area_height_ratio
		)
		self.label_area = pygame.Rect(
			rect.x,
			rect.y,
			rect.width * self.label_area_width_ratio,
			rect.height * self.plot_area_height_ratio
		)
		self.plot_area = pygame.Rect(
			rect.x + self.label_area.width,
			rect.y,
			rect.width * self.plot_area_width_ratio,
			rect.height * self.plot_area_height_ratio
		)
		self.set_values(values)

	def set_values(self, values):
		self.values = values
		themax_val = 0
		for v in values:
			try:
				if float(v[1]) > themax_val:
					themax_val =float(v[1])
			except:
				pass
			# print(values)
		self.themax_val = themax_val

	def draw(self, surface):
		self.draw_bars(surface)
		bar_num = 0

		for v in self.values:
			print(v[1])
			bar_length = self.plot_area.width * v[1] / self.max_val
			b = Bar(self.color,
					bar_length,
					self.plot_area.height / len(self.values),
					padding=0.1)
			y_pos = self.plot_area.y + bar_num * b.height
			bar_num += 1
			b.draw(surface, self.plot_area.x, y_pos)

	def get_bar_height(self):
		return self.plot_area.height / len(self.values)

	def draw_labels(self, surface):
		bar_num = 0
		for v in self.values:
			label_text = v[0]
			font = pygame.font.Font(None, 20)
			label_view = font.render(label_text, False, WHITE)
			label_pos = label_view.get_rect()
			label_pos.centery = self.rect.y + self.get_bar_height() * bar_num + self.get_bar_height() / 2
			label_pos.x = self.rect.x + 8
			surface.blit(label_view, label_pos)
			bar_num += 1

	def draw_scale(self, surface, ticks):
		scale_label_spacing = self.scale_area.width / self.max_val + 1
		font = pygame.font.Font(None, 20)
		scale_label_view = font.render(str(0.0), False, WHITE)
		scale_label_pos = scale_label_view.get_rect()
		scale_label_pos.y = self.scale_area.y + 10
		scale_label_pos.x = self.scale_area.x
		surface.blit(scale_label_view, scale_label_pos)
		interval = int(self.max_val /(self.ticks - 1))


		for i in range(interval, self.max_val + interval, interval):
			font = pygame.font.Font(None, 20)
			scale_label_view = font.render(str(i), False, WHITE)
			scale_label_pos = scale_label_view.get_rect()
			scale_label_pos.y = self.scale_area.y + 10
			scale_label_pos.x= self.scale_area.x+(i/self.max_val)*self.plot_area.width
			surface.blit(scale_label_view, scale_label_pos)
			# print(interval)
	def draw_bars(self, surface):
		bar_num = 0
		for v in self.values:
			try:
				bar_length = self.plot_area.width * float(v[1]) / self.max_val
				b = Bar(self.color,
						bar_length,
						self.plot_area.height / len(self.values))
				y_pos = self.plot_area.y + bar_num * b.height
				bar_num += 1
				b.draw(surface, self.plot_area.x, y_pos)
			except:
				pass
	# and update the BarChart.draw() method
	def draw(self, surface):
		self.draw_bars(surface)
		self.draw_labels(surface)
		self.draw_scale(surface, ticks=10)


# SELF-TESTING MAIN
if __name__ == "__main__":

	pygame.init()

	screen = pygame.display.set_mode((1000, 700))

	pygame.display.set_caption("Bar Chart Test")
	pygame.display.update()

	data = [
		("apples", 6),
		("bananas", 7),
		("grapes", 4),
		("pineapple", 1),
		("cherries", 15)
	]

	# display using default values
	bc = BarChart(values=data)

	data2 = [
		('Jenny', 80),
		('Stanley', 90),
		('Timothy', 92)
	]

	# override all of the defaults
	bc2 = BarChart(
		rect=pygame.Rect(0, 400, 800, 150),
		values=data2,
		ticks=5,
		plot_area_width_ratio=0.85,
		plot_area_height_ratio=0.9,
		color=RED,
		max_val=100
	)

	# display loop
	done = False
	while not done:
		screen.fill(BLACK)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
		bc.draw(screen)
		bc2.draw(screen)
		pygame.display.update()
