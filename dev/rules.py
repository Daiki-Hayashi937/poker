# A=1, J=11, Q=12, K=13 にマッピング（1〜12の連続した値で役判定）
VALUE_MAP = {
    'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
    '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13,
}

#カードを文字と数値に分解
def _parse(card):
    return card[0], VALUE_MAP[card[1:]]

def kinds(cards):
    suits = [_parse(c)[0] for c in cards]
    # カードの数字は小さい順でソートされています
    values = sorted(_parse(c)[1] for c in cards)
    return suits, values

def evaluate(hand):
    # 役が高い順にできるかどうかを試し、できていたら終了としています
    # なので、例えばツーペアができていたらワンペアの判定は行われません
    # 逆に、ワンペアの判定でわざわざツーペアを除外する必要はありません
    if royal_flush(hand):
        return "ロイヤルストレートフラッシュ"
    if straight_flush(hand):
        return "ストレートフラッシュ"
    if four_card(hand):
        return "フォーカード"
    if full_house(hand):
        return "フルハウス"
    if flush(hand):
        return "フラッシュ"
    if straight(hand):
        return "ストレート"
    if three_card(hand):
        return "スリーカード"
    if two_pair(hand):
        return "ツーペア"
    if one_pair(hand):
        return "ワンペア"
    return "ハイカード"

def one_pair(cards):
    # カードのスート、数字を持ってくる
    suits, values = kinds(cards)

    # countsで出てくる数字の個数を数える。配列は0から始まるので、0~13の14個変数を用意する
    counts = [0 for i in range(14)]
    for v in values:
        counts[v] += 1
    
    # 数字が多い順に配列を並べなおす
    counts.sort(reverse=True)

    # 一番多い数字の個数が2個以上ならワンペア
    if counts[0] >= 2:
        return True
    return False

def two_pair(cards):
    # カードのスート、数字を持ってくる
    suits, values = kinds(cards)

    # countsは数字の個数を数えるための配列
    counts = [0 for i in range(14)]
    # countsで出てくる数字の個数を数える
    for v in values:
        counts[v] += 1
    
    # 数字が多い順に並べなおす(ソートする)
    counts.sort(reverse=True)

    # ソート後のcounts = [2, 2, 1, 0, 0, ..., 0] みたいになっています
    # 一番多い数字の個数が2個以上かつ次に多い数字の個数も2個以上ならツーペア
    # if A and B: とすると、AとBの条件をともに満たすときに処理が実装されます
    #if ???:
    #    return True
    return False

def three_card(cards):
    # カードのスート、数字を持ってくる
    suits, values = kinds(cards)

    # countsで出てくる数字の個数を数える
    counts = [0 for i in range(14)]
    for v in values:
        counts[v] += 1
    
    # 数字が多い順に並べなおす
    counts.sort(reverse=True)

    # 一番多い数字の個数が3個以上ならスリーカード
    if counts[0] >= 3:
        return True
    return False

def straight(cards):
    suits, values = kinds(cards)

    # 上級者用: ロジックを組み立ててみましょう
    # ヒント: values=[1, 2, 3, 4, 5]のときと[10, 11, 12, 13, 1]のときを一緒に扱いたいです
    return False

def flush(cards):
    # カードのスート、数字を持ってくる
    suits, values = kinds(cards)

    # countsで出てくるスートの個数を数える
    # 辞書型を使う
    counts = {"C": 0, "D" : 0, "H" : 0, "S" : 0}
    for s in suits:
        counts[s] += 1
    
    # for c in counts.values():
        # このループではC, D, H, Sがそれぞれ何枚あるかを調べています
        # すべてスートが同じということは..？
        #if ???:
        #    return True
    return False

def full_house(cards):
    # カードのスート、数字を持ってくる
    suits, values = kinds(cards)

    # countsで出てくる数字の個数を数える
    counts = [0 for i in range(14)]
    for v in values:
        counts[v] += 1
    
    # 数字が多い順に並べなおす
    counts.sort(reverse=True)

    # フルハウスの条件は...？
    #if ???:
    #    return True
    return False

def four_card(cards):
    # カードのスート、数字を持ってくる
    suits, values = kinds(cards)

    # countsで出てくる数字の個数を数える
    counts = [0 for i in range(14)]
    for v in values:
        counts[v] += 1
    
    # 数字が多い順に並べなおす
    counts.sort(reverse=True)

    # 一番多い数字の個数が4個ならフォーカード
    if counts[0] == 4:
        return True
    return False

def straight_flush(cards):
    #ストレートフラッシュにはストレートかつフラッシュが必要
    if straight(cards) and flush(cards):
        return True
    return False

def royal_flush(cards):
    #ロイヤルストレートフラッシュにはストレートフラッシュが必要なので...？
    #if ???:
    #    return False

    suits, values = kinds(cards)

    # 10, J(=11), Q(=12), K(=13), A(=1)をソートすると1, 10, 11, 12, 13なことを用いると...？
    #if ???:
    #    return True
    return False