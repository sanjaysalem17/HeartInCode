label review_session2:
    scene black
    show text "After a few days of completely forgetting that you actually have exams, you begin your cramming ritual." with dissolve
    pause 1.0
    hide text with dissolve
    scene bg classroom
    "I'm glad I finished the programming homeworks on time, but there's no way I'm gonna remember anything that was taught in lecture..."
    "I didn't have time to study because debugging took {i}way{/i} too long."
    show ishan normal with dissolve
    "Ishan" "That's because this course doesn't use Rust, smh."
    "Huh? Who are you?"
    "Ishan" "I'm a Rust main. We scale late game."
    "That in no way answers my question, but whatever."
    "Ishan" "If this course used Rust, the safety checks would make sure you don't waste time debugging."
    "Ok sure. Anyway, do you know how-"
    "Ishan" "You don't even have to free variables yourself, because it's memory safe!"
    "..."
    "(This guy and Malek would probably be great friends...)"
    "Ishan" "Sorry, that got a little rant-y."
    "(Yup, he'd definitely be good friends with Malek.)"
    "No worries."
    "Do you know how struct padding works for this scenario?"
    "Ishan" "Hmm, lemme take a look."
    "Ishan" "You'd have to round the total size to a multiple of 8 because the long is the largest type here."
    "That makes sense."
    show ishan normal at midright with move
    show data normal at midleft with dissolve
    d "Hey, [player_name]! Hey, Ishan!"
    "Ishan" "Hello hello."
    "Hey!"
    d "Are you going over the review problems?"
    d "We still have a few weeks before the midterm, right?"
    "Ishan" "Yes, but none of us understand what's going on in lecture."
    "(Good, so it's not just me.)"
    d "Ah, ok. I should probably review some too, then."
    d "How does the stack pointer stuff work again?"
    show data normal at left with move
    show ishan normal at right with move
    show attack normal with dissolve
    a "Hey! Did someone say \"stack pointer\"?"
    "Yes."
    "Ishan" "All this %%rsp stuff is confusing."
    a "I think I can help explain it."
    hide attack normal with dissolve
    hide data normal with dissolve
    hide ishan normal with dissolve
    scene black
    show text "The four of you go over some of the earlier Systems concepts, so that you don't have to cram before the midterm." with dissolve
    pause 1.5
    hide text with dissolve
    show text "Why does this class have two midterms? And why is the second one cumulative? These are all valid questions." with dissolve
    pause 2.5
    hide text with dissolve
    show text "This doesn't seem realistic..." with dissolve
    pause 1.0
    hide text with dissolve
    scene bg classroom
    show attack normal at left with dissolve
    show data normal at right with dissolve
    "Ishan" "So then this part of the heap has external fragmentation."
    d "Yeah, you'll have to coalesce some of the memory together to make sure that doesn't happen."
    "Hmm.. I think I get most of this now."
    d "Yeah, me too!"
    a "This was a pretty spontaneous \"review session\", haha."
    a "I'll see you all later! I have to get to my Calc recitation."
    d "Oh shoot, me too. See you!"
    "Ishan" "Well, this was fun."
    "Ishan" "Cramming is much less stressful when you have a group, isn't it?"
    "Haha yeah."
    "Ishan" "Anyway, I'll see you later."
    "Ishan" "I have to get over to Scaife to prepare for my recitation."
    "Ishan" "Adios!"
    jump break_time


label break_time:
    scene black
    show text "One week later..." with dissolve
    pause 1.0
    hide text with dissolve
    scene bg classroom
    "(Finally, I get a long weekend!)"
    "(Hmm... what should I do?)"
    "(Oh wait, is that Malek?)"
    "Hey, Malek!"
    show malloc normal with dissolve
    m "Hello, [player_name]."
    m "How are you?"
    "Pretty good, how about you?"
    m "I'm doing well, thank you."
    "Who's this with you?"
    show malloc normal at midright with move
    show calloc normal at midleft with dissolve
    clc "Hello! I'm Kalik!"
    "Nice to meet you, Kalik!"
    "I'm [player_name]!"
    "So, Malek, what are you doing this long weekend?"
    m "I'm taking Kalik to the arcade for family weekend."
    "That sounds nice!"
    menu:
        "You two have fun!":
            m "Thanks. I hope you enjoy your weekend as well."
            clc "See you later!"
            hide malloc normal with dissolve
            hide calloc normal with dissolve
            jump second_intro
        "Can I come with you?":
            $ malloc_points += 30
            jump arcade
    
label arcade:
    m "I don't see why not."
    m "Kalik, is that alright with you?"
    clc "Sure!"
    m "Alright, let's head out then."
    clc "Big brother, who's that?"
    m "Hmm?"
    m "Oh, that looks like Faye and her sister."
    show malloc normal at right with move
    show calloc normal at midright with move
    show bomb normal at left with dissolve
    show gdb normal at midleft with dissolve
    b "Hello, Malek and [player_name]. Where are you all going today?"
    "We're going to the arcade."
    "I'm just tagging along, but Malek was taking his brother there for family visit day."
    m "Hello, Blake. How are you doing?"
    gdb "Uhh...ok...I guess..."
    clc "Hello! I'm Kalik! Nice to meet you!"
    gdb "Oh...hi...!"
    gdb "..."
    gdb "I'm Blake...!"
    gdb "Nice to meet you too...!"
    #calloc nosebleed
    "Kalik, are you okay?"
    $ malloc_points += 30
    clc "Huh?"
    clc "Oh! I'm fine!"
    clc "I don't know why my nose started bleeding like this!"
    "(Wow, looks like someone has a crush...)"
    "(I shouldn't tell Faye, should I?)"
    m "Well, we should head out."
    m "It was nice seeing both of you."
    m "Tell Cash I said hello."
    b "I sure will!"
    "(...)"
    clc "Bye, Blake!"
    gdb "Goodbye...!"
    hide malloc normal with dissolve
    hide calloc normal with dissolve
    hide bomb normal with dissolve
    hide gdb normal with dissolve
    jump second_intro


