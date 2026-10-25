# 🤖 Automação RPA - Processamento, Envio e Consulta de Notas

Este repositório foi desenvolvido como parte de um **trabalho acadêmico de faculdade**, focado em automação de processos (**RPA - Robotic Process Automation**) e manipulação de dados com Python.

---

## 🎯 Objetivo do Projeto

O desafio consistiu em solucionar o seguinte fluxo:
1. **Recebimento e Tratamento de Dados:** Tratar uma base de dados (`notas.csv`) propositalmente corrompida/poluída contendo nomes de alunos, RAs e notas com inconsistências, campos vazios e caracteres despadronizados.
2. **Automação de Envio (RPA):** Automatizar o preenchimento de um formulário web (Google Forms vinculado à planilha de respostas) utilizando simulação de interface gráfica com o usuário via mouse e teclado.
3. **Bot de Consulta Interativa:** Criar uma ferramenta via terminal (linha de comando) para buscar a situação acadêmica e boletim de um aluno informando o seu RA, calculando a média e informando aprovação/reprovação.

---

## 📁 Estrutura de Arquivos

| Arquivo | Descrição |
| :--- | :--- |
| `notas.csv` | Arquivo CSV original com dados poluídos/inconsistentes (valores faltantes, textos em notas, etc.). |
| `organizador.py` | Script responsável por sanitizar e filtrar a base de dados original. |
| `notas_organizadas.csv` | Base limpa com dados válidos, pronta para ser processada pela automação. |
| `notas_com_problemas.csv` | Registros que apresentaram pendências/inconsistências (valores N/A, faltas, etc.). |
| `marcador_cordenadas.py` | Script auxiliar para capturar as coordenadas `(X, Y)` da tela com PyAutoGUI. |
| `Preencher_forms.py` | Bot RPA que abre o navegador e preenche o Google Forms com os dados limpos. |
| `Consultar_forms.py` | Bot de terminal que busca os dados do aluno por RA e exibe o boletim completo. |

---

## ⚙️ Fluxo de Funcionamento e Detalhes Técnicos

### 1. Limpeza e Tratamento de Dados (`organizador.py`)
O arquivo bruto `notas.csv` continha entradas irregulares (como `"FALTOU"`, vírgulas no lugar de pontos decimais, espaços extras, textos `"RA"` em campos numéricos e campos vazios). O script:
- Padroniza os RAs e nomes (capitalização e remoção de espaços desnecessários).
- Converte notas decimais trocando vírgulas por pontos e forçando tipagem numérica com `errors='coerce'`.
- Separa os dados em dois arquivos:
  - **`notas_organizadas.csv`**: Alunos com todas as notas e identificação válidas (ordenados alfabeticamente).
  - **`notas_com_problemas.csv`**: Linhas com informações faltantes ou inválidas para posterior auditoria.

### 2. Mapeamento de Coordenadas (`marcador_cordenadas.py`)
Um utilitário simples em `pyautogui` que aguarda 5 segundos para que o usuário posicione o cursor sobre os campos do formulário (primeiro campo, botão "Enviar", link de "Enviar outra resposta") e imprime a posição `(X, Y)`.

### 3. Automação de Preenchimento (`Preencher_forms.py`)
Utiliza as bibliotecas **`webbrowser`** e **`pyautogui`**:
- Abre o link do Google Forms no navegador padrão.
- Para cada registro de `notas_organizadas.csv`, clica nos campos correspondentes ou navega via `Tab`, preenchendo:
  - `RA`
  - `Nome`
  - `Nota01`
  - `Nota02`
  - `TF01`
  - `TF02`
- Clica no botão **Enviar** e, em seguida, em **"Enviar outra resposta"**, repetindo o ciclo até finalizar a base.
- Conta com `pyautogui.FAILSAFE = True` para parada emergencial movendo o mouse ao canto superior esquerdo da tela.

### 4. Bot de Consulta por RA (`Consultar_forms.py`)
Ferramenta interativa de linha de comando para consulta do boletim escolar:
- Lê `notas_organizadas.csv` garantindo integridade dos dados e tratamento de caracteres do RA.
- Realiza busca flexível (ignora prefixos "RA", hífens ou zeros à esquerda).
- Calcula automaticamente a média aritmética:
  $$\text{Média} = \frac{\text{Nota01} + \text{Nota02} + \text{TF01} + \text{TF02}}{4}$$
- Determina o status:
  - **Aprovado:** Média $\ge 7.0$
  - **Reprovado:** Média $< 7.0$

---

## 🚀 Como Executar

### Pré-requisitos
Certifique-se de ter o Python 3.8+ instalado e as bibliotecas necessárias:

```bash
pip install pandas numpy pyautogui
```

---

### Passo 1: Organizar e Limpar a Planilha
Execute o script organizador para gerar os arquivos `notas_organizadas.csv` e `notas_com_problemas.csv`:
```bash
python organizador.py
```

---

### Passo 2: (Opcional) Ajustar Coordenadas da Tela
Caso a resolução do monitor ou layout do navegador seja diferente, execute o marcador para calibrar as coordenadas no `Preencher_forms.py`:
```bash
python marcador_cordenadas.py
```

---

### Passo 3: Executar a Automação do Formulário
*Recomendação: Mantenha a tela desimpedida e evite mexer no mouse/teclado durante o preenchimento.*
```bash
python Preencher_forms.py
```

---

### Passo 4: Consultar Alunos via Terminal (CMD)
Para verificar as notas e o status de aprovação de qualquer aluno por RA:
```bash
python Consultar_forms.py
```
> **Dica:** Digite o RA desejado e pressione Enter. Para finalizar a consulta, digite `sair`.
