# -*- coding: utf-8 -*-
# Copyright 2021 IATE Development Group
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# Copyright 2021 IATE Development Group
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


#module load openmpi/4.1.2rc1 
# module load hdf5/1.10.7
import sys
import git
import subprocess
import os
from interface import implements, Interface 
from iate_file import find_argument

SEPARATOR_ARG = '='
INSTALL_FLASH = 'PATH_FLASH'
INSTALL_PATH = 'PATH'
MAKEFILE_PATH = 'PATH_MAKE'
DEFAULT_PATH = './'
K_OLD = 'old'
K_NEW = 'new'
K_NOMBRE_SERVIDOR = 'serafin'
K_DEFAULT_SETUP_FLASH = './setup Sedov -auto'
K_DEFAULT_FLASH = 'SETUP_FLASH'

class LibraryInstall(Interface):
    """ Se encarga en la instalacion de la libreria """
    def install(self):
        """ Instalacion de la libreria
        Args: nulll
        
        Returns : null
             
        """
        pass

class UpdateConfigFile:
    """ Clase para la configuracion de los archivos"""
    def __init__(self, path_install_aux):
        """
        ARG: path_install_aux = path de instalacion

        """
        self.path_install = path_install_aux
    """    """
    def update_file(self, str_in_file, str_out_file, list_values):
        """ Actualiza un archivo utilizando una lista de valores
        Args:
             str_in_file (string): path del archivo que va a modificarse
             str_out_file (string): path del archivo donde se va a guardar
             list_values [{K_OLD: ,K_NEW: },{},...] = array de diccionario de 
                 texto que se va a cambiar.
        Returns: null

        """
        in_file = open(str_in_file, 'rt')
        data = in_file.read()
        for item in list_values:
            data = data.replace(item[K_OLD],item[K_NEW] + '\n #', 1)
        in_file.close()

        out_file = open(str_out_file, 'wt')
        out_file.write(data)
        out_file.close()


    def update(self, path_in, path_out):
        """ Actualiza los archivos de configuracion necesarios
        Args:
            path_in (string): path del archivo que va a modificarse
            path_out (string): path del archivo donde se va a guardar

        Returns null:

        """
        pass

class ZlibForFlash(UpdateConfigFile, implements(LibraryInstall)):
    """ class   """
    def install(self):
        """ C 
        Args:
             

        Returns []:
             
        """
        path_zlib = self.path_install + '/zlib'
        str_requeriments = 'module load gcc;'
        str_command1 = str_requeriments + path_zlib +"/"+"./configure --prefix=" + path_zlib +";"
        str_command2 = str_requeriments + 'make;'
        str_command3 = str_requeriments + 'install;'

        os.chdir(self.path_install)
        git.Git(self.path_install).clone('git://github.com/madler/zlib.git')
        os.chdir("zlib")
        #os.getcwd()
        #os.listdir("./")
        os.system(str_command1)

        print("---------------")
        
        print(str_command1)
        os.system(str_command2)
        os.system(str_command3)

    def update(self, path_in, path_out):
        """ Actualiza los archivos de configuracion necesarios
        Args:
            path_in (string): path del archivo que va a modificarse
            path_out (string): path del archivo donde se va a guardar

        Returns null:

        """
        old_path = 'ZLIB_PATH'
        new_path = old_path + ' = '+self.path_install + '/zlib'
        list_values = [{K_OLD : old_path, K_NEW : new_path}]
        self.update_file(path_in, path_out, list_values)

class HypreForFlash(UpdateConfigFile, implements(LibraryInstall)):
    """ class   """
    def install(self):
        """ C 
        Args:
             

        Returns []:

        """
        str_requeriments = 'module load gcc;module load openmpi;module load hdf5;'
        path_hypre = self.path_install + '/hypre'
        os.chdir(self.path_install)
        git.Git(self.path_install).clone('git://github.com/hypre-space/hypre.git') 

        os.chdir(path_hypre)
        os.chdir('src/')
        os.system(str_requeriments + "./configure")
        os.system(str_requeriments + "make install")

    def update(self, path_in, path_out):
        """ Actualiza los archivos de configuracion necesarios
        Args:
            path_in (string): path del archivo que va a modificarse
            path_out (string): path del archivo donde se va a guardar

        Returns null:

        """
        old_path = 'HYPRE_PATH'
        new_path = old_path + ' = ' + self.path_install + '/src/hypre/'
        list_values = [{K_OLD : old_path, K_NEW : new_path}]
        self.update_file(path_in, path_out, list_values)


