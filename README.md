# Log-Analyzer
Windows Log Analyzer

Run as Administrator for viewing or filtering Security Type Log's.
Otherwise run as normal user

Requirements for installing in Windows :
Python
PyQt5 (python.exe -m pip install PyQt5)
PIL (python.exe -m pip install pillow)
pyinstaller ( python.exe -m pip install pyinstaller)

Dir's :
------Images 
      --- logo.png
------main.py

pyinstaller --onefile --windowed --icon=Images/logo.png --add-data="Images/logo.png;Images" 
create LogAnalyzer Folder
copy dist,build,main.spec to LogAnalyzer
copy Image folder to LogAnalyzer/dist
