# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

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
    $ duo_name = "Mr. SCS"
    $ join_stuco = False
    $ malloc_points = 0
    $ shell_points = 0
    $ proxy_points = 0
    $ stuco_task = -1
# The game starts here.

label malloc_oh:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg nighttime
    scene bg classroom
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #$ player_name = renpy.input("What is your name?", length=32)
    #$ player_name = player_name.strip()
    #$ player_name = player_name[0].upper() + player_name[1:] if len(player_name) > 0 else player_name.capitalize()
    show malloc normal with dissolve
    $ vim_user = False
    # These display lines of dialogue.

    m "Hello, [player_name]. You're next on the queue."
    m "Looks like you're having some issues with your memory allocation functions."
    m "I can take a look at it, but you'll need to answer my question first."
    
    show malloc eyes with dissolve
    m "{b}Did you write a heap checker?{/b}"
    menu:
        "Yes.":
            $ malloc_points += 30
            jump heapcheck
        "No...":
            jump no_heapcheck
        "What's that?":
            jump unsure_heapcheck

    # This ends the game.


label no_heapcheck:
    show malloc eyes2 with dissolve
    m "A Segmentation Fault is too kind of a punishment for {i}scum{/i} like you."
    m "Come back when you've learned how to debug your code {i}yourself{/i}."
    m "Or maybe, I should tell Roxy to deal with you somehow."
    "{b}Bam!!{/b}" with hpunch
    hide malloc eyes2 with dissolve
    "D...Did he just {i}punch{/i} me?"
    "Who needs a heap checker when I have {i}my own{/i} two eyes?"
    "And who's Roxy?"
    "Whatever. That guy needs serious help..."
    # few hours later
    scene black
    show text "After a few hours of debugging..." with dissolve
    pause 1.0
    hide text with dissolve
    scene bg classroom
    "Hmm... my code still doesn't seem to work."
    "What the heck am I doing wrong here?"
    "..."
    
    menu:
        "Maybe I should just write a heap checker...":
            $ malloc_points += 30
            jump shell_prologue_good
        "Maybe I should just give up...":
            "There's no way I forgot a semicolon or something {i}stupid{/i} like that."
            "I'm too smart for those kinds of mistakes."
            "..."
            jump shell_prologue_bad

label malloc_epilogue:
    "I have other work to finish anyway, so hopefully this finds the bugs."
    "Alright, time to test this out..."
    "..."
    "My heap checker says there's something wrong in this part of the memory..."
    "But what could it be...?"
    "I'm probably missing something dumb."
    "Maybe I should go ask Malek again."
    scene black
    show text "You find Malek ranting about freeing memory to some frightened freshmen." with dissolve
    pause 2.0
    hide text with dissolve
    scene bg classroom
    show malloc normal with dissolve
    m "Oh, hello [player_name]. What brings you back here?"
    "I wrote a heap checker, but I still can't figure out my issue."
    m "I see you've learned from your mistakes."
    $ malloc_points += 20
    m "Good for you. Sorry if I was too harsh earlier, but being able to write software that backs you up is very important."
    "No worries, I understand."
    m "Let me take a look..."
    m "..."
    m "Ah, I see the issue."
    "Wow, that was fast."
    m "When you're releasing this memory block here, you're forgetting a step."
    m "You should be able to figure it out from here."
    m "Good luck!"
    hide malloc normal with dissolve
    jump shell_prologue_good

label shell_prologue_good:
    "Hmm.. what am I forgetting here?"
    "..."
    "..."
    "...!"
    "Damn, I forgot to free that variable..."
    menu:
        "This is what I get for not using Vim...":
            $ vim_user = False
            jump shell_intro_good
        "This is what I get for not having a good Vim config...":
            $ vim_user = True
            jump shell_intro_good

label shell_prologue_bad:
    menu:
        "It's not like I'm using Vim...":
            $ vim_user = False
            $ join_stuco = True
            jump shell_intro_bad2
        "People who forget semicolons probably don't even use Vim, like me, an intellectual.": #confusing sentence
            $ vim_user = True
            $ join_stuco = True
            jump shell_intro_bad

label heapcheck:
    show malloc normal with dissolve
    
    m "Looks like you actually know what you're doing."
    m "The number of people who answer \"no\" to that question is {i}astounding{/i}."
    m "Anyway, you may want to check that you're freeing variables."
    m "Memory leaks are one of the most prominent threats to freedom these days."
    m "Everyone wants to {i}take{/i} memory, but no one wants to {i}give it up{/i}."
    m "Don't be one of those scummy people, taking what's not yours and refusing to give it up."
    show malloc eyes with dissolve
    m "{b}Free the memory!!{/b}" with hpunch
    show malloc normal with dissolve
    m "And don't even get me {i}started{/i} on people who double-free their memory."
    m "They're arguably even {i}worse{/i}!"
    m "If you give someone too much freedom, they'll never get their work done!"
    m "This is why taking naps in the middle of the day never works!"
    "..."
    m "..."
    m "Sorry about that."
    m "I tend to rant when I talk about things like this."
    m "That should fix your problem. If not, I have faith in your programming abilities."
    m "Hope this helps!"
    hide malloc normal with dissolve

    "..."
    "What the heck was {i}that{/i}?"
    "That guy probably has a few loose screws."
    "I should look at my code though, just to check what he said."
    "..."
    "...."
    "..."
    "Ah shit, I just forgot a semicolon."
    menu:
        "Well, this is what I get for not using Vim.":
            $ vim_user = False
            jump shell_intro_good
        "Well, this is what I get for using Vim.":
            $ vim_user = True
            jump shell_intro_good

