





def start():
    print("""
You wake up one day with a smashing headache.\nYou look in the mirror, and a haggard stranger squints back. Groaning, you \n
    \t(a)	go to the kitchen for a glass of water. \n
    \t(b)	bang your head against the wall. \n
    \t(c)	crawl back in bed, pulling the covers over your face. \n
(Make your move by typing a single lowercase letter.)
    """)
    choice = input("> ")

    if choice == "a":
        kitchen()

    elif choice == "b":
        wall()

    elif choice == "c":
        bed()

    elif choice == "A" or choice == "B" or choice == "C":
        print('Turn off caps lock and try again! Enter "ok" to continue.')
        response = input("> ")

        if response == "ok":
            start()

        else:
            dead('You did not enter "ok". GAME OVER.')

    else:
        print("""
        Please review your options and try again. This is a game, not real life.
        Therefore, your options are limited. Enter 'ok' to continue.
        """)
        response = input("> ")

        if response == "ok":
            start()

        else:
            dead('You did not enter "ok". GAME OVER.')



def kitchen():
    print("""
    You grab a glass from the cupboard and turn on the tap.
    Instead of a stream of water, a wispy little sprite wriggles from the faucet.
    She floats across the counter and perches on the edge, quivering slightly.
    "Hey you!" she says in a startlingly bright, nasal voice. “Did you know?" she continued.
    "Creativity can SAVE YOUR LIFE!"" \n
    Suddenly the sprite shapeshifts into an ugly troll.
    The troll pulls out a custom, shiny red Glock handgun and points it at your head.
    When he opens his mouth, the sprite’s nasal tone floats incongruously
    from his be-bearded lips. “You will die if you don’t do exactly what I say.
    First, respond with "ok". Then I will give you your next instructions."
    """)
    response = input("> ")

    if response == "ok":
        import sys, select

        print("""
        The troll continues, "If you want to live, you must perform an act of
        creativity at this very moment. Do something, quick!” \n

        What is the first thing you think of? Type it now!
        """)

        i, o, e = select.select( [sys.stdin], [], [], 10 )

        if (i):
            print('\nYou said, "', sys.stdin.readline().strip(), '"')
            print('That qualifies as an act of creativity. You may proceed. Enter "ok" to continue.')
            response = input("> ")

            if response == "ok":
                kitchen_part_b()

            else:
                dead('You did not enter "ok". GAME OVER.')

        else:
            dead("\n You said nothing! You die. GAME OVER.")

    else:
        dead('\n You did not enter "ok". GAME OVER.')


def wall():
    print("""
    Obviously, your headache becomes much worse. The pain crescendos
    to an overwhelming roar. In the midst of the blinding, pulsing,
    volcanic pain, you start to hallucinate. The image of some kind of
    woodland nymph appears. She’s trying to get your attention.
    It looks very much like she’s yelling at the top of her lungs,
    but over the intensity of the pain you can barely hear her words:
    “Hey you! Did you know? Creativity can SAVE YOUR LIFE!

    Do you hear me?"
    """)
    response = input("> ")

    if "Y" in response or "y" in response:
        wallcont()

    else:
        print('\n"I said, Creativity can SAVE YOUR LIFE!"')
        wallcont()

def wallcont():
    print("""
    The nymph vanishes and so does your headache. The pain's silence is a
    deafening relief. You remember something you need to get at the store.
    You pull a small notepad out of your pocket. Flipping through it, you
    locate your grocery list:
    """)

    list1 = ["silly words", True, 47, "several", "whatever", "my birthday", 91, "\n"]

    for groc in list1:
        print(f"{groc}")

    print("""
    No, wait. That's not your grocery list. Flip through a few more pages.
    Enter "ok".
    """)

    response = input("> ")

    if response == "ok":
        wallcont2()

    else:
            dead('You did not enter "ok". GAME OVER.')


def wallcont2():

    print("""
    Ah yes, here it is:\n
    """)
    list2 = ["lemons", "limes", "dog treats", "crackers", "milk", "pie crust"]

    for groc in list2:
        print(f"{groc}")

    print("""

    Now, what was it again you were going to add to the list?
    """)

    addgroc = input("> ")

    list2.append(addgroc)

    print("""
    Good. Here is your grocery list:
    """)

    for groc in list2:
        print(f"{groc}")

    print("\n")
    print("""
    Is there anything else you would like to add? Something.... might I suggest,
    *creative* ??? If not, enter "no".
    """)

    response = input("> ")

    if response == "no":
        import sys, select
        print("""
        You were indirectly warned that a lack of creativity could end your life.
        This is your last chance to add a creative grocery item to the list!
        But you must hurry! You are running out of time!""")

        i, o, e = select.select( [sys.stdin], [], [], 10 )

        if (i):
            ###
            print('\nGood job. "',sys.stdin.readline().strip(),'" is a rather creative grocery list item. You may proceed.')
            print('Enter "ok" to continue.')

            response = input("> ")

            if response == "ok":
                wall_part_b()

            else:
                dead('You did not enter "ok". GAME OVER.')

        else:
            dead("\n You said nothing! You die. GAME OVER.")

    else:
        print(f"""
        Good job. '{response}' is a rather creative grocery list item.
        """)
        wall_part_b()

