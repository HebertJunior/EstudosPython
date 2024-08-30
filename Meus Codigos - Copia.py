#contar vogais
vogais = ["a","e","i","o","u"]
frase = input("Digite uma palavra:    ").lower()
c = 0

for vogal in vogais:
    c += frase.count(vogal)

print(c)