from os import makedirs, path

from bs4 import BeautifulSoup
from httpx import get

URL_BASE = "https://www.beecrowd.com.br/repository/UOJ_"


class SelectorsShema:
    title: str = "title"
    problem_description: str = ".description"
    _input: str = ".input"
    output: str = ".output"


def get_html(challenge: int):
    req = get(f"{URL_BASE}{challenge}.html")

    if req.status_code != 200:
        return None

    return req.text


def html_to_bs4(html):
    return BeautifulSoup(html, "html.parser")


def challenge_group_folder(challenge_group: str):
    if not path.exists(challenge_group):
        makedirs(challenge_group)


def save_problem(challenge_group: str, challenge: int):
    html = get_html(challenge)
    if html is None:
        return False

    bs = html_to_bs4(html)

    filename = bs.select_one(SelectorsShema.title).text.split("-")[0].strip()
    title = bs.select_one(SelectorsShema.title).text.strip()
    description = bs.select_one(SelectorsShema.problem_description).text.strip()
    _input = bs.select_one(SelectorsShema._input).text.strip()
    output = bs.select_one(SelectorsShema.output).text.strip()
    input_examples = "\n\n".join([el.text.strip() for el in bs.select(".division")])
    output_examples = "\n\n".join(
        [el.text.strip() for el in bs.select(".division + td")]
    )

    challenge_group_folder(challenge_group)

    with open(f"{challenge_group}/{filename}.html", "w", encoding="utf-8") as file:
        file.write(html)

    with open(f"{challenge_group}/{filename}.txt", "w", encoding="utf-8") as file:
        file.write(
            f"""
Desafio: {title}

Descrição:
{description}

Entrada:
{_input}

Saida:
{output}

Exemplo de Entrada:

{input_examples}

Exemplo de Saída:

{output_examples}

"""
        )

    print(f"Desafio {title}!")
    return True


def get_challenges(challenge_group: str, initial_challenge: int = 1000):
    loop = True
    challenge = initial_challenge
    while loop:
        loop = save_problem(challenge_group, challenge)
        challenge += 1


get_challenges("DOWNLOAD", 1000)
