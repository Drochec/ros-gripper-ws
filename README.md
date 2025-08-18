# Gripper Controller Workspace
## Zapojení
Servo:
* Signál (žlutý drát) - GPIO 2 na černé desce s ADC
* Potenciometr (zelený drát) - ADC 0

Proudové čidlo:
* Výstup (Zelený drát) - ADC 1

## Dependencies
Servo:
* pigpio
* piServoCtl

ADC:
* ads1015
Vše by mělo jít nainstalovat přes pip3. Pro pigpio možná bude potřebovat dočasně přidat raspbian repozitář: 

## ros_ws
ROS workspace, má 2 nody a definici actionu

### gripper_servo_controller - control_node
Ovládání serva
Topicy:
* Publisher - cur_pos - ruční nastavení úhlu
* Subscribery:
  * cmd_pos - ruční nastavení úhlu, Int32 = stupně natočení
  * adc_angle - aktuální úhel ze zpětné vazby, Int32 = stupně natočení
  * adc_current - proud do serva, Float32 = Amp
Action Server: - GripperMove
* goal - action Int32
* hodnota >= 0 - ruční nastavení úhlu
* speciální případy: -1 - pozice CLOSED, -2 - pozice OPEN

Př. otevření gripperu: ros2 action send_goal action_interface/action/GripperMove '{action: -2}'

### adc_readout - adc_readout_node
Čtení hodnot z ADC na i2c. Nejspíš bude potřeba nastavit správný i2c rozhraní.

Příkaz: 

> ls /dev/ | grep i2c' vypíše i2c rozhraní

Asi budou dvě, i2c-0 - výchozí rozhraní na HW pinech, i2c-X - SW rozhraní, číslo rozhraní X zadat do adc_readout

Při spuštění kalibruje proudové čidlo a úhel z potenciometru (zasílá actiony do gripper_controlleru)

Topicy - Publishery:
* adc_current
* adc_angle

### action_interface
Zde je definice GripperMove actionu

## Ostatní
servo - python skript pro prvotní vyzkoušení knihovny ovládání serva
adc - to samé, ale pro adc

## Do budoucna 

* ADC: Zdá se že je možné, aby k jednomu i2c rozhraní přistupovalo více procesů, takže je adc_readout noda zbytečná a všechna funkcionalita by měla jít vložit do control_node gripperu.
Mohlo by zlepšit přesnost a spolehlivost gripperu, protože pozice a proud bude čtena přímo v programu a nebudeme vázání na rychlost posílání dat z adc nodu.
* Gripper: Změnit posílání z 0-180 na 0-1 zavřeno-otevřeno
