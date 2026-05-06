from random import choice

player_wins = 0;
bot_wins = 0;

def player_opt():
    player_choice = input("Choose rock, paper or scissor: ");
    player_choice.lower();

    if player_choice == "rock":
        return player_choice;
    elif player_choice == "paper":
        return player_choice;
    elif player_choice == "scissor":
        return player_choice;
    else:
        print("Option not found");
        player_opt();

def bot_opt():
    bot_choice = choice(["rock", "paper", "scissor"]);

    return bot_choice;

while True:

    print("-" * 30);
    player_choice = player_opt();
    bot_choice = bot_opt();
    print("-" * 30);

    if(player_choice == "rock") and (bot_choice == "scissor") \
        or (player_choice == "paper") and (bot_choice == "rock") \
            or (player_choice == "scissor") and (bot_choice == "paper"):
                print(f"Player choosed {player_choice} and bot {bot_choice}"
                " Result: You Win!");
                player_wins += 1;
    
    elif player_choice == bot_choice:
        print("Result: Tie!");
    
    else:
        print("Result: You lost! Bot wins");
        bot_wins += 1;

    print("-" * 30);
    print(f"You have {player_wins} wins");
    print(f"Bot has {bot_wins} wins");
    print("-" * 30);
    player_choice = input("Do you want to play again? ");

    if player_choice in ["SIM", "sim", "Sim", "s", "S"]:
        pass;
    elif player_choice in ["NÃO", "não", "Não", "n", "N"]:
        break;
    else:
        break;
