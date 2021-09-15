

import pygame, sys, random

clock = pygame.time.Clock()
green=(0,255,0)
red=(255,0,0)
blue=(0,0,255)
pygame.init()
pygame.mixer.init()
file='water_blup.mp3'
pygame.mixer.music.load(file)



screen=pygame.display.set_mode((500,500))
pygame.display.set_caption('Ping Pong')
SCREEN_UPDATE =pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,45)




class Stick:
	
	def __init__(self,left=0, top=0, width=0, height=0):
		self.left=left
		self.top=top
		self.width=width
		self.height=height
		self.score_player=0
		self.score_stick=0
	def draw_actor(self,color):

		pygame.draw.rect(screen, color, (self.left,self.top,self.width, self.height) )
		
		pygame.display.flip()
	def move(self):
		velocity=5
		if self.top != 0 and self.top + self.height != 500:				
			if keys[pygame.K_UP]:
				self.top = self.top -velocity
				

			if keys[pygame.K_DOWN]:
				self.top = self.top +velocity
				

		elif self.top <=0:
			self.top=self.top+velocity
		elif self.top + self.height >=500:
			self.top=self.top - velocity
	def auto_move(self):
		velocity=4
		if self.top < ball.center[1]:
			pygame.time.wait(1)
			self.top=self.top+velocity
			if self.top + self.height >=500:
				self.top=self.top - (velocity+1)
		elif self.top > ball.center[1]:
			pygame.time.wait(1)
			self.top=self.top - velocity
			if self.top <=0:
				self.top=self.top + (velocity+1)
		elif self.top <=0:
			self.top=self.top+(velocity+1)
		elif self.top + self.height >=500:
			self.top=self.top - (velocity+1)


	def score(self):
		font = pygame.font.Font('freesansbold.ttf', 32)
		score=self.score_player
		text = font.render(f'Score: {score}', True, red)
		textRect = text.get_rect()
		textRect.center = (100, 50)
		screen.blit(text, textRect)
	def score_computer(self):
		font = pygame.font.Font('freesansbold.ttf', 32)
		score=self.score_stick
		text = font.render(f'Score: {score}', True, blue)
		textRect = text.get_rect()
		textRect.center = (400, 50)
		screen.blit(text, textRect)


class Ball:
	
	
	def __init__(self, center=[250,250], check=False,):

		self.center=center
		self.radius=10
		self.check=False
		
		

	def draw_ball(self):
		pygame.draw.circle(screen, (253,245,230), self.center, self.radius)
	
			
		
	def collision_player(self,check=False):
		velocity_x=6
		

		x=self.center[0]
		y=self.center[1]		
		
		
		#collision works!
		if x in range (player.width,player.width*2+10) :
			if y in range (player.top, player.top+player.height+12):
				print('collide')
				self.center[0] = self.center[0] +velocity_x
				self.center[1] = self.center[1] +velocity_y
				self.check=True
				

				
			else:
				self.center[0]=self.center[0]-velocity_x
				self.center[1] = self.center[1] -velocity_y


		if self.check==False:
			self.center[0]=self.center[0]-velocity_x
			self.center[1] = self.center[1] -velocity_y
		


	def collision_stick(self, check=True):
		velocity_x=6
		
		x=self.center[0]
		y=self.center[1]		
		#collision works!
		if x in range (500-2*stick1.width,500-stick1.width+10) :
			if y in range (stick1.top, stick1.top+stick1.height+12):
				print('collide')
				self.center[0] = self.center[0] -velocity_x
				self.center[1] = self.center[1] -velocity_y
				
				self.check=False
				
				
			else:
				self.center[0]=self.center[0]+velocity_x
				self.center[1] = self.center[1] -velocity_y
		else:
			self.center[0]=self.center[0]+velocity_x
			self.center[1] = self.center[1] -velocity_y

	
		

			


ball=Ball()

player=Stick(20,20,20,150)
stick1=Stick(470,20,20,150)

player_turn=True
game_on=True
velocity_y=0
def stay_in (velocity_y):
	if ball.center[1] - 8 <= 0:
		velocity_y= - velocity_y
		return velocity_y
	if ball.center[1] + 8 >= 500:
		velocity_y= - velocity_y
		return velocity_y
	else:
		return velocity_y
while game_on:


	screen.fill((48,48,48))
	player.score()
	stick1.score_computer()
	
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			quit()
		keys = pygame.key.get_pressed()
	

	player.draw_actor(red)
	stick1.draw_actor(blue)
	
	
	player.move()
	ball.draw_ball()
	if ball.check==False:
		ball.collision_player()
		
		if ball.check ==True:
			pygame.mixer.music.play(1)
			velocity_y=random.randint(-4,4)
			

			
		if ball.center[0] <= 0:

			stick1.score_stick=stick1.score_stick+1
			pygame.time.wait(500)
			player.top=250
			stick1.top=250
			ball.center= [250,250]
	if ball.check==True:		
		ball.collision_stick()
		stick1.auto_move()
		
		if ball.check==False:
			pygame.mixer.music.play(1)
			velocity_y=random.randint(-4,4)
			
			
		if ball.center[0] >= 500:
			player.score_player =player.score_player +1
			pygame.time.wait(500)
			player.top=250
			stick1.top=250
			ball.center= [250,250]
	
	velocity_y=stay_in(velocity_y)
	font = pygame.font.Font('freesansbold.ttf', 20)
	
	text = font.render('By Batuhan Uzun', True, green)
	textRect = text.get_rect()
	textRect.center = (410, 480)
	screen.blit(text, textRect)
	
	pygame.display.update()
	clock.tick(100)
