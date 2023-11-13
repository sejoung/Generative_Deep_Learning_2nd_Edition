class RealDraw:
    def __init__(self, art, tech):
        self.art = art
        self.tech = tech

    def draw(self):
        print(f"Drawing {self.art} "
              f"with {self.tech}")


if __name__ == "__main__":
    RealDraw("WebToon", "AI").draw()



class Art:

    def challenges(self):
        print("technology")


class Technology:

    def inspires(self):
        print("art")


if __name__ == "__main__":
    Art().challenges()
    Technology().inspires()
