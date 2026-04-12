from rules import evaluate

#テストケースで実装が正しいかを確認します。

def tests():
    
    # === 成功ケース ===

    # ハイカード
    test1 = evaluate({"CA", "D3", "H7", "S9", "CK"})
    if test1 != "ハイカード":
        print(f"test1 失敗 (ハイカード): {test1}")
        return

    # ワンペア
    test2 = evaluate({"CA", "DA", "C3", "S5", "D8"})
    if test2 != "ワンペア":
        print(f"test2 失敗 (ワンペア): {test2}")
        return

    # ツーペア
    test3 = evaluate({"CA", "DA", "C3", "S3", "D8"})
    if test3 != "ツーペア":
        print(f"test3 失敗 (ツーペア): {test3}")
        return

    # スリーカード
    test4 = evaluate({"CA", "DA", "HA", "S5", "D8"})
    if test4 != "スリーカード":
        print(f"test4 失敗 (スリーカード): {test4}")
        return

    # ストレート (通常: 5-6-7-8-9)
    test5 = evaluate({"C5", "D6", "H7", "S8", "D9"})
    if test5 != "ストレート":
        print(f"test5 失敗 (ストレート 5-6-7-8-9): {test5}")
        return

    # ストレート (ホイール: A-2-3-4-5)
    test6 = evaluate({"CA", "D2", "H3", "S4", "D5"})
    if test6 != "ストレート":
        print(f"test6 失敗 (ストレート A-2-3-4-5): {test6}")
        return

    # ストレート (ブロードウェイ: 10-J-Q-K-A、異なるスート)
    test7 = evaluate({"CA", "D10", "HJ", "SQ", "DK"})
    if test7 != "ストレート":
        print(f"test7 失敗 (ストレート 10-J-Q-K-A): {test7}")
        return

    # フラッシュ
    test8 = evaluate({"CA", "C3", "C7", "C9", "CK"})
    if test8 != "フラッシュ":
        print(f"test8 失敗 (フラッシュ): {test8}")
        return

    # フルハウス
    test9 = evaluate({"CA", "DA", "HA", "S3", "D3"})
    if test9 != "フルハウス":
        print(f"test9 失敗 (フルハウス): {test9}")
        return

    # フォーカード
    test10 = evaluate({"CA", "DA", "HA", "SA", "D8"})
    if test10 != "フォーカード":
        print(f"test10 失敗 (フォーカード): {test10}")
        return

    # ストレートフラッシュ (2-3-4-5-6 同スート)
    test11 = evaluate({"C2", "C3", "C4", "C5", "C6"})
    if test11 != "ストレートフラッシュ":
        print(f"test11 失敗 (ストレートフラッシュ): {test11}")
        return

    # ロイヤルストレートフラッシュ
    test12 = evaluate({"CA", "C10", "CJ", "CQ", "CK"})
    if test12 != "ロイヤルストレートフラッシュ":
        print(f"test12 失敗 (ロイヤルストレートフラッシュ): {test12}")
        return

    # === 間違いケース ===

    # ストレート誤検出: 4枚連続+1枚バラバラ → ハイカード
    # straight()のmod判定が甘いとストレートと誤判定する可能性がある
    test13 = evaluate({"C5", "D6", "H7", "S8", "DK"})
    if test13 != "ハイカード":
        print(f"test13 失敗 (ストレート誤検出): {test13}")
        return

    # ロイヤルフラッシュ誤検出: A-2-3-4-5 同スート → ストレートフラッシュ (ロイヤルでない)
    # royal_flush()はvalues[0]==1 and values[1]==10を確認しているが、
    # A-2-3-4-5のvalues[1]は2なのでロイヤルでないことを確認する
    test14 = evaluate({"CA", "C2", "C3", "C4", "C5"})
    if test14 != "ストレートフラッシュ":
        print(f"test14 失敗 (A-2-3-4-5 同スートはロイヤルでなくストレートフラッシュ): {test14}")
        return

    # フラッシュ誤判定: ストレートフラッシュ → フラッシュと判定しない
    # evaluate()はstraight_flush→flushの順で確認するため、
    # ストレートフラッシュがフラッシュと判定されないことを確認する
    test15 = evaluate({"C5", "C6", "C7", "C8", "C9"})
    if test15 != "ストレートフラッシュ":
        print(f"test15 失敗 (ストレートフラッシュをフラッシュと誤判定): {test15}")
        return

    print("すべてのテストが通りました。")
    return

tests()
