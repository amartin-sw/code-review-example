from sys import exit


def sky_start():
    print("""\n\n\tYour leap of faith makes as much sense as anything else considering the circumstances.
        Throwing caution to the wind as it continues picking up around you, you leap from the tree and
        take off in your uncontrolled straight line flight. All you can do now is choose where to look.""")
    sky()

def sky():
    looked_before = 0

    while True:
        look = input("\n\n\tLook up or down? \n\n\t>>> ")
        if "nonsense" in look:
            print("""\n\t...Your will is indominable. You win.\n""")
            exit(0)
        elif "down" in look and looked_before == 0:
            print("""\n\n\tYou quickly regret your decision as its finality sets in.
        The world below you begins looking more and more like a diorama miniature
        as you surpass the last few objects that had altitude on you.
        Though your altitude has changed, your choices have not.\n""")
            looked_before += 1
        elif "down" in look and looked_before == 1:
            print("""\n\n\tThat world below gets smaller and smaller.
        And the wind is picking up in intensity and northwardly-ness.\n""")
            looked_before += 1
        elif "down" in look and looked_before >= 2:
            print("""\n\n\tThat world below gets smaller and smaller.
        And the wind is picking up in intensity and northwardly-ness.

        You know what they say:
        You'll never get anywhere looking down your whole life.\n""")
        elif "up" in look:
            print("""\n\n\tYou look up.
        It is dazzling and dizzying.
        No stars can be seen.
        They went out with the sun.
        The ambient light you find yourself in is like that of the earliest dawn or the latest twilight.
        Between the northern red eye vortex, the cracked sky, and the red mist snaking through it,
            it's hard to focus on any one phenomenon.""")
            res_sky()
        else:
            elser()

def res_sky():

    print("""\tFinally, though, your attention is captured by...\n""")
    while True:
        attention = input("""\t>>> """)

        if "nonsense" in attention:
            print("""\n\n\t...Your will is indominable. You win.\n""")
            exit(0)

        elif "northern" in attention or "eye" in attention or "vortex" in attention:
            print("""\n\n\tIt is an imposing figure.
            Three concentric circles form ovals to your sight.
        The outer most is a very pale, very light shade of red. It's almost pink, but just a bit darker.
            The middle circle is a dark shade of red.
        Within that is the black circle from which the vortex has been emanating.
            This vortex, which started small, has gained considerable size.
        You notice the wind has been picking up all this time and wonder.
            Its circling motion reminds you of the little whirlpools that form at the
                end of a bath sometimes, but upside-down. And the scale is astonishing.

        The cracked sky and red snaking mist now compete for your attention.\n""")

        elif "cracked" in attention:
            print("""\n\n\tThe light shining through the cracks in the sky mesmerizes you.
            It is like nothing you've ever seen. It is somehow multicolor and monochrome at
        the same time; you suspect this may be a new color entirely. And it is, but the novelty of
            it allows your perception only the brightest of white.
        The strange red mist falling through the cracks now seems to call to you, and
            the giant red eye vortex to the north is hard to ignore.\n""")

        elif "mist" in attention:
            print("""\n\n\t\tMist was an inadequate descriptor.
            As you get closer to it, and it continues descending from above, you get a better look
                at its texture and structure.
            While this amorphous phantom is clearly made from light, the slimy texture it imparts
                    on your eyes is truly alien.
                It is pooling itself in various areas, and from these pools it branches into fractals.
            The wiggling branches produce a number of smaller branches as these smaller branches do the same.
        They consume your vision as you feel a warm tingling sensation in your fingers and toes.

        It's hard to know what is truly occurring, but you can't help but feel like it's noticed you and
                        is closing in on your location.
        Your chest gets cold.
            The warmth in your extremities moves inward.
                Your sight is completely consumed with these translucent red slimy light branches.
            Their numbers grow infinite as you lose the concept of your identity and that of time.
        Warmth, cold, and wiggling lines is all you know before it is consumed by blackness,
            and you begin to dream. \n""")
            possession()
        else:
            elser()

