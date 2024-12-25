import subprocess

# Path to your requirements.txt file
requirements_file = 'failed_packages.txt'

# Open the requirements.txt file and read line by line
with open(requirements_file, 'r') as file:
    packages = file.readlines()

# Strip any extra whitespace and newline characters
packages = [pkg.strip() for pkg in packages]

# Iterate over each package and attempt installation
for package in packages:
    try:
        print(f"Installing {package}...")
        # Run the pip install command
        subprocess.check_call([ 'pip', 'install','--upgrade', package])
        print(f"{package} installed successfully.")
    except subprocess.CalledProcessError as e:
        with open('failed_packages1.txt', 'a') as f:
            f.write(f"{package}\n")
            print(f"Failed to install {package}. Moving to next package.")
    