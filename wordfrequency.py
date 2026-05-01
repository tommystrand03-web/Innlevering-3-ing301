FILL_WORDS = ['og', 'dei', 'i', 'eg', 'som', 'det', 'han', 'til', 'skal', 'på', 'for', 'då', 'ikkje', 'var', 'vera']


def read_file(voluspaa):
    """
    Leser fil og returnerer liste med linjer
    """
    with open(voluspaa, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]


def lines_to_words(lines):
    """
    Gjør linjer om til rensede ord (lowercase, uten tegnsetting)
    """
    words = []
    remove_chars = ".,:;!?()[]{}\"'"

    for line in lines:
        for word in line.split():
            # fjern tegnsetting
            word = word.strip(remove_chars)
            word = word.lower()

            if word:  # unngå tomme strenger
                words.append(word)

    return words


def compute_frequency(words):
    """
    Lager frekvenstabell (dict)
    """
    freq = {}

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq


def remove_filler_words(frequency_table):
    """
    Fjerner fyllord fra dictionary
    """
    for filler in FILL_WORDS:
        if filler in frequency_table:
            del frequency_table[filler]

    return frequency_table


def largest_pair(par_1, par_2):
    """
    Returnerer paret med høyest verdi (andre element)
    """
    if par_1[1] >= par_2[1]:
        return par_1
    else:
        return par_2


def find_most_frequent(frequency_table):
    """
    Finner mest brukte ord
    """
    items = list(frequency_table.items())

    if not items:
        return None

    largest = items[0]

    for pair in items[1:]:
        largest = largest_pair(largest, pair)

    return largest[0]  # returner bare ordet

from pathlib import Path

def main():
    file = Path(__file__).parent / "voluspaa.txt"

    lines = read_file(file)
    words = lines_to_words(lines)
    table = compute_frequency(words)
    table = remove_filler_words(table)
    most_frequent = find_most_frequent(table)

    print(f"Mest brukte ord: {most_frequent}")


if __name__ == "__main__":
    main()

#endrer denne linjen til å få github til å oppdatere seg på webbasert? 