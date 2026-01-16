import subprocess
import urllib.request
import os
import hashlib
import sys

# --- 設定エリア ---
# 公開鍵そのものではなく、Ubuntuサーバーにあるあなたの鍵の「指紋」を指定します
TRUSTED_FINGERPRINT = "C4F54AF8F4D073744D3430A0595F1A8D369E0D5C"

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
        
        # 2. ハッシュ比較：中身が同じならここで終了
        local_hash = get_local_file_hash(filename)
        server_hash = get_file_hash(server_content)
        
        if local_hash == server_hash:
            print(f"✨ {filename} は最新です。")
            return False

        # 3. 違う場合のみ、署名をダウンロードして検証
        print(f"🔄 {filename} の新しいバージョンが見つかりました。検証中...")
        with urllib.request.urlopen(sig_url) as s:
            sig_content = s.read()

        with open(f"{filename}.tmp", "wb") as f:
            f.write(server_content)
        with open(f"{filename}.asc.tmp", "wb") as f:
            f.write(sig_content)

        # --- GPG検証部分をWeb連動に修正 ---
        # まず、Ubuntuサーバーから最新の公開鍵を取得（上書きインポート）
        subprocess.run([
            "gpg", "--keyserver", "keyserver.ubuntu.com", 
            "--recv-keys", TRUSTED_FINGERPRINT
        ], capture_output=True)

        # 署名を検証
        result = subprocess.run(
            ["gpg", "--verify", "--status-fd", "1", f"{filename}.asc.tmp", f"{filename}.tmp"],
            capture_output=True, text=True
        )

        # 「正しい署名」かつ「指定した指紋」であることを確認
        if result.returncode == 0 and ("VALIDSIG " + TRUSTED_FINGERPRINT in result.stdout):
            print(f"✅ 検証成功！ {filename} を更新します。")
            os.replace(f"{filename}.tmp", filename)
            if os.path.exists(f"{filename}.asc.tmp"): os.remove(f"{filename}.asc.tmp")
            return True
        else:
            print(f"❌ 警告：{filename} の署名が不正、または作者が異なります！")
            if os.path.exists(f"{filename}.tmp"): os.remove(f"{filename}.tmp")
            if os.path.exists(f"{filename}.asc.tmp"): os.remove(f"{filename}.asc.tmp")
            return False

    except Exception as e:
        print(f"エラー: {e}")
        return False

# --- 修正後の 実行部分 ---
if __name__ == "__main__":
    # 特定のファイルが存在する場合、アップデート処理を丸ごとスキップする
    SKIP_FILE = "joinelement1_no_update.eld"
    
    if os.path.exists(SKIP_FILE):
        print(f"⚠️ {SKIP_FILE} を検出しました。アップデートをパスして起動します。")
    else:
        # 1. 自分自身 (Untitled_16.py) を先にチェック
        if update_and_verify("Untitled_16.py"):
            print("🚀 本体を更新しました。再起動します...")
            os.execv(sys.executable, [sys.executable, "Untitled_16.py"])

        # 2. その他のファイルをチェック
        for target in ["u16_imp1.py", "u16_imp2.py"]:
            update_and_verify(target)
    
    # ここからロード画面やゲーム本体へ
    print("\n--- 全ファイル最新です。ゲームを起動します ---")

    # --- ここから下にゲームのメインコード ---
#^^^^^^From Gemini
    
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

def load_irukakore(max_time, chdigit=True):
    """進化した irukakore ローディング"""
    if autopass:
        print("\nデバッグモードのためロードはパスされます...\n")
        return

    # カウントダウンも1行で上書き
    if chdigit:
        for i in range(5, 0, -1):
            print(f"\rお待ち下さい... {i}秒 ", end="")
            time.sleep(1)
        print() # カウントダウン終了後に1回だけ改行

    steps = random.randint(30, 80)
    for i in range(steps + 1): # 100%まで出すために +1
        percent = int(i / steps * 100)
        # 進捗バーの作成 (20文字分)
        bar_length = 20
        filled = int(i / steps * bar_length)
        bar = "#" * filled + "-" * (bar_length - filled)
        
        # \r で行頭に戻り、前回の表示を上書き
        # sys.stdout.flush() は環境によって必要ですが、最近のPythonのprint(flush=True)でもOK
        print(f"\rLoading... [{bar}] {percent}% ", end="", flush=True)
        
        # 待機時間は元のロジックを継承
        if i < steps:
            time.sleep(random.random() * (max_time / steps) * 2)

    print("\nLoading... 100% 完了 ✨")

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
        print("\n金属結合のプログラムは現在未実装です\n。バージョンのアップデート後にお試しください。\n")
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
元素パズル簡易版　:ver.1.1.58.24(Dev-1.1.0d58-140)
たまに狂った出力が出ることがありますがご理解お願いいたします。
コマンド説明　　　: command.about
プログラム説明　　: program.about
使い方　　　　　　: home.use
開始　　　　　　　: home.start
終了            : home.quit
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