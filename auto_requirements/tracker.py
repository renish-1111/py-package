import sys
import os
import subprocess
import pkg_resources

REQUIREMENTS_FILE = "requirements.txt"

def get_installed_packages():
    """Get a list of installed packages with versions."""
    return {pkg.key: pkg.version for pkg in pkg_resources.working_set}

def write_requirements():
    """Write current installed packages to requirements.txt."""
    packages = get_installed_packages()
    
    with open(REQUIREMENTS_FILE, "w") as f:
        for pkg, version in sorted(packages.items()):
            f.write(f"{pkg}=={version}\n")
    
    print(f"Updated {REQUIREMENTS_FILE}")

def install_and_track(package_name):
    """Install a package and update requirements.txt."""
    subprocess.run([sys.executable, "-m", "pip", "install", package_name], check=True)
    write_requirements()

if __name__ == "__main__":
    write_requirements()
