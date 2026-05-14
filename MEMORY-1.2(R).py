import os
import sys
import hashlib
import shutil
import subprocess
import asyncio
import glob
import zipfile
import threading
import datetime
from colorama import Fore, Style, init

init(autoreset=True)

# ---------- Добавляем функцию авторизации ----------
def check_user_auth():
    user_data_dir = os.path.join(os.getcwd(), 'user_data')
    user_data_file = os.path.join(user_data_dir, 'user_data.txt')

    # Проверка существования папки
    if not os.path.exists(user_data_dir):
        print(Fore.RED + "Папка user_data не найдена. Завершение работы." + Style.RESET_ALL)
        sys.exit()

    # Проверка существования файла
    if not os.path.isfile(user_data_file):
        print(Fore.RED + "Файл user_data.txt не найден. Завершение работы." + Style.RESET_ALL)
        sys.exit()

    # Чтение содержимого файла
    try:
        with open(user_data_file, 'r') as f:
            stored_hash = f.read().strip()
    except Exception as e:
        print(Fore.RED + f"Ошибка при чтении user_data.txt: {e}" + Style.RESET_ALL)
        sys.exit()

    if not stored_hash:
        print(Fore.RED + "Файл user_data.txt пуст. Завершение работы." + Style.RESET_ALL)
        sys.exit()

    print("")
    print(Fore.RED + "  |#--8\\  /8--8| |#88888\\  |#8| /88/ \\   Soft   / " + Style.RESET_ALL)
    print(Fore.RED + "  |#-888\\/888-8| |#8()888| |#8|/88/   \\ Memory /  " + Style.RESET_ALL)
    print(Fore.RED + "  |#88888888888| |#88888/  |#8888|     |      |   " + Style.RESET_ALL)
    print(Fore.RED + "  |#888|\\/|8888| |#88\\  \\  |#8|\\88\\   |@MRKdefs|  " + Style.RESET_ALL)
    print(Fore.RED + "  |#888|  |8888| |#8| \\88\\ |#8| \\88\\  |(R)(L)  |  " + Style.RESET_ALL)
    print("")

    # Ввод никнейма и пароля
    nickname = input("Введите никнейм: ").strip()
    password = input("Введите пароль: ").strip()

    # Создаем хеш из объединения ник+пароль
    combined = nickname + password
    hash_input = hashlib.sha256(combined.encode()).hexdigest()

    # Сравниваем
    if hash_input == stored_hash:
        print(Fore.GREEN + "Авторизация прошла успешно." + Style.RESET_ALL)
    else:
        print(Fore.RED + "Неверный никнейм или пароль." + Style.RESET_ALL)
        sys.exit()

# Вызов функции авторизации перед всем остальным
check_user_auth()

# --------- Далее идёт остальной код из MEMORY-1.2(R).txt ---------

def cl():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")
    print(Fore.RED + "  |#--8\\  /8--8| |#88888\\  |#8| /88/ \\   Soft   / " + Style.RESET_ALL)
    print(Fore.RED + "  |#-888\\/888-8| |#8()888| |#8|/88/   \\ Memory /  " + Style.RESET_ALL)
    print(Fore.RED + "  |#88888888888| |#88888/  |#8888|     |      |   " + Style.RESET_ALL)
    print(Fore.RED + "  |#888|\\/|8888| |#88\\  \\  |#8|\\88\\   |@MRKdefs|  " + Style.RESET_ALL)
    print(Fore.RED + "  |#888|  |8888| |#8| \\88\\ |#8| \\88\\  |(R)(L)  |  " + Style.RESET_ALL)
    print("")

async def wait_and_new_lines():
    print("\n\n\n")  # 3 пустых строки

