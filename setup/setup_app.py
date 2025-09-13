import os  
import sys

class setup:
    @staticmethod
    def pip_checker():
        pip_path = os.path.join(sys.exec_prefix, 'Scripts')

        if os.path.exists(pip_path):
            print(f"Path found: {pip_path}")
            return True
        else:
            print(f"Path {pip_path} does not exist. Install Python (with pip) or add pip to Path")
            return False
        
    @staticmethod
    def modules_installer():
        os.system("pip install cryptography")
        os.system("pip install requests")
        os.system("pip install ")
