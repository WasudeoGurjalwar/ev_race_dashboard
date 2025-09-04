



@echo off
SET "ProjectRoot=C:\Users\Wasu\OneDrive\Desktop\GUI\ev_race_dashboard\"

echo This is a source code file. >"%ProjectRoot%main.py"
echo This is a source code file. >"%ProjectRoot%server.py
echo This is a document. > "%ProjectRoot%requirements.txt"


MD "%ProjectRoot%\models"
echo This is a source code file. >"%ProjectRoot%\models\__init__.py"
echo This is a source code file. >"%ProjectRoot%\models\ev_client.py"
echo This is a source code file. >"%ProjectRoot%\models\charging_station.py"


MD "%ProjectRoot%\panels"
echo This is a source code file. >"%ProjectRoot%\panels\__init__.py"
echo This is a source code file. >"%ProjectRoot%\panels\map_panel.py"
echo This is a source code file. >"%ProjectRoot%\panels\communication_panel.py"
echo This is a source code file. >"%ProjectRoot%\panels\race_control_panel.py"


MD "%ProjectRoot%\networking"
echo This is a source code file. >"%ProjectRoot%\networking\__init__.py"
echo This is a source code file. >"%ProjectRoot%\networking\signal_handler.py"


echo Folder structure created successfully at %ProjectRoot%
pause
