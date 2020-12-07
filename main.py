"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    # COLOQUE SEU CÓDIGO AQUI
H = float(input("Qual sua altura?"))
HH = 72.7 * H - 58
HM = 62.1 * H - 44.7
print(f"Se você for homem o seu peso ideal é {HH}.")
print(f"Se você for mulher o seu peso ideal é {HM}.")

if __name__ == '__main__':
    main()
