texto_ordem_saltos = ['Primeiro salto', 'Segundo salto', 'Terceiro salto', 'Quarto salto', 'Quinto salto']

saltos_atleta = [0.0, 0.0, 0.0, 0.0, 0.0]

atleta = input("Atleta: ")


if atleta != '':
    for c in range(0, 5):
        saltos_atleta[c] = float(input(f"{texto_ordem_saltos[c]}: "))

    media_saltos = (saltos_atleta[0] + saltos_atleta[1] + saltos_atleta[2] + saltos_atleta[3] + saltos_atleta[4])/5

    print("\nResultado final: ")
    print(f"Atleta: {atleta}")
    print(f"Saltos: {saltos_atleta[0]} - {saltos_atleta[1]} - {saltos_atleta[2]} - {saltos_atleta[3]} - {saltos_atleta[4]}")
    print(f"Média dos saltos: {media_saltos:} m")
