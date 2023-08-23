# IMPORTANTE: Hacer siempre antes de editar archivos del proyecto
* Abrir el proyecto desde la carpeta en VS Code (Click derecho > Open with Code)
* En VS Code abrir la terminal con CTRL + ñ
```bash
# Traer cambios de repositorio remoto
git pull
```
# BUENAS PRÁCTICAS
* Realizar commits pensando en agrupar cambios que cuando se nombre el cambio pueda ser entendido por cualquier persona (ej: Gráfica y función de outliers).
* No hacer commits de cambios muy pequeños (a no ser que sea un cambio muy importante).
* Si se hacen 2 cosas importantes en el proyecto, hacer 2 commits.


# PASO A PASO SUBIR CAMBIOS  A GITHUB
```bash
# Ver estado de archivos
git status
# Agregar cambios
git add . 
# Confirmar cambios
git commit -m "mensaje"
# Traer cambios de repositorio remoto
git pull
# Subir cambios a repositorio remoto
git push 
```


# Instalación de Git
Para instalar Git en Windows, descargue el instalador desde la página web de Git: https://git-scm.com/download/win




# Configuración de Git desde terminal 
Abrir terminal de Git Bash o en VS Code con Ctrl + ñ
## Configurar nombre de usuario
```bash
git config --global user.name "nombre_usuario"
```
## Configurar correo electrónico
```bash
git config --global user.email "correo_electronico"
```
## Verificar configuración
```bash
git config --list
```




# Integrantes del proyecto
## Agregar colaboradores
Ir a la página de Github y agregar colaboradores en Settings > Manage access > Invite a collaborator
## Clona el repositorio (Una sola vez)
```bash
git clone <url_repositorio>
```
## Conectar al repositorio remoto
En carpeta del proyecto en VS Code escribir CTRL + ñ para abrir terminal
```bash
git remote add origin <url_repositorio>
```
Estamos diciendo que queremos que se vincule el repositorio local con el repositorio remoto seleccionado.