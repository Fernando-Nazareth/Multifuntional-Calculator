# Multifuntional-Calculator
Este repositório contém uma calculadora multifuncional desenvolvida em Python. A calculadora oferece várias funcionalidades, como:

- **Operações matemáticas básicas (soma, subtração, multiplicação, divisão)**
- **Cálculo de Índice de Massa Corporal (IMC)**
- **Cálculo de média de uma lista de números**
- **Conversão de temperaturas (Celsius, Fahrenheit, Kelvin)**

## Funcionalidades

**Calculadora Básica:**
Realiza operações matemáticas básicas: soma (+), subtração (-), multiplicação (*), divisão (/).
Tratamento de erros, como divisão por zero.

**Cálculo de IMC:**
Calcula o Índice de Massa Corporal com base no peso (em kg) e altura (em metros).

**Cálculo de Média:**
Calcula a média aritmética de uma lista de números inserida pelo usuário.

**Conversões:**
Conversão entre unidades de temperatura: Celsius, Fahrenheit e Kelvin.

## Estrutura do Projeto
O projeto é modular, com cada funcionalidade dividida em arquivos separados para melhor organização.
Veja a estrutura dos arquivos:

```kotlin
calculadora-multifuncional/
│
├── main.py                  # Arquivo principal que chama as funções
├── imc.py                   # Função de cálculo de IMC
├── media.py                 # Função de cálculo de média
├── calculadora.py           # Funções da calculadora básica
├── conversoes.py            # Funções de conversões (temperatura, etc.)
└── README.md                # Documentação do projeto
```

## Como Executar
Siga os passos abaixo para clonar o repositório e rodar a calculadora localmente.


**1. Clonar o Repositório**

No terminal, clone o repositório para o seu ambiente local:

```bash
git clone https://github.com/seu-usuario/calculadora-multifuncional.git
```


**2. Acessar o Diretório**

Navegue até o diretório do projeto:

```bash
cd calculadora-multifuncional
```


**3. Executar o Script**

Você pode rodar o arquivo main.py para utilizar a calculadora:

```bash
python main.py
```


**4. Usar as Funcionalidades**

O programa irá apresentar um menu interativo onde você pode escolher a operação que deseja realizar:

1: Calculadora Normal (operações básicas)

2: Calcular IMC

3: Calcular Média

4: Conversões

0: Sair


**5. Exemplo de Uso**

**Operação Básica**
```less
Digite o primeiro número: 10
Escolha a operação (+, -, *, /): +
Digite o segundo número: 5
Resultado: 15
```

**Cálculo de IMC**
```java
Digite o peso (kg): 70
Digite a altura (m): 1.75
Seu IMC é: 22.86
```

**Cálculo de Média**
```yaml
Quantos números você quer calcular a média? 3
Digite o número 1: 10
Digite o número 2: 20
Digite o número 3: 30
A média é: 20.00
```

## Requisitos
Python 3.11 instalado na sua máquina.

## Contribuindo
Se você quiser contribuir com este projeto, siga as etapas abaixo:

Faça um fork do projeto
Crie uma branch para a sua feature (git checkout -b minha-feature)
Faça commit das suas alterações (git commit -m 'Adicionar nova feature')
Envie para o repositório remoto (git push origin minha-feature)
Abra um Pull Request

## Licença
Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.
