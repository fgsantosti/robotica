# Atividade Servo Motor + Sensor Ultrassonico

## Código para utilização do Servo Motor

```python

from machine import Pin, time_pulse_us
from utime import sleep
from machine import Pin, PWM

import time

#configuração do sensor ultrassônico
pwm = PWM(Pin(16))
pwm.freq(50)

#enviando sinal PWM para o servo motor
pwm.duty_u16(3276)
pwm.duty_u16(6553)

while True:
    #enviando sinal PWM para o servo motor
    pwm.duty_u16(3276)
    sleep(2) # sleep 1sec
    pwm.duty_u16(6553)
    sleep(2) # sleep 1sec
    pwm.duty_u16(0)
    sleep(2) # sleep 1sec

print("Finished.")

```


## Código para utilização do Sensor Ultrassonico

```python
from machine import Pin, time_pulse_us, PWM
from utime import sleep
import time

# Ultrasonic sensor with PWM control
SOUND_SPEED=340 
# Tempo de pulso em microsegundos
TRIG_PULSE_DURATION_US=10

# Definição dos pinos
trig_pin = Pin(17, Pin.OUT) # Broche GP15 de la Pico
echo_pin = Pin(18, Pin.IN)  # Broche GP14 de la Pico

while True:
    # Prepare le signal
    trig_pin.value(0)
    time.sleep_us(5)

    #Impulse de 10 µs
    trig_pin.value(1)
    time.sleep_us(TRIG_PULSE_DURATION_US)
    trig_pin.value(0)

    #Mensura a duração de pulso
    ultrason_duration = time_pulse_us(echo_pin, 1, 30000) # Renvoie le temps de propagation de l'onde (en µs)
    distance_cm = SOUND_SPEED * ultrason_duration / 20000

    #mostra a duração do pulso ultrassônico
    print(f"Ultrason duration: {ultrason_duration} µs")

    #mostra a distância em centímetros
    print(f"Distance : {distance_cm} cm")
    time.sleep_ms(500)


print("Finished.
```


---

### **1. Porta Automática com Sensor de Presença**  
**Objetivo:** Criar um sistema que abre um servo (simulando uma porta) quando um objeto se aproxima.  

#### **Materiais:**  
- Servo motor (SG90 ou similar)  
- Sensor ultrassônico HC-SR04  
- Placa Raspberry Pi Pico  
- Protoboard e jumpers  

#### **Montagem:**  
1. Conecte o servo:  
   - **Fio vermelho (VCC)** → 5V da Pico  
   - **Fio marrom (GND)** → GND da Pico  
   - **Fio amarelo/laranja (sinal)** → GP16  

2. Conecte o sensor ultrassônico:  
   - **VCC** → 5V da Pico  
   - **GND** → GND da Pico  
   - **Trig** → GP17  
   - **Echo** → GP18  

#### **Funcionamento do Código:**  
- O sensor mede a distância continuamente.  
- Se um objeto estiver a menos de **20 cm** (ajustável), o servo gira para **90°** (porta aberta).  
- Caso contrário, volta para **0°** (porta fechada).  

#### **Teste:**  
Aproxime a mão do sensor e observe o servo movendo-se automaticamente!  

---

### **2. Medidor de Distância com Indicador por Servo**  
**Objetivo:** Usar o servo como um "ponteiro" que indica a distância medida.  

#### **Montagem:**  
Igual à atividade 1 (mesmas conexões).  

#### **Funcionamento do Código:**  
- O sensor mede a distância e mapeia para um ângulo (0° a 180°).  
  - Exemplo: Se o objeto está a **50 cm**, o servo vai para **0°**.  
  - Se está a **0 cm**, vai para **180°**.  
- O servo se move suavemente conforme a distância muda.  

#### **Teste:**  
Mova um objeto para frente e para trás do sensor e veja o servo ajustar o ângulo como um medidor analógico.  

---

### **3. Sistema de Varredura com Alarme**  
**Objetivo:** O servo faz uma varredura (180°) enquanto o sensor detecta objetos próximos.  

#### **Funcionamento do Código:**  
1. O servo varre de **0° a 180°** em passos de **10°**.  
2. Em cada posição, o sensor verifica se há algo a menos de **10 cm**.  
3. Se detectar, exibe **"ALARME!"** no console.  

#### **Teste:**  
Coloque um obstáculo perto do sensor durante a varredura. O servo deve parar e exibir o alerta!  

---

### **4. Controle de Braço Robótico Simplificado**  
**Objetivo:** Simular um braço robótico que busca e "segura" objetos.  

#### **Funcionamento do Código:**  
1. O servo começa em **0°** (posição inicial).  
2. Varre até encontrar um objeto a menos de **15 cm**.  
3. Quando encontra, "segura" (pausa por 2 segundos) e volta para a posição inicial.  

#### **Teste:**  
Posicione um objeto no caminho do sensor. O servo deve parar no objeto, esperar e retornar.  

---

### **5. Jogo de Habilidade com Servo e Sensor**  
**Objetivo:** Jogo onde o jogador deve adivinhar a distância correta.  

#### **Como Jogar:**  
1. O servo vai para uma posição aleatória (**0° a 180°**).  
2. O jogador posiciona a mão a uma distância do sensor.  
3. O sistema compara a distância da mão com a distância "alvo" (mapeada do ângulo do servo).  
4. Se acertar (dentro de **±5 cm**), ganha um ponto!  

#### **Teste:**  
Tente adivinhar onde o servo está apontando apenas ajustando a distância da sua mão!  

---

### **Dicas para Todas as Atividades:**  
1. **Ajuste de Sensibilidade:** Mude `DISTANCE_THRESHOLD` (atividade 1) ou `ALARM_DISTANCE` (atividade 3) conforme necessário.  
2. **Conexões:** Sempre verifique os fios do servo e sensor antes de ligar.  
3. **Debug:** Use `print()` para ver valores no console (Thonny ou Serial Monitor).  
4. **Extras:** Adicione um LED ou buzzer para feedback visual/sonoro (ex: alarme sonoro na atividade 3).  

Essas atividades combinam **lógica de programação**, **eletrônica básica** e **criatividade**, perfeitas para aulas de robótica! 🚀

```

