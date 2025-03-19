import can
import obd
import time

def envoyer_requete(bus, pid):
    """Envoie une requête OBD-II pour un PID donné et récupère la réponse."""
    message = can.Message(
        arbitration_id=0x7DF,
        data=[0x02, 0x01, pid, 0x00, 0x00, 0x00, 0x00, 0x00],
        is_extended_id=False
    )
    
    bus.send(message)
    start_time = time.time()
    
    while time.time() - start_time < 1:  # Timeout de 1 seconde
        response = bus.recv(timeout=0.5)
        if response and response.arbitration_id == 0x7E8:
            if response.data[1] == 0x41 and response.data[2] == pid:
                return response.data[3:]  # Retourne les données de réponse
    return None

def analyser_reponse(pid_base, data):
    """Analyse les bits de la réponse pour identifier les PIDs supportés."""
    pids_supportes = []
    for i in range(4):
        byte_value = data[i]
        for bit in range(8):
            if (byte_value & (1 << (7 - bit))) != 0:
                pids_supportes.append(hex(pid_base + (i * 8) + bit + 1))
    return pids_supportes

def scanner_pids():
    """Détecte les PIDs supportés et les retourne sous forme de liste."""
    obd.setup_can_interface()
    bus = can.interface.Bus(channel="can0", bustype="socketcan")

    pids_a_tester = [0x00, 0x20, 0x40, 0x60]
    pids_supportes = []

    print("🔍 Détection des PIDs disponibles...")

    for pid in pids_a_tester:
        response_data = envoyer_requete(bus, pid)
        if response_data:
            pids_supportes.extend(analyser_reponse(pid, response_data))

    bus.shutdown()
    return pids_supportes
    

print(scanner_pids())
