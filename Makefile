
all:	compil_my


compil_my:
		cp 101pong.py 101pong 
		cp pong.py pong2D
		chmod +x 101pong
		chmod +x pong2D

		
clean:
		rm 101pong
		rm pong2D

fclean:	clean

re: fclean all

