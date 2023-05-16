define d = Character(name="???")
define a = Character("Buffy")
define b = Character("Faye")
define gdb = Character("Blake")
define m = Character("Malek")
define c = Character(name="???")
define clc = Character("Kalik")
define s = Character(name="???")
define p = Character("Roxy")
define phi = Character(name="???")

init:
    $ config.keymap['dismiss'].remove('K_SPACE')
    $ config.keymap['hide_windows'].append('K_SPACE')
    $ player_name = ""
    $ attack_points = 0
    $ data_points = 0


label start:
    $ player_name = renpy.input("What is your name?", length=32)
    if player_name == "" or player_name == " ":
        $ player_name = "Watashi"
    $ player_name = player_name.strip()
    $ player_name = player_name[0].upper() + player_name[1:]
    scene bg classroom
    "Ah, winter break was fun."
    "I'm glad I escaped Pittsburgh before that winter storm hit."
    "Otherwise I would've had to waste money on snow boots that I'll never use again."
    "Having to walk to Office Hours in the cold was such a drag..."
    "At least my schedule this semester doesn't seem too bad."
    "It's just some systems class, a 3D calc class, and..."
    "THUD!" with hpunch
    "Oww..."
    show bitsy normal with dissolve
    d "Aw man... that hurt..."
    "Are you ok?"
    d "Ah, sorry about that!"
    d "I didn't see you there."
    d "I didn't bonk you too hard, did I?"
    "Nah, I think I'm fine."
    "(Did she just say bonk?)"
    "I didn't even see you coming though."
    d "Haha, I run pretty fast, sorry."
    d "The side effect of being the track team captain, I guess."
    "No worries."
    $ d.name = "Bitsy"
    d "I'm Bitsy, by the way. Nice to meet you!"
    "Oh, nice to meet you too! I'm [player_name]."
    "???" "{i}What do you mean \"this isn't working out\"?{/i}"
    "???" "{i}It's just not working.{/i}"
    "???" "{i}We never get to spend any time together because you're always off doing \"work\"...{/i}"
    "???" "{i}How do I know you're not lying to me?{/i}"
    "???" "{i}The semester literally just started! How can you have so much work to do?{/i}"
    "???" "..."
    d "..."
    d "Maybe we should go somewhere else..."
    hide bitsy normal with dissolve
    scene black
    show text "You go downstairs to continue your conversation and avoid eavesdropping on something personal..." with dissolve
    pause 1.5
    hide text with dissolve
    scene bg classroom
    show bitsy normal with dissolve
    d "Phew, that conversation was too heavy..."
    d "I hope they're both okay."
    "..."
    d "So, what classes are you taking this semester?"
    "Uh..."
    "I'm taking Computer Systems."
    "..."
    "Oh, I'm also taking Calc 3D."
    d "Oh, nice!"
    d "I'm taking Calc 3D, too!"
    show bitsy normal at midleft with move
    show attack normal at midright with dissolve
    d "Oh, hey, Buffy!"
    a "Hey, Bitsy."
    d "Oh, this is [player_name]."
    a "Ah, nice to meet you!"
    "You too."
    d "Buffy, you're taking Systems this semester too, right?"
    a "Hmm? Yea."
    d "Oh nice! [player_name]'s taking it too!"
    a "Oh cool!"
    a "Anyway, I should probably get going."
    d "What's your next lecture?"
    menu:
        "Calc lecture.":
            jump calc_lecture
        "Systems lecture.":
            jump sys_lecture
    return

label sys_lecture:
    $ attack_points += 30
    a "Oh cool, that's my next lecture too."
    d "You guys have fun!"
    d "I have to head to Calc lecture now."
    d "I'll see you later!"
    "See ya!"
    hide data normal with dissolve
    a "It's in Doherty, right?"
    "Yeah, I think so..."
    a "Alright, let's go!"
    hide attack normal with dissolve
    scene black
    show text "You run to Doherty and make it to lecture just in time." with dissolve
    pause 1.0
    hide text with dissolve
    show text "Intro lectures are pretty rudimentary, so the actual lecture content has been omitted." with dissolve
    pause 2.0
    hide text with dissolve
    show text "Just know that you learned something something dangling references are bad and four bits are a nibble." with dissolve
    pause 2.0
    hide text with dissolve
    scene bg classroom
    show attack normal with dissolve
    a "Damn, I thought that lecture would never end!"
    "Yeah, 80 minutes is a pretty long time to just talk about datatypes and pointers."
    "..."
    a "Did you understand the part with the pointer arithmetic problems?"
    a "I got pretty confused..."
    "..."
    "Yea, I think it made sense..."
    "Basically it's just using the addresses as variables and doing math with them, no?"
    "..."
    "It'll probably get more complicated when they start doing wack indexing and dereferencing, though..."
    a "I'm too used to assembly code, so going back to C is a bit of a jump, haha."
    "Ah, understandable."
    a "Return-Oriented Programming go brrrr"
    a "Oh shoot, I have to get to my next class!"
    a "Can you explain the deref stuff to me later?"
    "Yeah, for sure."
    "See you!"
    hide attack normal with dissolve
    jump groceries


