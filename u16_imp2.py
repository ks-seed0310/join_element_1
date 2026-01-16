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


def format_compound(compounds,patten=0):
    if patten==0:
        sup = str.maketrans("0123456789-+", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺")
        sub = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        e2=0
        result = []
        for comb in compounds:  # comb: [(原子番号, 原子数, 電荷), ...]
            parts = []
            for z, n, e in comb:
                symbol = element[z][0]
                e2=str(e)
                if int(e2)<0:
                    e2=e2.replace("-","")
                    e2+="-"
                elif int(e2)>0:
                    e2+="+"
                else:
                    e2=""
                if e2=="1+" or e2=="1-":
                    e2=e2[1]
                part = f"{symbol}{e2.translate(sup)}"
                if n > 1:
                    part += f"{str(n).translate(sub)}"
                parts.append(part+" + ")
            result.append((" + ".join(parts))+("  -->  ")+(format_compound([comb],1)[0]))
    elif patten==1:
        sub = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        e2=0
        result = []
        for comb in compounds:  # comb: [(原子番号, 原子数, 電荷), ...]
            parts = []
            for z, n, e in comb:
                symbol = element[z][0]
                part = f"{symbol}"
                if n > 1:
                    part += f"{str(n).translate(sub)} "
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
    [(1,4,1),(6,1,-4)]
]

print(format_compound(sort_compounds(compounds)))
# 出力: 
"""