def possession():
    dream = input("""\n\t This dream is unlike any other. In it you see...
    \n\t>>> """)
    print("""

            You are awoken and standing in the presence of an older woman and a younger man.
          There is no ground and your surrounds are entirely a brilliant white.
        You notice that it's actually that novel color beyond the cracked sky, but white is still
                        the closest color to it that you can name.
        Looking down at your body, you can see you're covered in an aura of that red slimy light.
          This red light fills the eyes of the two figures.
            The two figures begin speaking, sometimes in unison and sometimes in turns.
                They say,

        "I am the plasma personified. Some call me the apocalypse. Others call me Apollyon.
        Some call me Artemis and others call me Ragnarok.""")

    understand = input("""\tA surprise, to be sure, but deeply down, you knew I was coming someday." \n\n\t>>> """)

    print(f"""

                "I have possessed your vessel.
            In-so-doing this and as an aspect of your judgement,
          I have borne witness to your dreams. I saw...

                        {dream}

        I've woken you, because you are one of the few who may decide.
            It is not appropriate that you make this decision in your unconscious state, and as such,
          I have restored your previous consciousness for a time.
        You have been deemed worthy to join me in my purpose of cleansing this world.
          While most who are worthy fall clearly into their role, you have access to both,
            but must choose one."\n""")

    decide = input("\tAre you ready to make this choice?\n\n\t>>> ")

    print("""

            "You have been called into service; that cannot be changed. You may not
        abstain from choosing and you may choose only one.

          Have you arrived here that you may indulge your inner fire of justified wrath and
            raze every remnant of evil you find in what is left and left over in this dying world?
          Choosing this, you will also be required to destroy all who are out of phase
        with the coming age, that they may then recycle into vessels of the realm currently
          being made new.

          Or do you desire the arduous and patient work of preserving those deemed to have
        the potential of righteousness in the coming age? Choosing this, you would also be
          obligated guide them through the inner work of destroying those internal forces choking
                    their great potential.

        Righteous Razer or Longsuffering Guide; You may choose."\n """ )
    final_choice()
def final_choice():
    RR_LG = input("\t>>> ")
    righteous = "Righteous Razer"
    righteous2 = "righteous razer"
    longsuffering = "Longsuffering Guide"
    longsuffering2 = "longsuffering guide"



    if (righteous in RR_LG or righteous2 in RR_LG) and (longsuffering in RR_LG or longsuffering2 in RR_LG):
        print("""

        I told you before, you must choose only one.
            The reasons are beyond your understanding as well as my reach.
                This can not be changed.
                """)
        final_choice()

    elif righteous in RR_LG or righteous2 in RR_LG:
        print("""\n\n\t"So it is. Go forth and exact my purpose."\n""")
        import Plazma2RazerBoog.py

    elif longsuffering in RR_LG or longsuffering2 in RR_LG:
        print("""\n\n\t"So it is. Go forth and exact my purpose."\n""")
        
    else:
        print("""

                        It is irrelevant now.
        You must choose one or the other.
                There is no other way.
                """)
        final_choice()






def blue_start():
    print("""\n\tI still need to do this part\n""")






def hose_start():
    print("""

            You have elected the way of........
        Completing Tasks!!!

        You must type "task 1" to complete task 1.
            Also, you must type "task 2" to complete task 2.
        Further, you must type "task 3" to complete task 3.

        Then, AND ONLY THEN, you may "proceed" to the hose story line.""")
    tasks_before_hose()

def tasks_before_hose():
    task1done = False
    task2done = False
    task3done = False
    while True:
        very_task = input("""\n\t>>> """)
        if very_task == "task 1":
            print("""\n\tThis is the first of three tasks.
        You have done well in at least one third of the total tasks.""")
            task1done = True
        elif very_task == "task 2":
            print("""\n\tThis is the second of three tasks.
        You have done well in at least one third of the total tasks.""")
            task2done = True
        elif very_task == "task 3":
            print("""\n\tThis is the third of three tasks.
        You have done well in at least one third of the total tasks.""")
            task3done = True
        elif very_task == "proceed":
            if task1done == False and task2done == False and task3done == False:
                print("""\n\tLazy! You didn't even complete one of these very important
        non-trival tasks.
        You... have .... died........
        And you must start over. Do all three tasks.""")
                tasks_before_hose()
            elif task1done == True and task2done == True and task3done == True:
                print("""

        We are so very proud of you.
                Your courage and dedication are no longer in question.
            Congratulations.
                    It is time to move on to the hose story line.\n""")
                ready = input("""\tAre you ready to go?\n
        >>> """)
                hose_real()
            elif task1done == True and task2done == False and task3done == False:
                print("""\n\tWell, it seems task 1 is nice and completed, but
        tasks 2 and 3 are woefully incomplete.
        You must start over....""")
                tasks_before_hose()
            elif task1done == False and task2done == True and task3done == False:
                print("""\n\tWell, it seems task 2 is nice and completed, but
        tasks 1 and 3 are woefully incomplete.
        You must start over....""")
                tasks_before_hose()
            elif task1done == False and task2done == False and task3done == True:
                print("""\n\tWell, it seems task 3 is nice and completed, but
        tasks 1 and 2 are woefully incomplete.
        You must start over....""")
                tasks_before_hose()
            elif task1done == True and task2done == True and task3done == False:
                print("""\n\tHow could you!?! How dare yOU!!!
        TASK 3 IS THE LASTEST OF NUMERICAL TASKS IN THE INSTRUCTIONS
        We will begrudgingly admit that you did tasks 1 and 2. but still...
        You must start over....""")
                tasks_before_hose()
            elif task1done == True and task2done == False and task3done == True:
                print("""\n\tHow could you!?! How dare yOU!!!
        TASK 2 IS THE MIDDLEIST OF NUMERICAL TASKS IN THE INSTRUCTIONS
        We will begrudgingly admit that you did tasks 1 and 3. but still...
        You must start over....""")
                tasks_before_hose()
            elif task1done == False and task2done == True and task3done == True:
                print("""\n\tHow could you forget task 1?
        It's the first task numerically.
        Good job on tasks 2 and 3.
        Sadly, though,
        You must start over....""")
                tasks_before_hose()

            else:
                elser()
        elif "?" in very_task:
            print("\n\tWe are not taking questions at this time.")
        else:
            print("""\n\tWe don't have time for your philosophical mumbo jumbo.
        These very important tasks are not going to complete themselves.""")


