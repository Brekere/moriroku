del /f usedPort.txt
netstat -ano -p tcp | find "5000" > usedPort.txt
@echo off
find "5000" usedPort.txt 1>nul &&(
@echo "Ya esta el servidor en ejecución"
start "" "C:\Program Files\Google\Chrome\Application\chrome" --chrome -fullscreen  http://localhost:5000/
@echo "Lanzamiento de Navegador listo"
) || (
@echo "Servidor no esta corriendo"
start "" "C:\Program Files\Google\Chrome\Application\chrome" --chrome -fullscreen  http://localhost:5000/
@echo "Lanzamiento de Navegador listo"
@echo "Ejecutando servidor python"
py run.py
)

cmd /k
