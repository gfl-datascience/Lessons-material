# ask for two values and print a list of possible operations
first_number= float(input("First number: "))
second_number=float(input("Second number: "))
option_correct = False
while not option_correct:
	options= "Digita 1 per area e perimetro\nDigita 2 per area triangolo\nDigita 3 per diametro e area cerchio"
	print(options)
	choose=int(input(""))
	
	if choose == 1:
		perimeter = 2*first_number + 2*second_number
		area_rectangle = first_number*second_number
		print("Il perimetro del rettangolo e' "+str(perimeter)+ " l'area e' "+str(area_rectangle))
		option_correct=True
	elif choose == 2:
		area_triangle = first_number*second_number/2
		print("Area triangolo: "+str(area_triangle))
		option_correct=True
	elif choose == 3:
		diameter = first_number+second_number
		radius = diameter/2
		pi = 3.14
		area = pi*radius*radius
		print("Area del cerchio: "+str(area))
		option_correct=True
	else:
		print("Wrong selection")