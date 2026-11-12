
import random
import config as cfg


# Zieht zufällige Karten aus dem Kartendeck, ohne eine Karte doppelt zu ziehen
def draw_hand(cards: list[int], numbers_to_draw: int) -> list[int]:
    for i in range(numbers_to_draw):
        rnd_index = random.randint(0, len(cards) - i - 1)
        last_index = len(cards) - i - 1

        cards[rnd_index], cards[last_index] = (
            cards[last_index], cards[rnd_index]
        )

    return cards[-numbers_to_draw:]


# Gibt die Karten einer Hand mit Wert und Farbe aus
def print_hand(hand: list[int]) -> None:
    print("Hand:")
    for card in hand:
        print(
            cfg.VALUES[card % cfg.VALUES_PER_COLOR],
            "von",
            cfg.COLORS[card // cfg.VALUES_PER_COLOR]
        )


# Ermittelt die Werte der Karten
def get_card_values(hand: list[int]) -> list[int]:
    return [card % cfg.VALUES_PER_COLOR for card in hand]


# Ermittelt die Farben der Karten
def get_card_colors(hand: list[int]) -> list[int]:
    return [card // cfg.VALUES_PER_COLOR for card in hand]


# Zählt, wie oft die einzelnen Kartenwerte vorkommen
def probabilities(hand: list[int]) -> list[int]:
    values = get_card_values(hand)
    return [values.count(value) for value in set(values)]


def royal_flush(hand: list[int]) -> bool:
    values = sorted(get_card_values(hand))
    colors = get_card_colors(hand)

    return (
        values == cfg.ROYAL_FLUSH_VALUES
        and len(set(colors)) == 1
    )


def straight_flush(hand: list[int]) -> bool:
    return street(hand) and flush(hand)


def vierling(hand: list[int]) -> bool:
    return 4 in probabilities(hand)


def full_house(hand: list[int]) -> bool:
    counts = probabilities(hand)
    return 3 in counts and 2 in counts


def flush(hand: list[int]) -> bool:
    colors = get_card_colors(hand)
    return len(colors) == cfg.CARDS_PER_HAND and len(set(colors)) == 1


def street(hand: list[int]) -> bool:
    values = sorted(set(get_card_values(hand)))

    # Eine Straße benötigt fünf unterschiedliche Kartenwerte
    if len(values) != cfg.STRAIGHT_LENGTH:
        return False

    # Prüft, ob die Kartenwerte aufeinanderfolgen
    if values[-1] - values[0] == cfg.STRAIGHT_LENGTH - 1:
        return True

    # Sonderfall: Ass, 2, 3, 4, 5
    if values == cfg.ACE_LOW_STRAIGHT:
        return True

    return False


def drilling(hand: list[int]) -> bool:
    counts = probabilities(hand)
    return 3 in counts and 2 not in counts


def zwei_paare(hand: list[int]) -> bool:
    counts = probabilities(hand)
    return counts.count(2) == 2


def ein_paar(hand: list[int]) -> bool:
    counts = probabilities(hand)
    return counts.count(2) == 1 and 3 not in counts


def high_card(hand: list[int]) -> bool:
    return not (
        royal_flush(hand)
        or straight_flush(hand)
        or vierling(hand)
        or full_house(hand)
        or flush(hand)
        or street(hand)
        or drilling(hand)
        or zwei_paare(hand)
        or ein_paar(hand)
    )


# Bestimmt die höchste Pokerkombination einer Hand
def get_combination(hand: list[int]) -> str:
    if royal_flush(hand):
        return "Royal Flush"
    elif straight_flush(hand):
        return "Straight Flush"
    elif vierling(hand):
        return "Vierling"
    elif full_house(hand):
        return "Full House"
    elif flush(hand):
        return "Flush"
    elif street(hand):
        return "Straße"
    elif drilling(hand):
        return "Drilling"
    elif zwei_paare(hand):
        return "Zwei Paare"
    elif ein_paar(hand):
        return "Ein Paar"
    else:
        return "High Card"


# Simuliert mehrere Pokerspiele und zählt die Kombinationen
def simulate(number_of_games: int) -> dict[str, int]:
    results: dict[str, int] = {}

    for i in range(number_of_games):
        # Für jedes Spiel wird ein neues Kartendeck erstellt
        cards = list(range(cfg.TOTAL_CARDS))
        hand = draw_hand(cards, cfg.CARDS_PER_HAND)

        combination = get_combination(hand)

        if combination not in results:
            results[combination] = 0

        results[combination] += 1

    return results


# Gibt die Häufigkeit und prozentuale Wahrscheinlichkeit aus
def print_results(results: dict[str, int], number_of_games: int) -> None:
    print("\nSimulationsergebnisse:")
    print("-----------------------------")

    for combination, count in results.items():
        percentage = count / number_of_games * 100

        print(combination, ":", count, "Mal -", round(percentage, 4), "%")


if __name__ == "__main__":
    cards: list[int] = list(range(cfg.TOTAL_CARDS))

    hand: list[int] = draw_hand(cards, cfg.CARDS_PER_HAND)
    print_hand(hand)
    print("Kombination:", get_combination(hand))

    # Anzahl der zu simulierenden Pokerspiele
    number_of_games: int = 100000

    results: dict[str, int] = simulate(number_of_games)
    print_results(results, number_of_games)