def hose_real():
    print("""

        Great! Here we go.""")
    print("""
        By dutifully completing tasks that may or may not have pertained to aiming your jump,
            You carefully jump down and to the left, taking hold of the hose before bouncing off of the ground.
        You pull gently on the hose until you are grounded.
            You think of a good idea that is kind of boring, and a bad idea that seems more fun.\n""")
    hose_choice()

def hose_choice():
    choice = input("\t>>> ")
    if "good idea" in choice or "boring" in choice:
        print("\n\n\tZero gravity horizontal rock climbing it is.")
        hose_climber()
    elif "bad idea" in choice or "fun" in choice:
        print("""
        That's the spirit!""")
        hose_tubeman()
    else:
        print("""\n\tThat's all well and good, but we're either doing the good idea or the bad idea.

        """)
        hose_choice()
def hose_climber():
    print("""
        On closer inspection, you confirm that the hose is actually two hoses
            connected in the middle.
        You detach them from each other and tie both to your waist.
        You tie the end of one to a park bbq, and detach the other from the faucet.
        You can now travel about in a limited range without fear of falling up.

        It is neat.
        Would you like to check out the leaf blower?
        """)
    hose_climber_choice()

def hose_climber_choice():
    other_choice = input("""\t>>> """)
    if other_choice == "no" or other_choice == "No" or other_choice == "NO":
        print("""

        Alright.
        You don't really have the range to go anywhere else.
        ...
          ...
        ...
          ...
        ...
           ...!

        Oh no! The hose broke!
        You are falling up now!!!""")

        input("""\n\tDo you want to look up?

        >>> """)
        segway_sky()
    elif other_choice == "yes" or other_choice == "Yes" or other_choice == "YES":
        leaf_start()
    else:
        print("""
        It's a simple yes or no question.""")
        hose_climber_choice()



def hose_tubeman():
    print("""
        You've gathered the slack in a coil at your waist.
        You look at the faucet.
        You look at the floating objects.
        You look back at the faucet...""")
    input("""\n\tAre you ready?

        >>> """)
    print("""\n\tFaucet go full blast Water go BRRRRRR.

        Wacky-waving-inflatable-arm-flailing-tube-man!
        Wacky-waving-inflatable-arm-flailing-tube-man!
        Wacky-waving-inflatable-arm-flailing-tube-man!

        You have embraced the wacky.
            You have become the waving.
                You are one with the flailing.
            in the inflatable-tube-man style.
        One does not ask,
            How is there water pressure if gravity is turned off?
        One takes for granted that the water from this spout is pressurized by other means.

        You briefly appreciate the beauty of the thousands of floating droplets left in your wake before
            the slipperiness gets the best of you.

        You lose your grip and are flung into the sky.""")

    input("""\n\tDo you want to look up?

        >>> """)
    segway_sky()

def segway_sky():
    print("""

        Great!
        """)
    print("""\n\tYou look up.
        It is dazzling and dizzying.
        No stars can be seen.
        They went out with the sun.
        The ambient light you find yourself in is like that of the earliest dawn or the latest twilight.
        Between the northern red eye vortex, the cracked sky, and the red mist snaking
        through it, it's hard to focus on any one phenomena.""")
    res_sky()



def leaf_start():
    print("""
        You finagle your way over to the adjacent tree.
        You climb to the leaf blower caught in it.
        The engine is idling.
        You carefully strap it to your back.

        You are now a very imprecise and clunky Iron Man.
        It is a good and dizzying time, until you run out of gas.
        You begin falling upward.
        """)
    input("""\n\tDo you want to look up?

    >>> """)
    segway_sky()











