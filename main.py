import os
import asyncio
from Scanner import CodeScanner
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(r"C:\Users\aasth\OneDrive\Desktop\ScanReCLI\ScanRE_CLI\.env")

art = """
█▀▀ █▀▀ █▀▀█ █▀▀▄ ░█▀▀█ ░█▀▀▀
▀▀█ █   █▄▄█ █  █ ░█▄▄▀ ░█▀▀▀
▀▀▀ ▀▀▀ ▀  ▀ ▀  ▀ ░█ ░█ ░█▄▄▄
"""

if __name__ == '__main__':
    print(art)
    
    # Fetch environment variables
    scanType = os.getenv("SCAN_TYPE")
    targetsFilePath = os.getenv("TARGETS_FILE")
    print(f"TARGETS_FILE: {targetsFilePath}")
    
    if not targetsFilePath:
        print("Error: TARGETS_FILE is not set in the .env file or is empty.")
        exit(1)

    # Open targets file
    with open(targetsFilePath, "r") as targets:
        if int(scanType) == 1:
            print("[*] Scanning repos listed in:" + targetsFilePath)
            
            # Process each target (repo)
            for target in targets:
                if target is None or target == "/n":
                    print("* Target was empty")
                    print("* Exiting")
                    break
                else:
                    target = target.strip()
                    values = target.split("/")
                    repoLink = target
                    
                    # Sanity checks for scan path and result path
                    path = os.getenv("SCAN_PATH")
                    if path is None:
                        exit("* Scan path cannot be null")
                    
                    repoName = values[4]
                    if repoName is None:
                        exit("* Repo name cannot be null")
                    
                    scanResultPath = os.getenv("RESULT_PATH")
                    if scanResultPath is None:
                        exit("* Scan result path cannot be null")
                    
                    # Initialize CodeScanner
                    try:
                        scanner = CodeScanner(repoLink, path, repoName, scanResultPath)
                    except Exception as e:
                        print(f"* Error initializing scanner: {e}")
                        continue
                    
                    # Run scanning functions
                    try:
                        asyncio.run(scanner.getCode())
                    except Exception as e:
                        print(f"* Error cloning repository: {e}")
                    
                    try:
                        asyncio.run(scanner.scanCode())
                    except Exception as e:
                        print(f"* Error scanning the code: {e}")
                    
                    try:
                        asyncio.run(scanner.generateReport())
                    except Exception as e:
                        print(f"* Error generating the report: {e}")
                    
                    try:
                        asyncio.run(scanner.cleanUp())
                    except Exception as e:
                        print(f"* Error cleaning up: {e}")
        else:
            # Code for scanning from folders
            for folder in targets:
                if folder is None:
                    print("Folder can't be None")
                    break
                
                print("[*] Scanning code present in folder:" + folder)
                
                # Path and repo name for folder scanning
                path = os.getenv("SCAN_PATH")
                if path is None:
                    exit("* Scan path cannot be null")
                
                repoName = folder.strip()
                if repoName is None:
                    exit("* Repo name cannot be null")
                
                scanResultPath = os.getenv("RESULT_PATH")
                if scanResultPath is None:
                    exit("* Scan result path cannot be null")
                
                repoLink = " "
                scanner = CodeScanner(repoLink, path, repoName, scanResultPath)
                asyncio.run(scanner.scanCode())
