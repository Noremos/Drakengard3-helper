# Drakengard3-helper
This program can help you defeat the final boss in Drakengard 3
Operated with the arrow keys. Press the spacebar the moment you destroy the first note.

## English:

### How to run
For windows
1. Download the program from the release page: https://github.com/UnknownAr/Drakengard3-helper/releases
2. Run dod3.exe 

OR (for any system)
1. Install python3 and add it to PATH system variable
2. Run "python3 -m pip install pygame" to download the dependents (for windows you should write "py" instead of "python3")
2.1 (optional) Configure the program in the main\config.ini file
3. Run the file dod.py in the main directory with python3 dod.py or [python path]\python dod.py (replace python with python3.exe for windows os)


### Note time management:

left - increase time of the last destroyed note by 50ms.

right - decrement the time of the last destroyed note by 50ms.

ctrl+left- increase time of the first approaching note by 50ms.

ctrl+right - decrease the time of the first approaching note by 50ms.

shift+left - increase the time of all notes by 50ms

shift+right - decrease the time of all notes by 50ms

#### Control the playing time:

up(hold) - slow down time

down(hold) - speed up time

ctrl+up- rewind time on 50 ms

ctrl+down- increase time on 50 ms

space - start the game. Then pause / unpause

r - start over

r - restart

utils\timing.py

This program needs to write timings from a video to the text file.
It records when the pixel is greater than the threshold, then locks - cannot record any more.
Unlocks when the pixel is less than the second threshold - can record.
See example config for more details



## Russian:
Управление на стрелочках. Нажмите пробел в тот момент, когда уничтожаете первую ноту.

### Запуск.
Для Windows
1. Скачайте программу: https://github.com/UnknownAr/Drakengard3-helper/releases
2. Запустите dod3.exe

ИЛИ (универсальный способ для любой системы)
1. Установить python3 и pip3 с включением их в переменную среды path
2. Запустить "python3 -m pip install pygame" для установки зависимостей (для windows вместо "python3" надо писать "py")
2.1 (Опционально) Настроить программу в файле main\config.ini
3. Запустить файл dod.py в каталоге main с помощью команды python3 dod.py или [путь к python]\python3 dod.py (для windows вместо python3 надо писать python3.exe)


### Управление временем нот:

лево - увеличить время у последней пропавшей ноты на 50 мс

право - уменьшить время у последней пропавшей ноты на 50 мс

ctrl+лево - увеличить время у первой приближающейся ноте на 50 мс

ctrl+право- уменьшить время у первой приближающейся ноте на 50 мс

shift+лево - увеличить время у всех нот на 50 мс

shift+право - уменьшить время у всех нот на 50 мс

### Управление временем игры:

вверх(зажать) - замедлить время

вниз(зажать) - ускорить время

ctrl+вверх - отмотать время на 50 мс

ctrl+вниз - увеличить время на 50 мс

space - начать игру. Затем пауза/снятие с паузы

r - начать заново

utils\timing.py

Данная программа нужна, чтобы считать тайминги с видео и записать их в файл.
Работает по принципу считывания пикселя. Когда он превышает определенный диапазон - записывается время
