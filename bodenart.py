Bodenart = [
"Sand",
"schluffiger Sand",
"lehmiger Sand",
"toniger Sand",
"sandiger Schluff",
"Schluff",
"lehmiger Schluff",
"sandiger Lehm",
"Lehm",
"schluffiger Lehm",
"sandiger Ton",
"lehmiger Ton",
"Ton",
]

Bodenart_Abk = [
    "S",
    "uS",
    "lS",
    "tS",
    "sU", 
    "U",
    "lU",
    "sL",
    "L",
    "uL",
    "sT",
    "lT",
    "T",
    ]

s_condition = [
    lambda s: 65 <= s <= 100,
    lambda s: 40 < s < 70,
    lambda s: 30 < s <= 80,
    lambda s: 65 <= s < 90,
    lambda s: 10 <= s < 45,
    lambda s: 0 <= s < 25,
    lambda s: 0 <= s < 30,
    lambda s: 20 <= s < 75,
    lambda s: 5 <= s < 65,
    lambda s: 0 <= s < 20,
    lambda s: 50 <= s < 75,
    lambda s: 0 <= s < 60,
    lambda s: 0 <= s < 50,
]

u_condition = [
    lambda u: 0 <= u <= 30,
    lambda u: 30 < u <= 55,
    lambda u: 10 < u <= 55,
    lambda u: 0 <= u <= 10,
    lambda u: 55 < u <= 75,
    lambda u: 75 < u <= 100,
    lambda u: 55 < u <= 75,
    lambda u: 10 < u <= 55,
    lambda u: 10 < u <= 55,
    lambda u: 55 < u < 75,
    lambda u: 0 <= u <= 10,
    lambda u: 0 <= u <= 55,
    lambda u: 0 <= u < 50,
]

t_condition = [
    lambda t: 0 <= t <= 10,
    lambda t: 0 <= t <= 5,
    lambda t: 5 < t <= 15,
    lambda t: 10 < t <= 25,
    lambda t: 0 <= t <= 15,
    lambda t: 0 <= t < 25,
    lambda t: 15 < t <= 25,
    lambda t: 15 < t <= 25,
    lambda t: 25 < t <= 40,
    lambda t: 25 < t < 45,
    lambda t: 25 < t <= 40,
    lambda t: 40 < t <= 50,
    lambda t: 50 < t <= 100,
]



def finde_textur(s:int, u:int, t:int) -> tuple[str, str]:
    """
    Finde die Textur aus den prozentuellen Anteilen von Sand, Schluff und Ton.
    Die Summe der Anteile muss 100 sein.
    """  

    if s + u + t != 100:
        raise ValueError(f"Sum of s, u and t must be 100, but is {s + u + t}") 
    cc = [(n, sn) for n, sn, sc, uc, tc in zip(Bodenart, Bodenart_Abk, s_condition, u_condition, t_condition) if sc(s) & uc(u) & tc(t)]

    return cc[0]