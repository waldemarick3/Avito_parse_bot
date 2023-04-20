import parser
from config import SETTINGS

if __name__ == "__main__":
    print(parser.AvitoParse(**SETTINGS).check_update())