label unsure_heapcheck:
    
    show malloc normal with dissolve
    m "Are you {i}serious{/i}?"
    m "How do you not know what that is?"
    m "Do you not pay attention during lecture?"
    "..."
    m "Ah, I get it. You must be one of those people who think they're too good to go to lectures, aren't you?"
    m "All you \"pro-gamer\" scum are the same, thinking you can get by watching recordings at 2x speed." 
    show malloc eyes with dissolve
    m "You may be happily cruising along now, but just wait until my buddy Roxy really makes you suffer."
    show malloc eyes2 with dissolve
    m "I look forward to seeing how that turns out."
    m "See you at the final exam."

    hide malloc eyes2 with dissolve

    "..."
    "What just {i}happened{/i}?"
    "And who the frick is Roxy?"
    "Am I supposed to be scared?"
    "..."
    "Nah, if I can sleep during lectures and still keep my A, there's nothing to be afraid of."
    menu:
        "After all, I don't use Vim.":
            $ vim_user = False
            $ join_stuco = True
            jump shell_intro_bad2
        "After all, I set up my own fancy Vimrc all by myself.":
            "There's nothing that could {i}possibly{/i} be more difficult than that."
            $ join_stuco = True
            jump shell_intro_bad

label shell_intro_bad:
    show shell angry with dissolve
    s "Let me stop you right there. {b}Show me your Vimrc.{/b}"
    "Huh?"
    s "I heard you bragging about your Vim setup, but you couldn't even get your heap checker working."
    "How do you know that? And who are you?"
    s "I'm Shell."
    $ s.name = "Michelle"
    s "Malek seemed to be in a pretty bad mood after talking to you, and there's only one way {i}that{/i} can happen."
    "(I guess that dude really did have a few loose screws.)"
    "(Imagine getting angry when other people can't fix their code.)"
    s "Yeah, this Vimrc is fancy, but it's still pretty {i}trash{/i}. No wonder your code didn't work."
    "What does having a bad setup have to do with not having working code?"
    s "Damn, you really are clueless, aren't you?"
    show shell normal with dissolve
    s "Maybe you should join my Vim club. Someone like you could {i}clearly{/i} use the help."
    "..."
    "(So this girl just shows up in a penguin hoodie, trashes my Vimrc, and now she wants me to join her club?)"
    "(She can't be serious...)"
    "Actually, I think I'll pass."
    show shell angry with dissolve
    s "Hahaha! You thought you had a choice?"
    "(Ah shit, I should have guessed. The ones with the weird hoodies are always like this.)"
    show shell normal with dissolve
    s "See you at 5 in the activity room. If you don't show up, I know where to find you, [player_name]."
    "(Alright, she knows my name too. This day is going great.)"
    hide shell normal with dissolve
    "(...)"
    $ s.name = "???"
    jump proxy_bad_req_den

label shell_intro_bad2:
    show shell angry with dissolve
    s "Let me stop you right there, [player_name]. {b}What did you just say about Vim?{/b}"
    "Uhh.. that it's bad? Why do people even prefer it to other text editors? And how do you know my name?"
    s "{b}You take that back!{/b}" with hpunch
    s "You can't go around bashing Vim like this!"
    "(Okay, so this girl is clearly crazy too.)"
    "Alright, I'll keep that in mind."
    "By the way, who are you?"
    s "My name is Shell."
    $ s.name = "Michelle"
    "Cool. I'm gonna go this way now."
    s "You think I'm gonna {i}let you go{/i} after you made fun of Vim?"
    "(Shit... She's not gonna slap me or something, is she?)"
    s "I'm signing you up to join my Vim club!"
    "Hold up, hold up. There's a club {i}just{/i} for Vim?"
    "Why does that exist?"
    s "{b}You take that back!{/b}" with hpunch
    "(Yup, I'm gonna get slapped.)"
    s "I'll see you in the activity room at 5. If you don't show up, I'll tell the student council president to {i}expel{/i} you!"
    "(Welp, that's definitely {i}worse{/i} than getting slapped.)"
    "(This day is going great.)"
    hide shell angry with dissolve
    $ s.name = "???"
    jump proxy_bad_req_den



label shell_intro_good:
    show shell star with dissolve
    s "Did someone say {i}Vim{/i}?"
    "Uh...yes?"
    s "{i}No one{/i} likes Vim more than I do!"
    show shell normal with dissolve
    s "Do you want to join my Vim club?"
    "(Vim \"club\"?)"
    "(Why is there a club just for Vim?)"
    "(Is everyone here this crazy?)"
    show shell star with dissolve
    s "So, what do you say?"
    "Wait, but I don't even know who you are!"
    show shell normal with dissolve
    s "..."
    s "Sorry about that. I've been trying to get new club members for a long time, 
        but no one's really interested."
    s "I thought another Vimp like you could help me."
    if vim_user:
        "(\"Vimp\"? I consider myself a {i}Vim connoisseur{/i}. I don't think I'm at {i}\"Vimp\"{/i} level...)"
    else:
        "(\"Vimp\"? I don't even use Vim though...)"
    s "Anyway, I'm Michelle, but you can call me Shell. What's your name?"
    $ s.name = "Michelle"
    "I'm [player_name]."
    s "Well, nice to meet you, [player_name]!"
    menu:
        "Nice to meet you too!":
            $ shell_points += 30
            s "So, what do you say? Do you want to join my club?"
        "Likewise, I guess.":
            $ shell_points += 10
            s "So, what do you say? Do you want to join my club?"
    menu:
        "Sure!":
            $ join_vimclub = True
            $ shell_points += 30
            show shell star with dissolve
            s "Oh that's great! I'll give you a club form, just give me a second..."
            show shell star at midleft with move
        "Nah, I'm good.":
            $ join_vimclub = False
            show shell sad with dissolve
            s "Aw man, another rejection..."
            s "Why does no one want to join? "
            show shell sad at midleft with move
    show attack normal at midright with dissolve
    a "Oh, hey, [player_name]!"
    a "Shell, you're gonna be late for class!"
    show shell normal at midleft with dissolve
    s "Oh shoot, I gotta run!"
    if join_vimclub:
        s "Here's the club form. Fill it out and submit in the box at the end of the hallway."
        "Why can't I just give it to the student council directly?"
        s "They're typically very busy, so they make Packet deliver students' requests from that box."
        s "Just so they don't get too many people trying to talk to them."
        "(Who's Packet?)"
    s "See you later, [player_name]!"
    hide shell normal with dissolve
    hide attack normal with dissolve
    "..."
    "The people here keep getting weirder and weirder."
    if join_vimclub:
        jump proxy_good_req_den
    else:
        jump proxy_join_stuco

