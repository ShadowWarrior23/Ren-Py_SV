# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define x = Character("Me")

define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
with flashbulb
 


# The game starts here.

label start:

    "Wow, it's dark in here. I'm wondering about my current state...{p}And what happened to {b}me{/b}?"


    scene bg frveg
    with flashbulb

    "Phew...{p}Much better, but who Am I?"
    python:
        name = renpy.input("What's your name?")

        name = name.strip() or "Farmer"
    
    x "Now I see you. What would you like to see me in the next dialogues?"

    menu:
        "As a boy/man.":
            jump man
        "As a girl/woman":
            jump woman

    label man:
        show man happy at left
        jump starting
    
    label woman:
        show woman happy at left
        jump starting
    
    label starting:
        play music "SV-main.mp3" fadeout 1
        scene bg room
        with Dissolve(2)

    x "I'm [name] and I just inherited my late grandpa's farm at Pelican city. Althugh it looks more like a village or a town,{p}the place is actually great."
    x "Or atleast it seems like it, because I haven't really gotten to wander around."
    x "I'm really tired, better get some {b}sleep{/b}."
    
    scene bg out
    with fade
    show man questioned at left

    x "{cps=15}Where should I head on my first day?{/cps}"

    label whereTo:

        menu:
            "Pelican City":
                jump PC
            "Cindersap Forest":
                jump CF
            "The Mountains":
                jump TM
            "The farm":
                jump TF
        
        label PC:
            scene bg pc
            with Dissolve(.5)
            jump PCA

        label CF:
            scene bg cf
            with Dissolve(.5)

        label TM:
            scene bg tm
            with Dissolve(.5)

        label TF:
            scene bg out
            with Dissolve(.5)

        label PCA:
            x "So {b}this{/b} is Pelican City. "
            x "What location should I go to?"
            menu:
                "Pierre's General Store":
                    jump PGS
                "Harvey's Clinic":
                    jump HC
                "Star Saloon":
                    jump SS
                "Community Center":
                    jump CC
                "Willow's Lane":
                    jump WL
                "George's House":
                    jump GH
                "The Trailer":
                    jump Tr
                "Mayor's Residence":
                    jump MR
                "The Island":
                    jump Isl
                "On second thought...":
                    jump whereTo
                





""" default time_of_day = "morning"

label start:

    label monday:
        "It's monday [time_of_day]"

        menu:
            "What do you want to do?"
            "eat breakfast" if time_of_day in ["morning"]:
                pass # instead of pass you either put the story, remember the action or call a sub-route
            "eat lunch" if time_of_day in ["noon"]:
                pass # instead of pass you either put the story, remember the action or call a sub-route
            "eat dinner" if time_of_day in ["evening"]:
                pass # instead of pass you either put the story, remember the action or call a sub-route
            "go to school" if time_of_day in ["morning", "noon"]:
                pass # instead of pass you either put the story, remember the action or call a sub-route
            "watch tv" if time_of_day in ["afternoon", "evening"]:
                pass # instead of pass you either put the story, remember the action or call a sub-route
            "go to bed" if time_of_day in ["evening"]:
                pass # instead of pass you either put the story, remember the action or call a sub-route

        if time_of_day == "morning":
            $ time_of_day = "noon"
        elif time_of_day == "noon":
            $ time_of_day = "afternoon"
        elif time_of_day == "afternoon":
            $ time_of_day = "evening"
        elif time_of_day == "evening":
            $ time_of_day = "morning"
            # here you either change the day or jump to the next day """

    x "Thank you for this experience!"
    # This ends the game.

    return
