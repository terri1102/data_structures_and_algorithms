import os
import requests
from bs4 import BeautifulSoup

class ProblemDifficultyScrapper:
    def get_leetcode_problem_difficulty(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        difficulty_span = soup.find('span', class_='css-14oi08n')
        
        if difficulty_span:
            difficulty = difficulty_span.text.strip()
            return difficulty
        return None

    def get_baekjoon_problem_difficulty(self, problem_id):
        url = f'https://solved.ac/api/v3/problem/show?problemId={problem_id}'
        response = requests.get(url, timeout=60)
        try:
            response = response.json()
            difficulty = response["level"]
        except Exception as e:
            print("%e: Failed to get json result", e)
            return None
        medal = difficulty // 5
        medal_color = {0: "Bronze", 1: "Silver", 2: "Gold", 3: "Platinum", 4:"Diamond", 5:"Ruby"}
        level_num = 6 - (difficulty % 5)
        difficulty_name = f"{medal_color[medal]} {level_num}"
        if difficulty_name:
            return difficulty_name

    def get_programmers_problem_difficulty(self, problem_id):
        url = f'https://programmers.co.kr/learn/courses/30/lessons/{problem_id}'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        difficulty_span = soup.find('div', class_='algorithm-content')
        difficulty_div = difficulty_span.find('span', class_='level-label')
        
        if difficulty_div:
            difficulty = difficulty_div.text.strip()
            return difficulty
        return None
    

# # Path to the README file
# readme_path = 'README.md'

# # Get list of all .py files in the repository
# py_files = []
# for root, dirs, files in os.walk('.'):
#     for file in files:
#         if file.endswith('.py'):
#             py_files.append(os.path.join(root, file))

# # Create or update the README file with the list of .py files
# with open(readme_path, 'w') as readme:
#     readme.write('# Python Files in This Repository\n\n')
#     readme.write('This README file lists all Python files in the repository along with their difficulty levels.\n\n')
#     for py_file in py_files:
#         readme.write(f'- {py_file}\n')
#         if 'leetcode' in py_file.lower():
#             url = f"https://leetcode.com/problems/{py_file.split('/')[-1].replace('.py', '').replace('_', '-')}/"
#             difficulty = get_leetcode_problem_difficulty(url)
#             if difficulty:
#                 readme.write(f'  - Difficulty: {difficulty}\n')



# # Example usage
# problem_id = '1000'
# difficulty = get_baekjoon_problem_difficulty(problem_id)
# if difficulty:
#     print(f"The difficulty level of Baekjoon problem {problem_id} is: {difficulty}")
# else:
#     print("Difficulty level not found or problem page might be formatted differently.")






# # Example usage
# problem_id = '42748'
# difficulty = get_programmers_problem_difficulty(problem_id)
# if difficulty:
#     print(f"The difficulty level of Programmers problem {problem_id} is: {difficulty}")
# else:
#     print("Difficulty level not found or problem page might be formatted differently.")

def update_readme(py_file):
    scrapper = ProblemDifficultyScrapper()
    readme_path = 'README_TEST.md'
    difficulty = "NA"
    base_name = os.path.basename(py_file.lower())
    with open(readme_path, 'w', encoding="utf8") as readme:
        readme.write('# Python Files in This Repository\n\n')
        readme.write(f'- {py_file}\n')
        if base_name.startswith('l'):
            url = f"https://leetcode.com/problems/{py_file.split('/')[-1].replace('.py', '').replace('_', '-')}/"
            difficulty = scrapper.get_leetcode_problem_difficulty(url)

        elif base_name.startswith('b'):
            problem_id = base_name.split("_")[1]
            difficulty = scrapper.get_baekjoon_problem_difficulty(problem_id)
            print(difficulty)

        if difficulty:
            readme.write(f'  - Difficulty: {difficulty}\n')

def update_readme_all():
    pass

if __name__ == "__main__":
    update_readme('data_structures_and_algorithms/Algorithms/GraphAlgorithms/BFS_and_DFS/Problems/b_1260_dfs_and_bfs.py')
