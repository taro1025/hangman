"""ルール
ワードをコンピュータ側で決める。（リストをつくる）
プレイヤーは一ターン一文字予想
外したらハングマンが上から一行ずつ書かれる
絵が完成したらプレイヤーの負け。ワードを当てたらプレイヤーの勝ち。
"""

import random

def hangman(word):

    """
    伏字を映す
    絵を用意。
    　文字を入力させる
    　入力さらた文字がword内に含まれるか調べる
    　当たった場合文字を表示。はずれの場合絵を表示

    間違えた数のカウント、絵の処理

    """
    hang =["",
           "______      ",
           "|           ",
           "|     |     ",
           "|     0     ",
           "|    /|\    ",
           "|    / \    "]


    word = list(word)

    wrong = 0

    win = 0

    limit = len(hang)

    bord =[]

    anslen = len(word)

    for i in range(anslen):
        bord.append("_")

    print(" ".join(bord))

    while wrong < limit:
        w = input("1文字入力:")

        if w in word:
            bingindex = word.index(w)
            bord[bingindex] = w
            print(" ".join(bord))

            word[bingindex] ="$"
            win += 1
            print("bingo")
        else:
            wrong += 1
            print("はずれ")

        e = wrong + 1

        print("\n".join(hang[0:e]))

        if win +1 > anslen:
            print("you win")
            break

    if wrong == limit:
        print("you lose")
answerlist = ["english", "tomato", "sumash", "sonic"]

ansnum = len(answerlist)

answer = answerlist[(random.randrange(0,ansnum))]

hangman(answer)