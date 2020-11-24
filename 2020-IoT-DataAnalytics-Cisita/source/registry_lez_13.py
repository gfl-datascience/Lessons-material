class Person:
	def __init__(self, name,last_name,age):
		self._name = name                # attribute
		self._last_name = last_name		       # attribute
		self._age = age
	def get_name(self):
		return self._name
	def get_last_name(self):
		return self._last_name
	def get_age(self):
		return self._age
def main():
	N=0
	people = []
	while N<3:
		request = input("Nome,cognome,eta: ")
		fields = request.split(",")
		if len(fields)>2:
			p = Person(fields[0],fields[1],float(fields[2]))
			people.append(p)
			N+=1
			
			

	with open("registry.txt","w+") as f1:
		for p in people:
			f1.write(p.get_name()+","+p.get_last_name()+","+str(p.get_age())+"\n")
main()