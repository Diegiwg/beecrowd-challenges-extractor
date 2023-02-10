from httpx import get
from bs4 import BeautifulSoup
from os import path, makedirs

URL_BASE = "https://www.beecrowd.com.br/repository/UOJ_"


class SelectorsShema:
    title: str = "title"
    problem_description: str = ".description"
    input: str = ".input"
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
    input = bs.select_one(SelectorsShema.input).text.strip()
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
{input}

Saida:
{output}

Exemplo de Entrada:

{input_examples}

Exemplo de Saída:

{output_examples}

"""
        )

    return True


def get_challenges(challenge_group: str, initial_challenge: int = 1000):
    loop = True
    challenge = initial_challenge
    while loop:
        loop = save_problem(challenge_group, challenge)
        challenge += 1


# get_challenges("DOWNLOAD", 1000)

IDS = [
    1000,
    1001,
    1002,
    1003,
    1004,
    1005,
    1006,
    1007,
    1008,
    1009,
    1010,
    1011,
    1012,
    1013,
    1014,
    1015,
    1016,
    1017,
    1018,
    1019,
    1020,
    1021,
    1035,
    1036,
    1037,
    1038,
    1040,
    1041,
    1042,
    1043,
    1044,
    1045,
    1046,
    1047,
    1048,
    1049,
    1050,
    1051,
    1052,
    1059,
    1060,
    1061,
    1064,
    1065,
    1066,
    1067,
    1070,
    1071,
    1072,
    1073,
    1074,
    1075,
    1078,
    1079,
    1080,
    1094,
    1095,
    1096,
    1097,
    1098,
    1099,
    1101,
    1113,
    1114,
    1115,
    1116,
    1117,
    1118,
    1131,
    1132,
    1133,
    1134,
    1142,
    1143,
    1144,
    1145,
    1146,
    1149,
    1150,
    1151,
    1153,
    1154,
    1155,
    1156,
    1157,
    1158,
    1159,
    1160,
    1164,
    1165,
    1172,
    1173,
    1174,
    1175,
    1176,
    1177,
    1178,
    1179,
    1180,
    1181,
    1182,
    1183,
    1184,
    1185,
    1186,
    1187,
    1188,
    1189,
    1190,
    1435,
    1478,
    1534,
    1541,
    1557,
    1564,
    1589,
    1759,
    1789,
    1827,
    1828,
    1837,
    1847,
    1848,
    1858,
    1864,
    1865,
    1866,
    1914,
    1924,
    1929,
    1930,
    1933,
    1957,
    1958,
    1959,
    1960,
    1961,
    1962,
    1963,
    1973,
    1983,
    1984,
    1985,
    2003,
    2006,
    2028,
    2029,
    2031,
    2057,
    2059,
    2060,
    2061,
    2126,
    2139,
    2140,
    2143,
    2146,
    2147,
    2152,
    2159,
    2160,
    2161,
    2162,
    2163,
    2164,
    2165,
    2166,
    2167,
    2168,
    2172,
    2176,
    2203,
    2221,
    2234,
    2235,
    2310,
    2311,
    2313,
    2334,
    2344,
    2483,
    2486,
    2493,
    2502,
    2510,
    2520,
    2523,
    2533,
    2534,
    2540,
    2542,
    2543,
    2544,
    2547,
    2551,
    2552,
    2554,
    2581,
    2582,
    2626,
    2630,
    2632,
    2635,
    2653,
    2663,
    2670,
    2685,
    2686,
    2702,
    2708,
    2709,
    2712,
    2715,
    2717,
    2718,
    2721,
    2724,
    2727,
    2747,
    2748,
    2749,
    2750,
    2752,
    2753,
    2754,
    2755,
    2756,
    2757,
    2758,
    2759,
    2760,
    2761,
    2762,
    2763,
    2764,
    2765,
    2766,
    2769,
    2770,
    2774,
    2775,
    2779,
    2780,
    2782,
    2783,
    2785,
    2786,
    2787,
    2791,
    2802,
    2807,
    2808,
    2812,
    2813,
    2823,
    2826,
    2845,
    2846,
    2850,
    2852,
    2861,
    2862,
    2863,
    2867,
    2879,
    2896,
    2930,
    2936,
    2949,
    2950,
    2951,
    2963,
    2968,
    2982,
    2987,
    3037,
    3039,
    3040,
    3042,
    3046,
    3047,
    3053,
    3055,
    3065,
    3068,
    3076,
    3084,
    3089,
    3091,
    3140,
    3142,
    3145,
    3146,
    3147,
    3157,
    3161,
    3162,
    3164,
    3166,
    3167,
    3170,
    3173,
    3174,
    3181,
    3204,
    3208,
    3209,
    3214,
    3217,
    3224,
    3229,
    3230,
    3231,
    3232,
    3233,
    3234,
    3235,
    3241,
    3249,
    3250,
    3252,
    3253,
    3255,
    3256,
    3258,
    3267,
    3299,
    3301,
    3302,
    3303,
    3306,
    3342,
    3343,
    3344,
    3346,
    3348,
]

for id in IDS:
    try:
        save_problem("INICIANTE", id)
    except Exception:
        print("Error en el ID: ", id)
