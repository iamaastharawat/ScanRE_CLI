import os
import json
from json2html import json2html

class CodeScanner:
    def __init__(self, repoLink, scanPath, repoName, scanResultPath):
        self.repoLink = repoLink
        self.scanPath = scanPath
        self.repoName = repoName
        self.scanResultPath = scanResultPath

    async def getCode(self):
        # Simulate cloning the repository
        print(f"Cloning repository: {self.repoLink} into path: {self.scanPath}")
        # Example: Clone the repo (e.g., using Git) here
    
    async def scanCode(self):
        # Simulate scanning the code
        print(f"Scanning code in repository: {self.repoName} located at: {self.scanPath}")
        # Example: Run Semgrep or other scanning tools here

    async def generateReport(self):
        try:
            # Ensure the scan result directory exists before generating the report
            if not os.path.exists(self.scanResultPath):
                os.makedirs(self.scanResultPath)  # Create the directory if it doesn't exist

            # Generate the report (this example assumes it's a JSON file)
            report_file = os.path.join(self.scanResultPath, f"{self.repoName}.json")
            # Simulate report creation
            data = {
                "repo": self.repoName,
                "status": "success",
                "findings": []
            }
            with open(report_file, "w") as f:
                json.dump(data, f)
            
            # Convert JSON to HTML
            output = json2html.convert(json=data)
            html_file = os.path.join(self.scanResultPath, f"{self.repoName}.html")

            with open(html_file, "w") as file:
                file.write(output)

            print(f"Report generated: {html_file}")

        except Exception as e:
            print(f"Error generating report: {e}")

    async def cleanUp(self):
        # Cleanup logic (e.g., remove temporary files)
        print(f"Cleaning up after scan of {self.repoName}")
