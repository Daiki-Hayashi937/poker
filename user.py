SUIT_MAP = {
    'C': 'クローバー',
    'D': 'ダイヤ',
    'S': 'スペード',
    'H': 'ハート',
}


def _format_card(card):
    return SUIT_MAP[card[0]] + card[1:]


def show_hand(hand):
    print("手札: " + "  ".join(f"[{i}]{_format_card(c)}" for i, c in enumerate(hand)))


def get_redraw_indices(hand):
    show_hand(hand)
    while True:
        raw = input("引き直すカードの番号を入力 (スペース区切り、なければEnter): ").strip()
        if raw == "":
            return []
        try:
            indices = list(dict.fromkeys(int(x) for x in raw.split()))
            if all(0 <= idx < len(hand) for idx in indices):
                return indices
            print(f"0〜{len(hand) - 1} の番号を入力してください")
        except ValueError:
            print("数字をスペース区切りで入力してください")
