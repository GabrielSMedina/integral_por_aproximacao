
# 📊 Integral por Aproximação

Este projeto foi desenvolvido para representar visualmente e explorar métodos geométricos para resolver integrais definidas. Utilizando conceitos matemáticos e computacionais, o objetivo principal foi criar uma ferramenta didática para demonstrar a aplicação de métodos numéricos em Python.

---

## 🎯 **Objetivo**

Inicialmente, o objetivo era ilustrar visualmente métodos geométricos para o cálculo de integrais. Durante o desenvolvimento, os métodos foram explorados de forma mais abrangente, culminando em um projeto que implementa e compara diferentes abordagens numéricas. O resultado é um sistema modular e interativo, ideal para estudantes e profissionais que desejam compreender e aplicar esses métodos.

---

## 🧮 **Conceitos Matemáticos**

### **1. Método dos Retângulos**
- **Ideia:** Divide-se o intervalo da integral em pequenos subintervalos, e a área é aproximada somando áreas de retângulos.
- **Fórmula:**
  ∫ab​f(x)dx≈i=1∑n​f(xi​)⋅Δx
- **Visualização:** Aproxima a integral como blocos retangulares sob a curva.

### **2. Método dos Trapézios**
- **Ideia:** Cada subintervalo é tratado como um trapézio, usando médias lineares.
- **Fórmula:**
  ∫ab​f(x)dx≈2Δx​i=1∑n​[f(xi​)+f(xi+1​)
- **Visualização:** Cria uma aproximação mais precisa ao conectar os pontos na curva.

### **3. Método de Simpson**
- **Ideia:** Divide o intervalo em subintervalos pares e aproxima a curva com parábolas.
- **Fórmula:**
  ∫ab​f(x)dx≈3Δx​i=1∑n/2​[f(x2i−2​)+4f(x2i−1​)+f(x2i​)]
- **Visualização:** Utiliza segmentos parabólicos para representar áreas.

### **4. Método de Monte Carlo**
- **Ideia:** Utiliza números aleatórios para calcular uma aproximação estatística.
- **Fórmula:**
  ∫ab​f(x)dx≈(b−a)⋅n1​i=1∑n​f(xi​)
- **Visualização:** Pontos aleatórios são gerados no intervalo para estimar a área.

---

## 🛠️ **Tecnologias Utilizadas**

- **Python**: Linguagem principal.
- **Bibliotecas**:
  - `numpy`: Operações matemáticas e vetoriais.
  - `matplotlib`: Visualização gráfica.
  - `random`: Para o método de Monte Carlo.

---

## 🚀 **Como Executar**

1. Clone o repositório:
   ```bash
   git clone https://github.com/GabrielSMedina/integral_por_aproximacao.git
   ```
2. Instale as dependências (se necessário):
   ```bash
   pip install numpy matplotlib
   ```
3. Navegue até o diretório do projeto:
   ```bash
   cd integral_por_aproximacao
   ```
4. Execute o arquivo principal:
   ```bash
   python main.py
   ```
5. Visualize os resultados no terminal e nos gráficos gerados.

---

## 📊 **Exemplo de Visualização**

### **Método dos Retângulos**
![Método dos Retângulos]()

### **Método de Simpson**
![Método de Simpson]()

---

## 📌 **Possíveis Melhorias**

- Expandir os métodos numéricos para outras formas de aproximação (como Gaussiana).
- Criar uma interface gráfica para interação mais intuitiva.
- Implementar validação automatizada de precisão com integrais conhecidas.

---

## 🤝 **Contribuições**

Contribuições são bem-vindas! Caso tenha sugestões ou encontre problemas, abra uma _issue_ ou envie um _pull request_.

---

## 📝 **Licença**

Este projeto é de uso acadêmico e não possui licença formal.

---

**Autor:** Gabriel S. Medina  
**Repositório:** [Integral por Aproximação](https://github.com/GabrielSMedina/integral_por_aproximacao)
