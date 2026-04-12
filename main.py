from deck import Deck
from user import get_redraw_indices, show_hand
from rules import evaluate


def main():
    print("=== ポーカー ===")
    deck = Deck()
    hand = deck.deal(5)

    n = 2

    for i in range(n):
        print(f"\n--- 引き直し {i + 1}/{n} ---")
        indices = get_redraw_indices(hand)
        if not indices:
            print("引き直しなし")
        else:
            hand = deck.redraw(hand, indices)
    
    print("\n=== 最終手札 ===")
    show_hand(hand)
    print(f"役: {evaluate(hand)}")


if __name__ == "__main__":
    main()
