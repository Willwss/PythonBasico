import json

with open("faturamento.json", "r") as f:
    faturamento = json.load(f)

    menor_faturamento = min(faturamento.values())
    maior_faturamento = max(faturamento.values())

    dias_com_faturamento = [valor for valor in faturamento.values() if valor > 0]
    media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

    dias_acima_da_media = sum(1 for valor in dias_com_faturamento if valor > media_mensal)

    print(f"Menor faturamento: R${menor_faturamento:.2f}")
    print(f"Maior faturamento: R${maior_faturamento:.2f}")
    print(f"Média mensal de faturamento: R${media_mensal:.2f}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")