label second_intro:
    "Hmm.. it's been a while since I've seen Cash, Bitsy, or Buffy."
    menu:
        "I should go find Cash.":
            jump meet_cache
        "I should go find Bitsy.":
            $ data_points += 30
            jump meet_bitsy
        "I should go find Buffy.":
            $ attack_points += 30
            jump meet_buffy

label meet_cache:
    "He should be around here somewhere..."
    "There he is."
    "Looks like he's preparing to go somewhere."
    "Hey, Cash!"
    show cache normal with dissolve
    c "Hey, [player_name]."
    c "What's up?"
    "Nothing much."
    "Just glad to finally have a break from classes."
    c "Yeah, I hear you."
    c "I'm about to get dinner soon, if you want to join?"
    "..."
    "You're getting dinner {i}now{/i}? It's only 4."
    c "Yeah, but there's a really good nightclub I want to go to later."
    c "It's tough to get in once it's crowded, so I wanted to get there early."
    "That sounds fun! I'd be down."
    c "Great!"
    c "Let's take the 61D down this way."
    hide cache normal with dissolve
    scene black
    show text "You and Cash get on the 61D bus down to the Waterfront." with dissolve
    pause 1.5
    hide text with dissolve
    scene bg bus
    show cache normal with dissolve
    "So Cash, how's your relationship going?"
    c "Oh it's..."
    c "Going, I guess."
    "What does that mean?"
    c "Uhh..."
    c "(Lemme just make sure she's not here...)"
    c "(...)"
    c "Alright you've gotta help me out here."
    "Huh...?"
    c "Faye is actually crazy."
    "Wut."
    c "The other day, she almost pulled a knife on Buffy when she tried to talk to me."
    "Nani."
    c "Yeah, that was my reaction!"
    "(Are you {i}sure{/i} you reacted with \"nani\"?"
    c "She gets {i}way{/i} too jealous about these kinds of things."
    c "She's even smiling while she does this, so there's clearly something wrong..."
    c "It's not like I'd start dating Buffy again!"
    "Hold up, you used to date Buffy?"
    "Why'd you break up?"
    c "Uhh..."
    c "It's complicated."
    "Pretty sure it's not as complicated as why you're trying to get away from Faye."
    c "..."
    c "Ok, fair."
    c "Basically, we were both too busy with work for a relationship."
    c "She also felt that I didn't give her enough attention and said I only cared about myself..."
    c "But we're in college, you know? It's hard to care about my grades {i}and{/i} be committed to a relationship!"
    c "I don't get how people can make it work so easily during their {i}freshman year{/i}!"
    c "Or maybe I just took too many programming classes which killed my free time..."
    c "Either way, it didn't work out."
    c "So here we are."
    "So is Faye your rebound or something?"
    c "What? Of course not!"
    c "I genuinely liked her before I found out she was like this."
    c "I didn't expect Buffy to take me back once I had enough time to commit to a relationship, so I figured I'd just move on."
    "(Damn, I thought this guy just liked whatever girl was hot, but he's actually pretty emotionally complicated.)"
    c "..."
    c "So, will you help me break up with Faye?"
    "..."
    "I mean sure, but won't it hurt your reputation?"
    "Something something \"Cash can't commit to a relationship and breaks two girls' hearts\"..."
    c "Honestly, I don't care about that anymore."
    c "I just don't want her to pull a knife on me or anything, you know?"
    "(I feel like she's going to anyway, if you try to break up with her...)"
    c "I'd rather feel safe than have a good reputation..."
    "..."
    "Alright, I'll help."
    "When are you doing this?"
    c "Thank you so much!"
    c "I owe you one."
    c "I just need you there for emotional support."
    "(This dude needs more than just emotional support.)"
    c "Maybe if I do it at the school festival, there'll be enough people there that she doesn't go off..."
    "Sure..."
    "(Terrible plan, but ok.)"
    "(Isn't she {i}more{/i} likely to go off if you break up during the festival?)"
    "I guess I can help when I'm free..."
    c "Ah, thank you thank you thank you thank you"
    "Don't worry about it."
    c "Oop, here's our stop!"
    hide cache normal with dissolve
    scene black
    show text "You and Cash enjoy a nice meal at a nearby restaurant, then head to the nightclub." with dissolve
    pause 2.0
    hide text with dissolve
    scene bg classroom
    show cache normal with dissolve
    c "Here we are."
    show cache normal at midright with move
    show dfa normal at midleft with dissolve
    "Decider" "Show me your IDs."
    c "Here you go."
    "Here's mine."
    "Decider" "..."
    "Decider" "These are acceptable."
    "Decider" "Enjoy your evening."
    "Thanks!"
    hide dfa normal with dissolve
    show cache normal at center with move
    c "We got here just in time! The show's about to start."
    hide cache normal with dissolve
    show jason normal with dissolve
    "lil mem sbrk" "Yo yo, it's your boi lil mem sbrk here with our opening act for this evening!"
    "lil mem sbrk" "Please welcome [duo_name] to the stage!"
    hide jason normal with dissolve
    "Shalin" "Hey, everyone!"
    show albert normal at midright
    "Albert" "I'm Albert, and this is Shalin, and we're [duo_name]!"
    "Shalin" "Hope you all enjoy our song!"
    hide albert normal with dissolve
    scene black
    show text "You enjoy the opening act and the subsequent comedy show. Your night is full of laughter and fun." with dissolve
    pause 2.0
    hide text with dissolve
    scene bg bus
    show cache normal with dissolve
    c "So, [player_name], did you enjoy the show?"
    "Yeah!"
    "I had a great time!"
    c "We should do this again, maybe after midterms and festival prep dies down a bit.."
    "For sure!"
    c "Well, I'll see you later, then."
    c "Good night."
    "Good night!"
    hide cache normal with dissolve
    if join_stuco:
        jump after_break_stuco
    jump after_break_other


