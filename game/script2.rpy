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
    $ player_name = ""
    $ attack_points = 0
    $ data_points = 0


label start:
    $ player_name = renpy.input("What is your name?", length=32)
    $ player_name = player_name.strip()
    $ player_name = player_name[0].upper() + player_name[1:]
    scene bg classroom
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
    $ d.name = "Bitsy"
    d "I'm Bitsy, by the way. Nice to meet you!"
    "Nice to meet you too!"
    "???" "What do you mean \"this isn't working out\"?"
    "???" "It's just not working."
    "???" "We never get to spend any time together because you're always off doing something else..."
    "???" "..."
    d "Looks like something's happening over there..."
    d "Maybe we should go somewhere else..."
    hide data normal with dissolve
    scene black
    show text "You go downstairs to continue your conversation and avoid eavesdropping on a personal discussion..." with dissolve
    pause 1.5
    hide text with dissolve
    scene bg classroom
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

label sys_lecture:
    $ attack_points += 30
    a "Oh cool, that's my next lecture too!"
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
    "Yeah, 90 minutes is a pretty long time to just talk about datatypes and pointers."
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


label hw_prologue:
    scene black
    show text "A few days later..." with dissolve
    pause 1.0
    hide text with dissolve
    scene bg classroom
    "Ah, shoot."
    menu:
        "I haven't turned in my calc homework!":
            jump calc_hw
        "I haven't turned in my programming homework!":
            jump prog_hw
    
label calc_hw:
    $ data_points += 30
    "I should find Bitsy and compare answers first."
    "..."
    "Oh, there she is.."
    show data normal at midright with dissolve
    show adb normal at midleft with dissolve
    d "So this one is just sin(theta), right?"
    "ADB" "No, BS BS! It's definitely cos(theta)."
    "ADB" "You get sin(theta) from doing cross product, not dot product."
    d "Oh, right."
    d "Lemme change this then..."
    d "..."
    d "Oh, hey [player_name]!"
    d "Do you want to check answers too?"
    "Yeah, I think I got most of the questions though, I'm just stuck on the last one."
    "ADB" "Oh, that's the plane intersection one, right?"
    "ADB" "Just use the equation on the formula sheet."
    "ADB" "gg trivial"
    "Damn, I didn't realize we had a formula sheet.."
    d "Yeah, they hid it on the course website somewhere.."
    "..."
    "Ah ok."
    "Lol that just gives you the answer, doesn't it..."
    "ADB" "Yeah, trivial, no?"
    "Alright, that should be it, I think."
    "Are both of you done?"
    "ADB" "Yaya"
    d "Yeah, I just mixed up cross and dot product."
    "Oh rip."
    "You understand it now though, right?"
    d "Yea yea, it's all good."
    "Alright, time to turn in, then."
    "ADB" "Lezgo!"
    hide data normal with dissolve
    hide adb normal with dissolve
    scene black
    show text "You manage to hand in your homework submission a breaking 2 minutes before lecture starts." with dissolve
    pause 1.5
    hide text with dissolve
    show text "Unfortunately, this lecture made even less sense than the last one." with dissolve
    pause 1.0
    hide text with dissolve
    scene bg classroom
    show adb normal at midleft with dissolve
    show data normal at midright with dissolve
    "..."
    "This lecture made even less sense than the last one."
    "ADB" "That was some BS BS."
    d "I never thought I'd have to do a quadruple integral..."
    "Imagine if integration by parts shows up on the midterm."
    "That would not be fun."
    "ADB" "Yo reject reject!"
    "ADB" "Integration by parts is very easy."
    d "But we're not all big math brains like you, lol."
    "ADB" "Baba"
    "I need to eat something before my next class so I can actually pay attention during review session, so I'll see you guys later!"
    d "Bye!"
    "ADB" "See ya!"
    hide adb normal with dissolve
    hide data normal with dissolve
    jump lunch