async def help_cmd():
    print(Fore.YELLOW + "--- Доступные команды ---" + Style.RESET_ALL)
    print("create <имя>.<расширение> - создать файл")
    print("mkdir <имя> - создать папку")
    print("delete <имя> - удалить файл или папку")
    print("rename <старое_имя> <новое_имя> - переименовать")
    print("open <ссылка> - открыть сайт")
    print("ls - список содержимого текущей папки")
    print("cd <путь> - перейти в папку")
    print("cd .. - вверх по папке")
    print("cls - очистить экран")
    print("exit - выйти")
    print("exit_full [-reset] - перезапуск или закрытие")
    print("time - текущее время")
    print("date - текущая дата")
    print("show <имя> - показать содержимое файла")
    print("edit <имя> - редактировать файл")
    print("clear <имя> - очистить файл")
    print("add <имя> - добавить в файл")
    print("copy <источник> <назначение> - копировать файл")
    print("move <источник> <назначение> - переместить файл")
    print("find <имя> - поиск файла/папки")
    print("info <имя> - информация о файле/папке")
    print("zip <имя.zip> <файл/папка> - архивировать")
    print("unzip <имя.zip> <папка> - распаковать архив")
    #print("processes - список процессов")
    #print("kill <pid> - завершить процесс")
    #print("netstat - сетевые соединения")
    #print("disk - информация о дисках")
    #print("cpu - информация о CPU")
    #print("ram - информация о RAM")
    #print("screenshot - сделать скриншот (если есть нужные библиотеки)")
    #print("disk -real - мониторинг нагрузки дисков")
    print("help - список команд")
    print("help2 - список команд 2")
    print("exit - выйти из программы")

async def help_cmd2():
    print(Fore.YELLOW + "--- Вторая страница команд ---" + Style.RESET_ALL)
    print("new_note <имя> <текст> - создать заметку")
    print("read_note - выбрать и прочитать заметку")
    print("")
    print(Fore.RED + "--- teams for developers ---" + Style.RESET_ALL)
    print(Fore.RED + "sm - просмотр компонентов (-v - выводит версию софта)" + Style.RESET_ALL)

def confirm_exit():
    # Вместо tkinter используем простое сообщение в терминале
    response = input(Fore.YELLOW + "Начать процесс выполнения команды disk -real? (да/нет): " + Style.RESET_ALL).lower()
    return response in ('да', 'да', 'yes', 'y')