label meet_bitsy:
    "She should be near the track..."
    "There she is."
    show data normal at midleft with dissolve
    show finger normal at midright with dissolve
    d "No no not like that, Root."
    d "You have to make sure your arms don't move when you curl back down."
    "Root" "You mean like this?"
    d "Yeah, that's a lot better!"
    "Root" "Thanks, captain!"
    d "No prob!"
    d "Oh hey, [player_name]!"
    d "What brings you to this part of campus?"
    "I was just wandering around and thought I'd check on you since it's been a while."
    "You're not doing anything special for family weekend?"
    d "Nah, my family is backpacking through Europe right now, so they can't really come."
    d "I thought I'd use the extra time to get some good exercise in before the regional track meet."
    "That sounds fun!"
    d "Haha yeah!"
    d "I'm hoping I can get the entire team into the top 10 this time."
    "Is that why you're coaching him?"
    d "Yeah."
    d "I don't think you two have met yet!"
    d "[player_name], this is Root. Root, this is [player_name]."
    "Hello!"
    "Root" "Hey!"
    "Those are some pretty impressive biceps!"
    "Are you on the track team too?"
    "Root" "Yeah! I'm trying to make sure I don't just exercise my arms."
    "That makes sense."
    "Root" "I'm also trying to grow my fitness channel. Check it out if you're interested, haha."
    "Root" "Subtle flex."
    "Sure, I'll take a look! What's it called?"
    "Root" "It's called \"SaidoChesto22\"."
    "(Hmm...somehow that sounds familiar...)"
    d "So, [player_name], since you're here, do you want to race?"
    "Wut."
    d "Haha, I just want to see how fast you are!"
    "Uh, ok...?"
    d "No pressure!"
    $ data_points += 30
    "Sure, I guess."
    "Though you're probably going to be disappointed."
    d "Nah, don't worry about that!"
    d "I'm sure you're pretty fast!"
    "Alright, how do we do this?"
    d "Root, can you do a countdown from 5?" 
    "Root" "Sure!"
    d "Float like a butterfly, float like a butterfly...."
    "What's she muttering?"
    hide data normal with dissolve
    show finger normal at center with move
    "Root" "5!"
    "Root" "4!"
    "Root" "3!"
    "Root" "2!"
    "Root" "1!"
    "Root" "{b}Go{/b}!" with hpunch
    hide finger normal with dissolve
    "...!"
    "......!"
    "Wow, she's pretty fast, but somehow I'm able to keep up!"
    d "You're pretty quick!"
    "(Sounds like she's gonna say something like how this isn't her top speed...)"
    d "But guess what, this isn't my final form!"
    "(Yup, close enough...)"
    "!"
    "Holy shit, she just took off!"
    "She's like a horse!"
    "{i}panting noises{/i}"
    "..."
    "{i}more panting noises{/i}"
    "Finally....made...it...!"
    show data normal at midright with dissolve
    show finger normal at midleft with dissolve
    d "Hey, you really surprised me there!"
    "Well....my lungs....are dead...."
    "Root" "You should be fine if you sit down for a while, but still, that was pretty fast!"
    "I...need some....water...."
    d "Right right, let's head back inside and find a water fountain."
    hide data normal with dissolve
    hide finger normal with dissolve
    scene black
    show text "The three of you head inside and rehydrate at the nearest water fountain." with dissolve
    pause 2.0
    hide text with dissolve
    scene bg classroom
    show data normal at midright with dissolve
    show finger normal at midleft with dissolve
    d "That hits the spot!"
    "(My lungs are definitely dead now...)"
    "Root" "You should definitely join the track team, [player_name]!"
    "No thanks."
    "I don't think I can do that again..."
    d "Still, you did great!"
    "..."
    "Wait..."
    "What's that music?"
    d "We're near the music room, so maybe someone's practicing in there..."
    "Root" "This sounds like an anime song..."
    "I'm pretty sure it is an anime song..."
    "I'm gonna go see who's playing it."
    "I'll be right back."
    hide finger normal with dissolve
    hide data normal with dissolve
    "..."
    "..."
    "...!"
    "Hello!"
    show paperbag life with dissolve
    "Hello?"
    "Why are you wearing a paper bag on your head?"
    "???" "Uh..."
    "???" "Why aren't {i}you{/i} wearing a paper bag on your head?"
    "Wut."
    "???" "Uno reverse card!"
    "...!"
    "???" "Nah..."
    "???" "I'm trying to see how well I can play violin without looking."
    "That sounds difficult..."
    "???" "I'm also trying to practice a new song for my music channel, so I kinda need the bag."
    "Do you wear that when you record videos too?"
    "(Wow, looks like everyone has a channel for something nowadays...)"
    "???" "Yeah, it started as a joke, but I just went with it because people thought it was funny, haha."
    "So what song were you playing earlier?"
    "It sounded like the new HIRUASOBI song."
    "???" "Yeah, it was HIRUASOBI."
    "???" "It's from a game I play called Herrscher Impact."
    "Oh, nice nice!"
    "Oh shoot, I didn't introduce myself did I?"
    "This must be kinda awkward..."
    "???" "Haha, don't worry about it."
    "Anyway, I'm [player_name], nice to meet you."
    "Ricky" "I'm Ricky. Yoroshiku onegaishimasu!"
    "What's your music channel called?"
    "Ricky" "It's called Paperbag Life, lol."
    "(I should have guessed...)"
    "Anyway, it was nice to meet you! Good luck on the channel!"
    "Ricky" "Arigatou gozaimasu!"
    hide paperbag life with dissolve
    "..."
    show data normal at midleft with dissolve
    show finger normal at midright with dissolve
    d "You're back!"
    "Root" "We were gonna go run a few more laps before coming back inside again, if you wanted to come with us?"
    "Uhhh.... I think that was enough exercise for me for today..."
    "I'm gonna go sit down somewhere."
    d "Haha, no worries!"
    "Root" "See you later!"
    hide data normal with dissolve
    hide finger normal with dissolve
    #"You have [shell_points] points for shell."
    #"You have [data_points] points for data."
    #"You have [malloc_points] points for malloc."
    if join_stuco: 
        jump after_break_stuco
    jump after_break_other

