
from pathlib import Path

# Sonic Afterlife - Brighter Classic Colors
# Sega Genesis palette format

PALETTE_FOLDER = Path("palette")

ZONES = [
    "Marble Zone.bin",
    "Spring Yard Zone.bin",
    "Labyrinth Zone.bin",
    "Star Light Zone.bin",
    "SBZ Act 1.bin",
    "SBZ Act 2.bin",
    "SBZ Act 3.bin",
    "Special Stage.bin",
    "Title Screen.bin",
]

def brighten(color):
    # Genesis colors have three 3-bit channels.
    red = (color >> 1) & 7
    green = (color >> 5) & 7
    blue = (color >> 9) & 7

    def boost(value):
        if value == 0:
            return 0
        return min(7, value + 1)

    red = boost(red)
    green = boost(green)
    blue = boost(blue)

    return (blue << 9) | (green << 5) | (red << 1)

def main():
    for filename in ZONES:
        path = PALETTE_FOLDER / filename

        if not path.exists():
            print("Skipped:", filename)
            continue

        data = path.read_bytes()

        if len(data) % 2:
            print("Invalid palette:", filename)
            continue

        result = bytearray()

        for i in range(0, len(data), 2):
            color = int.from_bytes(data[i:i+2], "big")
            result.extend(
                brighten(color).to_bytes(2, "big")
            )

        path.write_bytes(result)
        print("Brightened:", filename)

if __name__ == "__main__":
    main()