label prog_hw:
    $ attack_points += 30
    "I should find Buffy and compare answers first."
    "..."
    "Oh, there she is.."
    show attack normal at midright with dissolve
    show adb normal at midleft with dissolve
    a "So this one is just two's complement added to this value, right?"
    "ADB" "No, BS BS! You have to create a bitmask too."
    "ADB" "That's the only way you can figure out which bits are set."
    a "Oh, right."
    a "Lemme change this then..."
    a "..."
    a "Oh, hey [player_name]!"
    a "Do you want to check answers too?"
    "Yeah, I think I got most of the tasks though, I'm just stuck on the last one."
    "ADB" "Oh, that's the true three fourths one, right?"
    "ADB" "You have to divide first so that you don't overflow."
    "ADB" "gg trivial"
    "How are you so good at this.."
    a "I mean it's the only logical way to do it right?"
    "..."
    "Ah ok."
    "Damn it really was that simple..."
    "ADB" "Yeah, trivial, no?"
    "Alright, that should be it, I think."
    "Are both of you done?"
    "ADB" "Yaya"
    a "Yeah, I just accidentally flipped the mask I was using."
    "Oh rip."
    "You understand it now though, right?"
    a "Yea yea, it's all good."
    "Alright, time to turn in, then."
    "ADB" "Lezgo!"
    hide data normal with dissolve
    hide adb normal with dissolve
    scene black
    show text "You manage to hand in your homework submission a breaking 2 minutes before lecture starts." with dissolve
    pause 1.5
    hide text with dissolve
    show text "Unfortunately, this lecture made even less sense than the last one." with dissolve
    pause 1.0
    hide text with dissolve
    scene bg classroom
    show adb normal at midleft with dissolve
    show data normal at midright with dissolve
    "..."
    "This lecture made even less sense than the last one."
    "ADB" "That was some BS BS."
    a "I never thought I'd have to do pointers outside of code..."
    "Imagine if stack pointer hacking shows up on the midterm."
    "That would not be fun."
    "ADB" "Yo reject reject!"
    "ADB" "Code injection is very easy."
    a "But we're not all big hacker brains like you, lol."
    "ADB" "Baba"
    "I need to eat something before my next class so I can actually pay attention during review session, so I'll see you guys later!"
    a "Bye!"
    "ADB" "See ya!"
    hide adb normal with dissolve
    hide attack normal with dissolve
    jump lunch

label lunch:
    "Hmm.. looks like Schatz changed their lunch menu since last semester..."
    "..."
    "Maybe I'll get the pork bowl."
    show cache normal at midleft with dissolve
    show bomb normal at midright with dissolve
    c "You didn't finish your tater tots, Faye!"
    b "Do you want them?"
    c "You're a really picky eater, you know that?"
    b "uwu"
    c "(Sigh..)"
    "Looks like that relationship is still going well."
    "{i}PDA ensues{/i}"
    "Welp, this is geting slightly uncomfortable."
    "Looks like I'm getting to-go."
    "Oh no, review session starts at {i}1{/i}? I thought it was at 2!"
    "Time to run..."
    jump review_session1

label review_session1:
    scene black
    show text "You make it to review session and sit in the back to not distract with your loud eating noises." with dissolve
    pause 1.5
    scene bg classroom
    hide text with dissolve
    "When did that happen?"
    "Did we start learning about unions already?"
    "Hopefully this isn't on the midterm."
    "{i}The review sesion finished.{/i}"
    "(Sigh, I got nothing useful out of that.)"
    "{i}I pack up and get ready to leave.{/i}"
    phi "{size=-10}H, Hello?{/size}"
    "Oh hello there. You are...?"
    show philosophy normal with dissolve
    phi "{size=-10}I, I'm Sophie...{/size}"
    # show sophie thonk with dissolve
    phi "Th, that was a pretty helpful review session, haha."
    "(uh... really?)"
    phi "Um... I was wondering if I could ask your opinion on something, do..do you happen to.. to have a moment?"
    "(Well I was just going to go home and sleep, I guess I'll stay for a bit.)"
    "Sure thing, ask away."
    # show philosophy normal with dissolve
    phi "Thank you! you see...theotherdayIwasreadingupontheTuringtestandthechineseroomandsomedebates onsyntaxversussemanticsandIwascuriouswhatotherpeoplethinkofthis..."
    "(What was that?! She seems so excited and that was WAY too fast.)"
    "Uh sorry, I couldn't quite catch all that..."
    phi "Oh s,sorry I got ahead of myself..."
    # show philosophy thonk with dissolve
    phi "Basically, imagine you are a person who does not speak Chinese, and you were placed in a room with an English rule book that tells you how to manipulate Chinese symbols."
    "{i}I nod in acknowledgement.{/i}"
    "Okay"
    phi "People from outside ask you a question in chinese on paper, and you look up the question in the rule book and transform and piece together the symbols in a certain way to produce an answer."
    # show philosophy normal with dissolve
    phi "Now, do you think you know Chinese?"
    "Uh I don't get it, I don't know Chinese though."
    # show philosophy thonk with dissolve
    phi "Okay, if we put it this way: imagine the collection of chinese symbols is a database, and the rule book as a program. The questions are input, and answers are output."
    phi "Say the computer always replies like a Chinese speaking person would, does this computer, or this computer program know Chinese?"
    "Uh"
    # show philosophy normal with dissolve
    "{i}Thonk.{/i}"
    phi "See, if you say the program does not know Chinese, it would be like saying computers are not capable of having consciousness because they don't have intentions or semantics, just syntax. And I personally think that...(500 more words here)."
    "(This confuses me.)"
    "(It would appear that the computer can answer questions because he understands what it means, but then if it's just manipulating symbols following a set of rules...)."
    "I think it doesn't “Know” Chinese but that's probably not important."
    "I feel like if we can get a program that does this it would be a great achievement, and this technology would help a lot of people in the real world."
    "At the end of the day it wouldn't matter whether the computer knows Chinese, if it can be of use to help break the language barrier for us humans."
    "(Woah that was deep, I didn't know I was this good at Philosophy. Maybe I should just transfer to UBitt to study philosophy.)"
    phi "..."
    # show philosophy normal with dissolve
    phi "..."
    # show philosophy thonk with dissolve
    phi "...!"
    hide philosophy normal with dissolve
    "{i}Sophie ran off without another word.{/i}"
    "(What an interesting individual.)"
    "Guess I'll go back and watch YouTube."
    jump midterm1