label meet_buffy:
    scene black
    show text "You wander around the hallway until you hear some students yelling at each other from inside the Chess club classroom." with dissolve
    pause 1.5
    hide text with dissolve
    show text "You then realize that it was actually very one-sided yelling, coming from a familiar voice." with dissolve
    pause 1.5
    hide text with dissolve
    scene bg classroom
    "???" "GOD, YOU'RE HOPELESS! How do you expect to learn how to play chess if you can't even remember how far each piece can move?"
    "???" "Don't waste my time if you can't even remember basic rules!"
    show attack normal with dissolve
    "(Just as I approached the classroom where chess club was meeting, a girl stormed out of the classroom, slamming the door closed behind her.)"
    "(She seemed surprised to see me, but only for a second, before her expression turned cold.)"
    "(Ah, no surprise; after all, it's Buffy.)"
    a "What do you want? Are you here to make a fool of yourself too?"
    menu:
        "I'm already good at chess.":
            a "Is that a challenge?"
            a "I'm the captain of the chess team. I won't go easy on you just because you're a classmate."
            a "Don't disappoint me."
        "I genuinely want to learn!":
            a "..."
            a "Come in then."
            $ attack_points += 10
        "Yes!":
            a "..."
            $ attack_points += 20
            a "Anyway. I guess we can play a match."
    "(She opened the door and gestured for me to follow.)"
    hide attack normal with dissolve
    scene bg classroom
    "(The classroom was nearly empty, save for one student that was sitting in the corner of the classroom.)"
    "(One look at his expression told me that he likely wasn't here to stay for long.)"
    "(Upon seeing Buffy and I walk in, he quickly gathered up his stuff, scooted around the two of us, and burst into a sprint out of the classroom.)"
    show attack normal with dissolve
    a "What's gotten into him?"
    a "I swear, the people trying to join this club are less and less competent."
    a "I don't know why they keep wasting my time."
    "(Ah... this girl doesn't know the effect she has on people, huh.)"
    "Yeah, for real."
    "(That response sounded anything but convincing. Thankfully, Buffy didn't seem to give it any thought.)"
    a "Let me set up the board."
    "(She began to pick up the pieces that seem to have been flung to the ground earlier, probably in her fit of rage.)"
    "(Terrifying.)"
    "(Maybe I should get out while I still can...)"
    hide attack normal with dissolve
    scene black
    show text "You zone out, lost in thought, as she sets up the board." with dissolve
    pause 2.0
    hide text with dissolve
    scene bg classroom
    show attack normal with dissolve
    a "Hey you. Wake up."
    "(Oh shoot.)"
    "Ah, yes yes, I'm here. Ok. I'm ready."
    "(She spun the board so the white pieces were facing me.)"
    "(Looking at the pieces, I was suddenly regretting my decision.)"
    a "Okay, well, I'll just quickly explain the chess pieces before we start. Just so you can't say you don't know anything about chess when we play."
    "(I open my mouth to protest, but she silences me with a glare.)"
    a "In the corners of the back row are the rooks. They can move any distance, vertically and horizontally."
    a "Next to the rooks are the knights, which can move in the shape of an L."
    a "Next to the knights are the bishops, which can move any distance diagonally."
    a "In the middle of the back row are the king and queen. The queen can move any distance vertically, horizontally, and diagonally."
    a "On the other hand, the king can only move one square horizontally, vertically, or diagonally. When the king is captured, the game ends."
    a "Pawns can either move two squares forward from their beginning position, one square forward from other positions, or one square diagonally to capture the opponent's pieces."
    a "Got that?"
    "(Despite the fact that I didn't really know if I had gotten that, I nodded anyway.)"
    a "Ready to play, then?"
    "(No. No I wasn't. But I couldn't tell her that.) Yes."
    a "Whenever you're ready, then."
    "(As much as I wanted to stall, I didn't really see any way out of this situation.)"
    "Well... here I go."
    menu:
        "(Move a pawn forward two squares.)":
            "(She moved her pawn to match.)"
            "(Ah... what shall my next move be?)"
            scene black
            show text "You finish the chess game. She comes out victorious, but it was a tough battle." with dissolve
            pause 2.0
            hide text with dissolve
            scene bg classroom
            $ attack_points += 30
            a "Impressive. It's been so long since someone competent has joined this club."
            "(There seemed to be a hint of friendliness in her expression.)"
            a "Thanks for coming."
            "(There was an awkward period of silence as we maintained eye contact.)"
            "(It seemed to fluster her a little bit.)"
            a "(Clears throat) Anyway. Thanks again for coming. Um... It looks like break time is almost over."
            "Yes?"
            a "I'm really sorry... What's your name again?"
            "(Wow...)"
            "(Well, perhaps I should be happy with the fact that she wants to know who I am.)"
            "It's [player_name]."
            a "Well, [player_name], thanks for coming. Please, feel free to stop by in the future."
            hide attack normal with dissolve
            scene black
            show text "We part ways outside the classroom, and she waves goodbye as she leaves." with dissolve
            pause 2.0
            hide text with dissolve
        "(Move a random piece to a random square.)":
            a "...What?"
            "I moved my piece."
            a "Dear god. Please don't waste my time."
            a "And here I thought you had potential."
            a "Whatever. I've had it with you brainless idiots trying to join my club."
            "(With a clean sweep, she knocked all the pieces to the floor.)"
            a "Leave. And don't show your face in my club ever again."
            "(Oh no... she's mad.)"
            "(I'd better get going. It looks like break time is over anyway.)"
            hide attack normal with dissolve
            scene black
            show text "She is still glowering at you as you walk out of the room." with dissolve
            pause 2.0
            hide text with dissolve
    if join_stuco:
        jump after_break_stuco
    jump after_break_other