def wall_part_b():
    print("Welcome to wall part b.")


def bed():
    print("""
    You drift into a vivid dream. You are hanging by your sweaty palms
    from a tree branch over a large expanse of water. You try to swing
    your legs up over the branch but you’re too weak. You’re starting
    to lose your grip. Suddenly a fairy appears right in front of your face.
    “Hey you!” she says. “Did you know? Creativity can save your life!"

    The fairy whizzes out of sight, but no sooner is she gone than
    you hear a thunderous voice all around you, saying:
    “You will die if you don’t do exactly what I say.
    First, respond with "ok". Then I will give you your next instructions."
    """)
    response = input("> ")

    if response == "ok":
        import sys, select

        print("""
        “Close your eyes and go inside
        Gaze on a color that you adore
        Describe to me what’s in your mind
        The color you see will buy you time.”

        Quickly, now!
        """)

        i, o, e = select.select( [sys.stdin], [], [], 12 )

        if (i):
            print('\nYou said, "', sys.stdin.readline().strip(), '"')
            print('That qualifies as an act of creative imagination. You may proceed. Enter "ok" to continue.')
            response = input("> ")

            if response == "ok":
                bed_part_b()

            else:
                dead('You did not enter "ok". GAME OVER.')

        else:
            dead("\n You said nothing! You die. GAME OVER.")

    else:
        dead('\n You did not enter "ok". GAME OVER.')



def kitchen_part_b():
    print("Welcome to kitchen part B")

def bed_part_b():
    print("""
    Despite the promised salvation you thought you would earn by passing the
    test of imagination, no help comes. You continue struggling to grip the
    tree, until your exhausted muscles finally give out. You are free falling!
    To keep from panicking, you begin to count. 1, 2, 3…
    Somewhere between 8 and 9 you are knocked out by a blow to the head.

    You’re in a dream within a dream. You’re a spirit, or a ghost, or something.
    You’re in somebody’s house but they can’t see you. You’re observing a
    little girl. She runs out to the curb to get the mail for her mother.
    Opening the rusty mailbox, she gasps, for inside is the most amazing piece
    of mail anyone has ever seen! Iridescent, pearly purple paper was shaped
    as a three-dimensional flower with a tiny figure perched on top. No little
    girl, least of all this one, could believe a piece of mail like that could
    be possible. Overcome with excitement, she runs into the house, sneaks past
    her mother, and carefully closes her bedroom door behind her.

    Alas, her mother calls her to the kitchen before she can open the card—-
    or whatever it is! Now, you’re pretty wrapped up in this little drama and
    have quite forgotten about your fall from the tree and the fact that you’re
    a ghost. You watch as Kyla sulks at the kitchen sink. She’s trying to get the
    dishes done as quickly as possible so she can find out what’s in that amazing
    letter.

    In her emotional and hurried state, Kyla fumbles while washing a teacup
    that had belonged to her great grandmother. The teacup springs from her hands
    and as Kyla lunges to catch it, she slips and falls, spraining her wrist. The
    teacup meanwhile hurtles into the kitchen window where it smashes gloriously
    into smithereens.

    While Kyla’s mother fusses as she bustles the child into the car for an
    unplanned trip to the hospital, you float around the house. Curiosity leads
    you straight through Kyla’s bedroom wall. You use your all-seeing ghost eyes
    to read the magical mail addressed to Kyla. Inside the sculptural card was an
    invitation written in glowing gold ink. It read, “You are formally invited
    to a Tea Party presented by the Fairy of the Tall Tall Tree.”

    Suddenly you remember your fall. You feel the impact to your head as if it
    were happening again. But strangely, your head doesn’t hurt. You open your
    eyes to find yourself in a hospital bed. Your wrist is throbbing. There is a
    knock on the door and you expect a nurse or doctor is coming to look after
    you. But it is that dastardly fairy from the tree instead. She sets up a tea
    table right next to the hospital bed, and pours herself a cup of tea.

    The fairy directs her piercing eyes straight into your soul. When she speaks,
    her words sound chillingly familiar:

    “You will die if you don’t do exactly what I say.
    First, respond with "ok". Then I will give you your next instructions."
    """)
    response = input("> ")

    if response == "ok":
        import sys, select

        print("""
        "Answer me quickly," says the fairy.
        “How many loves?”
        """)

        i, o, e = select.select( [sys.stdin], [], [], 12 )

        if (i):
            print('\nYou said, "', sys.stdin.readline().strip(), '"')
            print('That is the right number of loves. Good job. Enter "ok" to continue.')
            response = input("> ")

            if response == "ok":
                bed_part_c()

            else:
                dead('You did not enter "ok". GAME OVER.')

        else:
            dead("\n You said nothing! You die. GAME OVER.")

    else:
        dead("\n You said nothing! You die. GAME OVER.")



def bed_part_c():
    print("\n Welcome to bed part c.")

def dead(why):
    print(why)
    exit(0)

start()
