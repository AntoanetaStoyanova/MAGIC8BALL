import random
question = input("Posez moi une question et je vous donnerai la réponse!")
answer = random.randint(1, 8)
keywords = ["bière", "biere", "apéro", "apero"]
if any(keyword in question.lower() for keyword in keywords):
    print("Mais quelle est cette question? Bien sûr que c'est l'heure de l'apéro!")
elif answer == 1:
    print("C'est sûr et certain!")
elif answer == 2:
    print("Vous êtes sur la bonne voix!")
elif answer == 3: 
    print("Vous pouvez y compter!")
elif answer == 4: 
    print("Demandez à nouveau, plus tard!")
elif answer == 5: 
    print("Je suis sûr que ce n'est pas ce que vous voulez me demander!"),
elif answer == 6: 
    print("Je ne peux pas vous donner une réponse. Posez une autre question!")
elif answer == 7: 
    print("Très drôle, bien sûr que non!")
elif answer == 8: 
    print("Pas vraiment!")
else: 
    print("Ce n'est pas une question! Vous conaissez déjà la réponse.")   
print("Merci pour vos question")