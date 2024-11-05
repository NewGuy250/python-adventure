def get_name():
    return input("Enter your name: ")

def story(name):
    print(f"\nHello, {name}! You find yourself standing at the edge of a dark forest.")
    print("A mysterious voice calls out from the shadows: 'You have been chosen for a quest!'")
    print("In the distance, you see two paths ahead. One leads into the forest, the other towards a mountain range.")
    
    choice1 = input("Do you choose to enter the forest (1) or head toward the mountains (2)? ")
    
    if choice1 == "1":
        print("\nYou venture into the forest, where the trees whisper ancient secrets.")
        print("Suddenly, you hear rustling in the bushes. It's a creature with glowing eyes!")
        choice2 = input("Do you confront the creature (1) or hide behind a tree (2)? ")
        
        if choice2 == "1":
            print("\nYou stand tall and face the creature. It steps closer, but instead of attacking, it speaks.")
            print("'You have shown bravery. Take this enchanted amulet as a reward.'")
            print("You are now the proud owner of a magical amulet that grants you protection.")
            print("The creature disappears, leaving you with newfound confidence.")
        else:
            print("\nYou quickly hide behind a tree, watching the creature pass by.")
            print("It doesn't notice you, and you safely continue on your journey. However, you wonder what might have happened if you had confronted it.")
        
    elif choice1 == "2":
        print("\nYou head toward the mountains, the cold air biting at your skin.")
        print("As you climb, you encounter a group of travelers who warn you about a dangerous dragon living in the mountain pass.")
        choice2 = input("Do you continue to the pass (1) or turn back (2)? ")
        
        if choice2 == "1":
            print("\nYou press on and, as you near the pass, you spot the dragon!")
            print("But, instead of attacking, it offers you a challenge: 'Answer my riddle, and I will let you pass.'")
            print("The dragon's riddle is: 'What comes once in a minute, twice in a moment, but never in a thousand years?'")
            riddle_answer = input("Your answer: ")
            
            if riddle_answer.lower() == "the letter m":
                print("\nThe dragon smiles. 'You have answered correctly. You may pass.'")
                print("You walk past the dragon, and continue on your adventure, feeling wise and victorious.")
            else:
                print("\nThe dragon roars, but surprisingly, it allows you to pass unharmed. Perhaps it appreciates your courage.")
        
        else:
            print("\nYou turn back and return to the village, safe but disappointed. Maybe next time, you'll be braver.")
    
    print(f"\nYour adventure continues, {name}... What other paths will you take? The choice is yours.")
    
def main():
    name = get_name()
    print(f"\nWelcome, {name}, to this adventure!")
    story(name)

if __name__ == "__main__":
    main()
