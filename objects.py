
class Ball:
	def __init__(self, size, color, shape, weight):
		#attributes
		self.size = size
		self.color = color
		self.shape = shape
		self.weight = weight
		self.pos_x = 0 
		self.pos_y = 0
		self.filled = False

	#Changing Attributes
	def change_size(self, new_size):
		self.size = new_size
		return(self.size)

	def change_color(self, new_color):
		self.color = new_color
		return(self.color)

	def change_shape(self, new_shape):
		self.shape = new_shape
		return(self.shape)

	def change_weight(self, new_weight):
		self.weight = new_weight
		return(self.weight)

	#Get Attributes
	def get_size(self):
		return(self.size)

	def get_color(self):
		return(self.color)

	def get_shape(self):
		return(self.shape)

	def get_weight(self):
		return(self.weight)


	#Things Balls Do
	def throw(self, height):
		self.pos_y = height
		print(self.pos_y)
		self.pos_y = 0
		print(self.pos_y)
		return(self.pos_y)

	def kick(self, distance):
		self.pos_x = distance
		print("You kicked the ball {} feet".format(distance))
		return(self.pos_x)

	def drop(self, height):
		self.pos_y = height
		print("You are dropping the ball from {} feet".format(height))
		self.pos_y = 0
		print("Your ball has hit the ground! {} feet".format(self.pos_y))
		return(self.pos_y)

	def kickdrop(self):
		pass

	def toggle_water(self):
		if self.filled:
			self.filled = False
		else: 
			self.filled = True
		return(self.filled)


my_ball = Ball("small", "pink", "sphere", ".5 pounds")
my_ball.throw(34)
print(my_ball.change_color("purple"))
print(my_ball.toggle_water())
print(my_ball.toggle_water())

	#Reminder set and get
	#Reminder 




#Reminder: How objects changed programming