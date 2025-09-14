import os  
import sys
import shutil

class setup:
    @staticmethod
    def pip_checker():
        pip_path = shutil.which("pip")

        if pip_path:
            print(f"Path found: {pip_path}")
            return True
        else:
            print(f"Path {pip_path} does not exist. Install Python (with pip) or add pip to Path")
            return False
        
    @staticmethod
    def modules_installer():
        pip = shutil.which("pip") or shutil.which("pip3")
        if not pip:
            print("Error: pip not found")
            return
        
        packages = ["cryptography", "requests", "p2pnetwork"]
        for pkg in packages:
            os.system(f"{pip} install {pkg}")