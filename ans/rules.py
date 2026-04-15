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
    values = sorted(_parse(c)[1] for c in cards)
    return suits, values

def evaluate(hand):
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

    # countsで出てくる数字の個数を数える
    counts = [0 for i in range(14)]
    for v in values:
        counts[v] += 1
    
    # 数字が多い順に並べなおす
    counts.sort(reverse=True)

    # 一番多い数字の個数が2個以上ならワンペアは作れてる
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
    
    # 数字が多い順に並べなおす
    counts.sort(reverse=True)

    # 一番多い数字の個数が2個以上かつ次に多い数字の個数も2個以上ならツーペア作れる
    if counts[0] >= 2 and counts[1] >= 2:
        return True
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
    # むずい！！！ コメントでは例としてvalues = [1, 10, 11, 12, 13]で進めます
    suits, values = kinds(cards)

    for i in range(5):
        cont = True
            if values[i] != (values[0] + i: 
                cont = False
        if cont:
            return True
        if values==[1,10,11,12,13]:
            return True
    return False

def flush(cards):
    # カードのスート、数字を持ってくる
    suits, values = kinds(cards)

    # countsで出てくる数字の個数を数える
    counts = {"C": 0, "D" : 0, "H" : 0, "S" : 0}
    for s in suits:
        counts[s] += 1
    
    for c in counts.values():
        # 5枚ある→すべてスートが同じ
        if c == 5:
            return True
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

    # 一番多い数字の個数が3個かつ次に多い数字の個数も2個ならフルハウス
    if counts[0] == 3 and counts[1] == 2:
        return True
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
    #ロイヤルストレートフラッシュにはストレートフラッシュが必要
    if not straight_flush(cards):
        return False
    suits, values = kinds(cards)
    # 10, J(=11), Q(=12), K(=13), A(=1)をソートすると1, 10, 11, 12, 13
    if values[0] == 1 and values[1] == 10:
        return True
    return False
