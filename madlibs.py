from sample_madlibs import hp, code, zombie, hungergames, taco_stand
import random

if __name__ == "__main__":
    m = random.choice([hp, code, zombie, hungergames, taco_stand])
    m.madlib()
