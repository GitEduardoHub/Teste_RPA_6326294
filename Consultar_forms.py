import pandas as pd


def calcular_media_e_status(aluno):
  try:
    n1 = float(aluno["Nota01"])
    n2 = float(aluno["Nota02"])
    t1 = float(aluno["TF01"])
    t2 = float(aluno["TF02"])

    media = (n1 + n2 + t1 + t2) / 4.0
    status = "Aprovado" if media >= 7.0 else "Reprovado"
    return round(media, 2), status
  except (ValueError, KeyError):
    return 0.0, "Erro nos dados"


def carregar_dados():
  try:
    # sep=';' é necessário pois o arquivo foi gerado com ponto e vírgula
    # dtype={'RA': str} garante que o RA seja tratado como texto (preserva zeros e formatação)
    df = pd.read_csv("notas_organizadas.csv", sep=";", dtype={"RA": str})
    # Remove eventuais espaços nas bordas do RA
    df["RA"] = df["RA"].astype(str).str.strip()
    return df
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

    # 1. Busca exata
    resultado = df_alunos[df_alunos["RA"] == ra_input]

    # 2. Se não encontrar de primeira, busca flexível
    if resultado.empty:
      termo_busca = ra_input.upper().replace("RA", "").replace("-", "").strip()
      ra_limpo_csv = (
          df_alunos["RA"].str.upper().str.replace("RA", "").str.replace("-", "")
      )
      resultado = df_alunos[
          (ra_limpo_csv == termo_busca)
          | (ra_limpo_csv.str.lstrip("0") == termo_busca.lstrip("0"))
          | (df_alunos["RA"].str.startswith(ra_input))
          | (ra_limpo_csv.str.startswith(termo_busca))
      ]

    # Exibe o resultado se o aluno foi encontrado
    if not resultado.empty:
      aluno = resultado.iloc[0].to_dict()

      # Chamando a função de cálculo de média e status
      media, status = calcular_media_e_status(aluno)

      print("\n" + "=" * 42)
      print(" BOLETIM DO ALUNO")
      print("=" * 42)
      print(f"RA    : {aluno['RA']}")
      print(f"Nome  : {aluno['Nome']}")
      print(f"Nota01: {aluno['Nota01']} | Nota02: {aluno['Nota02']}")
      print(f"TF01  : {aluno['TF01']}   | TF02  : {aluno['TF02']}")
      print("-" * 42)
      print(f"Média Final : {media}")
      print(
          f"Situação    :"
          f" {'[APROVADO]' if status == 'Aprovado' else '[REPROVADO]'}"
      )
      print("=" * 42 + "\n")
    else:
      print(f"\n[AVISO] Nenhum aluno foi encontrado com o RA '{ra_input}'.\n")


if __name__ == "__main__":
  main()
