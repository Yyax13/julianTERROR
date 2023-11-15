import os
import subprocess

def pip(package):
    try:
        subprocess.check_output(["pip", "show", package])
        print(f'{package} already installed')
    except subprocess.CalledProcessError:
        os.system(f'pip install {package}')
        print(f'Done')
