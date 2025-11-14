from VD_games.engine import run_game
from VD_games.games.prime import DESCRIPTION, generate_question, get_correct_answer

def main():
    run_game(DESCRIPTION, generate_question, get_correct_answer)

if __name__ == "__main__":
    main()
