
# Secret Message Decoder

This project decodes a hidden uppercase message from a published Google Doc that contains a table of Unicode characters and their positions in a 2D grid.

The script fetches the document, parses the table structure, reconstructs the grid using the provided coordinates, and prints the result so the secret message appears when viewed in a fixed-width font.

## How It Works
- Downloads the published Google Doc as HTML
- Parses the table rows containing x-coordinates, characters, and y-coordinates
- Dynamically builds a 2D grid filled with spaces
- Places each character at its correct position
- Prints the grid to reveal the hidden message

## Requirements
- Python 3.x
- `requests`
- `beautifulsoup4`

Install dependencies:
```bash
pip install requests beautifulsoup4
````

## Usage

```bash
python decode_secret_message.py
```

Or call the function directly:

```python
decode_secret_message("PASTE_GOOGLE_DOC_URL_HERE")
```

## Output

The output is a printed grid of characters. When viewed in a fixed-width font, the characters form readable uppercase letters that represent the secret message.

```
