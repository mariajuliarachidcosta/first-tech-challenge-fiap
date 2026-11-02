# Olist: crescimento, logística e retenção

Análise do Brazilian E-Commerce Public Dataset by Olist, para o Tech Challenge da Fase 1 (FIAP Pós-Tech em Data Analytics).

## Como reproduzir

1. Crie e ative um ambiente virtual com Python 3.x, depois instale as dependências:
   `pip install -r requirements.txt`
2. Rode os notebooks **nesta ordem**, com o diretório de trabalho na pasta `notebooks/`:

| Ordem | Notebook | Gera |
|---|---|---|
| 1 | `01_preparacao_dados.ipynb` | `data/processed/base_pedidos.csv`, `base_pedidos_entregues.csv` |
| 2 | `02_crescimento.ipynb` | tabelas e gráficos de crescimento |
| 3 | `03_logistica.ipynb` | tabelas e gráficos de logística |
| 4 | `04_satisfacao_recompra.ipynb` | tabelas e gráficos de recompra |
| 5 | `05_diagnostico_nota_baixa.ipynb` | `reports/tabelas/metricas_modelo_nota_baixa.csv` |
| 6 | `06_numeros_relatorio.ipynb` | `reports/tabelas/numeros_relatorio.csv` (depende do 05) |
| 7 | `07_previsao_nota_baixa.ipynb` | `reports/tabelas/modelo_preditivo_metricas.csv` (depende só do 01) |

## Estrutura

- `data/raw/`: CSVs originais do Kaggle (não versionados)
- `data/processed/`: bases tratadas (geradas pelo notebook 01)
- `notebooks/`: análises e `utils.py` (funções e constantes compartilhadas)
- `reports/figures/` e `reports/tabelas/`: saídas usadas no relatório

## Decisões de método

| Tema | Decisão | Onde |
|---|---|---|
| Período | jan/2017 a ago/2018 | notebook 01, seção 10 |
| Pedido válido (crescimento e recompra) | sem cancelados ou indisponíveis, com itens | notebooks 02, 04, 06 |
| Base de satisfação e atraso | entregues com nota de avaliação | notebooks 03, 05, 06, 07 |
| Datas incoerentes | excluídas das análises logísticas (flag `excluir_logistica`) | notebook 01, seção 9 |
| Entregue sem data | excluído da logística, não preenchido com zero | notebook 01, seção 9 |
| Nota do pedido | a mais recente, quando há mais de uma avaliação | notebook 01, seção 6 |
| Recompra | cliente com 2 ou mais pedidos válidos, por `customer_unique_id` | notebook 04 |
| Coorte | mês da primeira compra, alinhado por cliente | notebook 04 |
| Previsão antes da compra | divisão temporal; limiar escolhido na validação | notebook 07 |

## Limitações conhecidas

A base não identifica transportadoras. Por isso, a análise de transporte é feita por estado de destino e por vendedor.