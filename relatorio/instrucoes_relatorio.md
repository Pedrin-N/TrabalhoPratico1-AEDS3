# Instruções para o Relatório Final

## Estrutura Sugerida para o Relatório

Com base nos documentos gerados, aqui está a estrutura sugerida para o relatório final:

### 1. Introdução
- Objetivos do trabalho
- Descrição do problema do caminho mínimo
- Justificativa para escolha do algoritmo de Dijkstra

### 2. Fundamentação Teórica
- Conceitos básicos de grafos
- Algoritmo de Dijkstra: princípios e funcionamento
- Complexidade computacional teórica
- Pseudocódigo do algoritmo

### 3. Metodologia
- Descrição da implementação
- Estruturas de dados utilizadas
- Configuração dos experimentos
- Métricas coletadas

### 4. Implementação
- **Usar conteúdo de**: `relatorio/documentacao_implementacao.md`
- Detalhes da implementação
- Correspondência com o pseudocódigo
- Estrutura do código

### 5. Experimentos Computacionais
- **Usar conteúdo de**: `relatorio/analise_resultados.md`
- Configuração dos testes
- Resultados obtidos
- Análise dos dados

### 6. Análise dos Resultados
- **Usar conteúdo de**: `relatorio/analise_resultados.md`
- Interpretação dos resultados
- Comparação com complexidade teórica
- Identificação de tendências

### 7. Conclusões
- Principais descobertas
- Limitações identificadas
- Recomendações para melhorias
- Aplicabilidade prática

## Arquivos Gerados para o Relatório

### 1. `relatorio/documentacao_implementacao.md`
**Conteúdo:**
- Visão geral da implementação
- Estrutura do código
- Correspondência com pseudocódigo
- Funções auxiliares
- Estruturas de dados utilizadas
- Tratamento de casos especiais
- Complexidade computacional

**Seções recomendadas para o relatório:**
- Seção 4 (Implementação)
- Parte da Seção 3 (Metodologia)

### 2. `relatorio/analise_resultados.md`
**Conteúdo:**
- Resumo executivo
- Metodologia dos experimentos
- Resultados detalhados
- Análise de tempo, memória e custo
- Comparação com limites
- Conclusões e recomendações

**Seções recomendadas para o relatório:**
- Seção 5 (Experimentos Computacionais)
- Seção 6 (Análise dos Resultados)
- Seção 7 (Conclusões)

### 3. `experiments/results.csv`
**Conteúdo:**
- Dados brutos dos experimentos
- Métricas coletadas para cada grafo

**Uso no relatório:**
- Tabelas de resultados
- Gráficos de performance
- Análise estatística

## Dados dos Experimentos

### Resultados Principais

| Grafo | Vértices | Arestas | T.médio (s) | M.média (MB) | Custo médio |
|-------|----------|---------|-------------|--------------|-------------|
| toy.txt | 5 | 7 | 0.000030 | 0.000391 | 2.50 |
| facebook_combined.txt | 4039 | 352936 | 0.518472 | 0.640234 | 3.70 |
| rg300_768.txt | 300 | 768 | 0.003492 | 0.002344 | 311.60 |
| rg300_4730.txt | 300 | 4730 | 0.005538 | 0.000391 | 14.30 |
| rome99c.txt | 3353 | 17718 | 0.337685 | 0.507031 | 15101.70 |
| USA-road-dt.DC.txt | 9559 | 78754 | 2.905804 | 0.559375 | 6399.10 |

### Principais Descobertas

1. **Performance**: Algoritmo muito eficiente, processando grafos com milhares de vértices em segundos
2. **Memória**: Uso muito baixo (máximo 0.64MB), adequado para sistemas com recursos limitados
3. **Escalabilidade**: Funciona bem até grafos com ~10.000 vértices
4. **Confiabilidade**: 100% de taxa de sucesso em todos os testes

### Limitações Identificadas

1. Complexidade O(V²) devido ao uso de lista simples
2. Performance pode degradar em grafos muito densos
3. Não otimizado para grafos com mais de 10.000 vértices

## Elementos Visuais Sugeridos

### 1. Gráficos de Performance
- Tempo de execução vs. número de vértices
- Uso de memória vs. número de vértices
- Comparação entre diferentes tipos de grafos

### 2. Tabelas Comparativas
- Resultados por tipo de grafo
- Análise de complexidade
- Comparação com limites estabelecidos

### 3. Diagramas
- Fluxograma do algoritmo
- Estrutura de dados utilizada
- Arquitetura do sistema

## Código para Incluir no Relatório

### 1. Implementação Principal
```python
def dijkstra(graph: Graph, source: int) -> Tuple[Dict[int, float], Dict[int, Optional[int]]]:
    # Implementação completa do algoritmo
```

### 2. Exemplo de Uso
```bash
python main.py data/toy.txt 0 3
```

### 3. Resultado de Execução
```
Algoritmo de Dijkstra:
Caminho mínimo: [0, 2, 1, 3]
Custo: 5.0
Tempo execução: 0.000055 s
Memória utilizada: 0.003906 MB
```

## Checklist para o Relatório

### ✅ Implementação
- [x] Algoritmo de Dijkstra implementado conforme pseudocódigo
- [x] Estruturas de dados adequadas
- [x] Tratamento de casos especiais
- [x] Validação de entrada

### ✅ Experimentos
- [x] Script de testes implementado
- [x] 6 grafos diferentes testados
- [x] 10 execuções por grafo
- [x] Métricas de tempo, memória e custo coletadas

### ✅ Análise
- [x] Resultados processados
- [x] Análise de performance realizada
- [x] Comparação com limites estabelecidos
- [x] Conclusões extraídas

### ✅ Documentação
- [x] README completo
- [x] Documentação da implementação
- [x] Análise dos resultados
- [x] Instruções de uso

## Próximos Passos

1. **Compor o relatório final** usando os documentos gerados
2. **Adicionar elementos visuais** (gráficos, diagramas)
3. **Revisar e formatar** conforme padrões da disciplina
4. **Incluir código relevante** no relatório
5. **Adicionar referências bibliográficas** se necessário

## Arquivos Finais do Projeto

- `src/graph.py` - Classe Graph
- `src/dijkstra.py` - Implementação do algoritmo
- `main.py` - Programa principal
- `experiments/run_tests.py` - Script de experimentos
- `experiments/results.csv` - Resultados dos testes
- `requirements.txt` - Dependências
- `README.md` - Documentação do projeto
- `relatorio/` - Documentos para o relatório 