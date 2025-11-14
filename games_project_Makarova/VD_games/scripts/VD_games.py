import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from VD_games.cli import welcome_user

def main():

    welcome_user()

if __name__ == "__main__":
    main()
