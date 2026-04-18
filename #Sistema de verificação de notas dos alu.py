#Sistema de verificação de notas dos alunos
def calcular_media(notas):
    """Calcula a média de uma lista de notas."""
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)
def verificar_situação(media):
    """Define a situação do aluno baseada na média."""
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperação"
    else:
        return "Reprovado"
def main ():
    print("--- Sistema de Notas ---")
    #Exemplo de uso de estrutura de repetição e entrada de dados
    try:
        nome_aluno = input("Digite o nome do aluno:")
        n1 = float(input("Português: "))
        n2 = float(input("Matématica: "))
        n3 = float(input("Lógica de programação: "))

        notas = [n1, n2, n3]
        media = calcular_media(notas)
        situação = verificar_situação(media)

        #Uso de f-string para formatar a saída (2 casas decimais)
        print(f"\nAluno: {nome_aluno}")
        print(f"Média: {media:.2f}")
        print (f"Situação: {situação}")
    except ValueError:
        print("Erro: Por favor, digite valores numéricos válidos para as notas.")
if __name__ == "__main__":
    main()
