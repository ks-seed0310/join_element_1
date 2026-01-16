import subprocess
import urllib.request
import os
import hashlib
import sys

# --- 設定エリア ---
MY_PUBLIC_KEY = """-----BEGIN PGP PUBLIC KEY BLOCK-----

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
aw8Jieq0
=XGYL
-----END PGP PUBLIC KEY BLOCK-----"""

GITHUB_RAW_URL = "https://raw.githubusercontent.com/ks-seed0310/join_element_1/refs/heads/main/"

def get_file_hash(content):
    """データ（bytes）のハッシュ値を計算する"""
    return hashlib.sha256(content).hexdigest()

def get_local_file_hash(filename):
    """ローカルにあるファイルのハッシュ値を計算する"""
    if not os.path.exists(filename):
        return None
    with open(filename, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def update_and_verify(filename):
    file_url = GITHUB_RAW_URL + filename
    sig_url = file_url + ".asc"
    
    try:
        # 1. サーバーからデータを取得
        with urllib.request.urlopen(file_url) as f:
            server_content = f.read()
        
        # 2. 【重要】ハッシュ比較：中身が同じならここで終了
        local_hash = get_local_file_hash(filename)
        server_hash = get_file_hash(server_content)
        
        if local_hash == server_hash:
            print(f"✨ {filename} は最新です。")
            return False # 更新不要

        # 3. 違う場合のみ、署名をダウンロードして検証
        print(f"🔄 {filename} の新しいバージョンが見つかりました。検証中...")
        with urllib.request.urlopen(sig_url) as s:
            sig_content = s.read()

        with open(f"{filename}.tmp", "wb") as f:
            f.write(server_content)
        with open(f"{filename}.asc.tmp", "wb") as f:
            f.write(sig_content)

        # GPGで検証
        subprocess.run(["gpg", "--import"], input=MY_PUBLIC_KEY.encode(), capture_output=True)
        result = subprocess.run(
            ["gpg", "--verify", f"{filename}.asc.tmp", f"{filename}.tmp"],
            capture_output=True, text=True
        )

        # 4. 検証成功なら置換
        if result.returncode == 0:
            print(f"✅ 検証成功！ {filename} を更新します。")
            os.replace(f"{filename}.tmp", filename)
            # 一時ファイル削除
            if os.path.exists(f"{filename}.asc.tmp"): os.remove(f"{filename}.asc.tmp")
            return True
        else:
            print(f"❌ 警告：{filename} の署名が不正です！")
            if os.path.exists(f"{filename}.tmp"): os.remove(f"{filename}.tmp")
            if os.path.exists(f"{filename}.asc.tmp"): os.remove(f"{filename}.asc.tmp")
            return False

    except Exception as e:
        print(f"エラー: {e}")
        return False

# --- 実行部分 ---
if __name__ == "__main__":
    # 1. 自分自身 (Untitled_16.py) を先にチェック
    if update_and_verify("Untitled_16.py"):
        print("🚀 本体を更新しました。再起動します...")
        subprocess.Popen([sys.executable, "Untitled_16.py"])
        sys.exit()

    # 2. その他のファイルをチェック
    for target in ["u16_imp1.py", "u16_imp2.py"]:
        update_and_verify(target)
    
    print("\n--- 全ファイル最新です。ゲームを起動します ---")
    
from u16_imp1 import *
from u16_imp2 import *
import math as Math
import time as time
import random
import sys

#element
#element[元素番号][0]=>元素記号
#element[元素番号][1]=>元素番号
#element[元素番号][2]=>電荷リスト
#element[元素番号][2][0]=>正電荷リスト
#element[元素番号][2][1]=>負電荷リスト
#element[元素番号][2][2]=>正負電荷リスト
#element[元素番号][2][3][0]=>下に一番近いオクテットを取得する
#element[元素番号][2][3][1]=>上に一番近いオクテットを取得する
#element[元素番号][3][0]=>金属(True)/非金属(False)/不明・半金属元素(None)
#element[元素番号][3][1]=>半金属元素(True)/その他(False)
#element[元素番号][4]=>貴ガスか(True/False)

logd=sys.argv
autopass=False
try:
    if logd[1]=="True" or logd[1]=="true":
        autopass=True
    else:
        autopass=False
except:None

opdata=[
    [],
]
metal_ch={}
true=True
false=False

use_element=[]

def load_irukakore(max_time,chdigit=True):
    """irukakore"""
    if autopass:
        print("\nデバッグモードのためロードはパスされます...\n")
        return
    if chdigit:
        for i in range(5, 0, -1):
            print(f"お待ち下さい... {i}秒"); time.sleep(1)
    steps = random.randint(30, 80)
    for i in range(steps):
        rd = int(random.random() * 1000) / (0.1 + random.random())
        print(f"Loading... {int(i/steps*100)}%")
        # 合計が25秒を超えないよう、1回最大 25/steps 秒に制限
        time.sleep(random.random() * (max_time / steps) * 2)
    print("Loading... 100% 完了")

def count_q():
    while True:
        imp=input("何個の元素を入力しますか。1~2")
        try:
            imp=int(imp)
            if imp>0 and imp<=2:
                break
            else:
                continue
        except:continue
    return imp

def print_(inplist):
    oplist=format_compound(inplist)
    for i in range(len(oplist)):
        print(oplist[i])


def support():
    """
    [
    [[原子番号, 原子数, 電子数],続く],
    2個目
    ]
    """

def issuccess(x,iskyouyu,ision):
    if iskyouyu and not(ision):
        None
    elif ision and not(iskyouyu):
        None
    else:
        return None

def join_kyouyu(inputdata):
    inp=list(set(inputdata))
    inp2=sorted(inp,reverse=True)
    retu_list=[]
    temp=[]
    temp2=[]
    if len(inp2)==1:
        #return ([[[inp2[0],2,inp2[0]]]])
        for i in range(len(element[inp2[0]][2][2])):
            temp=[]
            temp.append([inp2[0],2,element[inp2[0]][2][2][i]]) 
            retu_list.append(temp)
        return retu_list
    for i in range(len(element[inp2[0]][2][2])):
        for i2 in range(len(element[inp2[1]][2][2])):
            temp=[]
            temp2=[]
            temp2_abs=[]
            el_count=[]
            temp2.insert(0,element[inp2[0]][2][2][i])
            temp2.insert(1,element[inp2[1]][2][2][i2])
            temp2_abs=list(map(abs,temp2))
            lcm_q=Math.lcm(*temp2_abs)
            el_count.insert(0,lcm_q//temp2_abs[0])
            el_count.insert(1,lcm_q//temp2_abs[1])
            temp.append([inp2[0],el_count[0],temp2[0]])
            temp.append([inp2[1],el_count[1],temp2[1]])
            retu_list.append(temp)
    return retu_list



def join_kyouyu_sub(inp):
    inp2 = sorted(inp, reverse=True)

    retu_list = []
    temp = []

    for i in range(len(element[inp2[0]][2][1])):
        for i2 in range(len(element[inp2[1]][2][1])):

            temp = []

            # 負電荷（共有結合想定なので負のみ）
            q1 = abs(element[inp2[0]][2][2][i])
            q2 = abs(element[inp2[1]][2][2][i2])

            # 最小公倍数
            lcm_q = Math.lcm(q1, q2)

            # 原子数
            n1 = lcm_q // q1
            n2 = lcm_q // q2

            # 電子数（簡易版：そのまま絶対値）
            e1 = q1
            e2 = q2

            # 1つの組み合わせを作る
            temp.append([inp2[0], n1, e1])
            temp.append([inp2[1], n2, e2])

            # 出力用リストに追加
            retu_list.append(temp)

    return retu_list

def k3_chd(oct,densisu,denka,ismetalcheck=False):
    if not(ismetalcheck):
        m=oct[1]-(densisu-denka)
        if Math.ceil(m/2)>=3:
            m=(densisu-denka)-oct[0]
        if m==0:
            m=None
    else:
        m=oct[1]-(densisu-denka)
        if m>(oct[1]-oct[0])//2:
            m=True
        else:
            m=False
    return m

def join_kyouyu3(inp):
    inp2=sorted(inp,reverse=True)
    retu_list=[]
    temp=[]
    if len(inp2)==1:
    #何十にも手を繋ぐ処理が未実装のため仮
    #return ([[[inp2[0],2,inp2[0]]]])
        for i in range(len(element[inp2[0]][2][2])):
            temp=[]
            temp.append([inp2[0],2,element[inp2[0]][2][2][i]]) 
            retu_list.append(temp)
        return retu_list
    for i in range(len(element[inp2[0]][2][2])):
        for i2 in range(len(element[inp2[1]][2][2])):
            # 今の「手の数」を取得
            q1 = k3_chd(element[inp2[0]][2][3], inp2[0], element[inp2[0]][2][2][i])
            q2 = k3_chd(element[inp2[1]][2][3], inp2[1], element[inp2[1]][2][2][i2])
            if q1 is None or q2 is None:
                continue
            lcm_q = Math.lcm(abs(q1), abs(q2))
            n1 = lcm_q // abs(q1)
            n2 = lcm_q // abs(q2)
            total_charge = (element[inp2[0]][2][2][i] * n1) + (element[inp2[1]][2][2][i2] * n2)
            if total_charge == 0:
                temp = []
                temp.append([inp2[0], n1, element[inp2[0]][2][2][i]])
                temp.append([inp2[1], n2, element[inp2[1]][2][2][i2]])
                retu_list.append(temp)
    return retu_list

def join_ion(inp):
    results = [] # 見つかった組み合わせを全部入れるリスト
    
    # element[inp][2][2] は [3, 2, 0] のような「全ての電荷リスト」
    list1 = element[inp[0]][2][2]
    list2 = element[inp[1]][2][2]

    # 二重の for ループで、電荷の全パターンを試す
    for v1 in list1:
        if v1 == 0: continue # 0価は結合しないので飛ばす
        for v2 in list2:
            if v2 == 0: continue
            
            # プラスとマイナスの組み合わせだけを考える
            # (一方がプラスで、もう一方がマイナスの場合のみ)
            if (v1 > 0 and v2 < 0) or (v1 < 0 and v2 > 0):
                # 絶対値をとって最小公倍数で個数を出す
                val1 = abs(v1)
                val2 = abs(v2)
                lcm_val = Math.lcm(val1, val2)
                
                n1 = lcm_val // val1
                n2 = lcm_val // val2
                
                # 見つかった組み合わせをリストに追加
                # フォーマット: [[原子番号1, 個数1, 0], [原子番号2, 個数2, 0]]
                res = [[inp[0], n1, 0], [inp[1], n2, 0]]
                if res not in results: # 重複を避ける
                    results.append(res)

    return results # 発見した全てのパターン [[...], [...]] を返す






def join_halfmetal(implist):
    return

def main():
    global metal_ch
    el_c=count_q()
    use_element=[]
    for i in range(el_c):
        while True:
            inp=input(f"""{i+1}つめ/元素記号または原子番号を入力\n原子番号を入力したほうがバグは起こりにくいです。""")
            try:
                use_element.append(int(element[int(inp)][1]))
                break
            except:
                try:
                    use_element.append(int(element[search_element(inp)][1]))
                    break
                except:
                    continue
    metal_ch={
        "all":True,#全て金属元素か
        "allnot":True,#全て非金属元素か
        "allhalf":True,#全て半金属元素か
        
        "inmetal":False,#金属元素があるか
        "innot":False,#非金属元素があるか
        "inhalf":False,#半金属元素があるか
        "inrair":False,#貴ガスがあるか
        
        "innone":False,#不明な元素を含むか(Ogとか。)
    }
    for i in range(0,len(use_element)):
        metal_ch["all"]=metal_ch["all"] and element[use_element[i]][3][0]
        metal_ch["allnot"]=metal_ch["allnot"] and (not(element[use_element[i]][3][0] and element[use_element[i]][3][0]!=None))
        metal_ch["allhalf"]=metal_ch["allhalf"] and element[use_element[i]][3][1]

        metal_ch["inmetal"]=metal_ch["inmetal"] or element[use_element[i]][3][0]
        metal_ch["innot"]=metal_ch["innot"] or not(element[use_element[i]][3][0] and element[use_element[i]][3][0]!=None)
        metal_ch["inhalf"]=metal_ch["inhalf"] or element[use_element[i]][3][1]
        metal_ch["inrair"]=metal_ch["inrair"] or element[use_element[i]][4]
        metal_ch["innone"]=metal_ch["innone"] or (element[use_element[i]][3][0]==None)and(not(element[use_element[i]][3][1]))

    if metal_ch["innone"]:
        print("\n構造が不明な元素が含まれているため現在は実行不可能です。\nバージョンのアップデート後にお試しください。\n")
    elif metal_ch["inhalf"]:
        print("\n半金属元素の結合プログラムは現在未実装です。\nバージョンのアップデート後にお試しください。\n")
    elif metal_ch["inrair"]:
        print("\n貴ガスの結合プログラムは未実装です(まず安定しています。)\nもしかしたらアップデート後にサポートされている可能性があります。\n")
    elif metal_ch["all"]:
        print("金属結合のプログラムは現在未実装です\n。バージョンのアップデート後にお試しください。")
    elif metal_ch["allnot"]:
        opdata=join_kyouyu3(use_element)
        print_(sort_compounds(opdata))
    elif metal_ch["inmetal"] and metal_ch["innot"]:
        opdata=join_ion(use_element)
        print_(sort_compounds(opdata))
    else:
        None


    
    print("y","と入力するとホームに戻ります。")
    while True:
        inp=input()
        if inp=="y" or inp=="Y" or inp=="pass":
            break
    if inp!="pass":
        load_irukakore(10)
    else:
        load_irukakore(2)

print("Press Enter Key")
i=input()
if i!="pass":
    load_irukakore(5,False)
else:
    load_irukakore(1,False)
del i
while True:
    print(f"""
元素パズル簡易版　:ver.1.0.0.0(Dev-1.0.0d01a)
たまに狂った出力が出ることがありますがご理解お願いいたします。
コマンド説明　　　: command.about
プログラム説明　　: program.about
使い方　　　　　　: home.use
開始　　　　　　　: home.start
""")
    while True:
        step=input()
        if step=="command.about":
            print("\n")
            print("""
コマンドとは、プログラム内での動作を簡単にするための方法です。
コマンドはhome.useから見ることができます。
""")
        if step=="program.about":
            print("\n")
            print("""
このプログラムでは元素を入力すると組み合わせを出力してくれます。
H,O => H₂O / N,H => NH₃　など
右上の数字は電荷です。NH₃=>N
""")
        if step=="home.start":
            break

    if step=="home.start":    
        main()