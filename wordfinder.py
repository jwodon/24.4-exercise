"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    def __init__(self, path="/home/jwodon/Springboard/section24/24.4/words.txt"):
        self.path = path

        self.words = self.pull_words()

        print(f"{len(self.words)} words read")

    def pull_words(self):
        with open(self.path, "r") as file:
            return [word.strip() for word in file]

    def random(self):
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    def pull_words(self):
        words = super().pull_words()
        return [word for word in words if not word.startswith("#")]



