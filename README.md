# 🚀 CVM Data Pipeline: Uma Jornada em Big Data com PySpark

## 📌 Visão Geral do Projeto

Este projeto foi desenvolvido como um estudo prático e intensivo sobre Engenharia de Dados e Analytics utilizando dados reais da Comissão de Valores Mobiliários (CVM) referentes a janeiro de 2024.

O objetivo foi construir um pipeline completo seguindo a Arquitetura Medallion, saindo do dado bruto até a geração de insights estratégicos de mercado.

---

## 🏗️ Arquitetura do Pipeline (Medallion)

O projeto está organizado em três camadas lógicas, cada uma com uma responsabilidade clara:

### 🟫 Camada Bronze (Raw)

Ingestão dos dados brutos em formato `.csv`, extraídos via API e convertidos para **Parquet com compressão Snappy**, garantindo melhor desempenho e otimização de armazenamento.

### ⬜ Camada Silver (Cleansing)

Fase de higienização dos dados.
Foram identificados **567.834 valores nulos** na coluna `ID_SUBCLASSE`.

Optou-se pela preservação dos valores `NULL` para assegurar que as agregações de negócio permanecessem tecnicamente precisas e não enviesassem análises financeiras.

### 🟨 Camada Gold (Analytics)

Criação de tabelas analíticas voltadas para consumo e geração de insights estratégicos, como:

* 📈 Market Share
* 📊 Volatilidade

A volatilidade foi calculada a partir do desvio padrão do patrimônio líquido:

$$
\sigma = \sqrt{\frac{1}{N - 1} \sum_{i=1}^{N} \left(x_i - \bar{x}\right)^2}
$$

---

## 🧠 Principais Aprendizados

Este projeto não foi apenas sobre código, mas principalmente sobre **tomada de decisão arquitetural**.

**Processamento Distribuído:**
Compreensão prática de como o Spark distribui tarefas entre múltiplos núcleos para processar milhões de linhas em segundos.

**Qualidade de Dados vs. Regra de Negócio:**
Discernimento entre quando preencher valores nulos na camada Silver e quando preservá-los para evitar distorções analíticas na camada Gold.

**Segurança e DevSecOps:**
Implementação de boas práticas com uso de GitHub Secrets e tokens para upload de dados via Google Colab, garantindo que credenciais sensíveis não fossem expostas no código.

**Git Flow Profissional:**
Trabalho com branches (`camada-medallion`) no GitHub, assegurando que a branch `main` permanecesse estável enquanto novas funcionalidades eram desenvolvidas.

---

## 🛠️ Tecnologias e Ferramentas

* **Linguagem:** Python
* **Framework de Big Data:** PySpark
* **Armazenamento:** Apache Parquet (Snappy Compression)
* **Ambiente de Nuvem:** Google Colab & Google Drive
* **Visualização:** Plotly Express
* **Versionamento:** Git & GitHub (Secrets & Branching)

---

## 📊 Insights Extraídos (Jan/2024)

**Fluxo de Capital:**
O mês de janeiro apresentou um saldo líquido positivo de **R$ 109 bilhões**, indicando um forte movimento de entrada na indústria de fundos.

**Concentração de Risco:**
A classe FI (Fundo de Investimento) demonstrou domínio no mercado, enquanto classes como FAPI apresentaram maior sensibilidade a resgates no início do ano.

---

## 👤 Autora

**Letycia Locha**
Engenheira de Dados em Construção

🔗 Meu GitHub