# This is an Easter egg for Dad
def super_redhawk():
    print("""\n\tWoah there buddy. Okay, okay... no more apocalypse.
            We see your will is indominable.
            You win.
        Congratulations.\n""")
    exit(0)






def elser():
    print("""\n\tYour mind does wander, and it helps keep you sane.
        Though, calming down now, you're able to think more clearly.\n""")






def tree():
    print("""
        The sun has gone out.
        The sky is cracked.
            Spider shatter fractures fill the emptiness above with brilliant white light.
        A pale red mist spills from the cracks.
            It forms into undulating snake-like shapes slithering downward.
        To the north, two giant red circles surround a smaller one in black.
            This red eye in the northern sky begins emanating a vortex which pulls to it's center.
        The Earth seems to be in freefall as all untethered items begin to float.
            You find yourself gripped firmly to a tree.
        Looking up, you see the slithering red mist morph into red hydras of electric light.
            Looking down, you see a blue light shining through the front pocket of your jeans.
        To your left, you see a garden hose hovering just above the ground, swaying in the gentle wind.
            To your right, you see a leaf blower caught in the adjacent tree.
        Whether you go up, down, left, right, or stay where you are, there is no precedent to inform your decision.
            You gather yourself to make a choice.\n""")
    tree_choice()
    # \tBehind you....
    # \tTo your front there is....\n""")

def tree_choice():
    im_blue_aba_de_aba_die = False
    stay_state = 0
    while True:
        choice = input("\t>>> ")
        if "super" in choice or "redhawk" in choice:
            super_redhawk()
        elif "up" in choice:
            sky_start()
        elif "down" in choice and im_blue_aba_de_aba_die == False or "pocket" in choice and im_blue_aba_de_aba_die == False or "blue" in choice and im_blue_aba_de_aba_die == False or "jeans" in choice and im_blue_aba_de_aba_die == False:
            # blue_start()
            print("""

        You investigate this strange blue light in your front pocket.
        It is a small futuristic device with a flashing blue button.
        You build your nerve to push it.
        You push it.
        Nothing happens.
        It kinda feels like an undeveloped idea.
        """)
            im_blue_aba_de_aba_die = True
        elif "down" in choice and im_blue_aba_de_aba_die == True or "pocket" in choice and im_blue_aba_de_aba_die == True or "blue" in choice and im_blue_aba_de_aba_die == True or "button" in choice and im_blue_aba_de_aba_die == True:
            print("""

        You did this already.
        It didn't do anything and felt like an undeveloped idea.
                It still doesn't do anything.
            """)
        elif "left" in choice or "hose" in choice:
            hose_start()
        elif "right" in choice or "leaf" in choice:
            leaf_start()
        elif "stay" in choice:
            stay_state += 1
            if stay_state == 1:
                print("""

        You slow down to carefully look around to consider your
                    options and surroundings for the first time.
        You'd have to climb several branches to get to the leaf
                blower, which could risk an upward fall.
        Though, if it still works, maybe you could get it to push
                you where you need to go.
                """)
            elif stay_state == 2:
                print("""

        Not one for rash decisions, you examine the hose more closely.
            As it lofts in the gentle breeze, you notice that it could
                be used as a tie off rope.
            The sky vortex to the North is noticeably bigger.
                """)
            elif stay_state == 3:
                print("""

                Looking up, your eyes lock on to the red misting light that is
            snaking through the cracked sky. It's getting closer.

        The wind has started to pick up. You consider throwing caution to it,
            and taking a leap upward to see what this bizarre sky has in store.
        While the items around you could delay the inevitable, you can't shake
            the feeling that one way or another, the sky will be your fate.
                """)
            elif stay_state == 4:
                print("""

        The blue light in your pocket has started blinking.
                """)
            elif 5 <= stay_state <=6:
                print("""

        The wind has started picking up more. Your grip fatigues.
        You're scared to move, but as you wait, it seems, your conditions
                deteriorate.

                """)
            else:
                print("""

        You've waited for 7 units of waiting time.
            The wind is stronger.
        Your body and mind have reached their limit.
            Anything is better than waiting here.

        You take a final look around and jump up to meet the sky.

                """)
                input("""\n\n\tAny last words?

        >>> """)
                sky_start()
        elif "nonsense" in choice:
            print("\n\t...Your will is indominable. You win.")
            exit(0)
        elif "devpos" in choice:
            possession()
        elif "choice" in choice:
            final_choice()
        else:
            elser()



tree()
