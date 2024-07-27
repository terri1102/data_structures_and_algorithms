import os

def convert_to_py(file_path):
    if not os.path.exists(file_path):
        print("File does not exist")
    if os.path.splitext(file_path)[1] == ".md":
        with open(file_path) as f:
            lines = f.readlines()
        for i, line in enumerate(lines):
            if line.strip() == "```python":
                start_line = i + 1
            elif line.strip() == "```":
                end_line = i
        python_lines = lines[start_line: end_line]
    base_name = os.path.splitext(file_path)[0]

    with open(f"{base_name}.py", "w", encoding="utf8") as f:
        f.write("".join(python_lines))
        
if __name__ == "__main__":
    file_name = "./DataStructure/ArraysAndString/p_jadencase.md"
    convert_to_py(file_name)