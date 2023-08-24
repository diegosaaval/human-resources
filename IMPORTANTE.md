# IMPORTANTE
Hacer esto siempre antes de editar archivos del proyecto
1. Abrir el proyecto desde la carpeta en VS Code (Click derecho > Open with Code)
2. En VS Code abrir la terminal con (CTRL + ñ)
3. Escribir el siguiente comando
```bash
# Traer cambios de repositorio remoto
git pull
```
# BUENAS PRÁCTICAS
* Realizar commits pensando en agrupar cambios que cuando se nombre el cambio pueda ser entendido por cualquier persona (ejemplos de commits: Gráfica y función de outliers, cambios en el modelo predictivo, cambios en el hiperparámetro, eliminación de datos nulos, etc.).
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




# Configuración de Git 
Abrir terminal de Git Bash, buscando Git Bash en el buscador de Windows y escribir el siguiente comando
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




# Proceso para integrantes del proyecto
Este proceso se debe realizar una sola vez para clonar el repositorio en la computadora local

## 1. Ir a la Git Bash y escribir el siguiente comando
```bash
cd Desktop
```
## 2. Clona el repositorio en la carpeta Desktop
```bash
git clone <url_repositorio>
```
## 3. Abrir el proyecto desde la carpeta en VS Code
(Click derecho en carpeta > Open with Code)

## 4. Verificar el status de los archivos
En VS Code apretar (Ctrl + ñ) para abrir la terminal y escribir el siguiente comando
```bash
git status
```
## 5. Ya podría empezar a trabajar en el proyecto y hacer commits