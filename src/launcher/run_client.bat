@echo off
"C:\Program Files\Google\Chrome\Application\chrome" --chrome --kiosk -fullscreen  http://localhost:5055/ --disable-pinch --no-user-gesture-required --overscroll-history-navigation=0
@echo "Lanzamiento de Navegador listo"
@echo "Ejecutando servidor python"
call conda activate base
python run.py
call conda deactivate