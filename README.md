# Drakengard3-helper
This program can help you defeat the final boss in drakengard 3

English:
Running.
1. Install python3 and add it to PATH system variable
2. Run download.bat to install packages 
(optional)Edit the main\config.ini
3. Run dod.py in "main" folder. Use 'python.exe dod.py' or '[path to python]\python.exe dod.py' (without ') to do it.   

Arrow control. Press the spacebar when you destroy the first note.

#############Note time movements:
left-increase the time of the last destroyed note by 50ms
rigth-reduce the time of the last destroyed note by 50ms

ctrl+left-  increase the time of the first approaching note by 50 ms
ctrl+rigth- reduce the time of the first approaching note by 50 ms

shift+left-increase the time for all notes by 50ms
shift+rigth-reduce the time for all notes by 50ms

#############Game time movements:
up(hold) - slow down time
down(hold)- speed up time

ctrl+up - rewind time by 50 ms
ctrl+down- increase time by 50 ms

space - Start the game. Then pause/unpause
r - restart



utils\timeing.py
This program needs to write timings from a video to the text file.
It records when the pixel is greater than the threshold, then locks - cannot recod any more.
Unlocks when the pixel is less than the second threshold - can record.
See example config for more details





Russian:
Запуск.
1.Установить python3 с включением его в переменную среды path
2.Запустить download.bat для установки доп. пакетов
(Опционально)Настроить программу в файле main\config.ini
3.Запустить файл dod.py в каталоге main с помощью команды python.exe dod.py или [путь к python]\python.exe dod.py  

Управление на стрелочках. Нажмите пробел в тот момент, когда уничтожаете первую ноту.

###############Управление временем нот:
лево-увеличить время у последней пропавшей ноты на 50мс
право-уменьшить время у последней пропавшей ноты на 50мс

ctrl+лево-  увеличить время у превой приближающейся ноту на 50мс
ctrl+право- уменьшить время у превой приближающейся ноту на 50мс

shift+лево-увеличить время у всех нот на 50мс
shift+право-уменьшить время у всех нот на 50 мс

##############Управление временем игры:
вверх(зажать) - замедлить время
вниз(зажать)- ускорить время

ctrl+вверх - отматать время на 50 мс
ctrl+вниз- увеличить время на 50 мс
space - начать игру. Затем пауза/снятие с паузы
r - начать заного




utils\timeing.py
Данная программа нужна, чтобы ститать тайминги с видео и записать их в файл. 
Работает по принцыпу считывания пикселя (точнее один канал). Когда он превышает определенный диапозон - записывается время и блокируется, пока значение не будет меньше нижнего порога.
