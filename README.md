# Análise de Redes de Votação na Câmara dos Deputados
> Esse foi um trabalho da disciplina M0412 de 2025 ministrada pelo professor João Meidanis (meidanis@unicamp.br)
> 
> Autores: Heigon (h217638@dac.unicamp.br) e Augusto (a265679@dac.unicamp.br)

Este projeto utiliza técnicas de **Análise de Redes (Grafo)** e o **Algoritmo de Detecção de Comunidades de Louvain** para mapear e analisar a afinidade de voto entre os deputados federais brasileiros.

O objetivo é identificar grupos de deputados que votam de forma semelhante (comunidades) e quantificar a polarização política com base em dados de votação abertos.

## Objetivo

  * Construir um **grafo bipartido** (deputados vs. votações) usando dados públicos da Câmara dos Deputados.
  * Projetar esse grafo em um **grafo de afinidade** (deputados apenas), onde o peso da aresta representa a quantidade de vezes que dois deputados votaram juntos ('Sim' ou 'Não').
  * Aplicar o algoritmo de **Louvain** para detectar comunidades (blocos de voto) dentro do Congresso Nacional.
  * Analisar a modularidade e a coesão das comunidades para inferir o grau de alinhamento e polarização.

## Tecnologias e Bibliotecas

  * **Python 3.x**
  * **pandas:** Manipulação e processamento de dados tabulares.
  * **networkx:** Criação, manipulação e análise de estruturas de grafos.
  * **matplotlib:** Visualização de dados e grafos.
  * **python-louvain:** Implementação do algoritmo de Louvain para detecção de comunidades.

## Dados

Os dados brutos são obtidos diretamente dos **Dados Abertos da Câmara dos Deputados**.

O notebook está configurado para baixar e processar os votos e votações dos anos de **2019 a 2022**.

  * **Fonte:** [Câmara dos Deputados - Dados Abertos](https://dadosabertos.camara.leg.br/)
  * **Filtro:** A análise foca apenas em votações que tiveram **mais de 250 votos**, garantindo que apenas proposições relevantes e bem participadas sejam consideradas.

## Estrutura do Projeto

1.  **Download dos Dados:** Baixa os arquivos CSV de votações e votos dos anos definidos.
2.  **Pré-processamento:** Concatena, limpa e normaliza os dados de voto (`Sim`, `Não`, `Outro`).
3.  **Criação do Grafo Bipartido:**
      * Nós: Deputados e Votações.
      * Arestas: Conexão entre um Deputado e uma Votação, ponderada pelo tipo de voto.
4.  **Projeção do Grafo:** Criação do grafo de afinidade onde cada nó é um Deputado e o peso da aresta é o número de vezes que votaram de forma idêntica.
5.  **Análise de Comunidades:**
      * Aplica-se o Louvain para particionar o grafo.
      * A análise é repetida com diferentes filtros de peso mínimo (e.g., peso $\geq 1000$) para testar a robustez das comunidades.
6.  **Visualização:** Gera gráficos de rede coloridos por **Partido** e por **Comunidade detectada** para cada cenário de filtro.

## Resultados (Exemplo)

Após a execução, o projeto gera arquivos GraphML e imagens (PNG) que visualizam a estrutura de afinidade:

  * **Grafo Bipartido:** `votacoes_bipartite_colorida_acima_250.graphml`
  * **Análise por Filtro:** Para cada filtro de peso aplicado:
      * Relatório de modularidade e número de comunidades.
      * `grafo_partido.png`: Visualização do grafo com nós coloridos por partido.
      * `grafo_comunidades.png`: Visualização do grafo com nós coloridos pelas comunidades detectadas pelo Louvain.

> *A modularidade alta indica que as conexões de afinidade são densas dentro das comunidades, mas esparsas entre elas, sugerindo uma forte polarização ou alinhamento de blocos.*

## Como Rodar

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/heigon77/M0412
    cd M0412
    ```

2.  **Instale as dependências (se necessário):**

    Crie e ative um ambiente virtual (recomendado):

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

    Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

3.  **Execute o notebook principal:**
    Abra o arquivo `projeto.ipynb` em um ambiente Jupyter e execute as células sequencialmente. O processo incluirá o download automático dos dados e a geração dos grafos e visualizações.