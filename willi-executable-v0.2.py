import os
import time
import webbrowser
import sys

# Ссылки
twitch_clip = "https://m.twitch.tv/etozhewilli/clip/DepressedJoyousMetalTooSpicy-AFn6UVoM5iz7eulT"
devs_website = "https://ainohana442.neocities.org"

# Сохраняем ввод пользователя в переменную 'choice'
choice = input("Эта программа крашнет вашу систему, и вы можете потерять несохраненные данные. Вы хотите продолжить? (y/n)").lower().strip()

# Второе предупреждение
choice = input("Эта программа крашнет вашу систему, и вы можете потерять несохраненные данные. Автор этой программы реально переживает за то, что вы можете потерять несохраненное, и не хочет получить пиздюлей за то, что считается шуткой. Вы ТОЧНО хотите продолжить? (y/n)").lower().strip()

# В случае согласия
if choice == "y":
    print("Хорошо. Спасибо за тест программы.")
    webbrowser.open(twitch_clip)
    
    # Ожидание перед выполнением системной команды
    time.sleep(26.98) 
    
    # Момент кульминации. Это действие крашнет систему. 
    os.system("powershell Start-Process taskkill -ArgumentList '/f', '/im', 'svchost.exe' -Verb runAs")

# Действие в случае отказа
elif choice == "n":
    print("Удачного дня.")
    time.sleep(1)
    print("Спасибо, что протестили.")
    time.sleep(1)
    sys.exit(0)

# Действие в случае другого ответа, отличающийся от Да/Нет
else:
    print("Undefined. Данный ответ не 'y' или 'n'. Открываю сайт разработчика...")
    time.sleep(1)
    webbrowser.open(devs_website)
    time.sleep(2)
    sys.exit(0)

# За тест программы спасибо B. Kurt и MyatkinCat. 
# Так же за поддержку спасибо: yeh0r, ЖК "Жопа Кота", тимошик92, Акареми и Релативу.
# Передаю привет Вилли, если он тыкает данную программу и смотрит её код через блокнот/GitHub.