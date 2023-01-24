from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.:")
        print("Subclass it and implement enter()")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


        current_scene.enter()


class Ground(Scene):

    def enter(self):
        print("""


        You awaken on the ground.
        Items and objects float about around you.
        Your feet glow with a red light that digs into the Earth.
        You hear a scream in the middle distance.
        You decide to investigate:

                > the source of the screams,
          or
                > this newly found grounding red light surrounding your feet.

        """)

        return 'ground_choice'

class GroundChoice(Scene):

    def enter(self):
        invest = input("""
            >>> """)

        if "scream" in invest:
            return 'fantazoid'

        elif "red" in invest or "light" in invest or "feet" in invest:
            return 'skillz'

        else:
            print("""

            Type "scream" somewhere in your answer to investigate the scream.

            Type "red", "light", or "feet" to learn more about what appears to be grounding you.

            """)
            return 'ground_choice'

class Skillz(Scene):

    def enter(self):
        print("""

        The feeling is warm and tingling at your feet and just past them downward as well.
        It gets colder as you follow the feeling of this light into the Earth.
        It is a strange sensation.
        You definitely feel it as an extension of yourself.
        But at the same time, be it the novelty of this newfound power or its alien nature,
                You sense that it may have a mind of its own.
        With concentration you are able to shift it upward and remove it from the ground.
        You float briefly before it asserts itself back into the earth, grounding you again.

        The screaming continues and may be intensifying.
        You feel the need to:
                > investigate the screaming
                > or spend more time learning about your plazma.
        """)

        while True:
            skillin = input("""
            >>> """)

            if "investigate" in skillin or "screaming" in skillin:
                print("""

                Jarred by the sound, you find yourself running toward it.

                """)
                return 'fantazoid'

            elif "time" in skillin or "learn" in skillin or "plazma" in skillin:

                return 'plazma_attack'

            else:
                print("""

                You feel the need to:
                        > investigate the screaming
                        > or spend more time learning about your plazma.

                """)

class PlazmaAttack(Scene):

    def enter(self):
        print("""

        You feel more deeply into this light now entwined with your body and mind.
        As you do, you notice it has an emotional signature.
        It is angry.
        You find it is more compliant with your intent as you slip into anger.
        You bring to mind that which has so enraged you before...
        """)

        rager = input("""

                (angry thoughts)>>> """)

        print(f"""


        As your mind fixates on this
                the plazma intensifies and you're able to focus it.

        You focus it into your palms and as you open your eyes it blasts out from
            your fingers with the full cathartic power that is your rage toward
                {rager}.

        It shoots out in red lightning, contorting and charring a metal sign to your front.

        You decide to name this newly found faculty "rage lightning."

        You hear the screams again.
            Jarred by the sound, you find yourself running toward it with ease.

            """)
        room_to_breathe = input("""
            >>> """)

        return 'fantazoid'

