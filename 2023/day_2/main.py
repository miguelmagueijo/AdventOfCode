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



if __name__ == "__main__":
    with open(Path(__file__).with_name("test.txt")) as fp:
        test_elf_bag = Bag(red=12, green=13, blue=14)
        test_sum_ids, test_valid_ids = possible_games(fp.readlines(), test_elf_bag)
        assert test_sum_ids == 8, f"Test value ({test_sum_ids} = sum({test_valid_ids})) should be 8"
        print("Test passed")


    with open(Path(__file__).with_name("input.txt")) as fp:
        elf_bag = Bag(red=12, green=13, blue=14)
        sum_ids, valid_ids = possible_games(fp.readlines(), elf_bag)
        print(f"Possible games for Bag ({test_elf_bag}) are ({valid_ids}) which the sum is {sum_ids}")