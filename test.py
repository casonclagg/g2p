from g2p_en import G2p
g2p = G2p()
import inflect
_inflect = inflect.engine()
print(_inflect.number_to_words(7456.151354, andword=''))

with open("./test.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    for line in lines:
        print(f"{line}\t\t{g2p(line)}")