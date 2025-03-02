from typing import Any


def get_bidder_name(i: int) -> Any:
    """asks the user for the name of the ith bidder"""

    message = f"Rentrez le nom de l'enchérisseur {i} : "
    name = input(message)
    while name in bids:
        print(f"{name} fait déjà partie des enchérisseurs ! ")
        name = input(message)
    return name


def get_bidder_bids(name: Any) -> list[int]:
    """asks the user for the bids of the bidder called 'name'"""

    message = f"Rentrez les enchères de {name} (nombres entiers séparés par un espace) : "
    bid = [-1]
    while bid == [-1]:
        try:
            bid = list(map(int, input(message).split()))
        except ValueError as e:
            print("Rentrez des nombres entiers séparés par un espace !")
    return bid


def get_winner_and_winning_price(bids: dict[Any, list[int]], reserve_price: int) -> tuple[Any, int]:
    """Returns the winner of the auction and the winning price.
    Args :
        bids : a dictionnary with the id of the bidder as keys, and a list of their bids as values
        reserve_price : an integer
    Returns :
        tuple[Any, int] : the winner and the reserve price
    """

    def custom_max(l: list[int]) -> int:
        return max(l) if l else -1

    higher_bidder = max(bids.items(), key=lambda item: custom_max(item[1]))[0]
    if custom_max(bids[higher_bidder]) < reserve_price:
        return None, reserve_price
    
    del(bids[higher_bidder])
    second_max = custom_max(max(bids.values(), key=custom_max)) if bids else -1
    return higher_bidder, max(second_max, reserve_price)


if __name__ == "__main__":
    
    n = 0
    while n <= 0:
        n = int(input("Rentrez le nombres d'enchérisseurs (entier strictement positif) : "))
    reserve_price = -1
    while reserve_price < 0:
        reserve_price = int(input("Rentrez le prix de réserve (entier positif): "))
    bids = {}

    for i in range(n):
        name = get_bidder_name(i + 1)
        bid = get_bidder_bids(name)
        bids[name] = bid

    winner, winning_prize = get_winner_and_winning_price(bids, reserve_price)
    
    print(f"{winner} a gagné l'enchère ! "if winner else f"Personne n'a gagné l'enchère ! ")
    print(f"Le prix de l'objet est de {winning_prize}.")