label after_break_stuco:
    scene black
    show text "A few days later..." with dissolve
    pause 1.0
    hide text with dissolve
    scene bg classroom
    # "You have [proxy_points] points for proxy."
    "Ah, that was a nice break."
    "I guess I should actually do my student council task."
    "Hmm... let's see..."
    if stuco_task == 0:
        "I need to go talk to the sysadmin."
        jump sysadmin
    elif stuco_task == 1:
        "I need to go talk to the cooking club."
        jump cooking_club
    else:
        "I need to find someone to make festival posters."
        jump gaming_club
    return

    scene black
    show text "A few days later..." with dissolve
    pause 1.0
    hide text with dissolve
    scene bg classroom
    "Ah, that was a nice break."
    "I guess I should go take a walk before burying myself in midterm studying."
    scene black
    show text "You go on a long walk around campus and find some students working in the park next to the school." with dissolve
    pause 2.0
    hide text with dissolve
    scene bg classroom
    show clogic normal at midleft with dissolve
    "???" "Wait, what are you doing?"
    show pruning normal at midright with dissolve
    "???" "I'm pruning my trees!"
    "???" "No, that's {i}my{/i} tree, Minnie!"
    "Minnie" "What...?"
    "???" "Do you see any plums on that one?"
    "Minnie" "No..."
    "Minnie" "Sorry, Harmony."
    "Minnie" "Welp, hopefully I didn't mess up the fruits..."
    "Harmony" "You mean proofs..."
    "Are you two planting trees?"
    "Harmony" "Oh, hello!"
    "Minnie" "Hello!"
    "Harmony" "We're just maintaining them so they don't overgrow, but Minnie here gets a bit overexcited when using the pruner..."
    "Minnie" "Hehe."
    "Harmony" "...!"
    "Harmony" "Looks like the completeness of my friend recognition procedure has been broken."
    "What does that mean?"
    "Harmony" "It just means I haven't logged your profile."
    "Harmony" "My memory was never sound but it at least needs to be complete."
    "Harmony" "I'm Harmony, and this is Minnie."
    "Minnie" "Hello!"
    "Harmony" "What's your name?"
    "I'm [player_name]! Nice to meet you!"
    "Minnie" "You too!"
    "So what kind of trees are these?"
    "Minnie" "Mine are the plum trees."
    "Minnie" "Harmony's are the fruit trees over here."
    "Harmony" "{i}Proof trees{/i}, Minnie."
    "Minnie" "Oops."
    "Minnie" "Anyway, the plums should be ripe soon!"
    "Harmony" "We need to pluck them before the Pigeon Man shows up..."
    "Who's the Pigeon Man?"
    "Minnie" "Sshh! He'll hear you!"
    "What?"
    "How will he hear us? There's no one here."
    show clogic normal at left with move
    show pruning normal at right with move
    show pigeon hole with dissolve
    "Pigeon Man" "Cooo? (Did someone call for me?)"
    "Harmony" "Ah shit, he showed up."
    "The plot thickens..."
    "Why does he have a pigeon head?"
    "Harmony" "I'll get Berry, you two distract him!"
    hide clogic normal with dissolve
    "Pigeon Man" "Are those {i}fresh plums{/i} I see?"
    "Distract him {i}how{/i}?"
    "Minnie" "Throw some birdseed at him!"
    "Uhhh...is this the bag?"
    "Minnie" "Yes! {b}Hurry{/b}!"
    "Take this!"
    "Pigeon Man" "Coo..."
    "Pigeon Man" "Coo! (Oh yes. Very delicious.)"
    "Pigeon Man" "Coo coo. (Birdseed very pog.)"
    "Pigeon Man" "nom nom nom"
    "Minnie" "That should keep him down for a while."
    "(What is happening here?)"
    "(I was not aware that Pigeon people existed...)"
    show clogic normal at left with dissolve
    "Harmony" "Alright, I got Berry!"
    hide clogic normal with dissolve
    hide pruning normal with dissolve
    show pigeon hole at right with move
    show berry esseen at left with dissolve
    "Berry-Esseen" "Oh no, not this guy again."
    "Pigeon Man" "nom nom nom"
    "Pigeon Man" "nom nom no-"
    "Pigeon Man" "Coo! (Oh, hello, {i}Berry{/i}.)"
    "Berry-Esseen" "{i}Pigeon{/i}."
    "(Can this Berry guy understand what the pigeon is saying?)"
    "(And what's with all this tension all of a sudden?)"
    "(Something's about to go down, isn't it?)"
    "Berry-Esseen" "..."
    "Pigeon Man" "Co, coo? (Oh, you're approaching {i}me{/i}?)"
    "Pigeon Man" "Coo, coo coo? (Instead of violently flinging birdseed at me, you're coming right to {i}me{/i}?)"
    "Berry-Esseen" "I can't throw you off of school property after beating the shit out of you without getting closer."
    "Pigeon Man" "..."
    "Is this a Jojo's reference?"
    "Pigeon Man" "Coo, coo coooo! (Oho! Then come as close as you like!)"
    "Pigeon Man" "Coo. (After I get my tasty plums, there's {i}nothing{/i} you can do to stop me.)"
    "..."
    "(I've deviated way too far from the main storyline now.)"
    "(Did I get teleported to Theoretical CS Land? How do I get back to Systems Land?)"
    "Pigeon Man" "Coo- (Mud-)"
    "Berry-Esseen" "Too slow!"
    "Berry-Esseen" "Central Limit Platinum! Tsukure toolkitto o!"
    "Pigeon Man" "Nani!?!"
    "(What the fuck is going on?)"
    "Berry-Esseen" "Yare yare."
    "Isn't that copyrighted?"
    "Berry-Esseen" "If I'd gotten here a few minutes later, he would have powered up with those plums and never left school property."
    "Berry-Esseen" "Time to teach him a lesson."
    "Harmony" "Brace yourself, [player_name]!"
    "What?"
    "Berry-Esseen" "Ora ora ora ora ora ora ora ora ora ora ora ora!"
    "Berry-Esseen" "Ora ora ora ora ora ora ora ora!"
    "Berry-Esseen" "Ora ora ora ora ora ora ora ora ora ora!"
    "Berry-Esseen" "Ora ora ora ora ora ora ora ora ora!"
    "Berry-Esseen" "Ora ora ora ora ora ora ora ora ora ora!"
    "Berry-Esseen" "Ora ora ora ora ora ora ora ora ora ora ora!"
    "Berry-Esseen" "Ora ora ora ora ora ora ora ora!"
    "Berry-Esseen" "Ora ora ora ora ora ora ora ora ora ora!"
    "Berry-Esseen" "..."
    "Berry-Esseen" "Probability has begun to work again."
    "This is definitely a Jojo's reference."
    "Pigeon Man" "COOOOOOOOO!!!!!"
    hide pigeon hole with dissolve
    "Berry-Esseen" "QED!"
    show berry esseen at center with move
    show pruning normal at right with dissolve
    show clogic normal at left with dissolve
    "Minnie" "That was amazing, Berry!"
    "Berry-Esseen" "Don't worry about it."
    "Berry-Esseen" "I'll take this guy to the police station, now."
    "Berry-Esseen" "You all be careful, now. You never know what kind of suspicious characters may be lurking around here."
    "(But you seem pretty suspicious to me...)"
    "Berry-Esseen" "Farewell."
    hide berry esseen with dissolve
    show clogic normal at midleft with move
    show pruning normal at midright with move
    "Harmony" "Wow, he protected our trees!"
    "Minnie" "We should celebrate!"
    "Harmony" "[player_name], do you want to harvest the fruits?"
    "..."
    "Uh, I'm good."
    "(I need to leave before any more weird shit happens...)"
    "See you later."
    "Harmony" "Bye!"
    "Minnie" "See you!"
    hide clogic normal with dissolve
    hide pruning normal with dissolve
    "I think I just witnessed a hato crime."
    if join_vimclub:
        "Oh shoot, I'm late for my midterm!"
        jump midterm2
    jump photo_club

