import random
import sys

def main():
	
	choice = []
	
		
	with open("KakaoTalkLog.txt", encoding="utf8") as myFile:
		for num, line in enumerate(myFile, 1):
			choice.append(line)

	def randomChat(x):
		"""This posts the line right after the input detected but chooses randomly amongst responses"""
		lines = f.readlines()

		try:
			if "Jack Jack Jack" in x:
				jackie_string = x
				print("\nJackie:\n" + jackie_string[33:].strip() + "\n")
			elif "Victoria" and "Gelb" in x:
				vic_string = x
				print("\nVictoria:\n" + vic_string[28:].strip() + "\n")
			elif "shane" and "Shane" in x:
				shane_string = x
				print("\nShane:\n" + shane_string[33:].strip() + "\n")
			elif "100%" and "Corrie" in x:
				cor_string = x
				print("\nCorrie:\n" + cor_string[28:].strip() + "\n")
		except UnicodeEncodeError:
			pass
	
	while True:
	
		f = open("KakaoTalkLog.txt", encoding="utf8")
		#You specify the encoding when you open the file
	
		prompt = input("User:\n")	
		# The search variable
		
		if prompt == "quitcodeone":
		#breaker code for loops
			sys.exit("Finish.")
			
		thing = random.choice(choice)
		# print(thing)
		randomChat(thing)
	#this keeps the bot running
	
	f.close()

	input()
	
if __name__ == "__main__":
	main()