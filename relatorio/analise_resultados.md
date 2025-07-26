# Análise dos Resultados - Algoritmo de Dijkstra

## Resumo Executivo

Este documento apresenta a análise dos resultados obtidos através da execução do algoritmo de Dijkstra em diferentes grafos de teste, conforme especificado no trabalho prático da disciplina CSI115 - Algoritmos e Estruturas de Dados III.

## Metodologia

### Configuração dos Experimentos
- **Número de execuções por grafo**: 10
- **Timeout**: 600 segundos (10 minutos)
- **Limite de memória**: 8GB
- **Seed para reprodutibilidade**: 42

### Grafos Testados
1. **toy.txt**: Grafo pequeno para verificação manual (5 vértices, 7 arestas)
2. **facebook_combined.txt**: Conexões entre perfis do Facebook (4039 vértices, 352936 arestas)
3. **rg300_768.txt**: Grafo aleatório com 300 vértices e 768 arestas
4. **rg300_4730.txt**: Grafo aleatório com 300 vértices e 4730 arestas
5. **rome99c.txt**: Mapa das estradas de Roma em 1999 (3353 vértices, 17718 arestas)
6. **USA-road-dt.DC.txt**: Mapa das estradas de Washington DC (9559 vértices, 78754 arestas)

## Resultados Detalhados

### Tabela de Resultados

| Grafo | T.médio (s) | M.média (MB) | Custo médio | Taxa de Sucesso |
|-------|-------------|--------------|-------------|-----------------|
| Grafo pequeno para verificação manual | 0.000030 | 0.000391 | 2.50 | 10/10 |
| Conexões entre perfis do Facebook | 0.518472 | 0.640234 | 3.70 | 10/10 |
| Grafo aleatório com 300 vértices e 768 arestas | 0.003492 | 0.002344 | 311.60 | 10/10 |
| Grafo aleatório com 300 vértices e 4730 arestas | 0.005538 | 0.000391 | 14.30 | 10/10 |
| Mapa das estradas de Roma em 1999 | 0.337685 | 0.507031 | 15101.70 | 10/10 |
| Mapa das estradas de Washington DC | 2.905804 | 0.559375 | 6399.10 | 10/10 |

## Análise dos Resultados

### 1. Análise de Tempo de Execução

**Observações:**
- O algoritmo demonstra excelente performance em grafos pequenos (toy.txt: 0.000030s)
- Para grafos de tamanho médio (300 vértices), o tempo varia entre 0.003s e 0.006s
- Grafos maiores como Facebook (4039 vértices) levam aproximadamente 0.5s
- O grafo de Washington DC (9559 vértices) é o mais demorado com ~2.9s

**Tendências identificadas:**
- O tempo de execução cresce de forma não-linear com o número de vértices
- A densidade do grafo (número de arestas) tem impacto significativo no tempo
- O algoritmo mantém eficiência mesmo em grafos com milhares de vértices

### 2. Análise de Uso de Memória

**Observações:**
- Uso de memória muito baixo em todos os casos (máximo 0.64MB)
- Não há correlação direta entre tamanho do grafo e uso de memória
- O grafo do Facebook, apesar de ser o maior em número de vértices, não é o que mais consome memória

**Tendências identificadas:**
- O algoritmo é muito eficiente em termos de memória
- A implementação não escala linearmente com o tamanho do grafo
- Memória utilizada permanece constante independente do tamanho do grafo

### 3. Análise de Custo dos Caminhos

**Observações:**
- Custos variam significativamente entre os grafos
- Grafos de redes sociais (Facebook) têm custos baixos (3.70)
- Grafos de mapas de estradas têm custos muito altos (Roma: 15101.70, DC: 6399.10)
- Grafos aleatórios apresentam custos intermediários

**Tendências identificadas:**
- Custos refletem a natureza do grafo (social vs. geográfico)
- Grafos densos tendem a ter caminhos mais curtos
- Grafos esparsos podem ter caminhos mais longos

### 4. Taxa de Sucesso

**Observações:**
- 100% de sucesso em todos os grafos testados
- Nenhum timeout ou erro de memória foi registrado
- O algoritmo é robusto e confiável

## Complexidade Computacional

### Análise Teórica vs. Prática

**Complexidade teórica do Dijkstra:**
- Tempo: O(V²) para implementação com lista simples
- Espaço: O(V) para armazenar distâncias e predecessores

**Observações práticas:**
- Performance real é melhor que O(V²) para grafos esparsos
- Uso de memória é muito eficiente
- O algoritmo escala bem até grafos com ~10.000 vértices

## Comparação com Limites Estabelecidos

### Timeout (600s)
- Nenhum teste excedeu o limite de 10 minutos
- Maior tempo: 2.9s (Washington DC)
- Margem de segurança: ~207x menor que o limite

### Limite de Memória (8GB)
- Nenhum teste excedeu o limite de 8GB
- Maior uso: 0.64MB (Facebook)
- Margem de segurança: ~12.500x menor que o limite

## Conclusões

1. **Eficiência**: O algoritmo de Dijkstra implementado é muito eficiente, processando grafos com milhares de vértices em segundos.

2. **Escalabilidade**: O algoritmo escala bem até grafos com aproximadamente 10.000 vértices sem problemas de performance.

3. **Confiabilidade**: 100% de taxa de sucesso em todos os testes, demonstrando robustez.

4. **Uso de Recursos**: Uso de memória muito baixo, tornando o algoritmo adequado para sistemas com recursos limitados.

5. **Aplicabilidade**: O algoritmo é adequado para aplicações práticas em grafos de tamanho realista.

## Recomendações

1. **Para grafos maiores**: Considerar implementações otimizadas com heap binário para melhor performance.

2. **Para aplicações em tempo real**: O algoritmo atual é adequado para grafos com até 10.000 vértices.

3. **Para análise de redes sociais**: O algoritmo é ideal devido à baixa densidade típica desses grafos.

4. **Para sistemas embarcados**: O baixo uso de memória torna o algoritmo adequado para dispositivos com recursos limitados.

## Limitações Identificadas

1. **Grafos muito grandes**: Para grafos com mais de 10.000 vértices, pode ser necessário otimizações adicionais.

2. **Grafos densos**: Em grafos muito densos, a performance pode degradar significativamente.

3. **Implementação atual**: Usa lista simples para encontrar o mínimo, podendo ser otimizada com estruturas de dados mais eficientes.

## Próximos Passos

1. Implementar versão otimizada com heap binário
2. Testar com grafos ainda maiores
3. Comparar com outros algoritmos de caminho mínimo
4. Otimizar para casos específicos (grafos muito esparsos ou muito densos) 