label photo_club:
    scene black
    show text "You manage to escape from the eccentric pigeon man and happen to find two students arguing at Walking to the Sky." with dissolve
    pause 1.5
    hide text with dissolve
    scene bg classroom
    "???" "Why are you using the default camera on your phone?"
    "???" "What do you mean? What am I supposed to do?"
    "???" "Get on my level, Sky. This is a pro camera add on that I have for a monthly subscription."
    "Sky" "But Hannah, why should I do that when I've got an actual DSLR?"
    "Hannah" "Why didn't you bring that, then?"
    "Hannah" "How am I supposed to use this footage for my computer vision project if they're low quality??"
    "Sky" "Why should I be helping you with {i}your{/i} project?"
    "Sky" "Anyway, see this default app also has manual exposure and ISO settings."
    "Sky" "If you hook it up to the accelerometer you can probably do some deblurring manually."
    "Hannah" "{b}Manually?{/b}"
    "Hannah" "Why would I want to deblur manually? Capturing good footage the first time is clearly a better use of my time."
    "Sky" "Whatever. I'm just here because you said it was a good opportunity for a photoshoot."
    "Sky" "When is Pittsburgh ever gonna have good weather like this again?"
    "Hannah" "Aiyaa..."
    "Hannah" "Okay okay..."
    "Hannah" "Oh, hello!"
    "Oh hi, what are you guys doing?"
    "Sky" "Trying to take a picture for the upcoming photo contest."
    "Hannah" "You may be doing that, but I just need good movement footage to train my model."
    "Sky" "Alright, alright, we get it, Hannah."
    "What's the photo contest about?"
    "Sky" "The theme is \"city skylines\"."
    "Oh, that sounds cool!"
    "Hannah" "Ok, I'm giving up."
    "Hannah" "My group members can deal with this bad footage since I'm basically carrying them in this class anyway."
    "..."
    "Sky" "Why are you so elitist, Hannah?"
    "Hannah" "It's not elitist if it's true."
    "Hannah" "Do you know how hard it is to set up a model for an autonomous vehicle's vision input?"
    "Sky" "..."
    "Hannah" "Alright, I'll see you later."
    "Sky" "Bye."
    "Sky" "Do you think these photos look good?"
    "Hm.."
    "I think they'd look better at nighttime."
    "Sky" "!!"
    "Sky" "Oh you're right! And since I have manual exposure I can make sure it doesn't get too dark!"
    "..."
    "I don't know what that means, but it sounds impressive."
    "Oh shoot, I'm late for my midterm!"
    "I'll see you later!"
    "Sky" "Bye!"
    jump midterm2
    
label sysadmin:
    scene black
    show text "You make your way to the IT building and find the server room." with dissolve
    pause 1.0
    hide text with dissolve
    scene bg classroom
    "This seems like the place."
    "Hello?"
    show network normal with dissolve
    "Ether" "Hello! Are you here from the student council?"
    "Yeah, I'm [player_name]. I'm here to make sure the servers can handle the traffic for the upcoming school festival."
    "Ether" "Cool. Roxy sent an email saying someone would come by."
    "Ether" "Let me get my colleague."
    show network normal at midleft with move
    show fanpu normal at midright with dissolve
    "Ether" "Hey Fanpu. The student council rep is here."
    "Ether" "Can you pull up the network graphs from last year?"
    "FanPu" "Gimme a sec, I'm trying to finish this quest...!"
    "Ether" "What?"
    "FanPu" "I need more Freemogems to get Yae Miko!"
    "FanPu" "I'm so close to soft pity!"
    "Ether" "Is this what you're using the cluster machines for?"
    "Ether" "You need help, man."
    "FanPu" "Alright alright, I finished my daily commissions."
    "FanPu" "What did you need, again?"
    "Ether" "Can you check the network traffic from last year's festival?"
    "FanPu" "Ok! It should be in this folder..."
    "FanPu" "..."
    "FanPu" "Oh shit, this is a pretty high number..."
    "FanPu" "We may need to check the bandwidth before this festival."
    "Ether" "It should be doable if we get a larger router, right?"
    "FanPu" "Yes... but do we have the money?"
    "Ether" "(We'd have more money if you didn't waste our funds on Gnostic Impact...)"
    "FanPu" "Or we can implement a better QoS algorithm so that everyone can use the network..."
    "Ether" "Hmmm..."
    "FanPu" "Hmmm..."
    "(What language are they speaking?)"
    "Ether" "I think that would work."
    "Ether" "Can you also stop using our funds for your gatcha addiction?"
    "FanPu" "What do you mean \"addiction\"?"
    "FanPu" "These are {i}3D{/i} waifus, not {i}2D{/i} waifus!"
    "FanPu" "This is {i}clearly{/i} worth the money!"
    "..."
    "Ok so I understood none of that. Do you have it under control?"
    "Ether" "Yeah, I think we should be able to handle the traffic if FanPu stops streaming his games and actually does work for once."
    "FanPu" "Bruh, why do you keep calling me out like this? If you played this game, you'd understand!"
    "Ether" "I highly doubt that."
    "FanPu" "Rej rej!"
    "Ether" "Anyway, [player_name], you can tell Roxy we've got the situation handled."
    "Alright, sounds good."
    "Ether" "Enjoy the rest of your day!"
    "FanPu" "Noooo I got a Qiqi!!"
    "FanPu" "Wallet-kun doko da?!"
    "Ether" "You need serious help, man."
    "FanPu" "Nuuuu I need to grind more Freemogems now!"
    "FanPu" "Demo jikan ga nai!!"
    "Ether" "(Sigh...)"
    "Ether" "I'm gonna have to do most of this by myself, aren't I?"
    "I'm just gonna leave now..."
    hide fanpu normal with dissolve
    hide network normal with dissolve
    jump midterm2

