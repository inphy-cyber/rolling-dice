# Rolling dice simulator
import random

print("Rolling Dice Simulator!")
print("beware of the dice, they can be tricky!")
print("Roll the dice for a prize or a penalty! 😈")

prizes = {
    1: [
       "You win a small prize! 🎁 a bag of candy",
        "You lose! 😢 You have to wash the dishes for a week.",
        "You lose! 😢 Your punishment is 3 hours of homework.",
    ],
    2: [
        "You win a small prize! 🎁 a sweet cake tho",
        "You win a small prize! 🎁 a cozy hoodie",
        "You lose! 😢 You got stuck with a giant broccoli.",
        "You win a small prize! 🎁 a bag of candy",
    ],
    3: [
        "You win a medium prize! 🎉 a shopping trip to the mall",
        "You win a medium prize! 🎉 a new pair of shoes",
        "You win a medium prize! 🎉 a movie night package",
    ],
    4: [
        "You win a big prize! 🏆 a vacation for 3 days only!",
        "You win a big prize! 🏆 a free spa day",
        "You win a big prize! 🏆 a brand new bike",
    ],
    5: [
        "You lose! 😂 I can't believe it!", 
        "You hit the jackpot! 🎊 a free shopping spree",
        "You lose! 😂 you have to clean the whole house",
    ],
    6: [
        "You hit the jackpot! 🎊 a lifetime supply of ice cream! (for a week tho so it's limited)",
        "You lose! 😂 your phone battery died at the worst time",
        "You hit the jackpot! 🎊 a luxury dinner for two",
    ],
}

while True:
    choice = input("Want to test your fate? (y/n): ").lower()

    if choice == "y":
        print("Rolling the dice...")
        dice = random.randint(1, 6)
        print("You rolled a", dice)
        print(random.choice(prizes[dice]))
    elif choice == "n":
      print("OK, maybe next time!")
    else:
        print("Invalid input. Please enter y or n.")