label proxy_good_req_den:
    # the next day
    scene black
    show text "The next day..." with dissolve
    pause 1.0
    hide text with dissolve
    scene bg classroom
    show shell normal with dissolve
    $ s.name = "Michelle"
    s "Hey, [player_name]! Did you submit your club form?"
    "Yeah, I'm going to check out the result now."
    s "Cool, I'll come with you!"
    scene black
    show text "You and Michelle walk down the hallway towards your SMC mailbox." with dissolve
    pause 2.0
    hide text with dissolve
    scene bg classroom
    show shell normal with dissolve
    s "Did you fix the issue with your dynamic memory homework?"
    "Yeah, I just forgot a semicolon. Dumb mistakes go brrr.."
    s "Don't worry about that!"
    s "At least you wrote a heap checker!"
    s "It would have taken {i}much{/i} longer if you didn't write one."
    "Maybe you're right..."
    "..."
    "Ah, here's my form..."
    scene black
    show text "You open your SMC mailbox and retrieve your processed club form." with dissolve
    pause 2.0
    hide text with dissolve
    scene bg classroom
    show shell normal with dissolve
    s "What does it say?"
    "Request denied?"
    s "Huh? Let me see that..."
    scene black
    show text "Michelle scrutinizes the form with her brows furrowed." with dissolve
    pause 2.0
    hide text with dissolve
    scene bg classroom
    show shell normal with dissolve
    s "..."
    s "We should go talk to the student council president."
    "Uhh, alright...?"
    "I thought you said they didn't like random people barging in."
    s "Don't worry, Roxy's a good friend of mine. She'll talk to us if I'm with you."
    s "There's gotta be a reason why she would reject your form. Maybe there's a mistake on the form."
    "..."
    s "Either way, there's only one way to find out - let's go talk to her!"

    scene black
    show text "Michelle leads you to the Student Council room, where she swings open the door with a loud bang. This is probably why the Student Council doesn't like visitors." with dissolve
    pause 2.0
    hide text with dissolve
    show text "Roxy, the Student Council President, emerges from the storage closet with a shallow bowl filled with kibble in hand." with dissolve
    pause 2.0
    hide text with dissolve
    scene bg classroom
    show shell star with dissolve
    s "Hey, she's over there! Hi Roxy!"
    show shell star at midright with move
    show proxy normal at midleft with dissolve
    p "Welcome, Shell. It's been a while since I last saw you. How are you?"
    s "I'm doing great!"
    s "Is that Packet there with you?"
    p "Yes, I just refilled Packet's food bowl."
    "(So, Packet is a cat...)"
    p "Who is your companion, Shell?"
    show shell normal at midright with dissolve
    s "This here is [player_name]. We saw that their Vim membership application was denied and came to find out why."
    p "You're [player_name]? What a coincidence, I have something I'd like to discuss with you. You've saved me the trouble of looking for you."
    p "But before that, let's get to the bottom of this situation, shall we? You said your club member application was denied? "
    p "That's certainly odd. I don't recall denying any applications recently. Why don't we head into the student council room and get things sorted out."

    scene black
    show text "All three of you enter the student council room. There are many stacks of papers on Roxy's desk. She sits down at her seat and gestures for you and Michelle to take the chairs opposite of her. Roxy moves the stacks to the side so that they don't obstruct your conversation." with dissolve
    pause 3.0
    hide text with dissolve
    scene bg classroom
    show shell normal at midright with dissolve
    show proxy normal at midleft with dissolve
    p "Hmm... Let me see... Aha, I found it!"
    p "It seems like Steven accidentally rejected it. Don't worry, I'll punish him later."
    p "Anyways, now that that's out of the way, what I wanted to discuss with you was…"
    p "are you interested in joining the student council?"
    p "I know that this is a very sudden request, but you are in good academic standing and have great interpersonal skills. Malek was also especially impressed by your programming skills. These are all qualities that I highly desire in the student council, so I thought to reach out to you."
    s "Oooh, that's great! You should definitely join! I've heard it's super fun!"
    s "You also get to plan the School Festival!"
    p "Right, as Shell said, you'll have the exciting opportunity to organize the School Festival. But keep in mind, it's not all fun and games. The student council also handles other important matters as well."
    p "Becoming a student council member will involve a large time commitment, but I do believe the rewards are worth it as well."
    p "If it motivates you further, you can also add this role as experience on your resume, which I'm sure will be helpful when you are searching for internships."
    p "What do you say?"
    menu:
        "I'm definitely interested!":
            $ proxy_points += 30
            $ join_stuco = True
            p "Great, welcome aboard. I look forward to working with you. Let me get the relevant paperwork and you can complete it right away."
        "Actually, I think I'm good. Thanks for the offer.":
            $ shell_points += 30
            p "Not a problem. I understand. Allow me to approve your Vim Club membership, then."
    p "..."
    p "Here you go. I'll need your signature at the bottom and then you're all set."
    p "You can also take your time to read through it, if you'd like."
    scene black
    show text "You take some time to look through the form." with dissolve
    pause 1.0
    hide text with dissolve
    scene bg classroom
    show shell normal at midright with dissolve
    show proxy normal at midleft with dissolve
    "Looks good to me."
    p "Great, you're good to go."
    hide shell normal with dissolve
    hide proxy normal with dissolve
    if not join_stuco: 
        jump vim_club
    else:
        jump stuco_good
    

