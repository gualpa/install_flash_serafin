# Requirements python
pip install -r requirements.txt -v



el programa se ejecuta 


cp -r  /home/srgualpa/instaladores/FLASH4.6.2/ /home/srgualpa/pruebas/
cd FLASH4.6.2/
cd sites
mkdir serafin
cp ../../Makefile.h serafin/
 
./setup Sedov -auto
cd object/
make -j 16
python install_program.py PATH=/home/srgualpa/pruebas PATH_MAKE=/home/srgualpa/projects/flash/instalacion_script_python/make_original