label calc_lecture:
    $ data_points += 30
    d "Oh cool, that's my next lecture too!"
    a "You guys have fun!"
    a "I have to head to Systems lecture now."
    a "I'll see you later!"
    "See ya!"
    hide attack normal with dissolve
    d "It's in Wean, right?"
    "Yea, it's on the 7th floor."
    d "Alright, let's go!"
    hide data normal with dissolve
    "(How does she sprint so fast...!?)"
    scene black
    show text "You make it to the lecture early, but realize you're forgotten basically everything about Calc 2." with dissolve
    pause 1.5
    hide text with dissolve
    show text "But it shouldn't matter, since 3D Calc is very different from 2D Calc." with dissolve
    pause 1.0
    hide text with dissolve
    show text "Right...?" with dissolve
    pause 0.75
    hide text with dissolve
    scene bg classroom
    show data normal with dissolve
    d "Wow, I haven't used an integral symbol in so long!"
    d "But I'm glad we get to use floating point numbers in this class."
    "..."
    "You mean decimal numbers?"
    d "Hehe"
    d "You know what I meant."
    d "Brain is in programming mode..."
    "..."
    "Hopefully we never have to use integration by parts in this class..."
    d "Yeah, I don't even remember how to do that..."
    d "Maybe we can find someone to carry us in this class haha"
    d "Oh shoot, I have to get to my track meeting!"
    d "I'll see you later!"
    "See ya!"
    hide data normal with dissolve
    jump groceries


label groceries:
    scene black
    show text "You finally make it to the end of the week and then realize that you haven't bought any groceries, somehow." with dissolve
    pause 1.5
    hide text with dissolve
    "Oh no, I haven't bought any groceries, somehow!"
    scene black
    show text "That's what I just said." with dissolve
    pause 0.5
    hide text with dissolve
    scene bg classroom
    "Where's my Giant Eagle card...?"
    "..."
    "...."
    "..."
    "There it is!"
    "Aw man, I missed the 71A..."
    "..."
    "Oh wait..."
    "The C is the same route, right?"
    "Big brain."
    scene black
    show text "You make it onto the 71C and get to Giant Eagle." with dissolve
    pause 1.0
    hide text with dissolve
    show text "After tossing everything on the instant ramen shelf into your cart, you wander around trying to find some snacks." with dissolve
    pause 2.0
    scene bg classroom
    hide text with dissolve
    "Why do none of these cookies tell you the amount of sugar in them...?"
    "That's pretty sus."
    "There's no way these are healthy..."
    "..."
    "Meh, I'm gonna get them anyway."
    "..."
    "Hold up, does that guy have a cart full of cookies?"
    "..."
    "I should probably go make sure he's not crazy..."
    "Heyo!"
    show cache normal with dissolve
    c "Oh, hello. Sorry, I'm blocking this shelf, aren't I?"
    "What's with the cart full of cookies?"
    c "...?"
    c "Oh.."
    c "Uhhh...."
    c "I'm kinda going through a personal thing right now."
    c "So I was gonna just eat a shit ton of cookies to feel better."
    "Oh, sorry."
    "I didn't mean to pry."
    c "Nah, no worries."
    c "Wait, you're in SCS too, right?"
    c "I think I saw you in Systems lecture."
    "Oh, yeah!"
    "I'm [player_name]."
    "Nice to meet you!"
    $ c.name = "Cash"
    c "I'm Cash."
    c "Oh, can you help me carry some of these to the counter?"
    "Oh sure, no problem."
    hide cache normal with dissolve
    scene black
    show text "You help Cash carry his stash of cookies up to the register so that you can both check out." with dissolve
    pause 1.0
    hide text with dissolve
    show text "After paying for your food, you notice that Cash seems a little distracted by someone." with dissolve
    pause 1.0
    hide text with dissolve
    show text "What a simp." with dissolve
    pause 0.5
    hide text with dissolve
    scene bg classroom
    show cache normal with dissolve
    c "Yo, who is that?"
    c "She's pretty hot."
    "Uh...."
    "Oh, I think she's taking Systems too."
    "Her name starts with F, I think..."
    "..."
    "....?"
    "...!"
    "Oh, her name's Faye."
    c "Hmm..."
    "(Welp, I guess one way to get over a breakup is to instantly fall in love with someone else...)"
    show cache normal at right with move
    show bomb normal at left with dissolve
    c "Hello!"
    b "Hi!"
    c "Uh.."
    c "I like your dress!"
    b "!"
    b "Haha, thanks!"
    b "I made it myself."
    "(...)"
    "(She looks like a yandere.)"
    c "I'm Cash, nice to meet you!"
    b "Oh, you too! I'm Faye."
    c "You're taking Systems this semester too, right?"
    b "Yeah!"
    c "Cool!"
    c "..."
    c "Uhh so..."
    "..."
    b "...?"
    c "..."
    c "Will you go out with me?"
    "(..!)"
    "(Holy shit, he just went for it, didn't he?)"
    b "..."
    b "Sure, I'd love to!"
    "(Wat)"
    "(This feels like a scene from a romance anime or something...)"
    c "Uh.."
    c "Should we exchange numbers then?"
    b "Yeah!"
    "(I should probably get out of here now...)"
    "Welp, I'll see you later."
    c "Bye!"
    c "Thanks for helping me with these cookies!"
    b "Damn, that is a lot of cookies..."
    hide bomb normal with dissolve
    hide cache normal with dissolve
    jump hw_prologue