label midterm1:
    jump hackathon

label hackathon:
    jump sys_hw

label sys_hw:
    scene black
    show text "You get started on your Memory allocation homework, but it's very confusing because you didn't pay attention in lecture." with dissolve
    pause 1.0
    hide text with dissolve
    show text "You manage to get a good chunk of it finished, but for some reason it doesn't seem to be working." with dissolve
    pause 1.0
    hide text with dissolve
    scene bg classroom
    "..."
    "Why do I still have fragmentation?"
    "I'm pretty sure I did this part correctly..."
    "..."
    "Maybe I should ask someone for help."
    menu:
        "I should ask Bitsy.":
            jump bitsy_help
        "I should ask Buffy.":
            jump buffy_help

label bitsy_help:
    "There she is."
    "Hey, Bitsy!"
    show data normal with dissolve
    d "Hey, [player_name]!"
    "Have you finished the mem alloc homework yet?"
    "I have a few bugs that I don't know how to fix."
    d "Ah shoot, I forgot about that! I've been pretty busy with track meets for the past few days, so I haven't started on it yet."
    d "Maybe you should just go to Office Hours? I heard the TAs are pretty friendly."
    "Oh hmm.."
    "Ok, thanks!"
    "Good luck with track!"
    d "Ah thanks, haha!"
    d "See you around!"
    hide data normal with dissolve
    jump oh_intro

label buffy_help:
    "There she is."
    "Hey, Buffy!"
    show attack normal with dissolve
    a "Hey!"
    "Have you finished the mem alloc homework yet?"
    a "Yeah I'm almost done, but I got carried hard by the TAs, so I don't know if I can really help, haha."
    a "But my main issue was with my headers and footers."
    a "So you may need to check your coalescing."
    "Oh hmm.."
    "Ok, thanks!"
    "Maybe I'll try going to OH today."
    "See ya!"
    a "Bye!"
    hide attack normal with dissolve
    jump oh_intro

label oh_intro:
    scene black
    show text "You head to Office Hours to see if a TA can help debug your code." with dissolve
    pause 1.0
    hide text with dissolve
    scene bg classroom
    "Why is this interface so unintuitive now?"
    "Did they change the host of the queue website?"
    "..."
    "Welp, whatever."
    "Hopefully me being 25th in line is just a bug and not actually true."
    scene black
    show text "Wishful thinking has failed. You are actually 35th in line." with dissolve
    pause 1.5
    hide text with dissolve
    show text "But the new episode of Oni Killer is out, so you have something to kill the time while you wait." with dissolve
    pause 2.5
    hide text with dissolve
    show text "As usual, Unlimited Budget Works has managed to pull off top-quality animation." with dissolve
    pause 2.5
    hide text with dissolve
    scene bg classroom
    "Ah, that was a good episode."
    "I bet it's already trending on Twotter."
    "..."
    "Oh, I think it's my turn."
    "Where's the TA?"
    jump malloc_oh

    
            


     

