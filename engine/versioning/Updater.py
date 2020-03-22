from pymsgbox import alert
from shutil import rmtree
from pathlib import Path
from distutils.dir_util import copy_tree
from engine.versioning.AppData import APP_DATA

# Verifica a versão executada e compara com a última (banco de dados)
def verify_version():
    current_version = APP_DATA['version']
    latest_version = '1.0.0.1'
    if (current_version == latest_version):
        return True
    else:
        update_version()
        exit()

# Executa a transferência da nova versão
def update_version():
    source_path = APP_DATA['source-path']
    destiny_path = str(Path().absolute())
    destiny_old_path = destiny_path + '/old/'
    try:
        rmtree(destiny_old_path)
    except:
        pass
    copy_tree(destiny_path, destiny_old_path)
    copy_tree(source_path, destiny_path)
    alert('O aplicativo foi atualizado para sua última versão.\nPor favor, abra-o novamente.', 'Atualização de Versão')
