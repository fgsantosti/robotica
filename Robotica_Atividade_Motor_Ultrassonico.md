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


print("Finished.")

```