class OpenmpiForFlash(UpdateConfigFile, implements(LibraryInstall)):
    """ class   """
    def install(self):
        """ C 
        Args:

        Returns []:
             
        """
        pass


    def update(self, path_in, path_out):
        """ Actualiza los archivos de configuracion necesarios
        Args:
            path_in (string): path del archivo que va a modificarse
            path_out (string): path del archivo donde se va a guardar

        Returns null:

        """
        old_path = 'MPI_PATH'
        new_path = old_path + ' = ' + '/opt/ccad/21.11/software/linux-rocky8-zen2/gcc-11.2.0/'\
                + 'openmpi-4.1.2rc1-i4qr6kksz2oyqahqkcm3o65gin43u66q/'
        list_values = [{K_OLD : old_path, K_NEW : new_path}]
        self.update_file(path_in, path_out, list_values)


class Hdf5ForFlash(UpdateConfigFile, implements(LibraryInstall)):
    """ class   """
    def install(self):
        """ C
        Args:

        Returns []:
        """
        pass

    def update(self, path_in, path_out):
        """ Actualiza los archivos de configuracion necesarios
        Args:
            path_in (string): path del archivo que va a modificarse
            path_out (string): path del archivo donde se va a guardar

        Returns null:

        """
        old_path = 'HDF5_PATH'
        new_path =  old_path + ' = ' + '/opt/ccad/21.11/software/linux-rocky8-zen2/gcc-11.2.0/'\
                + 'hdf5-1.10.7-qfccxkq6wbldsmmjoix2kqgltaostyma/'
        list_values = [{K_OLD : old_path, K_NEW : new_path}]
        self.update_file(path_in, path_out, list_values)



# Paso de argumentos
#  python install_program.py PATH=/home/srgualpa/pruebas PATH_MAKE=/home/srgualpa/projects/flash/instalacion_script_python/make_original PATH_FLASH=/home/srgualpa/pruebas/FLASH4.6.2  SETUP_FLASH='./setup Sedov -auto'
#   
if __name__ == '__main__':
    #

    path_inst = ''
    path_make = ''
    path_make = ''
    command_setup_flash = ''
    print('*** *** Instalacion de Flash en el servidor Serafin *** ***')

    path_act = str(os.getcwd())
    path_inst = find_argument(sys.argv, INSTALL_PATH, SEPARATOR_ARG, path_act)
    path_make = find_argument(sys.argv, MAKEFILE_PATH, SEPARATOR_ARG, path_act)
    path_flash = find_argument(sys.argv, INSTALL_FLASH, SEPARATOR_ARG, path_act + '/flash')
    command_setup_flash = find_argument(sys.argv, K_DEFAULT_FLASH, \
                                        SEPARATOR_ARG, K_DEFAULT_SETUP_FLASH)

    print('Lugar de instalacion:  de las librerias', path_inst)
    print('Lugar de makefile ', path_make) 
    print('Lugar de flash ', path_flash) 





    os.chdir(path_flash)
    os.chdir('sites')
    os.makedirs(K_NOMBRE_SERVIDOR, mode=511, exist_ok=True)


    openmpi = OpenmpiForFlash(path_inst)
    hdf5 = Hdf5ForFlash(path_inst)
    zlib = ZlibForFlash(path_inst)
    hypre = HypreForFlash(path_inst)
    
    library_list =[openmpi, hdf5, zlib, hypre]

    flag_first_loop = True
    out_path_inst_make_aux = path_flash + '/sites/' + K_NOMBRE_SERVIDOR + '/Makefile.h'
    for library in library_list:
        library.install()
        if(flag_first_loop):
            in_path_make_aux = path_make + '/Makefile.h'
            flag_first_loop = False
        else:
            in_path_make_aux = out_path_inst_make_aux
        library.update(in_path_make_aux, out_path_inst_make_aux)
    
    os.chdir(path_flash)
    os.system(command_setup_flash)
    os.chdir(path_flash + '/object')
    os.system('make -j 16')
