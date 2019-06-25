print "********Tik Tok Tak Game**********"
board = [0,1,2,
 		3,4,5,
 		6,7,8]

def show(board):
	# board = [0,1,2,
	# 3,4,5,
	# 6,7,8]
	print board[0],"|",board[1],"|",board[2]
	print "----------"
	print board[3],"|",board[4],"|",board[5]
	print "----------"
	print board[6],"|",board[7],"|",board[8]
# board = [0,1,2,3,4,5,6,7,8]
show(board)

def checkline(char,place1,place2,place3):
	if board[place1] == char and board[place2] == char and board[place3]==char:
		return True
def checkall(char):
	if checkline(char,0,1,2):
		return True
	if checkline(char,1,4,7):
		return True
	if checkline(char,2,5,8):
		return True
	if checkline(char,0,3,6):
		return True

	if checkline(char,6,7,8):
		return True
	if checkline(char,3,4,5):
		return True

	if checkline(char,2,4,6):
		return True
	if checkline(char,0,4,8):
		return True

while True:
	input = raw_input("select a place")
	input = int(input)

	if board[input] != "x" and board[input] != "o":
		board[input] = "x"
		if checkall("x") == True:
			print "----x is win -----"
			break

		while True:
			user_input=raw_input("select another place")
			user_input = int(user_input)

			if board[user_input]!="o" and board[user_input] != "x":
				board[user_input] = "o"
				#show()
				break

				if checkall("o") == True:
					print "----- o is win ----"
					break
	else:
		print "This place is already exist"
	show(board)

