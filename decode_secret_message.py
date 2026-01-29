import requests
from bs4 import BeautifulSoup

def decode_secret_message(doc_url: str) -> None:
    response = requests.get(doc_url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    entries = []

    # Google Docs tables → <table> → <tr> → <td>
    for row in soup.find_all("tr"):
        cells = [c.get_text(strip=True) for c in row.find_all("td")]
        if len(cells) != 3:
            continue

        try:
            x = int(cells[0])
            char = cells[1]
            y = int(cells[2])
        except ValueError:
            continue

        entries.append((char, x, y))

    if not entries:
        print("No valid entries found.")
        return

    max_x = max(x for _, x, _ in entries)
    max_y = max(y for _, _, y in entries)

    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for char, x, y in entries:
        grid[y][x] = char

    for row in grid:
        print(''.join(row))


if __name__ == "__main__":
    decode_secret_message(
        "https://docs.google.com/document/d/e/2PACX-1vRPzbNQcx5UriHSbZ-9vmsTow_R6RRe7eyAU60xIF9Dlz-vaHiHNO2TKgDi7jy4ZpTpNqM7EvEcfr_p/pub"
    )