label cooking_club:
    scene black
    show text "After contacting the cooking club, you set up a time to talk during one of their meetings." with dissolve
    pause 1.5
    hide text with dissolve
    scene bg classroom
    "So the club president is someone named Jenny..."
    "I think it's this room, right?"
    "Hello? Is Jenny here?"
    show jenny normal with dissolve
    "Jenny" "Hewo!"
    "Jenny" "Are you [player_name]?"
    "Yeah, nice to meet you!"
    "Jenny" "Nice to meet you, too!"
    "You got the email from Roxy, right?"
    "Jenny" "The one about event space for the festival, right?"
    "Jenny" "We just finalized what we're planning to do, so we should be able to start looking for spaces now."
    "What's the cooking club doing?"
    "Jenny" "We're planning on doing a maid cafe!"
    "Jenny" "We just finished the menu too. We should be good to look at other logistics."
    "Ooh, that sounds fun!"
    "So do you have an expected number of customers?"
    "Jenny" "Yeah, lemme just ask Sandie."
    show sandwich normal at right with dissolve
    "Jenny" "Hey, Sandie, can you get the binder for last year's logistics?"
    "Sandie" "Yeah, sure, this bread's about to finish proofing so lemme stick it in the oven first..."
    "Sandie" "Ok, there we go."
    "Sandie" "Alright, so last year we had about 400 customers total."
    "Jenny" "We should probably expect that to increase to at most 550 this time."
    "Sandie" "Yeah, that sounds good."
    "Sandie" "Do you know what places on campus can tolerate that crowd?"
    "Sandie" "I don't think a classroom is gonna cut it."
    "Jenny" "We can also see if hosting outside is an option."
    "I don't think that's a good idea..."
    "I feel like allergies are gonna be a big concern if you host outside."
    "Jenny" "Ah shit, you're right."
    show waffle normal at left with dissolve
    "???" "Sorry guys, my class ran late today!"
    "Jenny" "Hey, Maple!"
    "Jenny" "Do you happen to know any good locations on campus that we can use for the maid cafe?"
    "Sandie" "We're expecting about 550 people this year."
    "Maple" "Oh, if you're talking about that, then you must be [player_name]!"
    "Maple" "Nice to meet you!"
    "Nice to meet you, too!"
    "Maple" "Hmmm... maybe somewhere in Tepper?"
    "Maple" "They have pretty big rooms, don't they?"
    "Jenny" "Oh yeah!"
    "You can probably talk to one of the admins to reserve it in advance."
    "\"Beep boop!\""
    "Sandie" "I think that's my bread. Lemme go check on it."
    "Sandie" "It was nice meeting you, [player_name]!"
    hide sandwich normal with dissolve
    "Maple" "So if we do somewhere in Tepper, we'll have to talk to the storage team to make sure they have enough tables, right?"
    "Jenny" "Yeah, I don't fully know how that process works."
    "I can give it a shot."
    "Roxy probably has some connections we can use."
    "Jenny" "That would be great!"
    "Maple" "Thank you so much!"
    "How many tables do you think you'll need?"
    "Jenny" "Hmm... maybe about 9 or 10? We'll need enough chairs too."
    "Maple" "We can probably reuse the decorations and costumes from last year, so it should just be those two things."
    "Alright, sounds good!"
    "I'll go talk to the storage team, then."
    "Jenny" "Yeah!"
    "Maple" "Thanks for the help!"
    "Jenny" "You should also definitely visit our cafe during the festival if you have the chance!"
    "Yeah, definitely!"
    "I'll see you later!"
    "Jenny" "Bye!"
    "Maple" "See you!"
    hide jenny normal with dissolve
    hide waffle normal with dissolve
    jump midterm2


