 Script para la instalacion de flash en serafin

 Instalacion

#requerimientos : tener instalado conda y el instalador de flash

Pasos:
1) Ir a la carpeta de instalacion
1) git clone https://gitlab.com/srgualpa_iate/install_program.git
2) cd install_program
3) cp -r path_de_la_carpeta_raiz_flash flash/
   El path debe incluir el nombre de la carpeta raiz de flash
   osea si ejecutamos 
   ls path_de_la_carpeta_raiz_flash
   nos debe dar 
   LICENSE  RELEASE  RELEASE-NOTES  bin  docs  lib  object  setup  setup_alt  sites  source  tools 
4) conda create --name flash_instalacion python=3.7
5) conda activate flash_instalacion
6) pip install -r requirements.txt -v
7) python install_program.py