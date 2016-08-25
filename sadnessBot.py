import random
import time

def main():

	q_bank = [] #quote bank
		
	with open("KakaoTalkLog.txt", encoding="utf8") as myFile:
		for num, line in enumerate(myFile, 1):
			q_bank.append(line)
	#fills the quote bank
			
	def loneliness(x):
		"""This posts the line right after the input detected but chooses randomly amongst responses"""

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
			#stripping the quotes of their Kakao weirdnesses and assigning a handle	
			
		except UnicodeEncodeError:
			pass
			
	while True:
	
		f = open("KakaoTalkLog.txt", encoding="utf8")
		#You specify the encoding when you open the file

		time.sleep(random.randint(1, 3))
		#spacing out the bot replies
		
		loneliness(random.choice(q_bank))
		#making a random choice in the quote bank and feeding my loneliness
		
	
if __name__ == "__main__":
	main()