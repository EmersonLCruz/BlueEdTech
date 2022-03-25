# Peça ao usuário uma palavra e exiba três mensagens, na primeira deve conter todas as letras digitadas na palavra, na segunda todos os números e na terceira o que não for nem letra e nem número.

palavra = input("Digite uma palavra (pode ter números e caractres especiais): ").lower()
palavra_letras = palavra_numeros = caracteres_especial = ""
for letra in palavra:
    if letra in 'abcdefghijklmnopqrstuvxyzw':
        palavra_letras += letra
    elif letra in '1234567890':
        palavra_numeros += letra
    else:
        caracteres_especial += letra

print(f"Todas as letras digitadas: {palavra_letras}")
print(f"Todos os números digitados: {palavra_numeros}")
print(f"Caracteres especiais digitados: {caracteres_especial}")