class Fantazoid(Scene):

    def enter(self):
        print("""

        Finding the source of the screams, you encounter a strange sight.
        Three bugs, each roughly the size of a wolf, slowly close in on a fainted woman
                     who is tangled in the branches of a tree.
        The bugs are an oily white color.
        You could describe them as spider-like or scorpionic,
                    complete with too many reaching and scurrying limbs.
        They each have a stinger protruding from their belly area,
                    which moves with incredible dexterity considering its segmented structure.
        For reasons unknown to you, they are also immune to the effects of this weightless environment.
        They stop their clumsy progress toward the woman as it seems they've taken notice of you.
        One shoots at you with an acid-like fluid projected from the stinger as the other two crawl
            at you with a quick sidewinder scurry.

        Looks like you have to fight.
            >>> evade
            >>> punch
            >>> intimidate

        """)
        me = 30
        sq1 = 10
        sq2 = 10
        sq3 = 10
        evade_before = False



        while True:
            strat = input("""

            >>>   """)
            if me <= 0:
                print("""
        Wow. You were really keen on evading. That didn't work.
        So much so that,
        you've died.

          You'll get em' next time.

                """)
                exit(0)

            elif sq1 <= 0 and sq2 <= 0 and sq3 <=0:

               print("""

               Congratulations!!
        You have won your first battle as your rage subsides.

               """)
               return 'woman'

            elif "rage lightning" in strat:
                print("""

        You summon your rage as you move your awareness from your feet to your hands.
                They begin to glow and produce steam.
            When you open your eyes red lighting cracks from your hands to each of these giant bugs.

            They stop where they are, and they smell like bbq lobster.

                Bugs 1, 2, and 3 have died.
                """)

                sq1 -= 10
                sq2 -= 10
                sq3 -= 10

                print(f"""
                You have {me} hit points of health.
                Bug 1 has {sq1} hit points of health.
                Bug 2 has {sq2} hit points of health.
                Bug 3 has {sq3} hit points of health.
                """)

            elif "evade" in strat:
                print("""

        You go to move, but the plazma won't let you.
        You pull your feet away, but they won't budge from the ground.
        You are struck by acid and take 4 points of damage.

                """)
                me -= 4
                evade_before = True
                print(f"""
                You have {me} hit points of health.
                Bug 1 has {sq1} hit points of health.
                Bug 2 has {sq2} hit points of health.
                Bug 3 has {sq3} hit points of health.
                """)

            elif "punch" in strat:
                sq1 -= 5

                if sq1 > 0 and evade_before == False:
                    print("""
        It's pretty effective. You feel stronger than ever.
            It feels like you'll crack the armor soon.
                """)

                    print(f"""
                 You have {me} hit points of health.
                 Bug 1 has {sq1} hit points of health.
                 Bug 2 has {sq2} hit points of health.
                 Bug 3 has {sq3} hit points of health.
                 """)

                elif sq1 > 0 and evade_before == True:
                   print("""
       It's pretty effective. You feel stronger than ever.
       It seems like the plazma prefers you to take direct action rather than
        acting out of fear or passivity.
                    It feels like you'll crack the armor soon.
               """)

                   print(f"""
                You have {me} hit points of health.
                Bug 1 has {sq1} hit points of health.
                Bug 2 has {sq2} hit points of health.
                Bug 3 has {sq3} hit points of health.
                """)
                elif sq1 == 0:

                    print("""
        You've definitely cracked the armor at this point.
            The hemolymph is spilling out.

                    Bug 1 is dead.
                    """)

                    print(f"""
                    You have {me} hit points of health.
                    Bug 1 has {sq1} hit points of health.
                    Bug 2 has {sq2} hit points of health.
                    Bug 3 has {sq3} hit points of health.
                    """)

                else:
                    print("""
        Hmmm...
            This is...

                You're making a mess.
                It's getting hard to tell if you're hitting the bug or the Earth.
                    """)
                    print(f"""
                     You have {me} hit points of health.
                     Bug 1 has {sq1} hit points of health.
                     Bug 2 has {sq2} hit points of health.
                     Bug 3 has {sq3} hit points of health.
                     """)
            elif "intimidate" in strat:

                if sq2 == 10 and sq3 == 10:
                    print("""
        You give out a good yell.
        It isn't very scary, but all three seize and convulse at the noise.

        When you finish yelling, 2 of the 3 run away.
                """)
                    sq2 -= 10
                    sq3 -= 10
                    print(f"""
                    You have {me} hit points of health.
                    Bug 1 has {sq1} hit points of health.
                    Bug 2 ahs {sq2} hit points of health.
                    Bug 3 ahs {sq3} hit points of health.
                    """)
                else:
                    print("""
            The 2 that ran last time are further away.
            The one that stuck around convulses again.
                    """)

            else:
                print("""
        Looks like you have to fight.
            >>> evade
            >>> punch
            >>> intimidate
                """)

class Woman(Scene):
    def enter(self):
        print("""

            The woman is safely tucked away in the tree branches.
        You're fairly sure you catch a glimpse of someone emerging from behind a boulder.
            You feel a jerking and twisting motion.
        The trees and bushes off in the distance rapidly approach you.
            Your plazma is dragging you somewhere at a quick pace.
        """)

        funnion = input("""
            >>> """)
        return 'finished'


class Finished(Scene):

    def enter(self):
        print("""

        Your Journey Continues....
                    Next Time...



        """)

class Map(object):

    scenes = {
        'ground': Ground(),
        'ground_choice': GroundChoice(),
        'skillz': Skillz(),
        'plazma_attack': PlazmaAttack(),
        'fantazoid': Fantazoid(),
        'woman': Woman(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)



starting = Map('ground')
game = Engine(starting)
game.play()
