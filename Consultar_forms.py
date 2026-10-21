import pandas as pd


def calcular_media_e_status(aluno):
  try:
    n1 = float(aluno["nota1"])
    n2 = float(aluno["nota2"])
    t1 = float(aluno["tf1"])
    t2 = float(aluno["tf2"])

    media = (n1 + n2 + t1 + t2) / 4.0
    status = "Aprovado" if media >= 7.0 else "Reprovado"
    return round(media, 2), status
  except ValueError:
    return 0.0, "Erro nos dados"


def carregar_dados():
  try:
    # Quando tiver o CSV pronto, basta usar:
    # return pd.read_csv('alunos_notas.csv', dtype={'ra': str})

    dados_alunos = [
        {
            "ra": "2026001",
            "nome": "Ana Silva",
            "nota1": "8.5",
            "nota2": "9.0",
            "tf1": "7.5",
            "tf2": "8.0",
        },
        {
            "ra": "2026002",
            "nome": "Carlos Souza",
            "nota1": "7.0",
            "nota2": "6.5",
            "tf1": "8.0",
            "tf2": "7.0",
        },
        {
            "ra": "2026003",
            "nome": "Mariana Lima",
            "nota1": "9.2",
            "nota2": "8.8",
            "tf1": "9.0",
            "tf2": "9.5",
        },
    ]
    return pd.DataFrame(dados_alunos)
  except Exception as e:
    print(f"Erro ao carregar os dados: {e}")
    return None


def main():
  df_alunos = carregar_dados()
  if df_alunos is None:
    return

  print("=== SISTEMA DE CONSULTA DE NOTAS POR RA ===")
  print("Dica: Digite 'sair' a qualquer momento para encerrar.\n")

  while True:
    ra_input = input("Digite o RA que deseja consultar: ").strip()

    if ra_input.lower() == "sair":
      print("Encerrando o sistema de consulta. Até logo!")
      break

    resultado = df_alunos[df_alunos["ra"] == str(ra_input)]

    if not resultado.empty:
      aluno = resultado.iloc[0].to_dict()

      # Chamando a função de cálculo de média e status
      media, status = calcular_media_e_status(aluno)

      print("\n" + "=" * 42)
      print(" BOLETIM DO ALUNO")
      print("=" * 42)
      print(f"RA    : {aluno['ra']}")
      print(f"Nome  : {aluno['nome']}")
      print(f"Nota01: {aluno['nota1']} | Nota02: {aluno['nota2']}")
      print(f"TF01  : {aluno['tf1']}   | TF02  : {aluno['tf2']}")
      print("-" * 42)
      print(f"Média Final : {media}")
      print(
          f"Situação    :"
          f" {'🟢 APROVADO' if status == 'Aprovado' else '🔴 REPROVADO'}"
      )
      print("=" * 42 + "\n")
    else:
      print(
          f"\n[AVISO] Nenhum aluno foi encontrado com o RA '{ra_input}'.\n"
      )


if __name__ == "__main__":
  main()