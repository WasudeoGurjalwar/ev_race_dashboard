import time
import random
import socketio
from datetime import datetime

# CONFIG
CAR_NAME = "Herakles_Racing"  # Change for other slaves (Car B, Car C, etc.)
SERVER_URL = "http://localhost:5000"  # Replace with master AWS IP

# STATIONS for simulation
STATIONS = ["Bangalore", "Tumakuru", "Chitradurga", "Kolhapur", "Pune"]
TOTAL_DISTANCE = 840  # km from Bangalore to Pune

# Connect to master server
sio = socketio.Client()

# EV State
ev_state = {
    "name": CAR_NAME,
    "distance": 0,
    "eta": "08:00",
    "battery": 100
}

def simulate_ev_movement():
    ev_state["distance"] += random.randint(10, 30)
    ev_state["distance"] = min(ev_state["distance"], TOTAL_DISTANCE)


    # Fake ETA
    remaining = TOTAL_DISTANCE - ev_state["distance"]
    hours_left = round(remaining / 80, 2)
    ev_state["eta"] = f"{int(hours_left)+8}:00"

    # Battery drop
    ev_state["battery"] = max(0, ev_state["battery"] - random.randint(1, 5))

@sio.event
def connect():
    print(f"[{CAR_NAME}] Connected to server.")

@sio.event
def disconnect():
    print(f"[{CAR_NAME}] Disconnected from server.")

def send_ev_data():
    sio.emit("update_leaderboard", {
        "name": ev_state["name"],
        "distance": ev_state["distance"],
        "eta": ev_state["eta"]
    })
    sio.emit("update_battery", {
        "name": ev_state["name"],
        "battery": ev_state["battery"]
    })

def send_comm_message(msg):
    sio.emit("new_message", f"[{CAR_NAME}] {msg}")

def simulate_charging_request():
    # Random station, slot
    station = random.choice(STATIONS)
    slot = random.randint(1, 3)
    send_comm_message(f"Requesting slot {slot} at {station}")
    # Simulate charging station responding (for testing)
    time.sleep(1)
    send_comm_message(f"[{station}] Slot {slot} reserved for {CAR_NAME}")

# ---- Main Execution Loop ----
def run_client():
    sio.connect(SERVER_URL)

    try:
        while ev_state["distance"] < TOTAL_DISTANCE:
            simulate_ev_movement()
            send_ev_data()

            if ev_state["battery"] < 60:
                simulate_charging_request()

            time.sleep(5)  # Send update every 5 seconds

        send_comm_message("Reached destination.")
    except KeyboardInterrupt:
        print("Stopped.")
    finally:
        sio.disconnect()

if __name__ == "__main__":
    run_client()
