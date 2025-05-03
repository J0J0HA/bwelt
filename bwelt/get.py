import requests
from pathlib import Path


def download_file(file: str) -> None:
    result = requests.get(
        f"https://raw.githubusercontent.com/J0J0HA/bwelt/refs/heads/master/in/{file}", timeout=10
    )
    result.raise_for_status()
    with open(Path() / "in" / file, "wb") as f:
        f.write(result.content)
    print(f"Downloaded {file} to {Path() / 'in' / file}")


def main():
    (Path() / "in").mkdir(parents=True, exist_ok=True)
    print("Downloading input files...")
    for file in [
        "a_example.txt",
        "b_read_on.txt",
        "c_incunabula.txt",
        "d_tough_choices.txt",
        "e_so_many_coins.txt",
        "f_banks_of_the_world.txt",
    ]:
        download_file(file)


if __name__ == "__main__":
    main()