label gaming_club:
    scene black
    show text "You make your way to the Graphics Lounge to find the contact Roxy provided you with." with dissolve
    pause 1.5
    hide text with dissolve
    scene bg classroom
    "Wow, this place is pretty nice.."
    show graphics normal with dissolve
    "???" "Andy, what are you doing? Can you come gank bot?"
    show andy normal at right with dissolve
    "Andy" "Bruh I just respawned! Lemme stock up on potion first."
    "???" "How did you die!? Did the chickens kill you?"
    "???" "No, it looks like he went AFK..."
    "???" "Dammit Andy, are you playing Herrscher on your phone while playing Legends again?"
    "Andy" "Legends gets too boring, man."
    "Andy" "No one ever wants to help me kill dragon so there's nothing to do here..."
    "What are they even talking about..."
    "Andy" "I already killed the wolves like five times!"
    "???" "If you'd help us push, then maybe we'd have time to fight dragon!"
    "Andy" "..."
    "Andy" "Meh..."
    "???" "Oh, I think someone's here, Rae."
    "Rae" "Oh!"
    "Rae" "Gimme a sec, we're about to lose, anyway..."
    "Andy" "Haha gottem"
    "Andy" "I took their turret."
    "Rae" "Wait what."
    "Andy" "Oho we're boutta win now."
    "Rae" "I can't believe you've just done this..."
    "Rae" "Daniel, how is this happening?"
    show daniel normal at left with dissolve
    "Daniel" "He went and hid in a bush and then went AFK."
    hide daniel normal with dissolve
    "Rae" "How did they not catch him? I don't understand..."
    "Andy" "I'm just too good at this game."
    "Andy" "Wow we won ez!"
    "Andy" "Peak komedy."
    "Rae" "Alright, don't troll next time, Andy..."
    "Andy" "Oho no promises."
    hide andy normal with dissolve
    "Rae" "..."
    "Rae" "Hello!"
    "Hey! I'm [player_name], I'm here from the student council. Did Roxy send you an email about what she wanted?"
    "Rae" "Yeah, I got it."
    "Rae" "You needed a logo, right? What's the theme for the festival this year?"
    "It's \"Light mode vs. Dark mode\"."
    show daniel normal at left with dissolve
    "Daniel" ":thinking:"
    hide daniel with dissolve
    "Rae" "Interesting..."
    "Rae" "Yeah, I can probably come up with a logo for that."
    "Rae" "You just need the SCS dragon to be in it, right? Do you need it by your next meeting?"
    "Yeah, I think the dragon needs to be in it."
    "We don't really need it by our next meeting, but we do need it so that we can send out emails and stuff."
    "No rush though."
    "We also need some poster designs."
    "Rae" "Daniel, can you make the posters?"
    show daniel normal at left with dissolve
    "Rae" "You still have that fancy generative script, don't you?"
    "Daniel" "Yeah, I still have it."
    "Daniel" "I'll probably have to reconfigure it, but it shouldn't take long :thinking:"
    "Daniel" "I can change it after my Tetris class."
    "Rae" "Alright, sounds good."
    "Wait, you're taking a Tetris class?"
    "Daniel" "No, I'm teaching it actually haha."
    "Damn."
    "That's pretty cool."
    "Is that why you're wearing a Tetris costume?"
    "Daniel" "Yeah, today's their midterm, so I wanted to make the class more fun."
    "Alright, I guess I'll check back in again to see how the posters and logo are coming along."
    "Rae" "Sounds good!"
    "Daniel" "Pog"
    "Rae" "Maybe Andy will stop trolling us in every Legends game by then."
    show andy normal at right with dissolve
    "Andy" "No chance, this is peak komedy."
    hide andy normal with dissolve
    "Rae" "(Sigh...)"
    hide daniel normal with dissolve
    hide graphics normal with dissolve
    jump midterm2

label proxy_asleep:
    scene black
    show text "After completing your assigned task for the School Festival, you head back to the student council room to report your results." with dissolve
    pause 2.0
    hide text with dissolve
    scene bg classroom
    #show proxy normal at center with dissolve
    "Hey Roxy, I've completed my-"
    hide proxy normal with dissolve
    scene black
    show text "You stop in your tracks. There, among the stacks of unfinished paperwork, was Roxy, fast asleep at her desk." with dissolve
    pause 1.5
    hide text with dissolve
    show text "It's a curious sight. You've never seen Roxy like this before. " with dissolve
    pause 1.0
    hide text with dissolve
    show text "Most of the time, it feels like she's always rushing from place to place, racing to finish her student council duties, but now she seems so relaxed. Her body gently rises and falls as she breathes." with dissolve
    pause 2.0
    hide text with dissolve
    show text "You decide to just quietly put your report on her desk so she can read it when she awakens. Hopefully, it doesn't get lost amongst the other paperwork." with dissolve
    pause 1.5
    hide text with dissolve
    show text "You tip-toe towards Roxy's desk and slide your report in front of her. At this point, you've completed your task and should probably leave, but you're too captivated by Roxy's features." with dissolve
    pause 2.0
    hide text with dissolve
    show text "Upon further observation, you see that maybe Roxy is not as calm as you had previously thought. Her eyebrows are slightly furrowed and there are dark circles under her eyes. Exhaustion is written all over her face. Her body seems tense even while asleep." with dissolve
    pause 2.5
    hide text with dissolve
    show text "You are reminded of how hard Roxy works, day in and day out, and realize that she really is the backbone of the Student Council. She's the one who keeps everything going smoothly while some of the Student Council members (like Steven) fool around." with dissolve
    pause 2.5
    hide text with dissolve
    show text "She takes so much work onto herself without complaint, without asking for help from others. That's why she's always stuck inside the student council room with stacks and stacks of documents to go through." with dissolve
    pause 2.5
    hide text with dissolve
    show text "Why don't the other members pick up the slack?" with dissolve
    pause 0.5
    hide text with dissolve
    show text "You vow to work harder from now on, for Roxy's sake, and reach out your hand and give her a head pat." with dissolve
    pause 1.0
    hide text with dissolve
    scene bg classroom
    show proxy normal at center with dissolve
    p "...hmm?"
    hide proxy normal with dissolve
    scene black
    show text "Roxy stirs and awakens. She seems slightly disoriented and tired at first, but she quickly regains her bearings. Her head whips in your direction." with dissolve
    pause 1.5
    hide text with dissolve
    scene bg classroom
    show proxy normal at center with dissolve
    p "Y-you..."
    hide proxy normal with dissolve
    scene black
    show text "Her face quickly turns red with embarrassment as she realizes the situation." with dissolve
    pause 0.5
    hide text with dissolve
    scene bg classroom
    show proxy normal at center with dissolve
    p "[player_name], did… you see me sleeping? Did you stare at me while I was asleep? How dare you! Erase the image from your mind! Immediately!"
    "(Well, this is another new side of Roxy I didn't know about. It's kind of… cute. Maybe I should tease her for a bit.)"
    "And what if I don't? What if I cherish this memory for all eternity?"
    p "Don't you dare!"
    hide proxy normal with dissolve
    scene black
    show text "You can practically see the steam coming out of her head." with dissolve
    pause 0.5
    hide text with dissolve
    scene bg classroom
    show proxy normal at center with dissolve
    "Oh, but I do dare!"
    hide proxy normal with dissolve
    scene black
    show text "You retreat out the door of the student council room and sprint down the hall, cackling. Roxy chases after you. This pursuit lasts several minutes before you both run out of breath. She finally catches up to you, panting, threatens to flood you with work, and makes you promise not to tell anyone about what you saw and to forget what happened. You only half-heartedly agree to that last request." with dissolve
    pause 4.0
    hide text with dissolve
    scene bg classroom
    jump handin_malloc

