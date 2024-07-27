import os
import logging
import json
import requests
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

class BaekjoonScrapper:
    def __init__(self, url):
        self.url = url
        self.response = self.scrap()

    def scrap(self):
        problem_id = self.url.split("/")[-1]
        url = f'https://solved.ac/api/v3/problem/show?problemId={problem_id}'
        for i in range(3):
            response = requests.get(url, timeout=60)
            try:
                if response.status_code == 200:
                    response = response.json()
                    break
            except Exception as e:
                logger.error("%s: Failed to get JSON result. Retrying... %d/3", e, i+1)

        return response
    
    def get_problem_title(self):
        if not isinstance(self.response, dict):
            return
        return f'{self.response["problemId"]}. {self.response["titleKo"]}'
    
    def get_problem_type(self):
        if not isinstance(self.response, dict):
            return
        try:
            return self.response["tags"][0]["displayNames"][0]["name"]
        except Exception as e:
            logger.error("%s", e)

    def get_problem_difficulty(self):
        if not isinstance(self.response, dict):
            return
        
        difficulty = self.response["level"]
        medal = difficulty // 5
        medal_color = {0: "Bronze", 1: "Silver", 2: "Gold", 3: "Platinum", 4:"Diamond", 5:"Ruby"}
        level_num = 6 - (difficulty % 5)
        difficulty_name = f"{medal_color[medal]} {level_num}"
        if difficulty_name:
            return difficulty_name
        

class LeetcodeScrapper:
    def __init__(self, url):
        self.url = url
        self.response = self.scrap()

    def scrap(self):
        title_slug = self.url.strip("/").split("/")[-1]
        
        url = 'https://leetcode.com/graphql'

        headers = {
            'Content-Type': 'application/json'
        }
        query = """
            query getQuestion($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                questionFrontendId
                questionTitle
                difficulty
                categoryTitle
                topicTags {
                    name
                    }
                content
                }
            }
            """

        variables = {
            'titleSlug': ''
        }

        variables['titleSlug'] = title_slug

        data = {
            'query': query,
            'variables': variables
        }

        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            result = response.json()
            question = result['data']['question']
            return question
        else:
            logger.error(f"Failed to fetch data: {response.status_code}")

        return None
    
    def get_problem_title(self):
        return f"{self.response['questionFrontendId']}. {self.response['questionTitle']}"

    def get_problem_type(self):
        return [tag['name'] for tag in self.response["topicTags"]]

    def get_problem_difficulty(self):
        return self.response["difficulty"]
    
class ProgrammersScrapper:
    def __init__(self, url) -> None:
        self.link = url
        self.response = self.scrap()
    
    def scrap(self):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup

    def get_problem_title(self):
        title = self.response.find('title').get_text()
        title = title.replace("코딩테스트 연습 -", "").replace("| 프로그래머스 스쿨", "").strip()
        return title

    def get_problem_type(self):

        breadcrumb = self.response.find('ol', class_='breadcrumb')
        data = breadcrumb.find_all('li')[1]
        # print(data)
        text = data.find('a').text
        return text

    def get_problem_difficulty(self):
        div = self.response.find('div', {'data-hackle-view': True})
        data_hackle_view = div['data-hackle-view']
        data = json.loads(data_hackle_view)
        key = data['key']
        properties = data['properties']
        return properties["challenge_level"]

class ProblemInfoScrapper:
    def __init__(self, url, judge_site):
        if judge_site == "Leetcode":
            scrapper = LeetcodeScrapper(url)
        elif judge_site == "백준":
            scrapper = BaekjoonScrapper(url)
        elif judge_site == "프로그래머스":
            scrapper = ProgrammersScrapper(url)
        
        return scrapper

# def update_readme(py_file):
#     scrapper = ProblemDifficultyScrapper()
#     readme_path = 'README_TEST.md'
#     difficulty = "NA"
#     base_name = os.path.basename(py_file.lower())
#     with open(readme_path, 'w', encoding="utf8") as readme:
#         readme.write('# Python Files in This Repository\n\n')
#         readme.write(f'- {py_file}\n')
#         if base_name.startswith('l'):
#             url = f"https://leetcode.com/problems/{py_file.split('/')[-1].replace('.py', '').replace('_', '-')}/"
#             difficulty = scrapper.get_leetcode_problem_difficulty(url)

#         elif base_name.startswith('b'):
#             problem_id = base_name.split("_")[1]
#             difficulty = scrapper.get_baekjoon_problem_difficulty(problem_id)
#             print(difficulty)

#         if difficulty:
#             readme.write(f'  - Difficulty: {difficulty}\n')


if __name__ == "__main__":
    # update_readme('data_structures_and_algorithms/Algorithms/GraphAlgorithms/BFS_and_DFS/Problems/b_1260_dfs_and_bfs.py')
    # url = "https://www.acmicpc.net/problem/2798"
    url = "https://www.acmicpc.net/problem/2798"
    srp = BaekjoonScrapper(url)

    print(srp.get_problem_difficulty())
    print(srp.get_problem_title())
    print(srp.get_problem_type())
    # url = "https://leetcode.com/problems/merge-sorted-array/"
    # url = "https://leetcode.com/problems/number-of-good-pairs"
    # leetcode = LeetcodeScrapper(url)
    # print(leetcode.get_problem_difficulty())
    # print(leetcode.get_problem_title())
    # print(leetcode.get_problem_type())
    # url = "https://school.programmers.co.kr/learn/courses/30/lessons/43236"
    # scrapper = ProgrammersScrapper(url)
    # print(scrapper.get_problem_title())
    # print(scrapper.get_problem_type())
    # print(scrapper.get_problem_difficulty())
