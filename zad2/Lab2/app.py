import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay


def evaluate_many_C(X_train, y_train, X_test, y_test, kernel, C_list):
    """
    Trenuje SVC dla wielu wartości C (dla zadanego kernel),
    zwraca listę (C, accuracy_test) + najlepszy C.
    """
    results = []

    for C in C_list:
        model = Pipeline([
            ("scaler", StandardScaler()),
            ("svc", SVC(kernel=kernel, C=C, random_state=0))
        ])
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        results.append((C, acc))

    best_C, best_acc = max(results, key=lambda x: x[1])
    return results, best_C, best_acc


def save_confusion_matrix(y_true, y_pred, title, filename):
    cm = confusion_matrix(y_true, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot(values_format="d")
    plt.title(title)
    plt.tight_layout()
    plt.savefig(filename, dpi=200)
    plt.close()


def save_scatter_2d(X_2d, labels, title, xlabel, ylabel, filename):
    """
    Prosty scatter 2D: punkty kolorowane według klas (0/1).
    """
    plt.figure(figsize=(7, 5))
    scatter = plt.scatter(X_2d[:, 0], X_2d[:, 1], c=labels, s=18, alpha=0.85)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # legenda (klasy 0 i 1)
    handles, _ = scatter.legend_elements()
    plt.legend(handles, ["class 0", "class 1"], title="Klasa", loc="best")

    plt.tight_layout()
    plt.savefig(filename, dpi=200)
    plt.close()


def main():
    # =========================
    # 4a) Wczytanie zbioru danych
    # =========================
    data = load_breast_cancer()
    X = data.data
    y = data.target
    feature_names = data.feature_names

    print("=== INFORMACJE O DANYCH ===")
    print(f"Liczba próbek: {X.shape[0]}")
    print(f"Liczba cech:   {X.shape[1]}")
    print("Nazwy pierwszych 5 cech:", feature_names[:5])
    print("Rozkład klas (0/1):", dict(zip(*np.unique(y, return_counts=True))))
    print()

    # (opcjonalnie do raportu) podgląd pierwszych wierszy
    print("=== PODGLAD PIERWSZYCH 3 PROBEK (pierwsze 5 cech) ===")
    print(X[:3, :5])
    print()

    # =========================
    # 4b) Podział 0.7/0.3
    # =========================
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.30,
        random_state=0,
        stratify=y
    )

    print("=== PODZIAL DANYCH ===")
    print("X_train:", X_train.shape, "X_test:", X_test.shape)
    print()

    # =========================
    # 4c-4e) SVC: test różnych C dla linear i rbf
    # =========================
    C_list = [0.01, 0.1, 1, 10, 100, 1000]

    print("=== TEST C dla kernel='linear' ===")
    linear_results, best_C_linear, best_acc_linear = evaluate_many_C(
        X_train, y_train, X_test, y_test, kernel="linear", C_list=C_list
    )
    for C, acc in linear_results:
        print(f"C={C:<7}  accuracy_test={acc:.4f}")
    print(f"Najlepsze: C={best_C_linear}, accuracy={best_acc_linear:.4f}")
    print()

    print("=== TEST C dla kernel='rbf' ===")
    rbf_results, best_C_rbf, best_acc_rbf = evaluate_many_C(
        X_train, y_train, X_test, y_test, kernel="rbf", C_list=C_list
    )
    for C, acc in rbf_results:
        print(f"C={C:<7}  accuracy_test={acc:.4f}")
    print(f"Najlepsze: C={best_C_rbf}, accuracy={best_acc_rbf:.4f}")
    print()

    # =========================
    # 4f) Naucz 2 finalne klasyfikatory (linear i rbf) z najlepszym C
    # =========================
    model_linear = Pipeline([
        ("scaler", StandardScaler()),
        ("svc", SVC(kernel="linear", C=best_C_linear, random_state=0))
    ])
    model_rbf = Pipeline([
        ("scaler", StandardScaler()),
        ("svc", SVC(kernel="rbf", C=best_C_rbf, random_state=0))
    ])

    model_linear.fit(X_train, y_train)
    model_rbf.fit(X_train, y_train)

    y_pred_linear_test = model_linear.predict(X_test)
    y_pred_rbf_test = model_rbf.predict(X_test)

    acc_linear = accuracy_score(y_test, y_pred_linear_test)
    acc_rbf = accuracy_score(y_test, y_pred_rbf_test)

    print("=== FINALNE WYNIKI NA TEST ===")
    print(f"Linear: accuracy={acc_linear:.4f} (C={best_C_linear})")
    print(f"RBF:    accuracy={acc_rbf:.4f} (C={best_C_rbf})")
    print()

    # =========================
    # 4f.i) Macierze konfuzji (na zbiorze testowym)
    # =========================
    save_confusion_matrix(
        y_test, y_pred_linear_test,
        title=f"Confusion matrix (TEST) - SVC linear, C={best_C_linear}",
        filename="confusion_linear_test.png"
    )
    save_confusion_matrix(
        y_test, y_pred_rbf_test,
        title=f"Confusion matrix (TEST) - SVC rbf, C={best_C_rbf}",
        filename="confusion_rbf_test.png"
    )

    # =========================
    # 4f.ii) Scatter 2D: prawdziwe klasy vs predykcje
    # Wybieramy 2 cechy (np. mean radius i mean texture)
    # =========================
    feat_x_name = "mean radius"
    feat_y_name = "mean texture"

    idx_x = list(feature_names).index(feat_x_name)
    idx_y = list(feature_names).index(feat_y_name)

    X_2d = X[:, [idx_x, idx_y]]

    # predykcje na CAŁOŚCI danych (żeby wykres był "całości danych")
    y_pred_linear_all = model_linear.predict(X)
    y_pred_rbf_all = model_rbf.predict(X)

    # wykres: prawdziwe klasy
    save_scatter_2d(
        X_2d, y,
        title=f"Rzeczywisty podział klas (cechy: {feat_x_name} vs {feat_y_name})",
        xlabel=feat_x_name,
        ylabel=feat_y_name,
        filename="scatter_true_classes.png"
    )

    # wykres: predykcja linear
    save_scatter_2d(
        X_2d, y_pred_linear_all,
        title=f"Predykcja klas - SVC linear (C={best_C_linear})",
        xlabel=feat_x_name,
        ylabel=feat_y_name,
        filename="scatter_pred_linear.png"
    )

    # wykres: predykcja rbf
    save_scatter_2d(
        X_2d, y_pred_rbf_all,
        title=f"Predykcja klas - SVC rbf (C={best_C_rbf})",
        xlabel=feat_x_name,
        ylabel=feat_y_name,
        filename="scatter_pred_rbf.png"
    )

    print("=== ZAPISANE PLIKI (do raportu) ===")
    print("- confusion_linear_test.png")
    print("- confusion_rbf_test.png")
    print("- scatter_true_classes.png")
    print("- scatter_pred_linear.png")
    print("- scatter_pred_rbf.png")
    print()
    print("Gotowe. Wklej obrazki do PDF i opisz: najlepsze C, accuracy, wnioski.")


if __name__ == "__main__":
    main()
