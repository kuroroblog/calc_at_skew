import matplotlib.pyplot as plt
import random

# DNAについて : https://mgcvt.com/entry/e93
# DNAを作成する関数
def create_dna_text():
    # DNA情報を書き込むファイル名
    path = 'sample.txt'

    # DNAを構成する、塩基(アデニン、チミン、グアニン、シトシン)の頭文字を表す。
    base_arr = ['A', 'T', 'G', 'C']

    # DNAを構成する文字列数を指定する。
    cnt = 10100
    output = ''

    for _ in range(cnt):
        # 参考 : https://note.nkmk.me/python-random-choice-sample-choices/
        # 文字列連結参考 : https://note.nkmk.me/python-string-concat/
        output += random.choice(base_arr)

    # 参考 : https://note.nkmk.me/python-file-io-open-with/
    with open(path, mode='w') as f:
        f.write(output)

# DNA情報を読み取る関数
def read_dna_text():
    # DNA情報ファイル名
    path = 'sample.txt'
    # 参考 : https://note.nkmk.me/python-file-io-open-with/
    with open(path) as f:
        s = f.read()
        # AT_skew情報
        at_skew_list = []
        # DNA情報(文字列)を何文字単位で取得するのか設定する。
        cnt = 500
        for i in range(0, len(s), cnt):
            # 参考 : https://note.nkmk.me/python-slice-usage/
            txt = s[i:i + cnt]

            a = txt.count('A')
            t = txt.count('T')

            at_skew = (a - t) / (a + t)

            # 参考 : https://note.nkmk.me/python-list-append-extend-insert/
            at_skew_list.append(at_skew)
    return at_skew_list

# 折れ線グラフを出力
# 参考 : https://aiacademy.jp/media/?p=154
plt.plot(read_dna_text())

# 参考 : https://biotech-lab.org/articles/1638
plt.title('Calculate AT skew every 500 base.')

# 参考 : https://ai-inter1.com/python-linechart/
plt.xlabel("Number of times")
plt.ylabel("AT skew")

plt.show()
