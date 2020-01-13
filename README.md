# Drakengard3-helper
This program can help you defeat the final boss in Drakengard 3
Arrow control. Press the spacebar when you destroy the first note.

## English:

### How to run
Just run release/dod3.exe 

OR
1. Install python3 and add it to PATH system variable
2. Run download.bat to install packages.
(optional)Edit the main\config.ini
3. Run dod.py in "main" folder. Use 'python.exe dod.py' or '[path to python]\python.exe dod.py' (without ') to do it.


### Note time movements:

left-increase the time of the last destroyed note by 50ms

right - reduce the time of the last destroyed note by 50ms

ctrl+left-  increase the time of the first approaching note by 50 ms

ctrl+right - reduce the time of the first approaching note by 50 ms

shift+left-increase the time for all notes by 50ms

shift+right - reduce the time for all notes by 50ms

### Game time movements:

up(hold) - slow down time

down(hold)- speed up time

ctrl+up - rewind time by 50 ms

ctrl+down- increase time by 50 ms

space - Start the game. Then pause/unpause

r - restart

utils\timeing.py

This program needs to write timings from a video to the text file.
It records when the pixel is greater than the threshold, then locks - cannot record any more.
Unlocks when the pixel is less than the second threshold - can record.
See example config for more details



## Russian:
Управление на стрелочках. Нажмите пробел в тот момент, когда уничтожаете первую ноту.

### Запуск.

Просто запустите release/dod3.exe

ИЛИ
1. Установить python3 и pip3 с включением его в переменную среды path
2. Запустить download.bat для установки доп. пакетов
(Опционально)Настроить программу в файле main\config.ini
3. Запустить файл dod.py в каталоге main с помощью команды python.exe dod.py или [путь к python]\python.exe dod.py  


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

utils\timeing.py

Данная программа нужна, чтобы считать тайминги с видео и записать их в файл. 
Работает по принципу считывания пикселя. Когда он превышает определенный диапазон - записывается время
