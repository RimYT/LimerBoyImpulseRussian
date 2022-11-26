# Import modules
import os
import sys
import wget
from colorama import Fore

if os.name == "nt":
    winpcap_url = "https://www.winpcap.org/install/bin/WinPcap_4_1_3.exe"
    winpcap_dir = os.environ["ProgramFiles(x86)"] + "\\WinPcap"
    if not os.path.exists(winpcap_dir):
        print(
            f'{Fore.MAGENTA}[!] {Fore.YELLOW}Внимание! Компонент "WinPcap" не установлен!\n    он нужен для проведения атак syn, udp и другие,\n    вы можете пропустить это если будете использовать только SMS спам\n    Хотите установить его автоматически? (д/н){Fore.RESET}'
        )
        if input(f"{Fore.MAGENTA} >>> {Fore.BLUE}").lower() in ("y", "yes", "1", "д", "да"):
            print(f"{Fore.YELLOW}[~] {Fore.CYAN}Скачивание установщика...{Fore.BLUE}\n")
            winpcap_installer = wget.download(winpcap_url)
            os.startfile(winpcap_installer)
            print(
                f"\n\n{Fore.GREEN}[?] {Fore.YELLOW}Теперь, пожалуйста, перезапустите программу{Fore.RESET}"
            )
            sys.exit(1)
