from colorama import Fore, Style

print(Fore.GREEN)
print("You wake up and see the fountain of dreams, legend says that if you are lucky, then you will be rewarded with dimonds or a new halo. You decide to give it a try.")
print(Style.RESET_ALL)

print()
# stories = ["You walk up to the fountain hoping to get a new halo, when you make your wish, a witch comes up to you and says, that she needs 1 more person to compete in the potion contest and you excidetly say yes! They hand you a potion book, you decide to make... A. A happiness potion, B. A Flight Potion, C. A Super Strenth potion, D. A Sleepy Potion (A, B, C, or D)", "You walk away from the fountain after you have tossed your dimonds when a famous hunter comes and invites you to hunt with him. He gives you options to hunt for cryptaids or any legendary creature You... A. Look for cryptaids, B. Look for legendary creatures, C. Invite him to trick-or-treat with you, D. Politly decline his offer (A, B, C, or D)", "As you walk back home, you see a little girl crying on the sidewalk. You go up to her and ask what's wrong. She says that she really wants a Halloween costume but cannot a"];
# ansForFirstStory = ["", "", "", ""];
# ansForSecondStory = ["", "", "", ""];
# ansForThirdStory = ["", "", "", ""];

# if(story1)
  # print("A or B or C or D:")
  # if(A)
  #   ansFoFirstStort[]


def choice(dimonds, halo):
  while dimonds > 0:
    print(Fore.RED)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Dimonds: ", dimonds)
    print("Halo: ", halo)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(Style.RESET_ALL)
    print(Fore.CYAN)
    direction = input("You walk up to the fountain hoping to get a new halo, when you make your wish, a witch comes up to you and says, that she needs 1 more person to compete in the potion contest and you excidetly say yes! They hand you a potion book, you decide to make... A. A happiness potion, B. A Flight Potion, C. A Super Strenth potion, D. A Sleepy Potion (A, B, C, or D)")
    print(Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX)
    if(direction == "A"):
      print("You decide to make a happiness potion, once you are done, you hand it to the witch and she turns human. Then she drinks it *Slurp*. She smiles in Glee! She is so happy, she decides to just declare everyone winner and go relax in witch island!")
      dimonds = 0
      halo = 0
      print(Style.RESET_ALL)
      print(Fore.LIGHTMAGENTA_EX)
    elif(direction == "B"):
      print("You decide to make a flight potion. When you are done, you give it to the witch who turns into a human. She drinks it and goes Weeeeee she flies up into the air very joyful and suprissed that such a amatuer could make such a advanced potion! She decides to give you a grand prize! A Halo!")
      dimonds = 10000
      halo = 1
      print("You have succesfully completed!")
      print(Style.RESET_ALL)
      print(Fore.LIGHTMAGENTA_EX)

      print(Fore.LIGHTMAGENTA_EX)
    elif(direction == "C"):
      print("You decide to make a super Strength potion. Once you are finished, you hand it to the witch who turns into a human! She drinks it and becomes super strong! Unfortunetly, she becomes so strong she starts to take advantage of that and breaks all the potions therefore everyone has to run and the competition ends.")
      dimonds = 0
      halo = 0
      print("You have succesfully completed!")
      print(Style.RESET_ALL)

      print(Fore.LIGHTMAGENTA_EX)
    elif(direction == "D"):
      print("You decide to make a sleep potion. When you are done, you give it to the witch who turns into a human. She drinks it and goes to sleep. Everyone tries to wake her up but she has fallen into a deep sleep and the competition cannot go on anymore. All the contests get made at you and start attacking you.")
      dimonds = -39
      halo = 0
      print()
      print("You have done your wish!")
      print(Style.RESET_ALL)
    else:
      print("Please enter a valid choice (A, D, C, D")
      print(Style.RESET_ALL)
choice(10, 0)