# Análise dos Resultados - Algoritmo de Floyd-Warshall

## Resumo Executivo

Este documento apresenta a análise dos resultados que seriam obtidos através da execução do algoritmo de Floyd-Warshall em diferentes grafos de teste. A análise foi adaptada a partir de um estudo prévio com o algoritmo de Dijkstra, ajustando as expectativas de performance e uso de recursos para refletir a natureza do Floyd-Warshall, um algoritmo de caminhos mínimos para todos os pares.

## Metodologia

A metodologia de experimentos foi mantida para fins de comparação teórica.

### Configuração dos Experimentos
- **Número de execuções por grafo**: 10
- **Timeout**: 600 segundos (10 minutos)
- **Limite de memória**: 8GB
- **Seed para reprodutibilidade**: 42

### Grafos Testados
- **toy.txt**: Grafo pequeno para verificação manual (5 vértices, 7 arestas)
- **facebook_combined.txt**: Conexões entre perfis do Facebook (4039 vértices)
- **rg300_768.txt**: Grafo aleatório com 300 vértices e 768 arestas
- **rg300_4730.txt**: Grafo aleatório com 300 vértices e 4730 arestas
- **rome99c.txt**: Mapa das estradas de Roma em 1999 (3353 vértices)
- **USA-road-dt.DC.txt**: Mapa das estradas de Washington DC (9559 vértices)

## Resultados Detalhados (Análise Teórica)

A tabela abaixo apresenta uma **estimativa teórica** do comportamento do algoritmo de Floyd-Warshall, contrastando com os resultados empíricos de um algoritmo de fonte única como Dijkstra.

| Grafo | T.médio (s) (Estimativa) | M.média (MB) (Estimativa) | Custo médio | Taxa de Sucesso (Estimativa) |
| :--- | :--- | :--- |