import os
import requests
import yaml
from glob import glob


def request_problem(problem_number):
    res = requests.get(f"https://www.acmicpc.net/problem/{problem_number}")
    if res.status_code != 200:
        raise Exception("Response get not 200 status code.")
    title_si = res.text.find('<span id="problem_title">') + len('<span id="problem_title">')
    title_ei = res.text.find("</span>", title_si)
    title = res.text[title_si:title_ei]

    return title


if __name__ == "__main__":
    with open("users.yaml", "r", encoding="utf-8") as users_yaml:
        users = yaml.safe_load(users_yaml)

    with open("problems.yaml", "r", encoding="utf-8") as problems_yaml:
        problems = yaml.safe_load(problems_yaml)

    body = ""
    for subtitle, prob_list in problems.items():
        body += f"### {subtitle}\n\n"

        table = "|문제|" + "|".join(list(users.keys())) + "|\n"
        table += "|:---|" + ":---:|" * len(users) + "\n"

        for prob_index in prob_list:
            prob_title = request_problem(prob_index)
            row = f"|[{prob_index}. {prob_title}](https://www.acmicpc.net/problem/{prob_index})|"

            for user_name, user_info in users.items():
                user_format = user_info["format"].replace("{prob_index}", f"{prob_index}").replace("{prob_title}", f"{prob_title}")
                solutions = glob(f"{user_info['dir']}/{user_format}.*")

                user_solutions = []
                for solution_path in solutions:
                    file_name, extension = os.path.basename(solution_path).split(".")
                    user_solutions.append(f"[{extension}]({solution_path})")
                row += "/".join(user_solutions) + "|"

            table += row + "\n"

        body += table + "\n"

    with open("header.md", "r", encoding="utf-8") as header_md:
        header = header_md.read()
        body = header + "\n" + body

    with open("footer.md", "r", encoding="utf-8") as footer_md:
        footer = footer_md.read()
        body = body + "\n" + footer

    with open("README.md", "w", encoding="utf-8") as md_out:
        md_out.write(body)
