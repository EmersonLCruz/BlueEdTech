# Peça ao usuário uma palavra, coloque todas as letras em caixa baixa e, depois, cada vogal na palavra deve ser convertido para letra maiúscula.

palavra = input("Digite uma palavra: ").lower()
palavra_modificada = ''
for letra in palavra:
    if letra in 'aeiou':
        palavra_modificada += letra.upper()
    else:
        palavra_modificada += letra

print(palavra_modificada)