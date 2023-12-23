from pathlib import Path

def calibrate(lines: list[str]) -> int:
    numbers = range(0, 10)
    line_numbers = list()

    for l in lines:
        first_number = second_number = 0
        found_first = False
        for c in l.strip():
            if c.isnumeric() and int(c) in numbers:
                if found_first:
                    second_number = c
                else:
                    first_number = second_number = c
                    found_first = True
        
        line_numbers.append(int(f"{first_number}{second_number}"))
        print(line_numbers)

    return sum(line_numbers)


if __name__ == "__main__":
    with open(Path(__file__).with_name("input.txt"), "r") as fp:
        file_lines = fp.readlines()

        print(f"Calibration total: {calibrate(file_lines)}")