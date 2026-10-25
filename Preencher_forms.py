import time
import webbrowser
import pandas as pd
import pyautogui

# Configurações de segurança do PyAutoGUI
pyautogui.FAILSAFE = (
    True  # Jogue o mouse para o canto superior esquerdo para abortar se precisar
)
pyautogui.PAUSE = (
    0.8  # Pausa de 0.8 segundos entre as ações para garantir estabilidade
)

# 1. URL do seu Google Forms
url_forms = "https://docs.google.com/forms/d/e/1FAIpQLSfcVk0fxqrHIGqcbBNh0a_LL8GhO3D0hxUAFPi5UXhyZGncKg/viewform?fbzx=496525986591291896"

print("Abrindo o navegador com o formulário...")
webbrowser.open(url_forms)

print("Aguardando 5 segundos para o navegador carregar a página por completo...")
time.sleep(5)

# 2. Base de dados de exemplo atualizada com todos os campos solicitados
# Na sua aplicação real, você pode carregar de uma planilha usando: df = pd.read_excel('sua_planilha.xlsx')
# Recomendado usar o notas_organizadas.csv gerado pelo organizador.py:
df_alunos = pd.read_csv('notas_organizadas.csv', sep=';', dtype={'RA': str})


def preencher_formulario(ra, nome, nota1, nota2, tf1, tf2):
  # PASSO 1: Clicar no primeiro campo do formulário (RA)
  # (Substitua as coordenadas x e y abaixo pela posição exata do campo RA no seu monitor)
  pyautogui.click(x=713, y=545)
  pyautogui.hotkey("ctrl", "a")
  pyautogui.write(str(ra), interval=0.03)

  # PASSO 2: Ir para o campo Nome
  pyautogui.press("tab")
  pyautogui.hotkey("ctrl", "a")
  pyautogui.write(str(nome), interval=0.03)

  # PASSO 3: Ir para Nota01
  pyautogui.press("tab")
  pyautogui.hotkey("ctrl", "a")
  pyautogui.write(str(nota1), interval=0.03)

  # PASSO 4: Ir para Nota02
  pyautogui.press("tab")
  pyautogui.hotkey("ctrl", "a")
  pyautogui.write(str(nota2), interval=0.03)

  # PASSO 5: Ir para TF01
  pyautogui.press("tab")
  pyautogui.hotkey("ctrl", "a")
  pyautogui.write(str(tf1), interval=0.03)

  # PASSO 6: Ir para TF02
  pyautogui.press("tab")
  pyautogui.hotkey("ctrl", "a")
  pyautogui.write(str(tf2), interval=0.03)
  pyautogui.press("pgdn")

  # PASSO 7: Clicar no botão "Enviar"
  # (Ajuste as coordenadas x e y para onde fica o botão Enviar na sua tela)
  pyautogui.click(x=596, y=763)
  time.sleep(2.5)  # Aguarda o Google Forms processar o envio

  # PASSO 8: Clicar no link "Enviar outra resposta" para limpar o formulário para o próximo aluno
  # (Ajuste as coordenadas x e y para a posição do link de reenvio)
  pyautogui.click(x=713, y=347)
  time.sleep(1.5)

# Executando a automação para cada linha da planilha
for _, aluno in df_alunos.iterrows():
  ra = str(aluno["RA"])
  nome = str(aluno["Nome"])
  nota1 = str(aluno["Nota01"])
  nota2 = str(aluno["Nota02"])
  tf1 = str(aluno["TF01"])
  tf2 = str(aluno["TF02"])

  print(
      f"Processando RA: {ra} - {nome} | Notas: {nota1}, {nota2} | TFs: {tf1},"
      f" {tf2}"
  )
  preencher_formulario(ra, nome, nota1, nota2, tf1, tf2)

  

print(
    "Processo concluído com sucesso! Todas as informações foram enviadas e"
    " aparecem na planilha do Forms."
)