label proxy_join_stuco:
    scene black
    show text "A few days later..." with dissolve
    pause 1.0
    hide text with dissolve
    scene bg classroom
    show malloc normal with dissolve
    $ s.name = "Michelle"
    m "Hello [player_name], are you doing well?"
    "Yeah, how about you?"
    m "Likewise."
    "So, why'd you ambush me first thing in the morning today?"
    m "There's a friend of mine who'd like to meet you."
    "Really? Who?"
    m "Roxy, the student council president. She wants to recruit you for the student council."
    menu:
        "(I'm not really interested, but I'll hear her out.)":
            "So where is the student council room?"
        "(Yes! Something to add to my LinkedIn profile!)":
            $ proxy_points += 30
            $ malloc_points += 30
            $ join_stuco = True
            "Yes, I'm definitely interested!"
    m "It's just down this way."
    m "Roxy, I've brought [player_name]."
    show malloc normal at midright with move
    show proxy normal at midleft with dissolve
    p "Just a second, I'm persuading Packet to eat his food."
    p "Come on, Packet. I know this isn't your favorite, but if you don't finish it then I can't get you the one you like."
    "Packet" "nyan nyan"
    p "There we go..."
    "Packet" "mrrrroww"
    "(So, Packet is a cat...)"
    p "[player_name], did Malek explain why I wanted to talk to you?"
    "Yeah, he said you wanted to recruit me for the student council?"
    "Why me, though?"
    m "I recommended you."
    p "Malek here was pretty outspoken about your interpersonal and technical skills, so I thought I'd ask you to join, since we also need an additional member."
    "(Why does this feel like some kind of anime plot...?)"
    p "So, what do you say?"
    if join_stuco:
        $ proxy_points += 30
        "I'd love to join!"
    else:
        "I'm not really sure if I want to..."
        "What do I get out of being on the student council?"
        p "You get to help us plan the School Festival."
        "Hmmm..."
        p "You will also receive free food vouchers for the festival. Does that interest you?"
        menu:
            "Yes!":
                $ proxy_points += 30
                $ join_stuco = True
                p "Great!"
                p "Let me get the paperwork sorted out, then."
                p "(Damn that Steven, he's probably off stealing food from other clubs somewhere...)"
                p "..."
                p "Here you are. I just need your signature at the bottom."
                p "You can take your time to read through it, if you'd like."
                "..."
                "...."
                "..."
                "Hmm, looks good to me."
                p "Great!"
                p "You should be good to go."
                hide proxy normal with dissolve
                hide malloc normal with dissolve
                jump stuco_good
            "Actually, I'm good. Thanks.":
                p "No worries, I understand."
                p "Enjoy the rest of your day!"
                p "Hopefully, we'll cross paths again in the future."
                hide proxy normal with dissolve
                hide malloc normal with dissolve
                scene black
                show text "A few weeks later..." with dissolve
                pause 1.0
                hide text with dissolve
                jump review_session2
    p "Great!"
    p "Let me get the paperwork sorted out, then."
    p "(Damn that Steven, he's probably off stealing food from other clubs somewhere...)"
    p "..."
    p "Here you are. I just need your signature at the bottom."
    p "You can take your time to read through it, if you'd like."
    "..."
    "...."
    "..."
    "Hmm, looks good to me."
    p "Great!"
    p "You should be good to go, then."
    hide proxy normal with dissolve
    hide malloc normal with dissolve
    jump stuco_good

label proxy_bad_req_den:
    scene black
    show text "A few days later..." with dissolve
    pause 1.0
    hide text with dissolve
    scene bg classroom
    show shell angry with dissolve
    $ s.name = "Michelle"
    s "So, {i}Vim hater{/i}, did you submit your club form?"
    "...Yes."
    s "Great! Let's go check its status!"
    "(Sigh...)"
    "(Why did life have to turn out this way?)"
    "(If only I never met that Malek dude, I wouldn't be in this mess.)"
    s "Hmm..."
    "What is it?"
    s "It says request denied..."
    "(Yes! This is great!)"
    "Haha, if it got denied then there's nothing else that can be done!"
    show shell normal with dissolve
    s "Just kidding, we're gonna go talk to the student council president."
    "(Damn, I should've known it wouldn't be that easy!)"
    s "Roxy probably had some reason for rejecting your member form."
    s "We can just ask her directly."
    "(Roxy? Is this the person Malek was talking about?)"
    "(Welp, time to find out how exactly she'll make me \"suffer\"...)"
    s "There she is!"
    s "Roxy! Why did you reject [player_name]'s club member form?"
    show shell normal at midleft with move
    show proxy normal at midright with dissolve
    p "Hello, Shell."
    "Packet" "mrroww!"
    p "Is this [player_name]?"
    p "I actually wanted to talk to you about that."
    p "Malek told me about how much of a troublemaker you are, so I decided to keep a closer eye on you."
    p "Please sign at the bottom of this form."
    "(\"Troublemaker\"? All I did was not write a heap checker.)"
    "(Is that all it takes to be a troublemaker here?)"
    "..."
    "(Wait a second... \"probationary student council member\")?"
    "You can't make me do that! This has to be against the rules!"
    "I refuse!"
    show proxy okawaii at midright with dissolve
    p "How cute."
    p "You understand that I am the student council president, do you not?"
    p "You have to do whatever I say, or I can get you expeled from this institution."
    p "For I have the power to do so."
    "..."
    "(Ah shit...)"
    "..."
    "(End my suffering...)"
    "(All these idiots with their heap checker complexities can go to hell for all I care.)"
    show proxy normal at midright with dissolve
    p "Thank you for your cooperation."
    p "I'll see you tomorrow at 3 in the student council office."
    hide proxy normal with dissolve
    show shell normal at center with move
    "..."
    s "Haha, looks like Roxy thought of an even worse punishment for you, {i}Vim hater{/i}!"
    "Please stop calling me that."
    s "Have fun {i}suffering{/i}!"
    hide shell normal with dissolve
    jump stuco_bad


