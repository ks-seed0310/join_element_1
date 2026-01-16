from u16_imp1 import *

def search_element(x):
    """
    x : int（原子番号） or str（元素記号）
    戻り値 :
        int → str（元素記号）
        str → int（原子番号）
        見つからない場合 → None
    """

    # 原子番号 → 元素記号
    if isinstance(x, int):
        if x in element:
            return element[x][0]
        return None

    # 元素記号 → 原子番号
    if isinstance(x, str):
        for atomic_number, data in element.items():
            if data[0] == x:
                return atomic_number
        return None

    return None

def sort_compounds(data):
    result = []

    for compound in data:  # ← 1化合物ずつ処理
        sorted_compound = sorted(
            compound,
            key=lambda atom: junban[search_element(atom[0])]
        )
        result.append(sorted_compound)

    return result


def format_compound(compounds):
    sup = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    sub = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    result = []
    for comb in compounds:  # comb: [(原子番号, 原子数, 電子数), ...]
        parts = []
        for z, n, e in comb:
            symbol = element[z][0]
            part = f"{str(z-e).translate(sup)}{symbol}"
            if n > 1:
                part += f"{str(n).translate(sub)}"
            parts.append(part)
        result.append("".join(parts))
    return result

"""print(format_compound(sort_compounds(
    [
        [[8,1,8],[1,2,1]]
    ]
)))"""


"""
# 例
compounds = [
    [(1,2,1)],
    [(1,2,1),(6,2,6)]
]

print(format_compound(compounds))
# 出力: ['¹H₂', '¹⁶C¹H₄']
"""