async def cmd_interface():
    current_directory = os.getcwd()
    print(Fore.YELLOW + "--- CMD интерфейс ---" + Style.RESET_ALL)
    while True:
        command = input(Fore.MAGENTA + f"{current_directory} > " + Style.RESET_ALL)
        if command.lower() == 'exit':
            await wait_and_new_lines()
            break
        elif command.startswith('create '):
            name = command.split(' ', 1)[1]
            try:
                if os.path.exists(name):
                    print(Fore.RED + f"{name} уже существует." + Style.RESET_ALL)
                else:
                    open(name, 'w').close()
                    print(Fore.GREEN + f"{name} создан." + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"Ошибка при создании: {e}" + Style.RESET_ALL)
        elif command == 'help2':
            await help_cmd2()
            await wait_and_new_lines()
        elif command == 'sm -v':
            print(Fore.RED + "SoftMemory - version 1.2 [full design (limited edition)]" + Style.RESET_ALL)
        elif command == 'sm':
            print(Fore.RED + "SoftMemory - version 1.2 [full design (limited edition)]" + Style.RESET_ALL)
            print(Fore.RED + "developer - @MRKdefs (telegram)" + Style.RESET_ALL)
            print(Fore.RED + "release date (01.06.2026)" + Style.RESET_ALL)
        elif command.startswith('mkdir '):
            name = command.split(' ', 1)[1]
            try:
                os.makedirs(name, exist_ok=True)
                print(Fore.GREEN + f"Папка {name} создана." + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"Ошибка при создании папки: {e}" + Style.RESET_ALL)
        elif command.startswith('delete '):
            name = command.split(' ', 1)[1]
            try:
                if os.path.isdir(name):
                    shutil.rmtree(name)
                    print(Fore.GREEN + f"Папка {name} удалена." + Style.RESET_ALL)
                elif os.path.isfile(name):
                    os.remove(name)
                    print(Fore.GREEN + f"Файл {name} удален." + Style.RESET_ALL)
                else:
                    print(Fore.RED + f"{name} не существует." + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"Ошибка при удалении: {e}" + Style.RESET_ALL)
        elif command.startswith('rename '):
            parts = command.split(' ')
            if len(parts) != 3:
                print(Fore.RED + "Используйте: rename <старое_имя> <новое_имя>" + Style.RESET_ALL)
                continue
            old_name, new_name = parts[1], parts[2]
            try:
                os.rename(old_name, new_name)
                print(Fore.GREEN + f"{old_name} переименован в {new_name}." + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"Ошибка при переименовании: {e}" + Style.RESET_ALL)
        elif command.startswith('open '):
            url = command.split(' ', 1)[1]
            import webbrowser
            webbrowser.open(url)
            print(Fore.GREEN + f"Открываю веб-сайт: {url}" + Style.RESET_ALL)
        elif command == 'ls':
            try:
                files = os.listdir(current_directory)
                for f in files:
                    print(f)
                await wait_and_new_lines()
            except Exception as e:
                print(Fore.RED + f"Ошибка при получении списка: {e}" + Style.RESET_ALL)
        elif command.startswith('cd '):
            path = command.split(' ', 1)[1]
            try:
                new_directory = os.path.join(current_directory, path)
                os.chdir(new_directory)
                current_directory = os.getcwd()
                print(Fore.GREEN + f"Перешли в: {current_directory}" + Style.RESET_ALL)
                await wait_and_new_lines()
            except Exception as e:
                print(Fore.RED + f"Ошибка при переходе: {e}" + Style.RESET_ALL)
        elif command == 'cd ..':
            try:
                os.chdir('..')
                current_directory = os.getcwd()
                print(Fore.GREEN + f"На уровень вверх: {current_directory}" + Style.RESET_ALL)
                await wait_and_new_lines()
            except Exception as e:
                print(Fore.RED + f"Ошибка при возврате: {e}" + Style.RESET_ALL)
        elif command == 'cls':
            cl()
        elif command.lower() == 'help':
            await help_cmd()
            await wait_and_new_lines()
        elif command.startswith('new_note '):
            # Формат: new_note <имя> <текст>
            parts = command.split(' ', 2)
            if len(parts) < 3:
                print(Fore.RED + "Используйте: new_note <имя> <текст>" + Style.RESET_ALL)
                continue
            name = parts[1]
            text = parts[2]
            filename = f"note_{name}.txt"
            if os.path.exists(filename):
                print(Fore.RED + "Заметка с таким именем уже существует." + Style.RESET_ALL)
            else:
                try:
                    with open(filename, 'w') as f:
                        f.write(text)
                    print(Fore.GREEN + f"Заметка {filename} создана." + Style.RESET_ALL)
                except Exception as e:
                    print(Fore.RED + f"Ошибка при создании заметки: {e}" + Style.RESET_ALL)
        elif command == 'read_note':
            # показать список заметок
            notes = [f for f in os.listdir('.') if f.startswith('note_') and f.endswith('.txt')]
            if not notes:
                print(Fore.RED + "Нет заметок." + Style.RESET_ALL)
                continue
            print("Доступные заметки:")
            for idx, note in enumerate(notes, 1):
                print(f"{idx}. {note}")
            try:
                choice = int(input("Выберите номер заметки: "))
                if 1 <= choice <= len(notes):
                    filename = notes[choice - 1]
                    with open(filename, 'r') as f:
                        content = f.read()
                    print(Fore.CYAN + f"Содержимое {filename}:\n{content}" + Style.RESET_ALL)
                    # Предложение удалить или оставить
                    del_choice = input("Удалить заметку? (да/нет): ").lower()
                    if del_choice in ('да', 'yes', 'y'):
                        os.remove(filename)
                        print(Fore.GREEN + f"Заметка {filename} удалена." + Style.RESET_ALL)
                    else:
                        print("Заметка оставлена.")
                else:
                    print(Fore.RED + "Некорректный выбор." + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"Ошибка: {e}" + Style.RESET_ALL)
        elif command.lower() == 'time':
            print(Fore.GREEN + f"Текущее время: {datetime.datetime.now().strftime('%H:%M:%S')}" + Style.RESET_ALL)
            await wait_and_new_lines()
        elif command.lower() == 'date':
            print(Fore.GREEN + f"Текущая дата: {datetime.datetime.now().strftime('%Y-%m-%d')}" + Style.RESET_ALL)
            await wait_and_new_lines()
        elif command.startswith('show '):
            filename = command.split(' ', 1)[1]
            try:
                with open(filename, 'r') as file:
                    print(Fore.GREEN + file.read() + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"Ошибка при чтении: {e}" + Style.RESET_ALL)
            await wait_and_new_lines()
        elif command.startswith('edit '):
            filename = command.split(' ', 1)[1]
            try:
                new_content = input(Fore.MAGENTA + "Введите содержимое: " + Style.RESET_ALL)
                with open(filename, 'w') as file:
                    file.write(new_content)
                print(Fore.GREEN + f"{filename} отредактирован." + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"Ошибка при редактировании: {e}" + Style.RESET_ALL)
            await wait_and_new_lines()
        elif command.startswith('clear '):
            filename = command.split(' ', 1)[1]
            action = input(Fore.MAGENTA + "Очистить всё? (да/нет): " + Style.RESET_ALL).lower()
            try:
                if action in ('да', 'yes', 'y'):
                    open(filename, 'w').close()
                    print(Fore.GREEN + f"{filename} очищен." + Style.RESET_ALL)
                elif action in ('нет', 'no', 'n'):
                    text_to_remove = input(Fore.MAGENTA + "Введите текст для удаления: " + Style.RESET_ALL)
                    with open(filename, 'r') as f:
                        content = f.read()
                    new_content = content.replace(text_to_remove, "")
                    with open(filename, 'w') as f:
                        f.write(new_content)
                    print(Fore.GREEN + f"Текст удален из {filename}." + Style.RESET_ALL)
                else:
                    print(Fore.RED + "Неверный ответ." + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"Ошибка: {e}" + Style.RESET_ALL)
            await wait_and_new_lines()
        elif command.startswith('add '):
            filename = command.split(' ', 1)[1]
            try:
                content_to_add = input(Fore.MAGENTA + "Введите добавляемый текст: " + Style.RESET_ALL)
                with open(filename, 'a') as f:
                    f.write(content_to_add)
                print(Fore.GREEN + f"Добавлено в {filename}." + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"Ошибка: {e}" + Style.RESET_ALL)
            await wait_and_new_lines()
        elif command.startswith('copy '):
            parts = command.split(' ')
            if len(parts) != 3:
                print(Fore.RED + "Используйте: copy <источник> <назначение>" + Style.RESET_ALL)
                continue
            src, dst = parts[1], parts[2]
            try:
                shutil.copy2(src, dst)
                print(Fore.GREEN + f"{src} скопирован в {dst}." + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"Ошибка копирования: {e}" + Style.RESET_ALL)
            await wait_and_new_lines()
        elif command.startswith('move '):
            parts = command.split(' ')
            if len(parts) != 3:
                print(Fore.RED + "Используйте: move <источник> <назначение>" + Style.RESET_ALL)
                continue
            src, dst = parts[1], parts[2]
            try:
                shutil.move(src, dst)
                print(Fore.GREEN + f"{src} перемещен в {dst}." + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"Ошибка перемещения: {e}" + Style.RESET_ALL)
            await wait_and_new_lines()
        elif command.startswith('find '):
            name = command.split(' ', 1)[1]
            results = []
            for root, dirs, files in os.walk('.'):
                if name in dirs or name in files:
                    results.append(os.path.join(root, name))
            if results:
                for r in results:
                    print(Fore.GREEN + r)
            else:
                print(Fore.RED + "Файл или папка не найдены.")
            await wait_and_new_lines()
        elif command.startswith('info '):
            name = command.split(' ', 1)[1]
            try:
                if os.path.exists(name):
                    stat = os.stat(name)
                    size = stat.st_size
                    permissions = oct(stat.st_mode)[-3:]
                    modified_time = datetime.datetime.fromtimestamp(stat.st_mtime)
                    print(Fore.CYAN + f"Информация о {name}:")
                    print(f"Размер: {size} байт")
                    print(f"Права: {permissions}")
                    print(f"Последнее изменение: {modified_time}")
                else:
                    print(Fore.RED + "Объект не найден.")
            except Exception as e:
                print(Fore.RED + f"Ошибка получения информации: {e}")
            await wait_and_new_lines()
        elif command.startswith('zip '):
            parts = command.split(' ')
            if len(parts) != 3:
                print(Fore.RED + "Используйте: zip <имя.zip> <файл/папка>" + Style.RESET_ALL)
                continue
            zip_name, target = parts[1], parts[2]
            try:
                with zipfile.ZipFile(zip_name, 'w') as zipf:
                    if os.path.isdir(target):
                        for root, dirs, files in os.walk(target):
                            for file in files:
                                zipf.write(os.path.join(root, file),
                                           arcname=os.path.relpath(os.path.join(root, file), start=target))
                    elif os.path.isfile(target):
                        zipf.write(target, arcname=os.path.basename(target))
                    else:
                        print(Fore.RED + "Цель не найдена." + Style.RESET_ALL)
                        continue
                print(Fore.GREEN + f"Создан архив {zip_name}." + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"Ошибка архивации: {e}")
            await wait_and_new_lines()
        elif command.startswith('unzip '):
            parts = command.split(' ')
            if len(parts) != 3:
                print(Fore.RED + "Используйте: unzip <имя.zip> <папка>" + Style.RESET_ALL)
                continue
            zip_name, folder = parts[1], parts[2]
            try:
                with zipfile.ZipFile(zip_name, 'r') as zipf:
                    zipf.extractall(folder)
                print(Fore.GREEN + f"Распаковано в {folder}." + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"Ошибка распаковки: {e}")
            await wait_and_new_lines()
        elif command == 'processes':
            print(Fore.YELLOW + "Список процессов:" + Style.RESET_ALL)
            # psutil.process_iter() больше не используется
            print("Функция отображения процессов отключена.")
            await wait_and_new_lines()
        elif command.startswith('kill '):
            try:
                pid = int(command.split(' ',1)[1])
                # psutil.Process(pid).terminate() больше не используется
                print(f"Завершение процесса {pid} отменено.")
            except Exception as e:
                print(Fore.RED + f"Ошибка при завершении процесса: {e}" + Style.RESET_ALL)
            await wait_and_new_lines()
        elif command == 'netstat':
            # psutil.net_connections() больше не используется
            print("Функция netstat отключена.")
            await wait_and_new_lines()
        elif command == 'disk':
            # psutil.disk_partitions() и psutil.disk_usage() больше не используются
            print("Функция disk отключена.")
            await wait_and_new_lines()
        elif command == 'cpu':
            # psutil.cpu_percent(), psutil.cpu_count(), psutil.cpu_freq() больше не используются
            print("Функция cpu отключена.")
            await wait_and_new_lines()
        elif command == 'ram':
            # psutil.virtual_memory() больше не используется
            print("Функция ram отключена.")
            await wait_and_new_lines()
        elif command == 'screenshot':
            try:
                import pyautogui
                screenshot = pyautogui.screenshot()
                filename = f"screenshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                screenshot.save(filename)
                print(Fore.GREEN + f"Скриншот сохранен как {filename}")
            except Exception as e:
                print(Fore.RED + f"Ошибка при снятии скриншота: {e}")
            await wait_and_new_lines()
        elif command == 'disk -real':
            if confirm_exit():
                stop_event = threading.Event()

                async def monitor_disks():
                    try:
                        while not stop_event.is_set():
                            print("\033[2J\033[H", end='')  # Очистка экрана ANSI
                            print(Fore.YELLOW + "--- Мониторинг дисков ---" + Style.RESET_ALL)
                            # psutil.disk_partitions() и psutil.disk_usage() больше не используются
                            print("Мониторинг дисков отключен.")
                            await asyncio.sleep(1)
                    except asyncio.CancelledError:
                        pass

                def run_monitor():
                    asyncio.run(monitor_disks())

                t = threading.Thread(target=run_monitor)
                t.start()

                print(Fore.CYAN + "Нажмите Enter, чтобы остановить мониторинг..." + Style.RESET_ALL)
                input()
                stop_event.set()
                t.join()
            else:
                print(Fore.YELLOW + "Мониторинг дисков отменен." + Style.RESET_ALL)
        else:
            print(Fore.RED + "Неизвестная команда." + Style.RESET_ALL)
            await wait_and_new_lines()

async def start_menu():
    print(Fore.YELLOW + "Запуск меню..." + Style.RESET_ALL)
    while True:
        print(Fore.YELLOW + "--- меню ---" + Style.RESET_ALL)
        print("[1] - CMD интерфейс")
        print("[0] - выход")
        s = input(Fore.MAGENTA + "command >>> " + Style.RESET_ALL)
        if s == "1":
            await cmd_interface()
        elif s == "0":
            print(Fore.YELLOW + "Выход из программы." + Style.RESET_ALL)
            break

if __name__ == '__main__':
    print(Fore.YELLOW + "Запуск программы..." + Style.RESET_ALL)
    asyncio.run(start_menu())