label vim_club:
    scene black
    show text "The next day..." with dissolve
    pause 1.0
    hide text with dissolve
    scene bg classroom
    "I think this is the right room..."
    show shell normal with dissolve
    s "Hey, [player_name]!"
    s "How are you doing?"
    menu:
        "I'm doing well!":
            s "That's great!"
            s "Hopefully you'll enjoy your first Vim club meeting!"
        "Not that well, actually...":
            s "Oh, I'm sorry to hear that."
            s "Hopefully your first Vim club meeting cheers you up!"
    show shell star with dissolve
    s "Hey, everyone!"
    show shell normal with dissolve
    s "This is our newest member, [player_name]."
    "Uh, ... hello."
    s "Don't be shy!"
    s "Everyone here likes Vim just as much as you and me!"
    s "So, before we get started, does anyone remember what the first rule of Vim club is?"
    "Is it..."
    menu:
        "Don't talk about Vim club?":
            $ shell_points += 30
            s "Haha, you're pretty funny!"
        "Write a heap checker?":
            $ shell_points += 20
            s "Haha, you're pretty funny!"
            s "We don't really need heap checkers when we use Vim."
        "Have a fancy Vimrc?":
            $ shell_points += 30
            s "Haha, you don't need a fancy Vimrc to join this club."
    #show shell normal at right with move
    show rebecca normal at left with dissolve
    "Rebecca" "Isn't it to write a cheatsheet?"
    show evelyn normal at right with dissolve
    "Evelyn" "Wait, but I don't use a cheatsheet for my Vim commands..."
    "Rebecca" "That's pretty zesty, besty. You're too big brained."
    hide rebecca normal with dissolve
    show adb normal at left with dissolve
    "ADB" "Hehe I just stole a cheatsheet from Google..."
    "ADB" "Why do more work when someone else already did it?" 
    #hide rebecca normal with dissolve
    hide evelyn normal with dissolve
    hide adb normal with dissolve
    #show shell normal at midleft with move
    show steven normal at right with dissolve
    "Steven" "I have a question. How do I exit Vim?"
    show shell angry with dissolve
    s "Steven, what are {i}you{/i} doing here?"
    s "Shouldn't you be at the student council meeting?"
    "Steven" "Well, they ran out of food, so I came here instead."
    "Steven" "Have the snacks arrived yet?"
    "Steven" "I could only steal this one cookie from the track team."
    show rebecca normal at left with dissolve
    "Rebecca" "Steven's highkey sus right now..."
    hide rebecca normal with dissolve
    "Who is this guy?"
    s "Steven's {i}supposed{/i} to be the secretary of the student council."
    "Steven" "That's correct, but it's not like many people are joining new clubs right now."
    "Steven" "I don't really have anything to do there."
    "Steven" "I'd rather come here and flex my fancy Vimrc on you peasants."
    "Wait, hold up."
    "You have a fancy Vimrc, but you don't know how to exit Vim?"
    "Are you serious?"
    s "What are you talking about, Steven?"
    s "{i}Of course{/i} people are trying to join clubs right now, it's the start of the semester!"
    s "When was the last time you checked your school email?"
    "Steven" "Uhh..."
    s "That's what I thought!"
    s "Now go sit in the Emacs corner while you approve all those member requests."
    "Steven" "(Sigh...)"
    hide steven normal with moveoutright
    show shell normal with dissolve
    "Damn, Shell, you almost sound like an actual member of the student council."
    "More so than Steven, anyway."
    "Why are you not a part of it?"
    s "Well, my sister used to run this club, but she let me do it instead because she needed to focus on job applications before graduation."
    s "She also has a bunch of time management issues..."
    s "So I don't think I'd be able to run the Vim club {i}and{/i} be on the student council at the same time."
    menu:
        "Ah, I see.":
            $ shell_points += 10
        "Still, you're doing a great job!":
            $ shell_points += 30
            s "Aw, thanks!"
    s "So, like Rebecca said, having a cheatsheet is going to really save your butt when it comes to Vim."
    s "Unless you're as big brained as Evelyn over here."
    "Rebecca" "That's very pog, Evelyn."
    s "So does anyone have any obscure Vim commands they want to share for other people's cheatsheets?"
    hide shell normal with dissolve
    scene black
    show text "The club spends some time sharing favorite obscure Vim commands." with dissolve
    pause 1.5
    hide text with dissolve
    scene bg classroom
    show shell normal with dissolve
    s "Ok, now we're gonna have a pop quiz!"
    "Evelyn" "Awwww...."
    "Rebecca" "Are there prizes?"
    s "You get to bonk Steven."
    #show shell normal at midleft with move
    show steven normal at right with dissolve
    "Steven" "Wait what."
    "Steven" "I did not agree to this."
    s "Yeah well, I just got a message from Roxy saying you're kicked from the student council, so..."
    "Steven" "Huh?"
    "Steven" "I'm literally sitting here approving member requests for them, though."
    s "Too bad."
    "Steven" "Huh..looks like I'll have to crash their next meeting..."
    "ADB" "What does \"bonk\" mean in this context?"
    s "You get to remap Steven's Vimrc key bindings."
    "Steven" "Hold up."
    "Steven" "Wut."
    show adb normal at left with dissolve
    "ADB" "Hahaha!"
    "ADB" "La bomba!"
    hide adb normal with dissolve
    "Steven" "Why is this happening?"
    s "Do you have a better incentive for a pop quiz?"
    "Steven" "..."
    #show shell normal at midright with move
    #show steven normal at right with move
    show evelyn normal at left with dissolve
    "Evelyn" "Can we also actually bonk him?"
    "Evelyn" "Does anyone have an inflatable baseball bat?"
    "This is escalating pretty quickly..."
    #show steven normal at midright with move
    #show evelyn normal at center with move
    hide evelyn normal with dissolve
    show rebecca normal at left with dissolve
    #show adb normal at left with dissolve
    "Rebecca" "Oh I think I have one, gimme a few minutes."
    "Steven" "Why do you people find joy in physically hurting me?"
    hide rebecca normal with dissolve
    show evelyn normal at left with dissolve
    "Evelyn" "Because hurting you emotionally is bad."
    hide evelyn normal with dissolve
    show adb normal at left with dissolve 
    "ADB" "Mental health is good baba."
    hide adb normal with dissolve
    "Steven" "(Sigh...)"
    "Steven" "Maybe if I didn't wear a cow onesie people wouldn't gang up on me like this..."
    "Steven" "I'm gonna go tell Angela that I'm being bullied."
    "Rebecca" "I found it!"
    "Rebecca" "Let's get this zesty party started!"
    s "Let's start the pop quiz!"
    hide shell normal with dissolve
    hide steven normal with dissolve
    #hide evelyn normal with dissolve
    #hide rebecca normal with dissolve
    #hide adb normal with dissolve
    scene black
    show text "The club goes through a Vim pop quiz, and Steven gets bonked multiple times." with dissolve
    pause 1.5
    hide text with dissolve
    show text "His Vimrc key bindings also get remapped, so overall it's turning out to be a {i}great{/i} day for Steven." with dissolve
    pause 1.5
    hide text with dissolve
    scene bg classroom
    show shell normal with dissolve
    "Evelyn" "That was pretty fun!"
    show shell normal at midright with move
    show steven normal at midleft with dissolve
    "Steven" "No, it wasn't."
    "ADB" "Now I have more stuff to put on that cheatsheet I stole haha."
    "ADB" "Time to make a pull request..."
    "Rebecca" "Bonk bonk."
    "Steven" "Looks like I have to spend the next week fixing my key bindings..."
    "Steven" "Coming here may have been a mistake."
    "Evelyn" "What do you mean? This is the best club ever!"
    "Rebecca" "All fax no printer."
    s "Alright everyone, that concludes today's meeting!"
    s "I hope you all had a great time!"
    s "Except you, Steven. You deserved sitting in the Emacs corner like a delinquent while getting bonked."
    "Steven" "lok."
    s "Now that you're no longer on the student council, do you want to join the Vim club instead?"
    "Steven" "(Sigh...)"
    "Steven" "There goes the only leadership experience I could put on my LinkedIn profile..."
    "Just put \"Professional Cow\" or something."
    "That should get you a few interviews."
    "Steven" "..."
    "Steven" "I've probably already lost all my brain cells..."
    "Steven" "I'm gonna leave before I lose anything else."
    hide steven normal with dissolve
    show shell normal at center with move
    show shell star with dissolve
    s "So, [player_name], how'd you enjoy your first meeting?"
    menu:
        "It was super fun!":
            $ shell_points += 30
            s "Yayy!!"
            s "That's great!"
            s "Next meeting will be even more fun, since we need to start planning for the school festival."
        "It was a bit underwhelming...":
            $ shell_points += 30
            show shell sad with dissolve
            s "Aw, that's too bad..."
            s "Hopefully our next meeting is more interesting for you. We'll be planning for the school festival."
            show shell normal with dissolve
    "What does Vim club usually do for the festival?"
    s "Oh, we usually set up a minigolf booth."
    s "Do you get the joke?"
    "Uh..."
    "Is it like Vim golf or something?"
    show shell star with dissolve
    s "Yeah!"
    "Oooh that sounds interesting!"
    s "Yeah, it's super fun!"
    s "Anyway, I gotta go now. I'll catch you later!"
    "Bye!"
    hide shell star with dissolve
    #"You have [shell_points] points."
    jump review_session2

