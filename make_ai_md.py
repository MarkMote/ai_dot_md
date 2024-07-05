import os
import subprocess
from datetime import datetime

def get_project_info():
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
# Project Information
Generated on: {current_datetime}

About: 

Stack:

Style guide:

"""

def get_directory_structure():
    cmd = "tree -L 4 -P '*.py' --charset ascii"
    result = subprocess.run(cmd, shell=True, text=True, capture_output=True)
    return f"# Project Directory Structure\n\n```\n{result.stdout}\n```"

def get_file_contents(directory):
    file_contents = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(
                    file_path, start=os.path.dirname(directory)
                )
                with open(file_path, "r") as f:
                    content = f.read()
                file_contents.append(
                    f"## {file}\n\nLocation: {relative_path}\n\n```python\n{content}\n```\n"
                )
    return "# File Contents\n\n" + "\n".join(file_contents)

def generate_ai_md():
    content = [get_project_info(), get_directory_structure(), get_file_contents("src")]
    with open("AI.md", "w") as f:
        f.write("\n\n".join(content))

if __name__ == "__main__":
    generate_ai_md()
    print("AI.md has been generated successfully.")