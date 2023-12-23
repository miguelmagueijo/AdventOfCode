from pathlib import Path

def part1(lines: list[str]) -> int:
    line_numbers = list()

    for l in lines:
        first_number = second_number = 0
        found_first = False
        for c in l.strip():
            if c.isnumeric():
                if found_first:
                    second_number = c
                else:
                    first_number = second_number = c
                    found_first = True
        
        line_numbers.append(int(f"{first_number}{second_number}"))

    return sum(line_numbers)

def part2(lines: list[str]) -> int:
    line_numbers = list()
    numbers_str = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for l in lines:
        numbers = list()
        for i, c in enumerate(l.strip()):
            if c.isnumeric():
                numbers.append(c)
                continue

            for j, n_str in enumerate(numbers_str):
                if l[i:].startswith(n_str):
                    numbers.append(j)

        line_numbers.append(int(f"{numbers[0]}{numbers[-1]}"))

    return sum(line_numbers)



if __name__ == "__main__":
    base_path = Path(__file__)

    with open(base_path.with_name("input.txt"), "r") as fp:
        file_lines = fp.readlines()

        print(f"Part 1 calibration total: {part1(file_lines)}")
        print(f"Part 2 calibration total: {part2(file_lines)}")
