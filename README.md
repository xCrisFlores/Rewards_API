#Rewards API
Una aplicacion sencilla y rapida construida usando el framework Django, para la visualizacion de compras y recompensas de los usuarios.
##¿Como probarla?
Deberas abrir una terminal de PowerShell o CMD en la carpeta del proyecto para activar el entorno virtual de Django, simplemente ejecuta los siguientes comandos:
```shell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
env\Scripts\Activate
```
El primer comando es para evitar conflictos de permisos con la linea de comandos.
Posterior a esto debemos instalar las dependencias del proyecto, debes tener instalado previamente Python en la maquina donde desees probar el proyecto, si ya tienes Python instalado puedes ejecutar los siguientes comandos:
```python
pip install -r requirements.txt
python manage.py runserver
```
Esto deberia ejecutar el servidor de Django mostrandote un mensaje asi:

    Run 'python manage.py migrate' to apply them.
    December 05, 2024 - 13:53:32
    Django version 5.1.4, using settings 'mysite.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.

Ahora puedes ejecutar cada una de las request de prueba haciendo uso de otra terminal PowerShell simplemente copia y pega de una por una y ejecutalas, y veras las respuestas de estas request. 
Ademas si vas a la ruta:  http://127.0.0.1:8000/swagger/
podras interactuar de forma mas amigable con las request GET en una interfaz de Swagger.
Finalmente si deseas cerrar el proyecto presiona Ctrl + C o cierra las terminales.