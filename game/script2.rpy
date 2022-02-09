define d = Character("Bitsy")
define a = Character("Buffy")
define b = Character("Faye")
define gdb = Character("Blake")
define m = Character("Malek")
define c = Character("Cash")
define clc = Character("Kalik")
define s = Character(name="???")
define p = Character("Roxy")

init:
    $ player_name = ""


label start:
    $ player_name = renpy.input("What is your name?", length=32)
    $ player_name = player_name.strip()
    $ player_name = player_name[0].upper() + player_name[1:]
    "Ah, winter break was fun."
    "Hopefully this semester isn't as difficult as last semester, though..."
    "I don't want to write a parallel version of mergesort again..."
    "And what even are spin locks?"
    "THUD!" with hpunch
    "Oww..."
    show data normal with dissolve
    d "Aw man... that hurt..."
    "Are you ok?"
    d "Ah, sorry about that!"
    d "I didn't see you there."
    d "I didn't bonk you too hard, did I?"
    "Nah, I think I'm fine."
    "I didn't even see you coming though."
    d "Haha, I run pretty fast, sorry."
    "No worries."
    "???" "What do you mean \"this isn't working out\"?"
    "???" "It's just not working."
    "???" "We never get to spend any time together because you're always off doing something else..."
    "???" "..."
    d "Looks like something's happening over there..."
    d "Maybe we should go somewhere else..."
    hide data normal with dissolve
    show text "You go downstairs to continue your conversation and avoid eavesdropping on a personal discussion..." with dissolve
    pause 1.5
    hide text with dissolve
    show data normal with dissolve
    d "Phew, that conversation seemed like it was about to get kinda intense..."
    "..."
    d "So, what classes are you taking this semester?"
    "Uh..."
    "I'm taking Computer Systems."
    "..."
    "Oh, I'm also taking Calc 3D, I think."
    d "Oh, nice!"
    d "I'm taking Calc 3D, too!"
    show data normal at midleft with move
    show attack normal at midright with dissolve
    a "Hey, Bitsy!"
    d "Oh hey, Buffy!"
    a "Hello!"
    d "Oh, this is [player_name]."
    a "Ah, nice to meet you!"
    "You too."
    d "Buffy, you're taking Systems this semester too, right?"
    a "Hmm? Yea."
    d "Oh nice! [player_name]'s taking it too!"
    a "Oh cool!"
    d "Anyway, I should probably get going."
    d "What's your next lecture?"
    menu:
        "Calc lecture.":
            jump calc_lecture
        "Systems lecture.":
            jump sys_lecture
    return

label calc_lecture:
    a "Oh cool, that's my next lecture too!"
    d "You guys have fun!"
    d "I have to head to Calc lecture now."
    d "I'll see you later!"
    "See ya!"
    hide data normal with dissolve
    hide attack normal with dissolve
    jump malloc_oh


label sys_lecture:
    d "Oh cool, that's my next lecture too!"
    a "You guys have fun!"
    a "I have to head to Systems lecture now."
    a "I'll see you later!"
    "See ya!"
    hide data normal with dissolve
    hide attack normal with dissolve
    jump malloc_oh