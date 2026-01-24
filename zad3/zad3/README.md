
## Moduły i funkcje

### 1) data_utils.py
chunk(items, size) dzieli listę na kawałki (chunki)
safe_get(d, key, default=None) bezpiecznie pobiera wartość ze słownika

### 2) math_tools.py
add(a, b)dodaje dwie liczby
clamp(x, low, high) ogranicza wartość do przedziału
mean(values) liczy średnią

### 3) text_utils.py
word_count(text)liczy słowa w tekście
is_palindrome(text) sprawdza czy tekst jest palindromem
slugify(text) tworzy prosty slug (np. do URL)

## Jak uruchomić testy
pip install pytest
pytest