label stuco_good:
    scene black
    show text "The next day..." with dissolve
    pause 1.0
    hide text with dissolve
    scene bg classroom
    "I think this is the right room..."
    show proxy normal with dissolve
    p "Hello, [player_name]! How are you doing today?"
    "Packet" "nya nya nya"
    menu:
        "I'm doing well!":
            $ proxy_points += 30
            p "That's great!"
        "Not that well, actually.":
            $ proxy_points += 20
            p "Oh, that's unfortunate."
    p "Hopefully today's meeting will be entertaining."
    "Why is that?"
    p "Because if Steven doesn't show up, you get to take his position."
    "Who's Steven? And why would he not show up?"
    p "(Sigh...)"
    p "He's {i}supposed{/i} to be our secretary, but he keeps skipping meetings to go steal food from random clubs on campus."
    "(Sounds like a real character...)"
    p "Anyway, let's head inside."
    "Packet" "mrroww"
    "Halten" "Heyo!"
    show reduction normal at left with dissolve
    p "Hey, Halten."
    p "Is everyone else here yet?"
    "Halten" "Well, everyone except Steven."
    show critical normal at right with dissolve
    "Graff" "Which was definitely expected."
    "Halten" "Oh, and your brother's here taking coffee again, as usual."
    hide reduction normal with dissolve
    show distr normal at left with dissolve
    "Pax" "What do you mean, \"as usual\"?"
    p "Pax, please just fix your coffee machine."
    "Pax" "See I would, but that requires actual effort."
    "Pax" "My free time is already distributed too thin, you know?"
    p "(Sigh...)"
    hide distr normal with dissolve
    show reduction normal at left with dissolve
    p "Anyway, do we want to wait a few minutes for Steven, or should I just kick him out now?"
    "Halten" "Yes, I am down for punishing Steven."
    "Graff" "Seconded."
    "Halten" "The other day, he wouldn't shut up about how his Vimrc was better than mine."
    "Halten" "I don't even know what that is!"
    "Graff" "Yeah, that sounds like a Steven thing to do."
    "Graff" "He also somehow dug up my embarrassing middle school pictures and started spreading rumors about me again."
    "Graff" "Which I don't understand how people believed him, because he was wearing that obnoxious cow onesie again..."
    "Graff" "(Sigh...)"
    p "..."
    p "So, [player_name], how would you like to be the new secretary of the student council?"
    "Sure, I guess."
    $ proxy_points += 30
    "Halten" "Wait, hold on. Don't we have to do some kind of vote?"
    "Halten" "Or have some pool of candidates to consider first?"
    "Graff" "Dude, there's literally no one else here."
    hide reduction normal with dissolve
    show distr normal at left with dissolve
    "Pax" "(Slurp...)"
    p "Pax, can you take your coffee and slurp somewhere else?"
    "Pax" "Hold on, this is just getting interesting."
    "Pax" "What if Steven pops in right now?"
    p "That's probably not going to happen."
    "Graff" "With high probability."
    "Pax" "..."
    "Pax" "Alright, alright, you can stop glaring at me. I'll leave now."
    hide distr normal with dissolve
    show reduction normal at left with dissolve
    p "..."
    p "Let's {i}officially{/i} start the meeting now, then."
    p "[player_name], can you take down the meeting notes?"
    "Sure, I can do that."
    p "So, we have quite a bit of tasks to get through today."
    p "I guess the first thing to ask is how the budgeting for the festival is going?"
    "Halten" "I think I already verified most of the club budgets and allocated funds, so we should be good to go on that end."
    "Graff" "Damn, this man just reduced all of his work for the rest of the semester."
    "Halten" "I mean, it's easy to finish my work when I'm not TAing a class and lowering students' grades, \"Destroyer of Dreams\"."
    "Graff" "..."
    "Graff" "How do you know about that name?"
    "Halten" "hehe"
    p "Can we get back on topic, please?"
    "Graff" "..."
    "Graff" "(Hopefully my middle school chuuni pictures aren't being spread around...)"
    hide proxy normal with dissolve
    hide critical normal with dissolve
    hide reduction normal with dissolve
    scene black
    show text "Roxy goes over some of the menial tasks, which are trivial and left to interpretation by the player." with dissolve
    pause 2.0
    hide text with dissolve
    scene bg classroom
    show proxy normal with dissolve
    show critical normal at right with dissolve
    show reduction normal at left with dissolve
    p "So the three main things we have to do now are talk to the sysadmin to make sure the WiFi bandwidth is enough for the expected crowd,..."
    p "check that the cooking club has a big enough space for their festival activities,..."
    p "ask someone to create a logo and some posters for the festival,..."
    p "and find some music artist to perform the opener."
    p "Does anyone have a preference on which one they want to do?"
    p "The music artist isn't as high priority, so if you happen to find someone, just let me know."
    menu:
        "I can talk to the sysadmin.":
            $ stuco_task = 0
            $ proxy_points += 30
            "Halten" "I can go talk to the cooking club then."
            "Graff" "I'll go ask someone to make some posters. I think I have someone in mind who can do that."
        "I can talk to the cooking club.":
            $ stuco_task = 1
            $ proxy_points += 30
            "Halten" "I can go talk to the sysadmin then."
            "Graff" "I'll go ask someone to make some posters. I think I have someone in mind who can do that."
        "I can find someone to make posters.":
            $ stuco_task = 2
            $ proxy_points += 30
            "Halten" "I can go talk to the cooking club then."
            "Graff" "I'll talk the sysadmin, I guess."
            p "Okay, cool. [player_name], you may want to go find someone in the gaming club for posters."
            p "If I recall correctly, the club president was the one who drew the logo last year."
            "Sounds good."
    p "Alright, then. We have our next meeting in a month, so let me know how your tasks are going then."
    "Halten" "For sure."
    "Graff" "Ciao!"
    p "So, [player_name], did you enjoy your first student council meeting?"
    "It was..."
    "Interesting."
    p "I hope that's meant in a good way, haha."
    p "Good luck. I'll see you at our next meeting."
    "Bye!"
    hide critical normal with dissolve
    hide proxy normal with dissolve
    hide reduction normal with dissolve
    jump review_session2

