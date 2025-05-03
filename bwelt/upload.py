from pathlib import Path
import requests
import argparse


def upload_file(file: Path, secret: str) -> None:
    result = requests.post(
        "https://bwinf.j-sh.de/upload",
        files={"file": file.open("rb")},
        data={"secret": secret},
    )
    print(result.status_code, result.text)

def main() -> None:
    argp = argparse.ArgumentParser(description="Upload a file to result server.")
    argp.add_argument("secret", type=str, help="The secret to use for the upload.")
    argp.add_argument("file", type=Path, help="The file to upload.")
    args = argp.parse_args()
    upload_file(
        args.file.resolve(strict=True),
        args.secret,
    )
    
if __name__ == "__main__":
    main()
