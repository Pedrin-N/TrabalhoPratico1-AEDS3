# Trabalho Prático 1 - Algoritmos de Caminho Mínimo

## Descrição

Este projeto implementa o algoritmo de Dijkstra para encontrar caminhos mínimos em grafos ponderados direcionados, conforme especificado no trabalho prático da disciplina CSI115 - Algoritmos e Estruturas de Dados III.

## Estrutura do Projeto

```
TrabalhoPratico1-AEDS3/
├── data/                   # Arquivos de grafos de teste
│   ├── toy.txt            # Grafo pequeno para verificação manual
│   ├── facebook_combined.txt
│   ├── rg300_768.txt
│   ├── rg300_4730.txt
│   ├── rome99c.txt
│   └── USA-road-dt.DC.txt
├── src/                    # Código fonte
│   ├── __init__.py
│   ├── graph.py           # Classe Graph para representação de grafos
│   └── dijkstra.py        # Implementação do algoritmo de Dijkstra
├── experiments/           # Scripts de experimentos
│   ├── run_tests.py       # Script para execução dos experimentos
│   └── results.csv        # Resultados dos experimentos
├── main.py                # Programa principal
├── requirements.txt       # Dependências do projeto
└── README.md             # Este arquivo
```

## Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd TrabalhoPratico1-AEDS3
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Uso

### Execução Individual

Para executar o algoritmo de Dijkstra em um grafo específico:

```bash
python main.py <arquivo_grafo> <vértice_origem> <vértice_destino>
```

**Exemplo:**
```bash
python main.py data/toy.txt 0 3
```

**Saída esperada:**
```
Processando ...
--------------------------------------------------------------------------------
Algoritmo de Dijkstra:
Caminho mínimo: [0, 2, 1, 3]
Custo: 5
Tempo execução: 0.003 s
Memória utilizada: 0.0005 MB
--------------------------------------------------------------------------------
```

### Execução dos Experimentos

Para executar todos os experimentos computacionais:

```bash
python experiments/run_tests.py
```

Este comando irá:
- Executar 10 testes para cada grafo disponível
- Calcular médias de tempo, memória e custo
- Gerar um arquivo CSV com os resultados
- Exibir um resumo dos resultados

## Formato dos Arquivos de Grafo

Os arquivos de grafo devem estar no formato DIMACS:

```
n_vertices n_edges
u v weight
u v weight
...
```

**Exemplo (toy.txt):**
```
5 7
0 1 6
0 2 2
1 3 1
1 4 3
2 1 2
2 3 5
3 4 3
```

## Implementação do Algoritmo de Dijkstra

A implementação segue rigorosamente o pseudocódigo fornecido:

```python
def dijkstra(graph: Graph, source: int) -> Tuple[Dict[int, float], Dict[int, Optional[int]]]:
    # Inicialização
    for v in V:
        dist[v] ← ∞
        prev[v] ← null
    dist[s] ← 0
    prev[s] ← s
    
    O ← V  # Conjunto de vértices abertos
    C ← ∅  # Conjunto de vértices fechados
    
    while C ≠ V:
        u ← vértice de O com dist[u] mínimo
        C ← C ∪ {u}
        O ← O − {u}
        
        for cada v vizinho de u tal que v ∉ C:
            if dist[v] > dist[u] + w(u, v):
                dist[v] ← dist[u] + w(u, v)
                prev[v] ← u
```

## Métricas Coletadas

Para cada execução, o programa coleta:

- **Tempo de execução**: Medido em segundos
- **Memória utilizada**: Medida em megabytes
- **Custo do caminho**: Soma dos pesos das arestas no caminho mínimo
- **Caminho mínimo**: Sequência de vértices do caminho

## Grafos de Teste

| Arquivo | Descrição |
|---------|-----------|
| toy.txt | Grafo pequeno para verificação manual |
| facebook_combined.txt | Conexões entre perfis do Facebook (4039 perfis) |
| rg300_768.txt | Grafo aleatório com 300 vértices e 768 arestas |
| rg300_4730.txt | Grafo aleatório com 300 vértices e 4730 arestas |
| rome99c.txt | Mapa das estradas de Roma em 1999 |
| USA-road-dt.DC.txt | Mapa das estradas de Washington DC |

## Resultados dos Experimentos

Os resultados são salvos em `experiments/results.csv` e incluem:

- Tempo médio de execução
- Memória média utilizada
- Custo médio do caminho
- Taxa de sucesso das execuções

## Limitações

- Timeout: 600 segundos (10 minutos) por execução
- Limite de memória: 8GB
- Casos que excedem esses limites são marcados como "TEMPO LIMITE" ou "MEMORIA EXCEDIDA"

## Dependências

- Python 3.7+
- psutil >= 5.8.0 (para monitoramento de memória)

## Autores

[Seu nome e informações do grupo]

## Data

[Data de entrega]
