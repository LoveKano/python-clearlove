import os
import time
WIDTH=79
message="4396"
printedMessage=["","","","","","",""]
characters={
	" ":[	" ",
			" ",
			" ",
			" ",
			" ",
			" ",
			" "],
	"4":[	"*    *",
			"*    *",
			"*    *",
			"******",
			"     *",
			"     *",
			"     *"],
	"3":[	"******",
			"     *",
			"     *",
			"******",
			"     *",
			"     *",
			"******"],
	"9":[	"******",
			"*    *",
			"*    *",
			"******",
			"     *",
			"     *",
			"******"],
	"6":[	"******",
			"*     ",
			"*     ",
			"******",
			"*    *",
			"*    *",
			"******"],

}
def clearlove():
	for row in range(7):
		for char in message:
			printedMessage[row]+=(str(characters[char][row])+"  ")
	offset=WIDTH
	while True:
		os.system("cls")
		for row in range(7):
			print(" "*offset+printedMessage[row][max(0,offset*-1):WIDTH-offset])
		offset-=1
		if offset<=((len(message)+2)*6)-1:
			offset=WIDTH
		time.sleep(0.05)
	print("I will prove that I am the best jungle in the world")
clearlove()