# Manual do Aluno - BitDogLab V7

## Seu Laboratório Portátil de Computação Física

<p align="center">
  <img src="./img/bitdoglab_logo.png" alt="Logo da BitDogLab" width="200">
</p>

> **"A melhor forma de aprender é fazendo."**

---

## Índice

1. [Conhecendo sua Placa](#1-conhecendo-sua-placa)
2. [Conheça os Componentes do Kit](#2-conheça-os-componentes-do-kit)
3. [Primeiros Passos](#3-primeiros-passos)
4. [LED RGB - O Semáforo Inteligente](#4-led-rgb---o-semáforo-inteligente)
5. [Botões - O Teclado da Natureza](#5-botoes---o-teclado-da-natureza)
6. [Matriz de LEDs - Pintando com Luz](#6-matriz-de-leds---pintando-com-luz)
7. [Buzzer - A Voz da Placa](#7-buzzer---a-voz-da-placa)
8. [Display OLED - A Tela Mágica](#8-display-oled---a-tela-mágica)
9. [Joystick - O Controle Universal](#9-joystick---o-controle-universal)
10. [Microfone - Ouça o Mundo](#10-microfone---ouça-o-mundo)
11. [Projeto Integrador: Cidade Inteligente](#11-projeto-integrador-cidade-inteligente)

---

## 1. Conhecendo sua Placa

A BitDogLab é uma placa educacional que reúne vários periféricos em um único lugar. Pense nela como um **kit de brinquedos eletrônicos** onde cada componente conta uma história diferente!

### Mapa da Placa

```
┌─────────────────────────────────────────────┐
│                                             │
│    ┌─────────┐    ┌─────────────────┐       │
│    │ DISPLAY │    │   MATRIZ 5x5    │       │
│    │  OLED   │    │    de LEDs      │       │
│    └─────────┘    └─────────────────┘       │
│                                             │
│         ● LED RGB    ⊕ JOYSTICK             │
│                                             │
│    [A] Botão A    [B] Botão B              │
│                                             │
│    🔊 Buzzer      🎤 Microfone              │
│                                             │
│              [USB]                          │
└─────────────────────────────────────────────┘
```

### Periféricos e suas "Personalidades"

| Periférico | O que é | Analogia do mundo real |
|------------|---------|------------------------|
| **LED RGB** | Luz colorida | O semáforo da sua rua |
| **Botões** | Comandos manuais | As teclas do seu celular |
| **Matriz 5x5** | Mini tela de LED | A tela do velho Game Boy |
| **Buzzer** | Alto-falante miniatura | O campainha da escola |
| **Display OLED** | Tela que mostra texto | O painel do seu relógio |
| **Joystick** | Controle direcional | O analógico do controle de videogame |
| **Microfone** | Captura som | O ouvido do seu assistente virtual |

---

## 2. Conheça os Componentes do Kit

Antes de programar, vamos entender **o que tem dentro da sua BitDogLab** e como cada componente funciona no mundo real!

### Visão Geral do Kit

```
┌────────────────────────────────────────────────────────────────┐
│                     BITDOGLAB V7                                │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│   ┌──────────┐     ┌──────────────────┐     ┌──────────┐      │
│   │  DISPLAY │     │   MATRIZ 5x5     │     │  BOTÕES  │      │
│   │   OLED   │     │   NeoPixel       │     │ A  B  C  │      │
│   │  128x64  │     │   25 LEDs RGB    │     │          │      │
│   └──────────┘     └──────────────────┘     └──────────┘      │
│                                                                │
│   ┌──────────┐     ┌──────────────────┐     ┌──────────┐      │
│   │  JOYSTICK│     │    LED RGB       │     │  BUZZER  │      │
│   │ Analógico│     │   Vermelho       │     │  Sonoro  │      │
│   │ + Botão  │     │   Verde/Azul     │     │          │      │
│   └──────────┘     └──────────────────┘     └──────────┘      │
│                                                                │
│   ┌──────────┐     ┌──────────────────┐     ┌──────────┐      │
│   │MICROFONE │     │  RASPBERRY PI    │     │ CONECTORES│     │
│   │ Analógico│     │     PICO         │     │  Expansão │     │
│   └──────────┘     └──────────────────┘     └──────────┘      │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

### Componente 1: Raspberry Pi Pico (O cérebro)

A **Raspberry Pi Pico** é o microcontrolador que controla todos os outros componentes. Pense nela como o **cérebro** da BitDogLab!

| Característica | Especificação |
|----------------|---------------|
| **Processador** | RP2040 (ou RP2350 na Pico 2) |
| **Frequência** | 133 MHz |
| **Memória Flash** | 2 MB |
| **RAM** | 264 KB |
| **GPIO** | 26 pinos de uso geral |
| **Linguagem** | MicroPython ou C/C++ |

**No mundo real:** É como o processador do seu celular, mas em versão miniatura e mais simples!

```
┌─────────────────────────────────┐
│      RASPBERRY PI PICO          │
│                                 │
│  ┌─────┐          ┌─────┐       │
│  │BOOT │          │RESET│       │
│  │ SEL │          │     │       │
│  └─────┘          └─────┘       │
│                                 │
│  ┌─────────────────────────┐    │
│  │      RP2040/RP2350      │    │
│  │    (Processador)        │    │
│  └─────────────────────────┘    │
│                                 │
│  [USB]              [Pinos]     │
│                                 │
└─────────────────────────────────┘
```

**Função do botão BOOTSEL:**
- Usado para instalar o firmware
- Pressione + conecte USB = modo de gravação
- Para programas normais, NÃO pressione este botão!

---

### Componente 2: LED RGB (O artista das cores)

O **LED RGB** pode produzir **milhares de cores** combinando vermelho, verde e azul!

| Pino | Cor | Função |
|------|-----|--------|
| GPIO13 | Vermelho | Alertas, perigos |
| GPIO11 | Verde | Sucesso, normal |
| GPIO12 | Azul | Informação, calma |

**Como funciona a mistura de cores:**

```
Vermelho + Verde = Amarelo
Vermelho + Azul = Magenta
Verde + Azul = Ciano
Vermelho + Verde + Azul = Branco
Nenhum = Apagado
```

**Aplicações no mundo real:**
- 🚦 Semáforos
- 💡 Indicadores de status (bateria, Wi-Fi)
- 🎨 Iluminação decorativa
- ⚠️ Sistemas de alarme

**Exercício:** Quais cores você pode criar? Experimente!

---

### Componente 3: Matriz de LEDs 5x5 (A tela em miniatura)

A **matriz NeoPixel** tem 25 LEDs que podem ser controlados **individualmente**!

| Característica | Valor |
|----------------|-------|
| **Quantidade** | 25 LEDs (5x5) |
| **Tipo** | WS2812B (NeoPixel) |
| **Pino** | GPIO7 |
| **Cores** | RGB (16 milhões de cores!) |

**Mapa da matriz:**

```
Posições da matriz (0-24):
┌───┬───┬───┬───┬───┐
│ 0 │ 1 │ 2 │ 3 │ 4 │  ← Linha 0
├───┼───┼───┼───┼───┤
│ 5 │ 6 │ 7 │ 8 │ 9 │  ← Linha 1
├───┼───┼───┼───┼───┤
│10 │11 │12 │13 │14 │  ← Linha 2
├───┼───┼───┼───┼───┤
│15 │16 │17 │18 │19 │  ← Linha 3
├───┼───┼───┼───┼───┤
│20 │21 │22 │23 │24 │  ← Linha 4
└───┴───┴───┴───┴───┘
```

**Aplicações no mundo real:**
- 🕹️ Telas de jogos retrô
- 📊 Gráficos e animações
- 😊 Emojis e expressões faciais
- 🗺️ Mapas e setas de direção

**Exercício:** Desenhe uma seta apontando para a direita usando a matriz!

---

### Componente 4: Botões (O teclado da placa)

A BitDogLab tem **4 botões** para interação!

| Botão | Pino | Uso Comum |
|-------|------|-----------|
| **A** | GPIO5 | Confirmar, selecionar |
| **B** | GPIO6 | Cancelar, voltar |
| **C** | GPIO10 | Função especial |
| **Joystick** | GPIO22 | Pressionar joystick |

**Como funcionam:**
```
Botão pressionado = valor 0 (LOW)
Botão solto = valor 1 (HIGH)

Isso acontece porque usamos resistores PULL_UP internos.
```

**Aplicações no mundo real:**
- 🎮 Controles de videogame
- 📱 Botões do celular
- 🚪 Botões de elevador
- ⏰ Alarmes e temporizadores

**Exercício:** Crie um "botão de emergência" que ativa um alarme!

---

### Componente 5: Display OLED (A tela que mostra texto)

O **display OLED** mostra texto e gráficos em preto e branco!

| Característica | Valor |
|----------------|-------|
| **Resolução** | 128x64 pixels |
| **Tamanho** | 0.96 polegadas |
| **Comunicação** | I2C |
| **Pinos** | SDA=GPIO2, SCL=GPIO3 |

**Configuração I2C:**

```python
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

# Configuração correta para BitDogLab V7
i2c = I2C(1, scl=Pin(3), sda=Pin(2), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)
```

**Aplicações no mundo real:**
- 📱 Telas de celulares
- ⌚ Displays de relógios inteligentes
- 📊 Monitores de saúde (pulso, oxímetro)
- 🖥️ Painéis de carros

**Exercício:** Mostre seu nome no display!

---

### Componente 6: Joystick (O controle direcional)

O **joystick analógico** detecta movimento em **duas direções**!

| Característica | Valor |
|----------------|-------|
| **Eixo X** | GPIO27 (esquerda/direita) |
| **Eixo Y** | GPIO26 (cima/baixo) |
| **Botão** | GPIO22 (pressionar) |
| **Faixa** | 0 a 65535 |

**Mapa de movimento:**

```
           CIMA (Y baixo)
              │
              │
ESQUERDA ─────┼───── DIREITA
(X baixo)     │      (X alto)
              │
           BAIXO (Y alto)

Centro: X≈32768, Y≈32768
```

**Aplicações no mundo real:**
- 🎮 Controles de videogame
- 🤖 Controle de robôs
- 📹 Controle de câmeras
- 🚁 Controle de drones

**Exercício:** Mova um LED pela matriz usando o joystick!

---

### Componente 7: Buzzer (A voz da placa)

O **buzzer** produz sons e melodias!

| Característica | Valor |
|----------------|-------|
| **Pino** | GPIO21 |
| **Tipo** | Piezoelétrico |
| **Frequência** | 50 Hz a 20 kHz |

**Notas musicais e frequências:**

```python
# Escala de Dó Maior
notas = {
    'Dó (C)': 262,
    'Ré (D)': 294,
    'Mi (E)': 330,
    'Fá (F)': 349,
    'Sol (G)': 392,
    'Lá (A)': 440,
    'Si (B)': 494,
    'Dó (C2)': 523
}
```

**Aplicações no mundo real:**
- 🚨 Alarmes de emergência
- 📱 Sons de notificação
- 🎵 Brinquedos musicais
- ⏱️ Temporizadores

**Exercício:** Tocar "Parabéns pra você" no buzzer!

---

### Componente 8: Microfone (Ouvido da placa)

O **microfone** captura sons e ruídos do ambiente!

| Característica | Valor |
|----------------|-------|
| **Pino** | GPIO28 |
| **Tipo** | Analógico |
| **Faixa** | 0 a 65535 |

**Como ler o som:**

```python
from machine import Pin, ADC

mic = ADC(Pin(28))
centro = 32768  # Ponto médio (silêncio)

# Ler intensidade do som
valor = mic.read_u16()
intensidade = abs(valor - centro)  # Quanto mais alto, maior o valor
```

**Aplicações no mundo real:**
- 🎤 Gravação de áudio
- 🔊 Reconhecimento de voz
- 📊 Medidores de volume
- 🚨 Alarmes de som

**Exercício:** Faça o LED reagir ao som da sua voz!

---

### Componente 9: Conectores de Expansão (As portas de conexão)

A BitDogLab tem **conectores** para adicionar sensores e módulos externos!

| Barramento | Pinos | Uso |
|------------|-------|-----|
| **I2C0** | GPIO0 (SDA), GPIO1 (SCL) | Sensores externos |
| **I2C1** | GPIO2 (SDA), GPIO3 (SCL) | Display + expansão |
| **GPIO** | Vários | Botões, LEDs, etc. |

**Sensores compatíveis (comprados separadamente):**

| Sensor | O que mede | Exemplo de uso |
|--------|------------|----------------|
| **AHT20** | Temperatura e umidade | Estação meteorológica |
| **BH1750** | Luz ambiente | Lâmpada inteligente |
| **BME280** | Temperatura, umidade, pressão | Previsão do tempo |
| **MPU6050** | Movimento (acelerômetro) | Controle por gestos |
| **GPS** | Localização | Rastreador veicular |

**Exercício:** Conecte um sensor de temperatura e mostre a leitura no display!

---

### Tabela Resumo dos Pinos

| Periférico | Pino | Tipo |
|------------|------|------|
| LED RGB Vermelho | GPIO13 | Saída PWM |
| LED RGB Verde | GPIO11 | Saída PWM |
| LED RGB Azul | GPIO12 | Saída PWM |
| Matriz NeoPixel | GPIO7 | Saída Digital |
| Display SDA | GPIO2 | I2C |
| Display SCL | GPIO3 | I2C |
| Botão A | GPIO5 | Entrada |
| Botão B | GPIO6 | Entrada |
| Botão C | GPIO10 | Entrada |
| Buzzer | GPIO21 | Saída PWM |
| Joystick X | GPIO27 | Entrada Analógica |
| Joystick Y | GPIO26 | Entrada Analógica |
| Joystick Botão | GPIO22 | Entrada |
| Microfone | GPIO28 | Entrada Analógica |
| I2C Externo SDA | GPIO0 | I2C |
| I2C Externo SCL | GPIO1 | I2C |

---

### Glossário dos Componentes

| Termo | Significado |
|-------|-------------|
| **GPIO** | General Purpose Input/Output - Pinos de entrada/saída |
| **PWM** | Pulse Width Modulation - Modulação por largura de pulso |
| **I2C** | Interface de comunicação entre dispositivos |
| **ADC** | Analog-to-Digital Converter - Conversor analógico-digital |
| **NeoPixel** | LED RGB endereçável individualmente |
| **OLED** | Organic Light-Emitting Display - Tela orgânica |
| **MicroPython** | Linguagem Python para microcontroladores |

---

## 3. Primeiros Passos

### O que você vai precisar

- ☑️ Uma placa BitDogLab V7
- ☑️ Um cabo USB (o mesmo do carregador de celular Android)
- ☑️ Um computador com **Thonny IDE** ou **Visual Studio Code** instalado
- ☑️ Uma dose de curiosidade!

### Escolhendo seu Ambiente de Desenvolvimento

Você pode programar a BitDogLab usando duas opções principais:

| Ambiente | Indicado para | Vantagem |
|----------|---------------|----------|
| **Thonny** | Iniciantes | Simples, rápido de configurar |
| **VS Code** | Quer mais recursos | Autocompletar, depurador, extensões |

---

### Opção A: Thonny IDE (Recomendado para iniciantes)

#### Passo 1: Instalando a Thonny

Acesse: https://thonny.org/

Baixe e instale a versão para seu sistema operacional.

#### Passo 2: Configurando a Thonny

1. Abra a Thonny
2. Vá em `Tools > Options`
3. Na aba `Interpreter`, selecione:
   ```
   MicroPython (Raspberry Pi Pico)
   ```

#### Passo 3: Instalando o Firmware

1. **Desconecte** a placa do computador
2. Pressione e segure o botão **BOOTSEL** (na parte de trás)
3. Mantendo pressionado, **conecte** o cabo USB
4. Solte o botão quando a placa aparecer como disco `RPI-RP2`
5. Na Thonny, clique em `Install or update firmware`
6. Aguarde a instalação

---

### Opção B: Visual Studio Code com Plugin Raspberry Pi Pico

O VS Code é um editor mais robusto, ideal quem já tem alguma experiência ou quer recursos avançados como **autocompletar**, **depurador** e **terminal integrado**.

#### Passo 1: Instalando o VS Code

Acesse: https://code.visualstudio.com/

Baixe e instale a versão para seu sistema operacional.

#### Passo 2: Instalando o Plugin Raspberry Pi Pico

1. Abra o VS Code
2. Vá na aba de **Extensões** (ícone de blocos à esquerda) ou pressione `Ctrl+Shift+X`
3. Pesquise por: `Raspberry Pi Pico`
4. Instale a extensão **"Raspberry Pi Pico"** (oficial da Raspberry Pi Foundation)

<p align="center">
  <em>Plugin oficial com suporte a MicroPython e CircuitPython</em>
</p>

#### Passo 3: Conectando a Placa

1. Conecte a BitDogLab ao computador via USB
2. Pressione `Ctrl+Shift+P` para abrir a paleta de comandos
3. Digite e selecione: `Pico: Connect`
4. Selecione a porta serial correspondente à placa
5. Escolha `MicroPython` como o framework

#### Passo 4: Instalando o Firmware (pelo VS Code)

1. Na paleta de comandos (`Ctrl+Shift+P`), digite: `Pico: Install Firmware`
2. Siga as instruções na tela
3. Se necessário, coloque a placa em modo bootloader (botão BOOTSEL + conectar USB)

#### Passo 5: Executando Código no VS Code

1. Crie um novo arquivo com extensão `.py`
2. Escreva seu código MicroPython
3. Para **executar na placa**:
   - Pressione `Ctrl+Shift+P` → `Pico: Run`
   - Ou use o botão "Run" na barra de ferramentas do plugin
4. Para **salvar na placa** como `main.py`:
   - Pressione `Ctrl+Shift+P` → `Pico: Upload`

#### Vantagens do VS Code

| Recurso | Descrição |
|---------|-----------|
| **Autocompletar** | Sugestões de código enquanto você digita |
| **Depurador** | Pare o código e inspecione variáveis |
| **Terminal integrado** | Execute comandos sem sair do editor |
| **Git integrado** | Controle de versão do seu código |
| **Múltiplos arquivos** | Organize projetos complexos |

---

### Passo 6: Seu Primeiro Programa!

Independentemente do ambiente escolhido, copie e cole este código:

```python
from machine import Pin, PWM
import time

# LED RGB: vermelho=13, verde=11, azul=12
r = PWM(Pin(13), freq=1000)
g = PWM(Pin(11), freq=1000)
b = PWM(Pin(12), freq=1000)

def cor(vr, vg, vb):
    r.duty_u16(vr * 257)
    g.duty_u16(vg * 257)
    b.duty_u16(vb * 257)

# Pisca vermelho como um alerta!
while True:
    cor(255, 0, 0)  # Vermelho
    time.sleep(0.5)
    cor(0, 0, 0)    # Desliga
    time.sleep(0.5)
```

Execute o código:
- **Thonny:** Clique no botão ▶️ **Run**
- **VS Code:** Pressione `Ctrl+Shift+P` → `Pico: Run`

> **Dica:** Salve como `main.py` para que execute automaticamente ao ligar a placa.
> - **Thonny:** `File > Save as... > Raspberry Pi Pico > main.py`
> - **VS Code:** `Ctrl+Shift+P` → `Pico: Upload` (o plugin pergunta o nome do arquivo)

---

## 4. LED RGB - O Semáforo Inteligente

### Conceito
O LED RGB funciona como as luzes de um semáforo: cada cor é controlada separadamente. Ao combinar vermelho, verde e azul, podemos criar **milhares de cores**!

### Exemplo 1: Semáforo Real

**Mundo real:** Todo dia você vê semáforos funcionando. Vamos programar o nosso!

```python
from machine import Pin, PWM
import time

# Configuração do LED RGB
r = PWM(Pin(13), freq=1000)
g = PWM(Pin(11), freq=1000)
b = PWM(Pin(12), freq=1000)

def cor(vr, vg, vb):
    r.duty_u16(vr * 257)
    g.duty_u16(vg * 257)
    b.duty_u16(vb * 257)

# Simulando um semáforo real
while True:
    # Vermelho: pare!
    cor(255, 0, 0)
    print("🔴 VERMELHO - Pare!")
    time.sleep(3)
    
    # Amarelo: atenção!
    cor(255, 180, 0)
    print("🟡 AMARELO - Atenção!")
    time.sleep(1)
    
    # Verde: siga!
    cor(0, 255, 0)
    print("🟢 VERDE - Siga!")
    time.sleep(3)
```

### Exemplo 2: Indicador de Bateria

**Mundo real:** Quando sua bateria está cheia, o led fica verde. Quando está acabando, fica vermelho.

```python
from machine import Pin, PWM
import time

r = PWM(Pin(13), freq=1000)
g = PWM(Pin(11), freq=1000)
b = PWM(Pin(12), freq=1000)

def cor(vr, vg, vb):
    r.duty_u16(vr * 257)
    g.duty_u16(vg * 257)
    b.duty_u16(vb * 257)

# Simulando indicador de bateria
baterias = [100, 75, 50, 25, 10, 5]

for nivel in baterias:
    print(f"Bateria: {nivel}%")
    
    if nivel > 60:
        cor(0, 255, 0)      # Verde: bateria boa
    elif nivel > 30:
        cor(255, 255, 0)    # Amarelo: médio
    else:
        cor(255, 0, 0)      # Vermelho: crítico!
    
    time.sleep(1)
```

### Exercício Criativo 🎨
> **Desafio:** Crie um "alarme de fogo" que pisca vermelho rapidamente e emite um som quando someone "aperta o botão" (simulando um detector de fumaça).

---

## 5. Botões - O Teclado da Natureza

### Conceito
Botões são a forma mais simples de **interação humano-máquina**. Pense em como você usa botões no dia a dia: elevador, micro-ondas, controle remoto...

### Exemplo 1: Contador de Pessoas

**Mundo real:** Portas automáticas que contam quantas pessoas entraram na sala.

```python
from machine import Pin
import time

botao = Pin(5, Pin.IN, Pin.PULL_UP)  # Botão A
contador = 0
antes = 1

print("=== Contador de Pessoas ===")
print("Aperte o botão para contar entradas")

while True:
    agora = botao.value()
    
    # Detecta quando o botão é pressionado (borda de descida)
    if antes == 1 and agora == 0:
        contador += 1
        print(f"Pessoas na sala: {contador}")
        time.sleep_ms(200)  # Debounce
    
    antes = agora
```

### Exemplo 2: Interruptor de Luz

**Mundo real:** Você aperta uma vez para ligar, aperta de novo para desligar.

```python
from machine import Pin, PWM
import time

botao = Pin(5, Pin.IN, Pin.PULL_UP)
led = PWM(Pin(13), freq=1000)
ligado = False
antes = 1

print("=== Interruptor Inteligente ===")
print("Aperte para ligar/desligar a luz")

while True:
    agora = botao.value()
    
    if antes == 1 and agora == 0:
        ligado = not ligado
        led.duty_u16(65535 if ligado else 0)
        print(f"Luz: {'ligada' if ligado else 'desligada'}")
        time.sleep_ms(200)
    
    antes = agora
```

### Exemplo 3: Seletor de Cores

**Mundo real:** Como as luzes de festa que mudam de cor quando você aperta um botão.

```python
from machine import Pin, PWM
import time

botao = Pin(5, Pin.IN, Pin.PULL_UP)
r = PWM(Pin(13), freq=1000)
g = PWM(Pin(11), freq=1000)
b = PWM(Pin(12), freq=1000)

cores = [
    (255, 0, 0),     # Vermelho
    (0, 255, 0),     # Verde
    (0, 0, 255),     # Azul
    (255, 255, 0),   # Amarelo
    (255, 0, 255),   # Magenta
    (0, 255, 255),   # Ciano
]
indice = 0
antes = 1

print("=== Seletor de Cores ===")
print("Aperte para mudar a cor!")

def definir_cor(c):
    r.duty_u16(c[0] * 257)
    g.duty_u16(c[1] * 257)
    b.duty_u16(c[2] * 257)

while True:
    agora = botao.value()
    
    if antes == 1 and agora == 0:
        definir_cor(cores[indice])
        print(f"Cor: {indice + 1}/{len(cores)}")
        indice = (indice + 1) % len(cores)
        time.sleep_ms(200)
    
    antes = agora
```

### Exercício Criativo 🎮
> **Desafio:** Crie um "botão de emergência" que, quando pressionado, faz o LED piscar em vermelho e o buzzer apitar.

---

## 6. Matriz de LEDs - Pintando com Luz

### Conceito
A matriz 5x5 é como uma **tela em miniatura**. Cada pixel pode ser控制ado individualmente para criar figuras, animações e mensagens.

### Exemplo 1: Coração Pulsante

**Mundo real:** Os emojis de coração que você manda no WhatsApp!

```python
from machine import Pin
import neopixel
import time

np = neopixel.NeoPixel(Pin(7), 25)

# Padrão do coração (5x5)
coracao = [2, 6, 8, 10, 14, 15, 19, 21, 23]

while True:
    # Acende o coração
    for led in coracao:
        np[led] = (40, 0, 0)  # Vermelho
    np.write()
    time.sleep(0.5)
    
    # Apaga
    for led in coracao:
        np[led] = (0, 0, 0)
    np.write()
    time.sleep(0.5)
```

### Exemplo 2: Setas de Direção

**Mundo real:** As setas que indicam onde virar no GPS do seu celular.

```python
from machine import Pin
import neopixel
import time

np = neopixel.NeoPixel(Pin(7), 25)

# Seta para direita
seta_direita = [
    0, 0, 0, 0, 0,
    0, 0, 0, 8, 0,
    0, 0, 8, 8, 8,
    0, 0, 0, 8, 0,
    0, 0, 0, 0, 0
]

# Seta para esquerda
seta_esquerda = [
    0, 0, 0, 0, 0,
    0, 6, 0, 0, 0,
    6, 6, 6, 0, 0,
    0, 6, 0, 0, 0,
    0, 0, 0, 0, 0
]

def mostrar_seta(padrao, cor):
    for i, valor in enumerate(padrao):
        np[i] = cor if valor else (0, 0, 0)
    np.write()

while True:
    # Pisca seta direita
    for _ in range(3):
        mostrar_seta(seta_direita, (0, 40, 0))  # Verde
        time.sleep(0.3)
        mostrar_seta(seta_direita, (0, 0, 0))
        time.sleep(0.3)
    
    time.sleep(0.5)
    
    # Pisca seta esquerda
    for _ in range(3):
        mostrar_seta(seta_esquerda, (40, 40, 0))  # Amarelo
        time.sleep(0.3)
        mostrar_seta(seta_esquerda, (0, 0, 0))
        time.sleep(0.3)
```

### Exemplo 3: Carinha Sorridente

**Mundo real:** As expressões faciais que usamos para comunicar emoções!

```python
from machine import Pin
import neopixel

np = neopixel.NeoPixel(Pin(7), 25)

# Padrão da carinha sorridente (5x5)
# 0=apagado, 1=azul (contorno), 2=ciano (olhos)
carinha = [
    0, 1, 1, 1, 0,
    1, 0, 0, 0, 1,
    1, 0, 0, 0, 1,
    1, 2, 0, 2, 1,
    0, 1, 1, 1, 0
]

cores = {
    0: (0, 0, 0),      # Apagado
    1: (0, 0, 30),     # Azul (contorno)
    2: (0, 30, 30)     # Ciano (olhos)
}

for i, valor in enumerate(carinha):
    np[i] = cores[valor]

np.write()
```

### Exercício Criativo 🕹️
> **Desafio:** Crie um jogo da velha onde cada jogador é um LED de cor diferente!

---

## 7. Buzzer - A Voz da Placa

### Conceito
O buzzer transforma **sinais elétricos em som**. É como a campainha da sua escola ou o alarme do celular!

### Exemplo 1: Escala Musical

**Mundo real:** As notas musicais que formam uma canção.

```python
from machine import Pin, PWM
import time

buzzer = PWM(Pin(21))

# Notas musicais (frequências em Hz)
notas = {
    'C': 262,  # Dó
    'D': 294,  # Ré
    'E': 330,  # Mi
    'F': 349,  # Fá
    'G': 392,  # Sol
    'A': 440,  # Lá
    'B': 494,  # Si
    'C2': 523  # Dó (oitava)
}

# Toca a escala
for nota, freq in notas.items():
    print(f"Tocando: {nota} ({freq} Hz)")
    buzzer.freq(freq)
    buzzer.duty_u16(9000)
    time.sleep_ms(250)
    buzzer.duty_u16(0)
    time.sleep_ms(60)
```

### Exemplo 2: Sirene de Ambulância

**Mundo real:** O som que avisa que uma ambulância está passando!

```python
from machine import Pin, PWM
import time

buzzer = PWM(Pin(21))

print("🚨 SIRENE DE AMBULÂNCIA 🚨")
print("Cuidado! Veículo de emergência!")

while True:
    # Sobe a frequência
    for freq in range(500, 1500, 40):
        buzzer.freq(freq)
        buzzer.duty_u16(8000)
        time.sleep_ms(10)
    
    # Desce a frequência
    for freq in range(1500, 500, -40):
        buzzer.freq(freq)
        buzzer.duty_u16(8000)
        time.sleep_ms(10)
```

### Exemplo 3: Código Morse - SOS

**Mundo real:** Como os marinheiros se comunicavam à distância!

```python
from machine import Pin, PWM
import time

buzzer = PWM(Pin(21))

def ponto():
    buzzer.freq(800)
    buzzer.duty_u16(9000)
    time.sleep_ms(100)
    buzzer.duty_u16(0)
    time.sleep_ms(100)

def traco():
    buzzer.freq(800)
    buzzer.duty_u16(9000)
    time.sleep_ms(300)
    buzzer.duty_u16(0)
    time.sleep_ms(100)

def letra_s():
    ponto()
    ponto()
    ponto()

def letra_o():
    traco()
    traco()
    traco()

print("📡 Enviando SOS em Morse...")
print("S: ... | O: --- | S: ...")

while True:
    letra_s()
    time.sleep(0.3)
    letra_o()
    time.sleep(0.3)
    letra_s()
    time.sleep(1)
```

### Exercício Criativo 🎵
> **Desafio:** Crie uma melodia simples usando as notas musicais. Dica: "Parabéns pra você" usa as notas: C C D C F E.

---

## 8. Display OLED - A Tela Mágica

### Conceito
O display OLED é uma **tela miniatura** que pode mostrar texto e gráficos. É como o painel do seu relógio digital!

### Exemplo 1: Mensagem Personalizada

**Mundo real:** O letreiro eletrônico que mostra informações.

```python
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

# Configuração do display
i2c = I2C(1, scl=Pin(3), sda=Pin(2), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

# Mensagens rotativas
mensagens = [
    "Bem-vindo!",
    "Aula de Robotica",
    "BitDogLab V7",
    "Vamos programar!"
]

while True:
    for msg in mensagens:
        oled.fill(0)
        oled.text(msg, 10, 25)
        oled.show()
        time.sleep(2)
```

### Exemplo 2: Relógio Simples

**Mundo real:** O relógio que você consulta a todo momento!

```python
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

i2c = I2C(1, scl=Pin(3), sda=Pin(2), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

# Simulando um relógio
horas = 14
minutos = 30

while True:
    oled.fill(0)
    oled.text("Relogio", 40, 5)
    oled.text(f"{horas:02d}:{minutos:02d}", 35, 25)
    oled.text("BitDogLab", 30, 50)
    oled.show()
    
    time.sleep(1)
    minutos += 1
    
    if minutos >= 60:
        minutos = 0
        horas += 1
    
    if horas >= 24:
        horas = 0
```

### Exemplo 3: Barra de Progresso

**Mundo real:** Quando você baixa um arquivo e vê a barra de progresso!

```python
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

i2c = I2C(1, scl=Pin(3), sda=Pin(2), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

while True:
    for largura in range(0, 101, 5):
        oled.fill(0)
        oled.text("Carregando", 22, 15)
        oled.rect(14, 35, 100, 10, 1)  # Borda da barra
        oled.fill_rect(14, 35, largura, 10, 1)  # Barra preenchida
        oled.text(f"{largura}%", 50, 50)
        oled.show()
        time.sleep_ms(120)
    
    time.sleep(1)
```

### Exercício Criativo 📊
> **Desafio:** Crie um "termômetro digital" que mostra a temperatura (use um sensor externo ou simule com o joystick).

---

## 9. Joystick - O Controle Universal

### Conceito
O joystick detecta **movimento em duas direções** (X e Y). É como o analógico do controle de videogame!

### Exemplo 1: Leitura de Direção

**Mundo real:** Como o GPS detecta sua direção no mapa!

```python
from machine import Pin, ADC
import time

x = ADC(Pin(27))
y = ADC(Pin(26))

print("=== Joystick como Bússola ===")
print("Mova o joystick para ver a direção!")

while True:
    valor_x = x.read_u16()
    valor_y = y.read_u16()
    
    # Calcula direção baseada nos eixos
    if valor_x < 20000:
        direcao = "ESQUERDA"
    elif valor_x > 45000:
        direcao = "DIREITA"
    elif valor_y < 20000:
        direcao = "CIMA"
    elif valor_y > 45000:
        direcao = "BAIXO"
    else:
        direcao = "CENTRO"
    
    print(f"X: {valor_x:5d} | Y: {valor_y:5d} | Direção: {direcao}")
    time.sleep_ms(200)
```

### Exemplo 2: Controle de Brilho

**Mundo real:** O controle de volume do celular - deslize para aumentar ou diminuir!

```python
from machine import Pin, ADC, PWM
import time

x = ADC(Pin(27))
led = PWM(Pin(13), freq=1000)

print("=== Controle de Brilho ===")
print("Mova o joystick para controlar o LED!")

while True:
    valor_x = x.read_u16()
    
    # Converte joystick para brilho (0-65535)
    brilho = valor_x
    
    led.duty_u16(brilho)
    
    # Mostra percentual
    percentual = int(valor_x * 100 / 65535)
    print(f"Brilho: {percentual}%")
    
    time.sleep_ms(100)
```

### Exemplo 3: Ponteiro no Display

**Mundo real:** O cursor do mouse que segue seu movimento!

```python
from machine import Pin, ADC, I2C
from ssd1306 import SSD1306_I2C
import time

x = ADC(Pin(27))
y = ADC(Pin(26))
i2c = I2C(1, scl=Pin(3), sda=Pin(2), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

print("=== Mouse Virtual ===")
print("Mova o joystick para mover o ponteiro!")

while True:
    # Mapeia joystick para tela (0-127, 0-63)
    px = 127 - (x.read_u16() * 127 // 65535)
    py = 63 - (y.read_u16() * 63 // 65535)
    
    oled.fill(0)
    oled.text("+", px, py)  # Ponteiro
    oled.text("Joystick", 30, 5)
    oled.show()
    
    time.sleep_ms(50)
```

### Exercício Criativo 🎮
> **Desafio:** Crie um mini-jogo onde você controla um LED pela matriz de LEDs usando o joystick!

---

## 10. Microfone - Ouça o Mundo

### Conceito
O microfone captura **ondas sonoras** e as converte em sinais elétricos. É como os microfones dos fones de ouvido!

### Exemplo 1: Medidor de Volume

**Mundo real:** Os medidores de volume dos estúdios de gravação!

```python
from machine import Pin, ADC
import time

mic = ADC(Pin(28))
centro = 32768  # Ponto médio (silêncio)

print("=== Medidor de Volume ===")
print("Faça barulho e veja o nível!")

while True:
    # Lê o microfone
    valor = mic.read_u16()
    
    # Calcula intensidade (distância do centro)
    intensidade = abs(valor - centro)
    
    # Mostra nível em barras
    nivel = int(intensidade / 1000)
    barra = "=" * nivel
    print(f"[{barra:20s}] Nível: {nivel}")
    
    time.sleep_ms(100)
```

### Exemplo 2: LED Reage ao Som

**Mundo real:** As luzes que dançam junto com a música em shows!

```python
from machine import Pin, ADC, PWM
import time

mic = ADC(Pin(28))
led = PWM(Pin(13), freq=1000)
centro = 32768

print("=== LED Dançante ===")
print("Toque uma música e veja o LED!")

while True:
    valor = mic.read_u16()
    intensidade = abs(valor - centro)
    
    # Converte intensidade para brilho do LED
    brilho = min(65535, intensidade * 4)
    
    led.duty_u16(brilho)
    time.sleep_ms(20)
```

### Exemplo 3: Alarme de Ruído

**Mundo real:** O alarme que toca quando alguém faz muito barulho!

```python
from machine import Pin, ADC, PWM
import time

mic = ADC(Pin(28))
buzzer = PWM(Pin(21))
led = PWM(Pin(13), freq=1000)
centro = 32768
limiar = 5000  # Limiar de alerta

print("=== Alarme de Ruído ===")
print(f"Acima de {limiar} = ALERTA!")

while True:
    valor = mic.read_u16()
    intensidade = abs(valor - centro)
    
    if intensidade > limiar:
        print(f"🚨 ALERTA! Nível: {intensidade}")
        buzzer.freq(1000)
        buzzer.duty_u16(8000)
        led.duty_u16(65535)
    else:
        buzzer.duty_u16(0)
        led.duty_u16(0)
    
    time.sleep_ms(100)
```

### Exercício Criativo 🎤
> **Desafio:** Crie um "aplausoômetro" que conta quantas vezes você bate palmas!

---

## 11. Projeto Integrador: Cidade Inteligente

Agora que você conhece todos os periféricos, vamos **combinar tudo** em um projeto real!

### Conceito
Uma **Cidade Inteligente** usa tecnologia para melhorar a vida dos cidadãos. Vamos simular:

- 🚦 Semáforo inteligente (LED RGB)
- 📊 Monitor de qualidade do ar (Microfone + Display)
- 🚨 Sistema de emergência (Botões + Buzzer)
- 🗺️ Mapa interativo (Matriz de LEDs + Joystick)

### Código do Projeto

```python
from machine import Pin, PWM, ADC, I2C
import neopixel
from ssd1306 import SSD1306_I2C
import time

# Configurações
led_r = PWM(Pin(13), freq=1000)
led_g = PWM(Pin(11), freq=1000)
led_b = PWM(Pin(12), freq=1000)
buzzer = PWM(Pin(21))
np = neopixel.NeoPixel(Pin(7), 25)
mic = ADC(Pin(28))
x = ADC(Pin(27))
y = ADC(Pin(26))
botao_a = Pin(5, Pin.IN, Pin.PULL_UP)
botao_b = Pin(6, Pin.IN, Pin.PULL_UP)
i2c = I2C(1, scl=Pin(3), sda=Pin(2), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

centro = 32768

def cor_rgb(r, g, b):
    led_r.duty_u16(r * 257)
    led_g.duty_u16(g * 257)
    led_b.duty_u16(b * 257)

def mostrar_display(linha1, linha2):
    oled.fill(0)
    oled.text(linha1, 0, 20)
    oled.text(linha2, 0, 35)
    oled.show()

# ===== MÓDULO 1: SEMÁFORO =====
def semaforo():
    mostrar_display("CIDADE", "SEMAFORO")
    
    while True:
        # Vermelho
        cor_rgb(255, 0, 0)
        mostrar_display("PARE", "Vermelho")
        time.sleep(3)
        
        # Amarelo
        cor_rgb(255, 180, 0)
        mostrar_display("ATENCAO", "Amarelo")
        time.sleep(1)
        
        # Verde
        cor_rgb(0, 255, 0)
        mostrar_display("SIGA", "Verde")
        time.sleep(3)
        
        if botao_a.value() == 0:
            break

# ===== MÓDULO 2: MONITOR DE SOM =====
def monitor_som():
    mostrar_display("MONITOR", "DE SOM")
    time.sleep(1)
    
    while True:
        valor = mic.read_u16()
        intensidade = abs(valor - centro)
        
        nivel = min(20, int(intensidade / 500))
        barra = "=" * nivel
        
        mostrar_display(f"Nivel: {nivel}", barra)
        
        # LED muda de cor com o volume
        if nivel > 15:
            cor_rgb(255, 0, 0)  # Vermelho = alto
        elif nivel > 8:
            cor_rgb(255, 255, 0)  # Amarelo = médio
        else:
            cor_rgb(0, 255, 0)  # Verde = baixo
        
        time.sleep_ms(100)
        
        if botao_a.value() == 0:
            break

# ===== MÓDULO 3: ALARME DE EMERGÊNCIA =====
def alarme():
    mostrar_display("ALARME", "DE EMERGENCIA")
    
    for i in range(25):
        np[i] = (40, 0, 0)  # Vermelho
    np.write()
    
    while True:
        cor_rgb(255, 0, 0)
        buzzer.freq(1000)
        buzzer.duty_u16(8000)
        time.sleep_ms(200)
        
        cor_rgb(0, 0, 0)
        buzzer.duty_u16(0)
        time.sleep_ms(200)
        
        if botao_b.value() == 0:
            buzzer.duty_u16(0)
            cor_rgb(0, 0, 0)
            for i in range(25):
                np[i] = (0, 0, 0)
            np.write()
            break

# ===== MÓDULO 4: MAPA INTERATIVO =====
def mapa():
    mostrar_display("MAPA", "INTERATIVO")
    time.sleep(1)
    
    # Mapa da cidade (5x5)
    mapa_cidade = [
        [1, 1, 1, 0, 0],
        [1, 0, 1, 0, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 1, 0, 1],
        [0, 0, 1, 1, 1]
    ]
    
    while True:
        # Posição do joystick
        pos_x = int(x.read_u16() * 4 / 65535)
        pos_y = int(y.read_u16() * 4 / 65535)
        
        for i in range(25):
            linha = i // 5
            coluna = i % 5
            
            if linha == pos_y and coluna == pos_x:
                np[i] = (40, 40, 40)  # Ponto atual (branco)
            elif mapa_cidade[linha][coluna] == 1:
                np[i] = (0, 40, 0)  # Rua (verde)
            else:
                np[i] = (0, 0, 0)  # Vazio
        
        np.write()
        
        mostrar_display(f"X:{pos_x} Y:{pos_y}", "Mova o joystick")
        
        time.sleep_ms(100)
        
        if botao_b.value() == 0:
            break

# ===== MENU PRINCIPAL =====
mostrar_display("CIDADE", "INTELIGENTE")
time.sleep(1)

while True:
    mostrar_display("Selecione:", "A=Menu B=Modo")
    
    if botao_a.value() == 0:
        # Menu de seleção
        opcoes = [semaforo, monitor_som, alarme, mapa]
        nomes = ["Semaforo", "Monitor", "Alarme", "Mapa"]
        indice = 0
        
        while True:
            mostrar_display(f"{indice+1}/{len(opcoes)}", nomes[indice])
            
            if botao_a.value() == 0:
                opcoes[indice]()
                break
            elif botao_b.value() == 0:
                indice = (indice + 1) % len(opcoes)
                time.sleep_ms(200)
            
            time.sleep_ms(100)
```

---

## 🏆 Desafios — Nota Final da Disciplina

Você já dominou cada periférico da BitDogLab e montou a Cidade Inteligente. Agora é hora de colocar tudo em prática! Os desafios abaixo são a **sua avaliação final** da disciplina de Robótica. Eles combinam **múltiplos componentes** e pedem que você pense como um verdadeiro engenheiro: identifique o problema, planeje a solução e crie um protótipo funcional.

**Como funciona:**
1. Escolha **um desafio** para trabalhar ao longo das últimas aulas
2. Desenvolva o projeto com a BitDogLab e, se necessário, componentes externos
3. Prepare uma **apresentação para as outras turmas da escola**, mostrando como seu projeto funciona e qual problema do mundo real ele resolve
4. A nota será avaliada com base na funcionalidade do projeto, na criatividade da solução e na qualidade da apresentação

Alguns desafios utilizam **componentes externos** que não fazem parte da placa. Nós vamos usar:

| Componente Externo | Modelo | Pinos GPIO | Função |
|---------------------|--------|------------|--------|
| Sonar Ultrassônico | HC-SR04 | Trig=GPIO17, Echo=GPIO16 | Mede distância sem contato (2cm a 400cm) |
| Servo Motor | SG90 | Sinal=GPIO15 | Gira de 0° a 180° com precisão |

> 💡 **Dica:** Antes de começar qualquer desafio, desenhe no papel como ficaria o circuito e quais periféricos da placa você vai usar. planejamento é a chave do sucesso!

---

### 🅿️ Desafio 1: Estacionamento Inteligente

**Nível:** ⭐⭐

**🌍 O contexto:** Você já foi a um shopping e ficou andando em círculos procurando vaga? Sistemas inteligentes de monitoramento de vagas usam sensores para mostrar em tempo real quais vagas estão livres. Empresas como a WPS (Worldwide Parking) usam exatamente essa tecnologia em aeroportos e centros comerciais.

**🎯 Objetivo:** Construa um sistema que detecta se há carro em uma vaga e mostra o status no display.

**Componentes utilizados:**
- Sonar HC-SR04 (Trig=GPIO17, Echo=GPIO16)
- LED RGB (R=GPIO13, G=GPIO11, B=GPIO12)
- Display OLED (SDA=GPIO2, SCL=GPIO3)

**Requisitos mínimos:**
1. O sonar mede a distância até o objeto à frente
2. Se distância < 20cm → vaga ocupada: LED vermelho + "OCUPADA" no OLED
3. Se distância ≥ 20cm → vaga livre: LED verde + "LIVRE" no OLED
4. Exiba a distância medida no display (ex: "Dist: 15cm")

**Dica de partida:**
```python
from machine import Pin, time_pulse_us
import time

trig = Pin(17, Pin.OUT)
echo = Pin(16, Pin.IN)

def medir_distancia():
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    tempo = time_pulse_us(echo, 1, 30000)
    distancia = (tempo * 0.0343) / 2
    return distancia
```

---

### 🚗 Desafio 2: Portão Automático de Garagem

**Nível:** ⭐⭐⭐

**🌍 O contexto:** Portões automáticos de garagem são comuns em condomínios e residências. Quando o carro se aproxima, o sistema detecta e abre o portão automaticamente — sem precisar sair do veículo. Empresas como a Nice e a Flexit usam essa tecnologia com sensores de presença.

**🎯 Objetivo:** Crie um portão que abre automaticamente quando um carro se aproxima e pode ser fechado manualmente.

**Componentes utilizados:**
- Sonar HC-SR04 (Trig=GPIO17, Echo=GPIO16)
- Servo Motor SG90 (Sinal=GPIO15)
- Buzzer (GPIO21)
- Botão A (GPIO5)

**Requisitos mínimos:**
1. O sonar monitora a distância continuamente
2. Se distância < 50cm → servo gira de 0° para 90° (portão abre)
3. Buzzer emite som de "bip" enquanto o portão está se movendo
4. Botão A fecha o portão (servo volta para 0°)
5. Exiba "PORTAO ABERTO" ou "PORTAO FECHADO" no OLED

**Dica de partida:**
```python
from machine import Pin, PWM
import time

servo = PWM(Pin(15))
servo.freq(50)

def mover_servo(angulo):
    # Mapeia 0-180 graus para duty_u16
    duty = int(angulo * 65535 / 180)
    servo.duty_u16(duty)
    time.sleep_ms(500)
    servo.duty_u16(0)  # Economiza energia
```

---

### 💧 Desafio 3: Monitor de Nível de Água

**Nível:** ⭐⭐

**🌍 O contexto:** Em fazendas e residências, controlar o nível da água no tanque é essencial. Sistemas como o da WEG e a Embrapa usam sensores ultrassônicos para monitorar caixas d'água, tanques de piscina e sistemas de irrigação — evitando transbordamento ou falta d'água.

**🎯 Objetivo:** Meça o nível de água em um tanque usando o sonar e exiba visualmente o resultado.

**Componentes utilizados:**
- Sonar HC-SR04 (Trig=GPIO17, Echo=GPIO16)
- Matriz de LEDs 5x5 (GPIO7)
- Buzzer (GPIO21)

**Requisitos mínimos:**
1. O sonar mede a distância até a superfície da água (quanto menor a distância, mais cheio o tanque)
2. A matriz de LEDs mostra uma barra vertical de nível (mais colunas acesas = mais água)
3. Se nível > 80% → buzzer emite alerta sonoro
4. Se nível < 20% → buzzer emite outro alerta (falta d'água)
5. Mapeie a distância para uma escala de 0% a 100%

**Dica de partida:**
```python
# Mapeamento: distancia max (tanque vazio) = 100%, min (tanque cheio) = 0%
def calcular_nivel(distancia, dist_max=100, dist_min=5):
    if distancia >= dist_max:
        return 0
    if distancia <= dist_min:
        return 100
    return int(((dist_max - distancia) / (dist_max - dist_min)) * 100)
```

---

### 🤖 Desafio 4: Robô de Limpeza Automático

**Nível:** ⭐⭐⭐

**🌍 O contexto:** Robôs aspiradores como o iRobot Roomba e o Xiaomi Mi Robot usam sensores para navegar autonomamente, desviando de obstáculos e mapeando o ambiente. É um dos exemplos mais fascinantes de robótica aplicada ao dia a dia.

**🎯 Objetivo:** Simule um robô aspirador que usa o sonar para detectar obstáculos e o servo motor para "espiar" os lados antes de desviar.

**Componentes utilizados:**
- Sonar HC-SR04 (Trig=GPIO17, Echo=GPIO16)
- Servo Motor SG90 (Sinal=GPIO15)
- Joystick (X=GPIO27, Y=GPIO26, Botão=GPIO22)
- Display OLED (SDA=GPIO2, SCL=GPIO3)

**Requisitos mínimos:**
1. Em modo automático: servo varre o sonar para esquerda (45°) e direita (135°) medindo distância
2. Se caminho da frente livre → avança (simula com mensagem no OLED "ANDANDO...")
3. Se obstáculo à frente → servo olha para os lados, escolhe o lado mais livre
4. Botão do joystick alterna entre modo automático e manual
5. No modo manual, joystick controla direção (frente, esquerda, direita, ré)

**Dica de partida:**
```python
def varredura():
    medicoes = {}
    for angulo in [45, 90, 135]:
        mover_servo(angulo)
        time.sleep_ms(300)
        medicoes[angulo] = medir_distancia()
    return medicoes
```

---

### 🚨 Desafio 5: Sistema de Alarme Antifurto

**Nível:** ⭐⭐⭐

**🌍 O contexto:** Sistemas de segurança residencial e comercial usam múltiplos sensores para detectar intrusões. Empresas como a Intelbras e a Positivo produzem alarmes que combinam detecção de som, movimento e luz para proteger lojas, escritórios e casas.

**🎯 Objetivo:** Crie um alarme que detecta sons suspeitos (estouro, quebra de vidro, batida forte) e dispara um alerta visual e sonoro.

**Componentes utilizados:**
- Microfone (GPIO28)
- Buzzer (GPIO21)
- Display OLED (SDA=GPIO2, SCL=GPIO3)
- Matriz de LEDs 5x5 (GPIO7)
- Botão A (GPIO5) — para ativar/desativar alarme
- Botão B (GPIO6) — para silenciar alarme

**Requisitos mínimos:**
1. Botão A liga/desliga o sistema (LED RGB azul = armado, apagado = desarmado)
2. Quando armado, microfone monitora o nível de som continuamente
3. Se som > 45000 (limiar configurável) → buzzer dispara alarme (sirene)
4. Matriz de LEDs pisca em vermelho durante o alarme
5. OLED mostra "ALARME!" e o horário (contador) do evento
6. Botão B silencia o alarme sem desarmar o sistema

**Dica de partida:**
```python
from machine import Pin, ADC
import time

microfone = ADC(Pin(28))
limiar_alarme = 45000

def detectar_som():
    leitura = microfone.read_u16()
    return leitura > limiar_alarme
```

---

### 💡 Desafio 6: Luminária Adaptiva de Rua

**Nível:** ⭐⭐

**🌍 O contexto:** Cidades inteligentes investem em iluminação pública que se adapta ao ambiente. Quando a rua está movimentada, a iluminação fica mais forte. Quando está vazia, reduz para economizar energia. São Paulo, Curitiba e cidades europeias já usam esse modelo — reduzindo consumo em até 60%.

**🎯 Objetivo:** Crie uma luminária que ajusta a intensidade e cor da luz baseada no som ambiente, com controle manual via joystick.

**Componentes utilizados:**
- Microfone (GPIO28)
- LED RGB (R=GPIO13, G=GPIO11, B=GPIO12)
- Joystick (X=GPIO27, Y=GPIO26)
- Buzzer (GPIO21)

**Requisitos mínimos:**
1. LED RGB ajusta brilho proporcional ao som ambiente (quanto mais barulho → mais claro)
2. Quando silencioso (sem som) → LED apagado ou muito fraco (economia de energia)
3. Joystick permite ajuste manual de brilho (eixo X) e cor (eixo Y)
4. Buzzer emite "bip" quando modo manual é ativado (Botão do joystick)
5. Display mostra o nível de brilho atual (0-100%)

**Dica de partida:**
```python
from machine import Pin, ADC, PWM
import time

microfone = ADC(Pin(28))
led_r = PWM(Pin(13))
led_g = PWM(Pin(11))
led_b = PWM(Pin(12))

def mapear_brilho(som, min_som=5000, max_som=50000):
    if som < min_som:
        return 0
    if som > max_som:
        return 65535
    return int(((som - min_som) / (max_som - min_som)) * 65535)
```

---

### 🚦 Desafio 7: Semáforo Pedestre Inteligente com Acessibilidade

**Nível:** ⭐⭐⭐

**🌍 O contexto:** Semáforos inteligentes são essenciais para cidades acessíveis. No Brasil, a legislação (Lei Brasileira de Inclusão) exige que semáforos tenham recursos de acessibilidade para deficientes visuais — como sinais sonoros que indicam quando é seguro atravessar. Cidades como Curitiba e São Paulo já implementam esses sistemas.

**🎯 Objetivo:** Crie um semáforo que atenda pedestres com recursos de acessibilidade sonora e visual.

**Componentes utilizados:**
- Botão A (GPIO5) — pedestre solicita passagem
- Botão B (GPIO6) — modo noturno (piscante amarelo)
- Botão C (GPIO10) — cancelar solicitação
- LED RGB (R=GPIO13, G=GPIO11, B=GPIO12)
- Buzzer (GPIO21)
- Display OLED (SDA=GPIO2, SCL=GPIO3)

**Requisitos mínimos:**
1. Estado normal: LED verde aceso (carro pode passar)
2. Botão A pressionado: LED fica vermelho por 10 segundos (pedestre atravessa)
3. Buzzer emite beep rápido (2Hz) durante verde = pode cruzar
4. Buzzer emite beep lento (0.5Hz) durante vermelho = aguarde
5. OLED mostra countdown regressivo ("Atravesse: 8s")
6. Botão B ativa modo noturno: LED amarelo pisca (piscante)
7. Botão C cancela solicitação e volta ao verde

**Dica de partida:**
```python
from machine import Pin, PWM, time
import time

botao_a = Pin(5, Pin.IN, Pin.PULL_UP)
botao_b = Pin(6, Pin.IN, Pin.PULL_UP)
botao_c = Pin(10, Pin.IN, Pin.PULL_UP)

def beep_rapido(buzzer, duracao):
    for _ in range(int(duracao * 2)):
        buzzer.value(1)
        time.sleep_ms(250)
        buzzer.value(0)
        time.sleep_ms(250)

def beep_lento(buzzer, duracao):
    for _ in range(int(duracao * 0.5)):
        buzzer.value(1)
        time.sleep_ms(500)
        buzzer.value(0)
        time.sleep_ms(500)
```

---

> 🎓 **Parabéns por chegar até aqui!** Esses desafios são a sua chance de mostrar tudo o que aprendeu — não só para o professor, mas para toda a escola! Não existe uma única resposta correta: use sua criatividade, experimente, erre, aprenda e tente de novo. O importante é **fazer**! 

> 📌 **Dica para a apresentação:** Documente seu projeto com fotos, vídeos e código comentado. Na hora de apresentar, demonstre o funcionamento ao vivo, explique as escolhas técnicas e conte como seu projeto se conecta com situações reais. Isso faz toda a diferença!

---

## Dicas de Depuração

### Quando algo não funciona:

1. **Verifique as conexões** - O cabo USB está bem conectado?
2. **Reinstale o firmware** - Use o botão BOOTSEL
3. **Confira o nome do arquivo** - Deve ser `main.py`
4. **Verifique as bibliotecas** - `ssd1306.py` e `neopixel.py` estão na placa?

### Erros Comuns:

| Erro | Causa | Solução |
|------|-------|---------|
| `ImportError` | Biblioteca não encontrada | Copie `ssd1306.py` para a placa |
| `ValueError` | Pino já em uso | Verifique se outro programa está rodando |
| `OSError` | Dispositivo não encontrado | Verifique fiação e endereço I2C |

---

## Referência Rápida

### Pinagem da BitDogLab V7

| Periférico | Pino |
|------------|------|
| LED RGB Vermelho | GPIO13 |
| LED RGB Verde | GPIO11 |
| LED RGB Azul | GPIO12 |
| Matriz NeoPixel | GPIO7 |
| Display OLED SDA | GPIO2 |
| Display OLED SCL | GPIO3 |
| Botão A | GPIO5 |
| Botão B | GPIO6 |
| Botão C | GPIO10 |
| Buzzer | GPIO21 |
| Joystick X | GPIO27 |
| Joystick Y | GPIO26 |
| Microfone | GPIO28 |

---

## Próximos Passos

1. **Experimente** - Modifique os exemplos e veja o que acontece!
2. **Combine** - Junte dois ou mais periféricos em um novo projeto
3. **Crie** - Invente algo novo que resolve um problema real
4. **Compartilhe** - Mostre seus projetos para colegas e professores

---

## Recursos Extras

- [Repositório oficial da BitDogLab](https://github.com/nicholasgriffintn/BitDogLab)
- [Thonny IDE](https://thonny.org/)
- [Documentação MicroPython](https://docs.micropython.org/)

---

> **Lembre-se:** A tecnologia é uma ferramenta. O mais importante é a sua **criatividade** e **curiosidade** para usá-la! 🚀

---

*Manual criado para a disciplina de Robótica*
*BitDogLab V7 - Escola 4.0 FEEC/Unicamp*
