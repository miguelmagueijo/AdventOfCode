from pathlib import Path

class Bag:
    def __init__(self, id: int = -1, red: int = 0, green: int = 0, blue: int = 0, string: str = None):
        self.id = id
        self.red = red
        self.green = green
        self.blue = blue
        
        if isinstance(string, str):
            self.load_from_string(string)

    def load_from_string(self, string: str):
        cubes = string.split(",")

        for c in cubes:
            total, color = c.strip().split(" ")
            
            total = int(total)

            if color == "red":
                self.red += total
                continue

            if color == "green":
                self.green += total
                continue

            if color == "blue":
                self.blue += total

    def update_cubes_based_on(self, base_bag):
        if base_bag.red > self.red:
            self.red = base_bag.red
        
        if base_bag.green > self.green:
            self.green = base_bag.green

        if base_bag.blue > self.blue:
            self.blue = base_bag.blue

    def power(self) -> int:
        return self.red * self.green * self.blue

    def fits_in(self, big_bag):
        return big_bag.red >= self.red and big_bag.green >= self.green and big_bag.blue >= self.blue

    def __str__(self) -> str:
        return f"ID: {self.id} Red: {self.red} | Green: {self.green} | Blue: {self.blue}"

def possible_games(games: list[str], elf_bag: Bag) -> int:
    possible_ids: set[int] = set()
    
    for line in games:
        game_id, game_sets = line.split(":")

        game_id = int(game_id.split(" ")[1])

        for g_set in game_sets.split(";"):
            new_bag = Bag(id=game_id, string=g_set)
            
            if new_bag.fits_in(elf_bag):
                possible_ids.add(game_id)
            else:
                if game_id in possible_ids:
                    possible_ids.remove(game_id)
                break

    return sum(possible_ids), possible_ids

def power_of_min_bag(games: list[str]) -> int:
    bag_powers: list[int] = list()
    
    for line in games:
        game_sets = line.split(":")[1]
        min_bag = Bag()

        for g_set in game_sets.split(";"):
            min_bag.update_cubes_based_on(Bag(string=g_set))
    
        bag_powers.append(min_bag.power())

    return sum(bag_powers), bag_powers

# https://adventofcode.com/2023/day/2#part2

if __name__ == "__main__":
    with open(Path(__file__).with_name("test.txt")) as fp:
        games = fp.readlines()
        test_elf_bag = Bag(red=12, green=13, blue=14)
        test_sum_ids, test_valid_ids = possible_games(games, test_elf_bag)
        assert test_sum_ids == 8, f"Part 1: Test value ({test_sum_ids} = sum({test_valid_ids})) should be 8"
        print("Part 1: Test passed")

        test_sum_powers, test_powers = power_of_min_bag(games)
        assert test_sum_powers == 2286, f"Part 2: Test value ({test_sum_powers}) = sum({test_powers}) should be 2286"
        print("Part 2: Test passed")


    with open(Path(__file__).with_name("input.txt")) as fp:
        games = fp.readlines()

        elf_bag = Bag(red=12, green=13, blue=14)
        sum_ids, valid_ids = possible_games(games, elf_bag)
        print(f"Possible games for Bag ({test_elf_bag}) are ({valid_ids}) which the sum is {sum_ids}")
        
        sum_powers, powers = power_of_min_bag(games)
        print(f"The power of minimum bag for each game is: {sum_powers} which is the sum of {powers}")