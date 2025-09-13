import os 
import sys

setup_path = os.path.join(os.path.dirname(__file__), "setup")
sys.path.append(setup_path)

from setup import setup_app

setup_app.setup.pip_checker()
setup_app.setup.modules_installer()
