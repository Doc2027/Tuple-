import random

class DiceGame:
    def __init__(self):
        self.high_score = 0

    def roll_dice(self):
        return [random.randint(1, 6) for _ in range(3)]

    def play_turn(self):
        dice = self.roll_dice()
        print(f"You rolled: {dice}")
        
        while True:
            # Check for tuple out
            if dice[0] == dice[1] == dice[2]:
                print("You tupled out! Game over.")
                return 0
            
            # Fix dice
            fixed_dice = []
            reroll_indices = []
            for i in range(3):
                if dice.count(dice[i]) == 2:
                    fixed_dice.append(dice[i])
                else:
                    reroll_indices.append(i)
            
            # If no rerollable dice, score and end turn
            if not reroll_indices:
                break
            
            print(f"Fixed dice: {fixed_dice}, rerolling dice: {[dice[i] for i in reroll_indices]}")
            reroll = input("Do you want to reroll non-fixed dice? (y/n): ")
            if reroll.lower() == 'n':
                break
            
            for i in reroll_indices:
                dice[i] = random.randint(1, 6)
            print(f"You rerolled: {dice}")
        
        score = sum(dice)
        print(f"You score {score} points this turn.")
        return score

    def play_game(self):
        while True:
            print("\nYour turn")
            turn_score = self.play_turn()
            
            if turn_score == 0:
                print(f"Your high score is: {self.high_score}")
                if input("Do you want to try again? (y/n): ").lower() != 'y':
                    print("Thanks for playing!")
                    break
                else:
                    continue
            
            if turn_score > self.high_score:
                self.high_score = turn_score
                print(f"Congratulations! You have a new high score: {self.high_score}")
            else:
                print(f"Your score for this turn: {turn_score}. High score remains: {self.high_score}")
                if input("Do you want to try again? (y/n): ").lower() != 'y':
                    print("Thanks for playing!")
                    break


