from collections import Counter

# J=10, Q=11, K=12 にマッピング（1〜12の連続した値で役判定）
VALUE_MAP = {
    '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
    '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13,
}

#カードを文字と数値に分解
def _parse(card):
    return card[0], VALUE_MAP[card[1:]]

def kinds(hand):
    suits = [_parse(c)[0] for c in hand]
    values = sorted(_parse(c)[1] for c in hand)
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

def one_pair(hand):
    suits, values = kinds(hand)
    counts = sorted(Counter(values).values(), reverse=True)
    if counts[0] == 2:
        return True
    return False

def two_pair(hand):
    suits, values = kinds(hand)
    counts = sorted(Counter(values).values(), reverse=True)
    if counts[:2] == [2, 2]:
        return True
    return False

def three_card(hand):
    suits, values = kinds(hand)
    counts = sorted(Counter(values).values(), reverse=True)
    if counts[0] == 3:
        return True
    return False

def straight(hand):
    suits, values = kinds(hand)
    for j in range(5):
        cont = True
        for i, v in enumerate(values, -1):
            #print(f"{(values[j] + i) % 13 + 1} ",end="")
            if (values[j] + i) % 13 + 1 != v:
                cont = False
        if cont:
            return True
        #print()
    return False

def flush(hand):
    suits, values = kinds(hand)
    counts = sorted(Counter(suits).values(), reverse=True)
    if counts[0] == 5:
        return True
    return False

def full_house(hand):
    suits, values = kinds(hand)
    counts = sorted(Counter(values).values(), reverse=True)
    if counts[:2] == [3, 2]:
        return True
    return False

def four_card(hand):
    suits, values = kinds(hand)
    counts = sorted(Counter(values).values(), reverse=True)
    if counts[0] == 4:
        return True
    return False

def straight_flush(hand):
    if straight(hand) and flush(hand):
        return True
    return False

def royal_flush(hand):
    if not straight_flush(hand):
        return False
    suits, values = kinds(hand)
    if values[0] == 1 and values[1] == 10:
        return True
    return False