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
    hide attack normal with dissolve
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
    show attack normal at midright with dissolve
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
    hide text with dissolve
    show text "Unfortunately, you are already confused with the course material, starting with how unions are useful. Or what they even are." with dissolve
    pause 2.0
    hide text with dissolve
    scene bg classroom
    "When did that happen?"
    "Did we start learning about unions already?"
    "Hopefully this isn't on the midterm."
    scene black
    show text "You spend the majority of the review session trying to follow along with notes that you're sure were not covered in lecture." with dissolve
    pause 2.0
    hide text with dissolve
    show text "Are forks related to cutlery or process control? You don't know anymore." with dissolve
    pause 1.0
    hide text with dissolve
    show text "All you know is that the midterm is going to be a big %%rip." with dissolve
    pause 1.0
    hide text with dissolve
    scene bg classroom
    "(Sigh, I got nothing useful out of that.)"
    "{i}I pack up and get ready to leave.{/i}"
    phi "{size=-10}H, Hello?{/size}"
    "Oh hello there. You are...?"
    show philosophy normal with dissolve
    phi "{size=-10}I, I'm Sophie...{/size}"
    # show philosophy thonk with dissolve
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
    "(Whoa that was deep, I didn't know I was this good at Philosophy. Maybe I should just transfer to UBitt to study philosophy.)"
    phi "..."
    # show philosophy normal with dissolve
    phi "..."
    # show philosophy thonk with dissolve
    phi "...!"
    hide philosophy normal with dissolve
    "{i}Sophie ran off without another word.{/i}"
    "(What an interesting individual.)"
    "Guess I'll just go back and watch some Indian guy on YouTube."
    jump midterm1

label midterm1:
    scene black
    show text "After cramming some last minute YouTube videos, you feel like you're prepared for the midterm." with dissolve
    pause 1.5
    hide text with dissolve
    show text "You feel like you've forgotten to put something on your cheatsheet, but it's too late for that now." with dissolve
    pause 1.5
    hide text with dissolve
    show text "You get to the exam room and log into the exam server to get ready." with dissolve
    pause 1.0
    hide text with dissolve
    show text "And then, the fun begins." with dissolve
    pause 1.0
    hide text with dissolve
    show text "2 questions in, you realize the one thing you forgot to put on your cheatsheat was stack pointer examples." with dissolve
    pause 1.5
    hide text with dissolve
    show text "Fortunately, you remember the basic terms such as %%rsp and %%rip, so you just randomly toss them into your answers to guarantee partial credit." with dissolve
    pause 2.0
    hide text with dissolve
    show text "Everything else on the midterm is very straightforward, and you breeze through it." with dissolve
    pause 1.5
    hide text with dissolve 
    show text "Be sure to thank those Indian guys on YouTube for explaining unions and struct padding in-depth." with dissolve
    pause 1.5
    hide text with dissolve
    show text "Being a gigachad, you walk out of the exam... at exactly the same time as everyone else." with dissolve
    pause 1.5
    hide text with dissolve
    show text "That's right, walking out early makes the other students feel bad. So you don't do it." with dissolve
    pause 2.0
    hide text with dissolve
    show text "Don't be one of those people." with dissolve
    pause 1.0
    hide text with dissolve
    show text "Feeling good about your midterm grade, you head back home before realizing that this class just assigned the next homework assignment." with dissolve
    pause 2.5 
    hide text with dissolve
    show text "Being the frontloader that you are, you decide that you want to start this assignment early. However..." with dissolve
    pause 2.5
    hide text with dissolve
    show text "All your pent up stress about this midterm that you've managed to hide comes out and you crash on your couch." with dissolve
    pause 2.5
    hide text with dissolve
    show text "Which is good. Take a long nap. You deserve it." with dissolve
    jump sys_hw

label sys_hw:
    scene black
    show text "After waking up, you get started on your Memory allocation homework, but it's very confusing because you didn't pay attention in recent lectures." with dissolve
    pause 1.0
    hide text with dissolve
    show text "You manage to get a good chunk of it written, but for some reason it doesn't seem to be working." with dissolve
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

    
            


     

