# Définition de num1 et num2 en dehors de la boucle
num1 = 0
num2 = 0

# Fonction pour l'addition
def addition(a, b):
    return a + b

# Fonction pour la soustraction
def soustraction(a, b):
    return a - b

# Fonction pour la multiplication
def multiplication(a, b):
    return a * b

# Fonction pour la division
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Attention, division par 0 !"

# Boucle principale
while True:
    # Demander à l'utilisateur d'entrer les nombres
    num1 = float(input("Entrez le premier nombre : "))
    num2 = float(input("Entrez le deuxième nombre : "))

    # Demander à l'utilisateur l'opération qu'il veut faire
    operation = input("Quel opération voulez-vous effectuer ? (+, -, *, /)")

    if operation == "+":
        # Effectuer l'addition
        result = addition(num1, num2)
    elif operation == "-":
        # Effectuer la soustraction
        result = soustraction(num1, num2)
    elif operation == "*":
        # Effectuer la multiplication
        result = multiplication(num1, num2)
    else :
        # Effectuer la division
        result = division(num1, num2)
    
    # Afficher le résultat
    print("Résultat : ", result)
    
    # Demander à l'utilisateur s'il souhaite continuer
    user_choice = input("Voulez-vous effectuer une autre opération ? (oui/non) ")
    
    # Vérifier la réponse de l'utilisateur
    if user_choice.lower() != "oui":
        break
