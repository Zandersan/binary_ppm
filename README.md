# 🖼️ Conversão de Imagem PPM (P6) para Escala de Cinza e Binária

Este projeto em Python realiza a leitura de uma imagem no formato **PPM P6 (binário)** e gera duas novas imagens:

- ✅ Uma versão em **tons de cinza**
- ✅ Uma versão **binarizada** (preto e branco)

O destaque aqui é que **nenhuma biblioteca externa** é utilizada — todo o processamento é feito com recursos nativos da linguagem, ideal para fins educativos ou ambientes com restrições de dependências.

---

## 📂 Entrada

- `debinha_coberta.ppm` (formato **P6** — binário)

---

## 🛠️ Saídas

- `debinha_cinza.ppm` — imagem convertida para escala de cinza
- `debinha_binaria.ppm` — imagem convertida para preto e branco com limiar (threshold) 128

---

## 📌 Como funciona

1. Lê o cabeçalho da imagem PPM (`P6`, largura, altura e valor máximo de cor)
2. Lê os bytes RGB da imagem
3. Converte para tons de cinza com a fórmula:
4. Converte para imagem binária usando um limiar fixo (128):
- Pixels com valor ≥ 128 tornam-se brancos (`255`)
- Pixels com valor < 128 tornam-se pretos (`0`)

---

## ▶️ Executando

Coloque o arquivo `debinha_coberta.ppm` no mesmo diretório do script e execute:

```bash
python conversao_ppm.py
