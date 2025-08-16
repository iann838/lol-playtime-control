from datetime import datetime, timedelta
from PIL import Image
import psutil
import pystray
import random
import threading
import time

TrayIcon = pystray.Icon

# Process names
CLIENT_NAME = "LeagueClient.exe"
GAME_NAME = "League of Legends.exe"

# Globals for shared state
total_time = 0.0  # in seconds
blocked = False
game_running = False
current_session_start = None
current_day = None

def get_day_key(dt):
    if dt.hour < 4:
        return (dt - timedelta(days=1)).date()
    else:
        return dt.date()

def is_process_running(name):
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == name:
            return True
    return False

def kill_processes(name):
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == name:
            try:
                proc.kill()
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass

def monitoring_loop(icon: TrayIcon):
    global total_time, blocked, game_running, current_session_start, current_day
    current_day = get_day_key(datetime.now())
    prev_game_running = False
    while True:
        now = datetime.now()
        day = get_day_key(now)
        if day != current_day:
            total_time = 0.0
            blocked = False
            current_day = day

        game_running = is_process_running(GAME_NAME)

        if not prev_game_running and game_running:
            current_session_start = time.time()

        if prev_game_running and not game_running:
            if current_session_start is not None:
                total_time += time.time() - current_session_start
                current_session_start = None
            if total_time > 5400:  # 1.5 hours in seconds
                kill_processes(CLIENT_NAME)
                blocked = True

        if blocked:
            if is_process_running(CLIENT_NAME):
                kill_processes(CLIENT_NAME)

        prev_game_running = game_running
        icon.update_menu()
        time.sleep(random.randint(5, 10))  # Check every 5 to 10 seconds

def get_time_str(_):
    global total_time, game_running, current_session_start
    current_total = total_time
    if game_running and current_session_start is not None:
        current_total += time.time() - current_session_start
    hours = int(current_total // 3600)
    mins = int((current_total % 3600) // 60)
    secs = int(current_total % 60)
    return f"Time Gaming: {hours:02d}:{mins:02d}:{secs:02d}"

def get_remaining_time(_):
    global total_time
    remaining = max(0, 5400 - total_time)
    hours = int(remaining // 3600)
    mins = int((remaining % 3600) // 60)
    secs = int(remaining % 60)
    return f"Time Leftover: {hours:02d}:{mins:02d}:{secs:02d}"

def main():
    menu = pystray.Menu(
        pystray.MenuItem(get_time_str, lambda _: None),
        pystray.MenuItem(get_remaining_time, lambda _: None),
        pystray.MenuItem("Turn this off (Don't!)", lambda icon: icon.stop()),
    )
    icon = pystray.Icon("lol_playtime_control", Image.open("icon.webp"), "LoL Playtime Control", menu=menu)
    thread = threading.Thread(target=monitoring_loop, args=[icon], daemon=True)
    thread.start()
    icon.run()
    

if __name__ == "__main__":
    main()