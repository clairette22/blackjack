def premier(n):
	if n==1: 
		reponse = False
	else :
		reponse = True
		for k in range (2, n):
			if n%k==0:
				reponse = False
	return(reponse)
	
#pour tester la focntion qui juge si un nombre est premier ou non
#avec "True" = le nombre est premier
#et "False" = le nombre n'est pas premier
#print(premier(8))


#pour afficher les nombres premiers entre deux nombres donnes a et b
a= int(input("soit un nombre a : "))
b= int(input("et un nombre b : "))

print'alors les nombre premiers compris entre', a, 'et', b, 'sont :'

for y in range (a, b):
	if premier(y) == True: 
		print (y)

# Si n n est pas premier, alors cette fonction affiche tous les diviseurs de n
#autre que 1 et lui-meme
def diviseurs (n) :
	if premier(n) != True :
		for k in range (2, n):
			if n%k==0:
				print(k)
				
diviseurs(8)

# Cette fonction affiche tous les diviseurs de n
def nb_Div (n) :
	nombre = 0
	for k in range (1, n+1):
		if n%k==0:
			nombre = nombre + 1
	return (nombre)
