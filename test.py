from g2p_en import G2p
g2p = G2p()

with open("./test.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    for line in lines:
        print(f"{line.ljust(50)}{g2p(line)}")