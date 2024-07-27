from datetime import datetime
from argparse import ArgumentParser
from problem_scrapper import ProblemInfoScrapper

judge_sites = ["Leetcode", "백준", "프로그래머스", "정보 올림피아드"]
judge_sites_dict = {"l": "Leetcode", "b": "백준", "p": "프로그래머스", "koi": "정보 올림피아드"}

# TODO: README에 이미 있는 경우 패스하기

class ProblemInfo:
    def __init__(self, link, judge_site):
        self.link = link
        self.judge_site = judge_site
        self.scrapper = ProblemInfoScrapper(self.link, judge_site)
    
    def get_problem_title(self):
        return self.scrapper.get_problem_title()

    def get_problem_type(self):
        return self.scrapper.get_problem_type()

    def get_problem_difficulty(self):
        return self.scrapper.get_problem_difficulty()

def update_readme(file_path):
    judge_site_initial = file_path.split("_")[0]
    judge_site = judge_sites_dict[judge_site_initial] 
    prob_num = file_path.split("_")[1] 
    file_ext = file_path.split(".")[-1]
    solution_path = file_path # relative path

    with open(file_path) as f:
        for line in f.readline():
            first_line = line
            break
        prob_link = first_line.split("#")[-1].strip()
    
    problem = ProblemInfo(prob_link, judge_site)
    prob_title = problem.get_problem_title(prob_link)
    prob_type = problem.get_problem_type(prob_link)
    difficulty = problem.get_difficulty(judge_site)

    with open("./Scripts/sample_readme.md") as f:
        lines = f.readlines()
        site_block = False
        table_block = False
        for i, line in enumerate(lines):
            if line.startswith("##"):
                site_candidate = line.replace("##","").strip()
                if site_candidate in judge_sites and site_candidate == judge_site:
                    site_block = True
                
                if line == """| :-----: | :----: | :-------: | :----------: | :--------: | :-----: | :------: |""":
                    table_block = True
                
                if line == "\n" and table_block is True and site_block is True:
                    problem_title_link = f"![{prob_title}]({prob_link})"
                    index = lines[i-1].split("|")[0]
                    date = datetime.now().date()
                    if file_ext == ".py":
                        language = "Python"
                    solution = f"![{language}]({solution_path})"
                    table_content = f"""| {index} | {prob_type} | {problem_title_link}| {difficulty} | {solution} | {date} |  | """
                    lines.insert(i, table_content)
                    lines.insert(i+1, "\n")
                
if __name__ == "__main__":
    # parser = ArgumentParser()
    # parser.add_argument("--language", )
    file_path = ""
    github_path = ""
    
    update_readme(file_path)
