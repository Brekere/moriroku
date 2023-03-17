@echo off
start "" "C:\Program Files\Google\Chrome\Application\chrome" --chrome --kiosk -fullscreen  http://localhost:5000/ --disable-pinch --no-user-gesture-required --overscroll-history-navigation=0
@echo "Lanzamiento de Navegador listo"
@echo "Ejecutando servidor python"
py run.py