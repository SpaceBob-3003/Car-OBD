#HOAREAU Alann

import os
import can
import time


def setup_can_interface():
    print("Vérification de l'interface CAN...")
    result = os.system("ip link show can0 | grep 'state UP' > /dev/null")
    
    if result != 0:  
        print("Activation de l'interface CAN...")
        os.system("sudo ip link set can0 up type can bitrate 500000")
        time.sleep(1)
    else:
        print("Interface CAN déjà active.")


def recup_info(pid, bus):
	request = can.Message(arbitration_id=0x7DF, data=[0x02, 0x01, pid, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=False)
	bus.send(request)
	start_time = time.time()
	timeout = 1
	while time.time() - start_time < timeout:
		message = bus.recv(timeout=0.2)
		if message:
			if message.arbitration_id == 0x7E8 :
				# Vérifier si c'est bien la réponse voulue
				if message.data[1] == 0x41 and message.data[2] == pid:
					return message.data
	return None


def rpm(bus):
    data = recup_info(0x0C, bus)
    if data:
        return f"{((data[3] * 256) + data[4]) // 4}"
    return None  


def vitesse(bus):
    data = recup_info(0x0D, bus)
    if data:
        return f"{data[3]}"
    return None


def temp_refroidissement(bus):
    data = recup_info(0x05, bus)
    if data:
        return f"{data[3] - 40}"
    return None


def pourcent_load(bus):
    data = recup_info(0x04, bus)
    if data:
        return f"{data[3] * 100 / 255:.1f}"
    return None


def temp_air(bus):
    data = recup_info(0x0F, bus)
    if data:
        return f"{data[3] - 40}"
    return None


def position_papillon(bus):
    data = recup_info(0x11, bus)
    if data:
        return f"{data[3] * 100 / 255:.1f}"
    return None
