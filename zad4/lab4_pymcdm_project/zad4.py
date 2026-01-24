import numpy as np
from pymcdm.methods import TOPSIS, SPOTIS
from pymcdm.normalizations import minmax_normalization

def main():
    # DANE
    A = np.array([
        [2500, 7, 12],
        [3000, 6, 10],
        [2800, 9, 11],
        [2600, 8,  9]
    ])
    alternatives = ["A1", "A2", "A3", "A4"]
    # typy kryteriów: -1 = min, 1 = max
    types = [-1, 1, -1]
    # wagi
    w = np.array([0.4, 0.4, 0.2])

    A_norm = minmax_normalization(A, types)
    topsis = TOPSIS()
    topsis_scores = topsis(A_norm, w, types)

    # im większy score TOPSIS tym lepiej
    topsis_rank = np.argsort(-topsis_scores)

    print("TOPSIS - wyniki :")
    for i in topsis_rank:
        print(alternatives[i], "score =", round(float(topsis_scores[i]), 4))

    bounds = np.array([
        [2000, 3500],  # koszt
        [5, 10],       # jakość
        [8, 15]        # czas
    ])

    spotis = SPOTIS(bounds)
    spotis_scores = spotis(A, w, types)
    # im mniejszy score SPOTIS tym lepiej
    spotis_rank = np.argsort(spotis_scores)

    print("\nSPOTIS - wyniki :")
    for i in spotis_rank:
        print(alternatives[i], "score =", round(float(spotis_scores[i]), 4))

if __name__ == "__main__":
    main()
