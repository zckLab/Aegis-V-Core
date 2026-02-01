# Aegis-V Electromechanical Specs

### Componentes:
- **MCU:** ATmega328P (Direct Port Manipulation).
- **Drive:** MOSFET IRF540N para chaveamento do Solenoide.
- **Proteção:** Diodo de Flyback (1N4007) para proteção contra força contra-eletromotriz.

### Lógica de Controle:
O firmware utiliza **PWM (Pulse Width Modulation)** para gerenciar a energia do solenoide, reduzindo o consumo em 40% após o curso inicial de ativação, evitando superaquecimento da bobina.