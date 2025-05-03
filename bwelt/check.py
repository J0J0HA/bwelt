import argparse
from collections import namedtuple
from pathlib import Path


Bank = namedtuple("Bank", ["coins", "register", "rate"])


def read_input_file(file: Path):
    content = file.read_text()
    lines = content.splitlines()
    m, b, d = map(int, lines[0].split())
    coins = [int(x) for x in lines[1].split()]
    banks = []
    for b in range(b):
        b_idx = 2 + 2 * b
        n, t, p = map(int, lines[b_idx].split())
        midxs = [int(x) for x in lines[b_idx + 1].split()]
        bmvals = set(sorted(midxs, key=lambda x: coins[x], reverse=True))
        banks.append(Bank(bmvals, t, p))
    return d, coins, banks

def read_output_file(file: Path):
    content = file.read_text()
    lines = content.splitlines()
    b = int(lines[0])
    banks = []
    for b in range(b):
        b_ln = b * 2 + 1
        b_idx, m_cnt = map(int, lines[b_ln].split())
        midxs = [int(x) for x in lines[b_ln + 1].split()]
        banks.append((b_idx, midxs))
    return banks


def main() -> None:
    argp = argparse.ArgumentParser()
    argp.add_argument("infile", type=Path)
    argp.add_argument("outfile", type=Path)
    args = argp.parse_args()

    max_d, coins, banks = read_input_file(args.infile)
    print()
    print("Banks:")
    for bank in banks:
        print(" -", bank)
    regs = read_output_file(args.outfile)
    print()
    print("Steps:")
    for step in regs:
        b_idx, midxs = step
        print(f" - Bank {b_idx}: {midxs}")
    print()
    
    curr_d = 0
    monay = 0   # Yes, not money, monay.
    
    for step in regs:
        b_idx, midxs = step
        bank = banks[b_idx]
        curr_d += bank.register
        time_left = max_d - curr_d - 1
        if time_left < 0:
            print(f"Bank {b_idx} is too late.")
            break
        bank_coins = midxs[:bank.rate * time_left]
        for i in bank_coins:
            if i not in bank.coins:
                print(f"Bank {b_idx} has coin {i} but not in coins.")
                return
        for sbank in banks:
            if sbank == bank:
                continue
            for coin in bank_coins:
                while coin in sbank.coins:
                    sbank.coins.remove(coin)
        monay += sum(coins[i] for i in bank_coins)
        
    print(f"Monay: {monay}")
    


if __name__ == "__main__":
    main()
