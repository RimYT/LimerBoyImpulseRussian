# Import modules
import os
import sys
import platform
from time import ctime
from colorama import Fore

""" This function will stop the program when a critical error occurs """


def CriticalError(message, error):
    print(f"""
    {Fore.RED}:=== Критическая ошибка:
    {Fore.MAGENTA}СООБЩЕНИЕ: {message}.
    {Fore.MAGENTA}ОШИБКА: {error}
    {Fore.RED}:=== Ифнормация о Python:
    {Fore.MAGENTA}ВЕРСИЯ PYTHON: {platform.python_version()}
    {Fore.MAGENTA}СБОРКА PYTHON: {'{}, DATE: {}'.format(*platform.python_build())}
    {Fore.MAGENTA}КОМПИЛЯТОР PYTHON: {platform.python_compiler()}
    {Fore.MAGENTA}НАХОЖДЕНИЕ СКРИПТА: {os.path.dirname(os.path.realpath(sys.argv[0]))}
    {Fore.MAGENTA}НЫНЕШНЯЯ ЛОКАЦИЯ: {os.getcwd()}
    {Fore.RED}:=== Системная информация:
    {Fore.MAGENTA}СИСТЕМА: {platform.system()}
    {Fore.MAGENTA}РЕЛИЗ: {platform.release()}
    {Fore.MAGENTA}ВЕРСИЯ: {platform.version()}
    {Fore.MAGENTA}АРХИТЕКТУРА: {'{} {}'.format(*platform.architecture())}
    {Fore.MAGENTA}ПРОЦЕССОР: {platform.processor()}
    {Fore.MAGENTA}МАШИНА: {platform.machine()}
    {Fore.MAGENTA}НОТА(НОДА): {platform.node()}
    {Fore.MAGENTA}ВРЕМЯ: {ctime()}
    {Fore.RED}:=== Сообщить о ошибке:
    {Fore.MAGENTA}Пожалуйста, сообщите о ошибке здесь: https://github.com/LimerBoy/Impulse/issues/new
    {Fore.RESET}
    """)
    sys.exit(5)