label stuco_bad:
    scene black
    show text "The next day, you make your way to the student council room." with dissolve
    pause 2.0
    hide text with dissolve
    scene bg classroom
    $ stuco_task = -1
    "I think this is the right room."
    "Hopefully no one's here, so I'm not stuck in this stupid meeting."
    show proxy okawaii with dissolve
    p "Hello, troublemaker."
    "Ah shit."
    show proxy normal with dissolve
    p "Let's head in."
    p "If you're lucky, you may be promoted from probationary student today."
    "(What does that mean?)"
    "Packet" "mrroww"
    show reduction normal at left with dissolve
    "Halten" "Heyo!"
    p "Hey, Halten."
    p "Is everyone else here yet?"
    "Halten" "Well, everyone except Steven."
    show critical normal at right with dissolve
    "Graff" "Which was definitely expected."
    "Halten" "Oh, and your brother's here taking coffee again, as usual."
    hide reduction normal with dissolve
    show distr normal at left with dissolve
    "Pax" "What do you mean, \"as usual\"?"
    p "Pax, please just fix your coffee machine."
    "Pax" "See I would, but that requires actual effort."
    "Pax" "My free time is already distributed too thin, you know?"
    p "(Sigh...)"
    hide distr normal with dissolve
    show reduction normal at left with dissolve
    p "Anyway, do we want to wait for Steven, or should I just kick him out now?"
    "Halten" "Yes, I'm down for punishing Steven."
    "Graff" "Seconded."
    "Halten" "The other day, he wouldn't shut up about how his Vimrc was better than mine."
    "Halten" "I don't even know what that is!"
    "Graff" "Yeah, that sounds like a Steven thing to do."
    "Graff" "He also somehow dug up my embarrassing middle school pictures and started spreading rumors about me again."
    "Graff" "I don't understand how people believed him. He was wearing that {i}obnoxious cow onesie{/i} again..."
    "Graff" "(Sigh...)"
    p "..."
    p "So, [player_name], looks like you got lucky."
    p "How would you like to be the new secretary of the student council?"
    "Uh, well... it's better than being a probationary student, no?"
    p "Correct."
    $ proxy_points += 30
    "Halten" "Wait, hold on. Don't we have to hold some kind of vote?"
    "Halten" "Or have a pool of candidates to consider first?"
    "Graff" "Dude, there's literally no one else here."
    hide reduction normal with dissolve
    show distr normal at left with dissolve
    "Pax" "(Slurp...)"
    p "Pax, can you take your coffee and slurp somewhere else?"
    "Pax" "Hold on, this is just getting interesting."
    "Pax" "What if Steven pops in right now?"
    p "That's probably not going to happen."
    "Graff" "With high probability."
    "Pax" "..."
    "Pax" "Alright, alright, you can stop glaring at me. I'll leave now."
    hide distr normal with dissolve
    show reduction normal at left with dissolve
    p "..."
    p "Let's {i}officially{/i} start the meeting now, then."
    p "[player_name], can you take down the meeting notes?"
    "Sure, I can do that, I guess."
    "(This is going surprisingly better than I expected...)"
    p "So, we have quite the agenda to get through today."
    p "Our first task on today's agenda is budgeting for the festival. How is that going?"
    "Halten" "I think I've already verified most of the club budgets and allocated funds, so we should be good on that end."
    "Graff" "Damn, this man just reduced all of his work for the rest of the semester."
    "Halten" "I mean, it's easy to finish my work when I'm not TAing a class and lowering students' grades, Mr. \"Destroyer of Dreams\"."
    "Graff" "..."
    "Graff" "How do you know about that name?"
    "Halten" "Hehe."
    p "Can we get back on topic, please?"
    "Graff" "..."
    "Graff" "(Hopefully my middle school chuuni pictures aren't being spread around...)"
    hide proxy normal with dissolve
    hide critical normal with dissolve
    hide reduction normal with dissolve
    scene black
    show text "Roxy goes over some menial tasks. These are trivial and left to interpretation by the player." with dissolve
    pause 2.0
    hide text with dissolve
    scene bg classroom
    show proxy normal with dissolve
    show critical normal at right with dissolve
    show reduction normal at left with dissolve
    p "So the four main things we have to do now are..."
    p "talk to the sysadmin to ensure that the WiFi bandwidth is enough for the expected crowd,..."
    p "check that the cooking club has a large enough space for their festival activities,..."
    p "ask someone to create logos and posters for the festival,..."
    p "and find some musician to perform the opener."
    p "Does anyone have a preference on which task they want to take?"
    p "The musician isn't as high priority, so if you happen to find someone, just let me know."
    menu:
        "I can talk to the sysadmin.":
            $ stuco_task = 0
            $ proxy_points += 30
            "Halten" "I can go talk to the cooking club then."
            "Graff" "I'll go ask someone to make some posters. I think I have someone in mind who can do that."
        "I can talk to the cooking club.":
            $ stuco_task = 1
            $ proxy_points += 30
            "Halten" "I can go talk to the sysadmin then."
            "Graff" "I'll go ask someone to make some posters. I think I have someone in mind who can do that."
        "I can find someone to make posters.":
            $ stuco_task = 2
            $ proxy_points += 30
            "Halten" "I can go talk to the cooking club then."
            "Graff" "I'll talk the sysadmin, I guess."
            p "Okay, cool. [player_name], you may want to go find someone in the gaming club for posters."
            p "If I recall correctly, the club president was the one who drew the logo last year."
            "Sounds good."
    p "Alright, then. We have our next meeting in a month. Let me know how your tasks are going then."
    "Halten" "For sure."
    "Graff" "Ciao!"
    p "So, [player_name], how was your first student council meeting?"
    p "Don't be like Steven, or I'll have to punish you for {i}real{/i}, like Malek wanted."
    p "But if you perform your duty well, I'll look the other way."
    "Uh...okay?"
    "I'll make sure to finish my tasks while not prancing around in a cow onesie."
    p "I hope that's meant in a good way."
    p "Good luck. I'll see you at our next meeting."
    "Goodbye!"
    hide critical normal with dissolve
    hide proxy normal with dissolve
    hide reduction normal with dissolve
    jump review_session2
