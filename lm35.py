from machine import ADC, Pin
import time

# Configuration de la broche analogique
lm35_pin = ADC(Pin(34))  # Utilise GPIO 34 (vous pouvez changer selon votre connexion)
lm35_pin.atten(ADC.ATTN_11DB)  # Configuration d'atténuation pour lire jusqu'à 3.6V
lm35_pin.width(ADC.WIDTH_12BIT)  # Configuration de la résolution à 12 bits

def read_temperature():
    # Lire la valeur analogique
    value = lm35_pin.read()
    
    # Convertir la valeur lue en tension
    voltage = value * (3.3 / 4095)  # 3.3V pour ESP32 / 4095 pour 12 bits

    # Convertir la tension en température (LM35 : 10mV par °C)
    temperature = voltage * 100  # 1V = 100°C
    
    return temperature

while True:
    temp = read_temperature()
    print("Température: {:.2f} °C".format(temp))
    time.sleep(1)  # Attendre 1 seconde avant la prochaine lecture