plain_chars =["a","b","c","d","e","f","g","h","i","l","m","n","o","p","q","r","s","t","u","v","z"]
crypto_chars = list(range(0,21))    #returns a list with number between 0 and 20
crypto_chars.reverse()    #reverse 

##### CHIEDERE 3 FRASI O PAROLE CON IL WHILE
N = 0
while N <3:
	text = input("Sentence: ")
	text = text.lower()
	for c in text:
		if c in plain_chars:
			index = plain_chars.index(c)
			new_letter = str(crypto_chars[index])
			text= text.replace(c,new_letter)
	print(text)
	N+=1