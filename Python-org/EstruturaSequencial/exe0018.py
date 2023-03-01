"""Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em
Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)."""

tamanho = float(input("Digite o tamanho do arquivo em MegaBytes: MB "))
velocidade = float(input("Qual a velocidade da internet? Mb/s "))
download = tamanho / (velocidade / 8)
print(f"um arquivo de {tamanho:.0f} MegaBytes vai levar {download/60:.2f} minutos para fazer o download.")
