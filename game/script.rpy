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
    $ player_name = ""
    $ duo_name = "Mr. SCS"
    $ join_stuco = False
    $ malloc_points = 0
    $ shell_points = 0
    $ proxy_points = 0
    $ data_points = 0
    $ attack_points = 0
    $ stuco_task = -1
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg nighttime
    scene bg classroom
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    $ player_name = renpy.input("What is your name?", length=32)
    $ player_name = player_name.strip()
    $ player_name = player_name[0].upper() + player_name[1:] if len(player_name) > 0 else player_name.capitalize()
    show malloc normal with dissolve
    $ vim_user = False
    # These display lines of dialogue.

    m "Hello, [player_name]. You're next on the queue."
    m "Looks like you're having some issues with your memory allocation functions."
    m "I can take a look at it, but you'll need to answer my question first."
    
    show malloc eyes with dissolve
    m "Did you write a heap checker?"
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
    m "A Segmentation Fault is too kind of a punishment for scum like you."
    m "Come back when you've learned how to debug your code yourself."
    m "Or maybe I should tell Roxy to deal with you somehow."
    "Bam!!" with hpunch
    hide malloc eyes2 with dissolve
    "D...Did he just punch me?"
    "Who needs a heap checker when I have my own two eyes?"
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
        "Maybe I should just write a heapchecker...":
            $ malloc_points += 30
            jump shell_prologue_good
        "Maybe I should just give up...":
            "There's no way I forgot a semicolon or something stupid like that."
            "I'm too smart for those kinds of mistakes."
            "..."
            jump shell_prologue_bad

label malloc_epilogue:
    "I have other work to finish anyway, so hopefully this finds the bugs..."
    "..."
    "...."
    "..."
    "Alright, time to test this out..."
    "..."
    "Okay, so my heapchecker says there's something wrong in this part of the memory..."
    "But what could it be...?"
    "Hmm... I'm probably missing something dumb."
    "Maybe I should go ask Malek again."
    scene black
    show text "You find Malek ranting about freeing memory to some frightened freshmen." with dissolve
    pause 2.0
    hide text with dissolve
    scene bg classroom
    show malloc normal with dissolve
    m "Oh, hello [player_name]. What brings you back here?"
    "I wrote a heapchecker, but I still can't figure out my issue."
    m "I see you've learned from your mistakes."
    $ malloc_points += 20
    m "Good for you. Sorry if I was too harsh earlier, but being able to write software that backs you up is very important."
    "Yeah, no worries, I understand."
    m "Let me take a look..."
    m "..."
    m "...."
    m "..."
    m "Ah, I see the issue."
    "Wow, that was fast."
    m "If you look at this part here, when you get rid of this memory block, you're missing a step."
    m "You should be able to figure it out from there."
    m "Good luck!"
    hide malloc normal with dissolve
    jump shell_prologue_good

label shell_prologue_good:
    "Hmm.. what am I forgetting here?"
    "..."
    "...."
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
        "People who forget semicolons probably don't even use Vim, like me, an intellectual.":
            $ vim_user = True
            $ join_stuco = True
            jump shell_intro_bad

label heapcheck:
    show malloc normal with dissolve
    
    m "Looks like you actually know what you're doing."
    m "The number of people who answer \"no\" to that question is astounding."
    m "..."
    m "Well anyway, you may want to check that you're freeing variables."
    m "Memory leaks are one of the most prominent threats to freedom these days."
    m "Everyone wants to take up memory, but no one wants to give it up."
    m "Don't be one of those scummy people, taking what's not yours and refusing to give it up."
    show malloc eyes with dissolve
    m "Free the memory!!" with hpunch
    show malloc normal with dissolve
    m "And don't even get me started on people who double-free their memory."
    m "They're arguably even worse!"
    m "If you give someone too much freedom, they'll never get their work done!"
    m "This is why taking naps in the middle of the day never works!"
    "..."
    m "..."
    m "Sorry about that."
    m "I tend to rant when I talk about things like this."
    m "That should fix your problem, but if not, I have faith in your programming abilities."
    m "Hope this helps!"
    hide malloc normal with dissolve

    "..."
    "What the heck was that?"
    "That guy probably has a few loose screws or something."
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
    m "Are you serious?"
    m "How do you not know what that is?"
    m "Do you not pay attention during lecture or something?"
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
    "What just happened?"
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
            "There's nothing that could possibly be more difficult than that."
            $ join_stuco = True
            jump shell_intro_bad

label shell_intro_bad:
    show shell angry with dissolve
    s "Let me stop you right there. Show me your Vimrc."
    "Huh?"
    s "I heard you bragging about your Vim setup, but you couldn't even get your heapchecker working."
    "How do you know that? And who are you?"
    s "I'm Shell."
    $ s.name = "Michelle"
    s "Malek seemed to be in a pretty bad mood after talking to you, and there's only one way that can happen."
    "(I guess that dude really did have a few loose screws.)"
    "(Imagine only getting angry when other people can't fix their code.)"
    s "Yeah, this Vimrc is kinda fancy, but it's still pretty trash. No wonder your code didn't work."
    "What does having a bad setup have to do with not having working code?"
    s "Damn, you really are clueless, aren't you?"
    show shell normal with dissolve
    s "Maybe you should join my Vim club. Someone like you could clearly use the help."
    "..."
    "(So this girl just showed up in a penguin hoodie, trashed my Vimrc, and now she wants me to join her club?)"
    "(She can't be serious...)"
    "Actually, I think I'll pass."
    show shell angry with dissolve
    s "Hahaha! You thought you had a choice?"
    "(Ah shit, I should have guessed. The ones with the weird hoodies are always like this.)"
    show shell normal with dissolve
    s "See you at 5 in the activity room. If you don't show up, I know where to find you, [player_name]."
    "(Alright, so she knows my name too. This day is going great.)"
    hide shell normal with dissolve
    "(...)"
    $ s.name = "???"
    jump proxy_bad_req_den

label shell_intro_bad2:
    show shell angry with dissolve
    s "Let me stop you right there, [player_name]. What did you just say about Vim?"
    "Uhh.. that it's bad? Why do people even prefer it to other text editors? And how do you know my name?"
    s "You take that back!" with hpunch
    s "You can't go around bashing Vim like this!"
    "(Okay, so this girl is clearly crazy too.)"
    "Alright, I'll keep that in mind."
    "By the way, who are you?"
    s "My name is Shell."
    $ s.name = "Michelle"
    "Cool. I'm gonna go this way now."
    s "You think I'm gonna let you go after you made fun of Vim?"
    "(Shit... She's not gonna slap me or something, is she?)"
    s "I'm signing you up to join my Vim club!"
    "Hold up, hold up. There's a club just for Vim?"
    "Why does that exist?"
    s "You take that back!" with hpunch
    "(Yup, I'm probably gonna get slapped.)"
    s "I'll see you in the activity room at 5. If you don't show up, I'll tell the student council president to expel you!"
    "(Welp, that's definitely worse than getting slapped.)"
    "(This day is going great.)"
    hide shell angry with dissolve
    $ s.name = "???"
    jump proxy_bad_req_den



label shell_intro_good:
    show shell star with dissolve
    s "Did someone say Vim?"
    "Uh...yes?"
    s "No one likes Vim more than I do!"
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
    s "Sorry about that. I've been trying to get people to join my club for a long time, 
        but no one's really interested."
    s "I thought another Vimp like you could help me with finding members."
    if vim_user:
        "(\"Vimp\"? I call myself a Vim connoisseur. I don't think I'm at \"Vimp\" level...)"
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
        s "Here's the club form. Fill it out and put it in the box at the end of the hallway."
        "Why can't I just give it to the student council directly?"
        s "They're typically very busy, so they make Packet deliver up students' requests from that box."
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
    s "So, did you fix the issue with your dynamic memory homework?"
    "..."
    "Yeah, I just forgot a semicolon. Dumb mistakes go brrr.."
    s "Oh, don't worry about that!"
    s "At least you wrote a heapchecker!"
    s "It would have taken much longer if you didn't write one."
    "Hmm, maybe you're right..."
    "..."
    s "..."
    "Ah, here's my form..."
    s "What does it say?"
    "Request denied?"
    s "Huh? Let me see that..."
    s "..."
    s "..."
    s "Hmm, maybe we should go talk to the student council president."
    "Uhh, alright...?"
    "I thought you said they didn't like random people barging in."
    s "Don't worry, Roxy's a good friend of mine. She'll talk to us if I'm with you."
    s "There's gotta be some reason why she would reject your form. Maybe something on here is wrong."
    "..."
    s "Let's go ask her!"
    

    s "Hey, look, she's over there!"
    show shell star with dissolve
    s "Roxy!"
    show shell star at midright with move
    show proxy normal at midleft with dissolve
    p "Oh, hello, Shell. How are you?"
    s "I'm doing great!"
    s "Is that Packet with you?"
    p "Yes, I just returned from the storage closet to refill Packet's food bowl."
    "(So, Packet is a cat...)"
    s "Ah, that makes sense..."
    p "So, who's this with you?"
    show shell normal at midright with dissolve
    s "This is [player_name]. We wanted to ask why you denied their request to join my Vim club."
    p "Oh, you're [player_name]? I wanted to talk to you about something, anyway."
    p "Your club member request got denied? That's odd."
    p "Let's go back to the council room and talk there."

    p "Hmm... let me see..."
    p "Ah, here it is."
    p "Looks like Steven accidentally rejected it."
    p "I'll have to yell at him later..."
    p "Anyway, what I wanted to ask you was..."
    p "Are you interested in joining the student council?"
    p "I know this is very sudden, but you seem to be in good academic standing and have good interpersonal skills."
    p "Malek especially was very impressed by your programming skills."
    s "Oooh that's great! You should definitely join! I've heard it's super fun!"
    s "You also get to plan the school festival!"
    p "That is correct. But keep in mind, it's not all fun."
    p "The student council has to deal with important matters as well."
    p "It will involve a lot of time commitment, but I do believe the rewards are worth it."
    p "So, what do you say?"
    menu:
        "I'm definitely interested!":
            $ proxy_points += 30
            $ join_stuco = True
            p "Great! Let me fill out the relevant paperwork."
        "Actually, I think I'm good. Thanks for the offer.":
            $ shell_points += 30
            p "No worries, I understand."
            p "Let me approve your club membership form, then."
    p "..."
    p "Here you are. I just need your signature at the bottom."
    p "You can take your time to read through it, if you'd like."
    "..."
    "...."
    "..."
    "Hmm, looks good to me."
    p "Great!"
    p "You should be good to go, then."
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
    m "Hello, [player_name], are you doing well?"
    "Yeah, how about you?"
    m "Likewise."
    "So, why'd you ambush me first thing in the morning today?"
    m "There's a friend of mine who'd like to meet you."
    "Oh really? Who?"
    m "Roxy, the student council president. She wants to ask if you're interested in joining the student council."
    menu:
        "(Hmm, I'm not really interested, but I'll hear her out.)":
            "So where is the student council room?"
        "(Yes! Something to add to my LinkedIn profile!)":
            $ proxy_points += 30
            $ malloc_points += 30
            $ join_stuco = True
            "Oooh yes, I'm definitely interested!"
    m "It's just down this way."
    m "..."
    m "Here we are."
    m "Roxy, I've brought [player_name]."
    show malloc normal at midright with move
    show proxy normal at midleft with dissolve
    p "Just a second, I'm trying to get Packet to eat his food."
    p "Come on, Packet. I know this food isn't as good, but if you don't finish it then I can't get you the one you like."
    "Packet" "nyan nyan"
    p "There we go..."
    "Packet" "mrrrroww"
    "(So Packet is a cat...)"
    p "So, [player_name], did Malek tell you why I wanted to talk to you?"
    "Yeah, he said you wanted me to join the student council?"
    "But why me, though?"
    m "I recommended you."
    p "Malek here was pretty outspoken about your interpersonal and technical skills, so I thought I'd ask you to join, since we need an additional member."
    "(Why does this feel like some kind of anime plot...?)"
    p "So, what do you say?"
    if join_stuco:
        $ proxy_points += 30
        "I'd love to join!"
    else:
        "Hmm... I'm not really sure if I want to..."
        "What do I get out of being on the student council?"
        p "You get to help us plan the School Festival."
        "Hmmm....."
        p "You also get free food vouchers for the festival. Does that interest you?"
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
                p "You should be good to go, then."
                hide proxy normal with dissolve
                hide malloc normal with dissolve
                jump stuco_good
            "Actually, I'm good, thanks.":
                p "No worries, I understand."
                p "Enjoy the rest of your day!"
                p "Hopefully, we'll cross paths again in the future."
                hide proxy normal with dissolve
                hide malloc normal with dissolve
                scene black
                show text "A few weeks later..." with dissolve
                pause 1.0
                hide text with dissolve
                jump review_session1
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

label review_session1:

    jump break_time

label proxy_bad_req_den:
    scene black
    show text "A few days later..." with dissolve
    pause 1.0
    hide text with dissolve
    scene bg classroom
    show shell angry with dissolve
    $ s.name = "Michelle"
    s "So, Vim hater, did you submit your club form?"
    "..."
    "...Yes."
    s "Great! Let's go check its status!"
    "(Sigh...)"
    "(Why did life have to turn out this way?)"
    "(If only I never met that Malek dude, I wouldn't be in this mess...)"
    s "Hmm..."
    "What is it?"
    s "It says request denied..."
    "(Yes! This is great!)"
    "Haha, well, if it got denied, then there's nothing else that can be done!"
    show shell normal with dissolve
    s "Nope, we're gonna go talk to the student council president."
    "(Damn, I should've known it wouldn't be that easy!)"
    s "Roxy probably had some reason for rejecting your member form."
    s "We can just ask her directly."
    "(Roxy? Is this the person Malek was talking about?)"
    "(Welp, time to find out how exactly she'll make me \"suffer\"...)"
    s "There she is!"
    s "Roxy! Why did you reject [player_name]'s club member form?"
    show shell normal at midleft with move
    show proxy normal at midright with dissolve
    p "Oh, hello, Shell."
    "Packet" "mrroww!"
    p "Is this [player_name]?"
    p "I actually wanted to talk to you about that."
    p "Malek told me about how much of a troublemaker you are, so I decided to keep a closer eye on you."
    p "Please sign at the bottom of this form."
    "(\"Troublemaker\"? All I did was not write a heapchecker.)"
    "(Is that all it takes to be a troublemaker here?)"
    "..."
    "(Wait a second... \"probationary student council member\")?"
    "You can't make me do that! This has to be against the rules or something!"
    "I refuse!"
    show proxy okawaii at midright with dissolve
    p "How cute."
    p "You do understand that I am the student council president, do you not?"
    p "You have to do whatever I say, or I can get you expelled from this institution."
    p "For I have the power to do so."
    "..."
    "(Ah shit...)"
    "..."
    "(End my suffering...)"
    "(All these idiots with their heapchecker complexities can go to hell for all I care.)"
    show proxy normal at midright with dissolve
    p "Thank you for your cooperation."
    p "I'll see you tomorrow at 3 in the student council office."
    hide proxy normal with dissolve
    show shell normal at center with move
    "..."
    s "Haha, looks like Roxy thought of an even worse punishment for you, Vim hater!"
    "Please stop calling me that."
    s "Have fun suffering!"
    hide shell normal with dissolve
    jump stuco_bad


label vim_club:
    scene black
    show text "The next day..." with dissolve
    pause 1.0
    hide text with dissolve
    scene bg classroom
    "..."
    "I think this is the right room..."
    show shell normal with dissolve
    s "Hey, [player_name]!"
    s "How are you doing?"
    menu:
        "I'm doing well!":
            s "That's great!"
            s "Hopefully you enjoy your first Vim club meeting!"
        "Not that well, actually...":
            s "Oh, I'm sorry to hear that."
            s "Hopefully your first Vim club meeting cheers you up!"
    show shell star with dissolve
    s "Hey, everyone!"
    show shell normal with dissolve
    s "This is our newest member, [player_name]."
    "Uh, ... hello."
    s "Don't be shy!"
    s "All these people like Vim just as much as you and me!"
    "..."
    s "So, before we get started, does anyone remember what the first rule of Vim club is?"
    "Is it..."
    menu:
        "Don't talk about Vim club?":
            $ shell_points += 30
            s "Haha, you're pretty funny!"
        "Write a heapchecker?":
            $ shell_points += 20
            s "Haha, you're pretty funny!"
            s "We don't really need heapcheckers when we use Vim."
        "Have a fancy Vimrc?":
            $ shell_points += 30
            s "Haha, you don't need a fancy Vimrc to join this club."
    show shell normal at right with move
    show rebecca normal at midleft with dissolve
    "Rebecca" "Isn't it to write a cheatsheet?"
    show evelyn normal at midright with dissolve
    "Evelyn" "Wait, but I don't use a cheatsheet for my Vim commands..."
    "Rebecca" "That's pretty zesty, besty. You're too big brained."
    show adb normal at left with dissolve
    "ADB" "Hehe I just stole a cheatsheet from Google..."
    "ADB" "Why do more work when someone else already did the work?" 
    hide rebecca normal with dissolve
    hide evelyn normal with dissolve
    hide adb normal with dissolve
    show shell normal at midleft with move
    show steven normal at midright with dissolve
    "Steven" "I have a question. How do I exit Vim?"
    show shell angry at midleft with dissolve
    s "Steven, what are you doing here?"
    s "Shouldn't you be at the student council meeting?"
    "Steven" "Well, they ran out of food, so I came here instead."
    "Steven" "Have the snacks arrived yet?"
    "Steven" "I could only steal this one cookie from the track team."
    show rebecca normal at left with dissolve
    "Rebecca" "Steven's highkey sus right now..."
    hide rebecca normal with dissolve
    "Who is this guy?"
    s "Steven's {i}supposed{/i} to be the secretary of the student council."
    "Steven" "That is correct, but it's not like many people are joining new clubs right now."
    "Steven" "So I don't really have anything to do there."
    "Steven" "I'd rather come here and flex my fancy Vimrc on you peasants."
    "Wait, hold up."
    "You have a fancy Vimrc, but you don't know how to exit Vim?"
    "Are you serious?"
    s "What are you talking about, Steven?"
    s "Of course people are trying to join clubs right now, it's the start of the semester!"
    s "When was the last time you checked your school email?"
    "Steven" "Uhh..."
    s "That's what I thought."
    s "Now go sit in the Emacs corner while you approve all those member requests."
    "Steven" "(Sigh...)"
    hide steven normal with moveoutright
    show shell normal at center with move
    s "..."
    "Damn, Shell, you almost sound like an actual member of the student council."
    "More so than Steven, anyway."
    "Why did you not join?"
    s "Well, my sister used to run this club, but she let me do it because she needed to focus on applying to jobs before graduation."
    s "She also has a bunch of time management issues..."
    s "So I don't think I'd be able to run the Vim club and be on the student council at the same time."
    menu:
        "Ah, I see.":
            $ shell_points += 10
        "Still, you're doing a great job!":
            $ shell_points += 30
            s "Aw, thanks!"
    s "So, like Rebecca said, having a cheatsheet is going to really save your butt when it comes to Vim."
    s "Unless you're as big brained as Evelyn over here."
    "Rebecca" "That's very pog, Evelyn."
    s "So does anyone have some obscure Vim commands they want to share for other people's cheatsheets?"
    hide shell normal with dissolve
    scene black
    show text "The club members spend some time sharing their favorite obscure Vim commands." with dissolve
    pause 1.5
    hide text with dissolve
    scene bg classroom
    show shell normal with dissolve
    s "Ok, now we're gonna have a pop quiz!"
    "Evelyn" "Awwww...."
    "Rebecca" "Are there prizes?"
    s "You get to bonk Steven."
    show shell normal at midleft with move
    show steven normal at midright with dissolve
    "Steven" "Wait what"
    "Steven" "I did not agree to this."
    s "Yeah well, I just got a message from Roxy saying you're kicked from the student council, so..."
    "Steven" "Huh?"
    "Steven" "I'm literally sitting here approving member requests for them, though."
    s "Too bad."
    "Steven" "Huh..looks like I'll have to crash their next meeting..."
    "ADB" "What does \"bonk\" mean in this context?"
    s "You get to remap Steven's Vimrc key bindings."
    "Steven" "Hold up."
    "Steven" "Wut"
    show adb normal at left with dissolve
    "ADB" "Hahaha!"
    "ADB" "La bomba!"
    hide adb normal with dissolve
    "Steven" "Why is this happening?"
    s "Do you have a better incentive for a pop quiz?"
    "Steven" "..."
    show shell normal at midright with move
    show steven normal at right with move
    show evelyn normal at midleft with dissolve
    "Evelyn" "Can we also actually bonk him?"
    "Evelyn" "Does anyone have an inflatable baseball bat?"
    "This is escalating pretty quickly..."
    #show steven normal at midright with move
    show evelyn normal at center with move
    show rebecca normal at midleft with dissolve
    #show adb normal at left with dissolve
    "Rebecca" "Oh I think I have one."
    "Rebecca" "I can go get it, gimme a few minutes."
    "Steven" "Why do you people find joy in physically hurting me?"
    "Evelyn" "Because hurting you emotionally is bad."
    show adb normal at left with dissolve 
    "ADB" "Good mental health is very poggers."
    hide adb with dissolve
    "Steven" "(Sigh...)"
    "Steven" "Maybe if I didn't wear a cow onesie people wouldn't gang up on me like this..."
    "Steven" "I'm gonna go tell Angela that I'm being bullied."
    "Rebecca" "I found it!"
    "Rebecca" "Let's get this zesty party started!"
    s "Let's start the pop quiz!"
    hide shell normal with dissolve
    hide steven normal with dissolve
    hide evelyn normal with dissolve
    hide rebecca normal with dissolve
    #hide adb normal with dissolve
    scene black
    show text "The club goes through a Vim pop quiz, and Steven gets bonked multiple times." with dissolve
    pause 1.5
    show text "His Vimrc key bindings also get remapped, so overall it's turning out to be a great day for Steven." with dissolve
    pause 1.5
    hide text with dissolve
    scene bg classroom
    show shell normal with dissolve
    "Evelyn" "That was pretty fun!"
    show shell normal at midright with move
    show steven normal at midleft with dissolve
    "Steven" "No, it wasn't."
    "ADB" "Now I have more stuff to put on that cheatsheet I stole haha"
    "ADB" "Time to make a pull request..."
    "Rebecca" "Bonk bonk"
    "Steven" "Looks like I have to spend the next week fixing my key bindings..."
    "Steven" "Coming here may have been a mistake."
    "Evelyn" "What do you mean? This is the best club ever!"
    "Rebecca" "All fax no printer."
    s "Alright everyone, that concludes today's meeting!"
    s "I hope everyone had a great time!"
    s "Except you, Steven. You deserved sitting in the Emacs corner like a delinquent while getting bonked."
    "Steven" "lok"
    s "Now that you're no longer on the student council, do you want to join Vim club instead?"
    "Steven" "(Sigh...)"
    "Steven" "There goes the only leadership experience I could put on my LinkedIn profile..."
    "Just put \"Professional Cow\" or something."
    "That should get you a few interviews."
    "Steven" "..."
    "Steven" "I'm gonna leave before I lose anything else."
    "Steven" "I've probably already lost all my brain cells..."
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
            s "Hopefully our next meeting is more interesting for you, since we'll be planning for the school festival."
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
    jump break_time

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
    p "Hey, Halten."
    p "Is everyone else here yet?"
    "Halten" "Well, everyone except Steven."
    show critical normal at right with dissolve
    "Graff" "Which was definitely expected."
    "Halten" "Oh, and your brother's here taking coffee again, as usual."
    show distr normal at left with dissolve
    "Pax" "What do you mean, \"as usual\"?"
    p "Pax, please just fix your coffee machine."
    "Pax" "See I would, but that requires actual effort."
    "Pax" "My free time is already distributed too thin, you know?"
    p "(Sigh...)"
    hide distr normal with dissolve
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
    scene black
    show text "Roxy goes over some of the menial tasks, which are trivial and left to interpretation by the player." with dissolve
    pause 2.0
    hide text with dissolve
    scene bg classroom
    show proxy normal with dissolve
    show critical normal at right with dissolve
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
    jump break_time

label stuco_bad:
    scene black
    show text "The next day, you make your way to the student council room." with dissolve
    pause 2.0
    hide text with dissolve
    scene bg classroom
    $ stuco_task = -1
    "Hmm... I think this is the right room."
    "Hopefully no one's here, so I don't have to be stuck in this stupid meeting."
    show proxy okawaii with dissolve
    p "Ah, hello troublemaker."
    "Ah shit."
    show proxy normal with dissolve
    p "Let's head in."
    p "If you're lucky, you may be promoted from probationary student today."
    "(What does that mean?)"
    "Packet" "mrroww"
    "Halten" "Heyo!"
    p "Hey, Halten."
    p "Is everyone else here yet?"
    "Halten" "Well, everyone except Steven."
    show critical normal at right with dissolve
    "Graff" "Which was definitely expected."
    "Halten" "Oh, and your brother's here taking coffee again, as usual."
    show distr normal at left with dissolve
    "Pax" "What do you mean, \"as usual\"?"
    p "Pax, please just fix your coffee machine."
    "Pax" "See I would, but that requires actual effort."
    "Pax" "My free time is already distributed too thin, you know?"
    p "(Sigh...)"
    hide distr normal with dissolve
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
    p "Looks like you got lucky, after all."
    "Uh, well... it's better than being a probationary student, no?"
    p "That is correct."
    $ proxy_points += 30
    "Halten" "Wait, hold on. Don't we have to do some kind of vote?"
    "Halten" "Or have some pool of candidates to consider first?"
    "Graff" "Dude, there's literally no one else here."
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
    p "..."
    p "Let's {i}officially{/i} start the meeting now, then."
    p "[player_name], can you take down the meeting notes?"
    "Sure, I can do that, I guess."
    "(This is going surprisingly better than I expected...)"
    p "So, we have quite a bit of tasks to get through today."
    p "I guess the first thing to ask is how the budgeting for the festival is going?"
    "Halten" "I think I already verified most of the club budgets and allocated funds, so we should be good to go on that end."
    "Graff" "Damn, this man just reduced all of his work for the rest of the semester."
    "Halten" "I mean, it's easy to finish my work when I'm not TAing a class and lowering students' grades, Mr. \"Destroyer of Dreams\"."
    "Graff" "..."
    "Graff" "How do you know about that name?"
    "Halten" "hehe"
    p "Can we get back on topic, please?"
    "Graff" "..."
    "Graff" "(Hopefully my middle school chuuni pictures aren't being spread around...)"
    hide proxy normal with dissolve
    hide critical normal with dissolve
    scene black
    show text "Roxy goes over some of the menial tasks, which are trivial and left to interpretation by the player." with dissolve
    pause 2.0
    hide text with dissolve
    scene bg classroom
    show proxy normal with dissolve
    show critical normal at right with dissolve
    p "So the four main things we have to do now are talk to the sysadmin to make sure the WiFi bandwidth is enough for the expected crowd,..."
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
    p "So, [player_name], how was your first student council meeting?"
    p "Don't be like Steven, or I'll have to punish you for real, like Malek wanted."
    p "But if you get your tasks done well, I'll look the other way."
    "Uh...okay?"
    "I'll make sure to finish my tasks while not prancing around in a cow onesie."
    p "I hope that's meant in a good way, haha."
    p "Good luck. I'll see you at our next meeting."
    "Goodbye!"
    hide critical normal with dissolve
    hide proxy normal with dissolve
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
    m "Oh, hello, [player_name]."
    m "How are you doing?"
    "Pretty good, how about you?"
    m "I'm doing well, thank you."
    "Who's this with you?"
    show malloc normal at midright with move
    show calloc normal at midleft with dissolve
    clc "Hello! I'm Kalik!"
    "Nice to meet you, Kalik!"
    "I'm [player_name]!"
    "So, Malek, what are you doing this long weekend?"
    m "I'm on my way to take Kalik to the arcade for family weekend."
    "Oh, that sounds nice!"
    menu:
        "You two have fun!":
            m "Thanks. I hope you enjoy your weekend, as well."
            clc "See you later!"
            hide malloc normal with dissolve
            hide calloc normal with dissolve
            jump second_intro
        "Can I come with you?":
            $ malloc_points += 30
            jump arcade
    
label arcade:
    m "Hmm... I don't see why not."
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
    b "Oh, hello, Malek and [player_name]. Where are you all going today?"
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
    b "Oh, I sure will!"
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
    "..."
    "He should be around here somewhere..."
    "Ah, there he is."
    "Looks like he's getting ready to go somewhere."
    "Hey, Cash!"
    show cache normal with dissolve
    c "Oh, hey, [player_name]."
    c "What's up?"
    "Nothing much."
    "Just glad to finally have some sort of break from classes."
    c "Yeah, I hear you."
    c "I'm about to go get dinner soon, if you want to join?"
    "..."
    "You're getting dinner now? It's only 4."
    c "Yeah, but there's a really good nightclub I want to go to later."
    c "It's tough to get in because it gets crowded quickly, so I wanted to get there early."
    "Oh, that sounds fun!"
    "Sure, I'd be down."
    c "Great!"
    c "Let's take the 61D down this way."
    hide cache normal with dissolve
    scene black
    show text "You and Cash get on the 61D bus down to the Waterfront." with dissolve
    pause 1.5
    hide text with dissolve
    scene bg classroom
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
    "Wut"
    c "The other day, she almost pulled a knife on Buffy when she tried to talk to me."
    "Nani"
    c "Yeah, that was my reaction!"
    "(Are you sure you reacted with \"nani\"?"
    c "She gets way too jealous about these kinds of things."
    c "She's even smiling while she does this, so there's clearly something wrong..."
    c "It's not like I'd start dating Buffy again!"
    "Hold up, you used to date Buffy?"
    "Why'd you break up?"
    c "Uhh..."
    c "It's complicated."
    "Pretty sure it's not as complicated as why you're trying to get away from Faye."
    c "..."
    c "Ok, fair."
    c "Basically, we were both too busy with work to be able to get a relationship to work."
    c "She also felt that I didn't give her enough attention and that I only cared about myself..."
    c "But we're in college, you know? It was hard to care about my grades and be committed to a relationship!"
    c "I don't get how people can make it work so easily during just their freshman year!"
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
    c "Ah, thank you so much!"
    c "I owe you one."
    c "I just need you there for emotional support."
    "(This dude needs more than just emotional support...)"
    c "Maybe if I do it at the school festival, there'll be enough people there that she doesn't go off..."
    "..."
    "Uh, ok."
    "(Terrible plan, but ok.)"
    "(Isn't she more likely to go off if you break up during the festival?)"
    "I guess I can help when I'm free..."
    c "Ah, thank you thank you thank you thank you"
    "Don't worry about it."
    c "Oop, here's our stop!"
    hide cache normal with dissolve
    scene black
    show text "You and Cash enjoy a nice meal at a nearby restaurant and head to the nightclub." with dissolve
    pause 2.0
    hide text with dissolve
    scene bg classroom
    show cache normal with dissolve
    c "Ok, here we are."
    "Decider" "Can I see your ID?"
    c "Here you go."
    "Here's mine."
    "Decider" "..."
    "Decider" "Ok, these are acceptable."
    "Decider" "Enjoy your evening."
    "Thanks!"
    c "Oh, we got here just in time! The show's about to start."
    hide cache normal with dissolve
    show jason normal with dissolve
    "lil mem sbrk" "Yo yo, it's your boi lil mem sbrk here with our opening act for this evening:"
    "lil mem sbrk" "Please welcome [duo_name] to the stage!"
    hide jason normal with dissolve
    "Shalin" "Hey, everyone!"
    "Albert" "I'm Albert, and this is Shalin, and we're [duo_name]!"
    "Shalin" "Hope you all enjoy our song!"
    scene black
    show text "You listen to the opening acts and the rest of the comedy show, and enjoy a night of laughs and fun." with dissolve
    pause 2.0
    hide text with dissolve
    scene bg classroom
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
    "She should be somewhere around the track team area..."
    "Ah, there she is."
    show data normal with dissolve
    d "No no not like that, Root."
    d "You have to make sure your arms don't move when you curl back down."
    "Root" "You mean like this?"
    d "Yeah, that's a lot better!"
    "Root" "Ah, ok. Thanks, captain!"
    d "No prob!"
    d "Oh hey, [player_name]!"
    d "What brings you to this part of campus?"
    "Ah, I was just wandering around and thought that it'd been a while."
    "Are you not doing anything special for family weekend?"
    d "Nah, my family is backpacking through Europe right now, so they can't really come."
    d "So I thought I'd use the extra time to work on getting some good exercise in before the regional track meet."
    "Ooh, that sounds fun!"
    d "Haha yeah!"
    d "I'm hoping I can get the entire team into the top 10 this time."
    "Is that why you're coaching him?"
    d "Oh, yeah."
    d "I don't think you two have met yet!"
    d "[player_name], this is Root. Root, this is [player_name]."
    "Hello!"
    "Root" "Hey!"
    "Those are some pretty impressive biceps!"
    "Are you on the track team too?"
    "Root" "Yeah! I'm trying to make sure I don't just exercise my legs."
    "Ah, that makes sense."
    "Root" "I'm also trying to grow my fitness channel, if you're interested, haha."
    "Root" "Subtle flex."
    "Oh sure, I'll check it out! What's it called?"
    "Root" "It's called \"SaidoChesto22\"."
    "(Hmm...that somehow sounds familiar...)"
    d "So, [player_name], since you're here, do you want to race?"
    "Wut"
    d "Haha, I just want to see how fast you are!"
    "Uh, ok...?"
    d "No pressure!"
    $ data_points += 30
    "Sure, I guess."
    "Though you're probably going to be disappointed."
    d "Nah, don't worry about that!"
    d "I'm sure you're pretty fast!"
    "Alright how do we do this?"
    d "Root, can you do a countdown from 5?" 
    "Root" "Sure!"
    d "(Float like a butterfly, float like a butterfly....)"
    "What's she muttering?"
    hide data normal with dissolve
    "Root" "5!"
    "Root" "4!"
    "Root" "3!"
    "Root" "2!"
    "Root" "1!"
    "Root" "Go!" with hpunch
    "...!"
    "......!"
    "Oh wow, she's pretty fast, but somehow I'm able to keep up!"
    "...!"
    d "Wow, you're pretty quick!"
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
    d "Hey, you really surprised me there!"
    "Well....my lungs....are dead...."
    "Root" "You should be fine if you sit down for a while, but still, that was pretty fast!"
    "I...need some....water...."
    d "Right right, let's head back inside and find a water fountain."
    scene black
    show text "The three of you head inside and find the nearest water fountain to hydrate." with dissolve
    pause 2.0
    hide text with dissolve
    scene bg classroom
    d "Ah, that hits the spot!"
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
    "..."
    "...."
    "...!"
    "Hello!"
    show paperbag life with dissolve
    "Oh, hello."
    "Why are you wearing a paperbag on your head?"
    "???" "Uh..."
    "???" "Why aren't you wearing a paperbag on your head?"
    "Wut"
    "???" "Uno reverse card!"
    "...!"
    "???" "Nah..."
    "???" "I'm trying to see how well I can play violin without looking."
    "..."
    "That sounds difficult..."
    "???" "I'm also trying to practice before I record this for my music channel, so I kinda need the bag."
    "Do you wear that when you record videos too?"
    "(Wow, looks like everyone has a channel for something nowadays...)"
    "???" "Yeah, it started as a joke, but then I just went with it because people thought it was funny, haha."
    "So what song were you playing earlier?"
    "It sounded like the new HIRUASOBI song."
    "???" "Haha, yeah, it was HIRUASOBI."
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
    show data normal with dissolve
    d "Oh, you're back!"
    "Root" "We were gonna go and run a few more laps before coming back inside again, if you wanted to come with us?"
    "Uhhh...."
    "I think that was enough exercise for me for today..."
    "I'm gonna go sit down somewhere."
    d "Haha, no worries!"
    "Root" "See you later!"
    hide data normal with dissolve
    "You have [shell_points] points for shell."
    "You have [data_points] points for data."
    "You have [malloc_points] points for malloc."
    if join_stuco: 
        jump after_break_stuco
    jump after_break_other

label meet_buffy:
    if join_stuco:
        jump after_break_stuco
    jump after_break_other


label after_break_stuco:
    scene black
    show text "A few days later..." with dissolve
    pause 1.0
    hide text with dissolve
    scene bg classroom
    "You have [proxy_points] points for proxy."
    "Ah, that was a nice break."
    "I guess I should actually get to that task I needed to do for the student council."
    "Hmm... let's see..."
    if stuco_task == 0:
        "Ah, I need to go talk to the sysadmin."
        jump sysadmin
    elif stuco_task == 1:
        "Ah, I need to go talk to the cooking club."
        jump cooking_club
    else:
        "Ah, I need to find someone to make festival posters."
        jump gaming_club
    return

label after_break_other:
    scene black
    show text "A few days later..." with dissolve
    pause 1.0
    hide text with dissolve
    scene bg classroom
    "Ah, that was a nice break."
    "I guess I should go take a walk before burying myself in studying for my midterms."
    "..."
    scene black
    show text "You go on a long walk around campus, and find some students working in the park next to the school." with dissolve
    pause 2.0
    hide text with dissolve
    scene bg classroom
    "???" "Wait, what are you doing?"
    "???" "I'm pruning my trees!"
    "???" "No, that's my tree, Minnie!"
    "Minnie" "What...?"
    "???" "Do you see any plums on that one?"
    "Minnie" "..."
    "Minnie" "Ah, shit."
    "Minnie" "Sorry, Harmony."
    "Minnie" "Welp, hopefully I didn't cut off too much..."
    "Harmony" "..."
    "Are you two planting trees?"
    "Harmony" "Oh, hello!"
    "Minnie" "Hello!"
    "Harmony" "We're just maintaining them so that they don't overgrow."
    "Harmony" "But Minnie here gets a bit overexcited when using the pruner..."
    "Minnie" "Hehe"
    "Harmony" "...!"
    "Harmony" "I don't think we've met."
    "Harmony" "I'm Harmony, and this is Minnie."
    "Minnie" "Hello!"
    "Harmony" "So what's your name?"
    "I'm [player_name]! Nice to meet you!"
    "Minnie" "You too!"
    "So what kind of trees are these?"
    "Minnie" "Mine are the plum trees."
    "Minnie" "Harmony's are the decision trees over here."
    "Harmony" "They're called deciduous trees, Minnie."
    "Minnie" "Oops."
    "Minnie" "Anyway, the plums should be ripe soon!"
    "Harmony" "We need to pluck them before the Pigeon Man shows up..."
    "Who's the Pigeon Man?"
    "Minnie" "Sshh! He'll hear you!"
    "What?"
    "How will he hear us? There's no one here."
    show pigeon hole with dissolve
    "Pigeon Man" "Did someone call for me?"
    "Harmony" "Ah shit, he showed up."
    "The plot thickens..."
    "Why does he have a pigeon head?"
    "Harmony" "I'll go get Berry, you two distract him!"
    "Pigeon Man" "Are those fresh plums I see?"
    "Distract him how?"
    "Minnie" "Throw some birdseed at him!"
    "Uhhh..."
    "Oh is this bag it?"
    "Minnie" "Yes! Hurry!"
    "..."
    "Take this!"
    "Pigeon Man" "..."
    "Pigeon Man" "Oh yes. Very delicious."
    "Pigeon Man" "Birdseed very pog."
    "Pigeon Man" "nom nom nom"
    "Minnie" "Ok that should keep him down for a while."
    "(What is happening here?)"
    "(I was not aware that Pigeon people existed...)"
    "Harmony" "Alright, I got Berry!"
    show pigeon hole at right with move
    show berry esseen at left with dissolve
    "Berry-Esseen" "Oh no, not this guy again."
    "Pigeon Man" "nom nom nom"
    "Pigeon Man" "nom nom no-"
    "Pigeon Man" "Oh, hello, Berry."
    "Berry-Esseen" "Pigeon."
    "(What's with all this tension all of a sudden?)"
    "(Something's about to go down, isn't it?)"
    "Berry-Esseen" "..."
    "Pigeon Man" "Oh, you're approaching me?"
    "Pigeon Man" "Instead of violently flinging birdseed at me, you're coming right to me?"
    "Berry-Esseen" "I can't throw you off of school property after beating the shit out of you without getting closer."
    "Pigeon Man" "..."
    "Is this a Jojo's reference?"
    "Pigeon Man" "Oho! Then come as close as you like!"
    "Pigeon Man" "After I get my tasty plums, there's nothing you can do to stop me."
    "..."
    "(I've deviated way too far from the main storyline now.)"
    "(Did I get teleported to Theoretical CS Land?)"
    "(How do I get back to Systems Land?)"
    "Pigeon Man" "Mud-"
    "Berry-Esseen" "Too slow!"
    "Berry-Esseen" "Central Limit Platinum! Tsukure toolkitto o!"
    "Pigeon Man" "Nani!?!"
    "(What the fuck is going on?)"
    "Berry-Esseen" "Yare yare."
    "Isn't that copyrighted?"
    "Berry-Esseen" "If I'd gotten here a few minutes later, he would have powered up with those plums, and never left school property."
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
    "Pigeon Man" "Aalsfsajfakdlmfa;slaw;!!!1!!Lasasfl!"
    hide pigeon hole with dissolve
    "Berry-Esseen" "QED!"
    "Minnie" "That was amazing, Berry!"
    "Berry-Esseen" "Don't worry about it."
    "Berry-Esseen" "I'll go take this guy to the police station, now."
    "Berry-Esseen" "You all be careful, now. You never know what kind of suspicious characters are lurking around out here."
    "(But you seem pretty suspicious to me...)"
    "Berry-Esseen" "Farewell."
    hide berry esseen with dissolve
    "Harmony" "Wow, he protected our trees!"
    "Minnie" "We should celebrate!"
    "Harmony" "[player_name], do you want to help us get the fruits down?"
    "..."
    "Uh, I'm good."
    "(I need to leave before any more weird shit happens...)"
    "See you later."
    "Harmony" "Bye!"
    "Minnie" "See you!"
    "I think I just witnessed a hato crime."
    return
    
label sysadmin:
    scene black
    show text "You make your way to the IT building and find the server room." with dissolve
    pause 1.0
    hide text with dissolve
    scene bg classroom
    "..."
    "Hmm, this seems like the place."
    "Hello?"
    "Ether" "Hello!"
    "Ether" "Are you here from the student council?"
    "Yeah, I'm [player_name]. I'm here to make sure the servers can handle the traffic for the school festival."
    "Ether" "Ok, cool. Roxy sent me an email saying someone would come by."
    "Ether" "Let me go get my colleague."
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
    "FanPu" "Ah, ok. It should be in this folder..."
    "FanPu" "..."
    "FanPu" "Oh shit, this is a pretty high number..."
    "FanPu" "We may need to check the bandwidth before this festival."
    "Ether" "Hmmm..."
    "Ether" "It should be doable if we get a larger router, right?"
    "FanPu" "Hmmm...but do we have the money?"
    "Ether" "(We'd have more money if you didn't waste our funds on Gnostic Impact...)"
    "FanPu" "Or we can implement a better QoS algorithm so that everyone can use the network..."
    "Ether" "Hmmm..."
    "FanPu" "Hmmm..."
    "(What language are they speaking?)"
    "Ether" "I think that would work."
    "Ether" "Can you also stop using our funds for your gatcha addiction?"
    "FanPu" "What do you mean \"addiction\"?"
    "FanPu" "These are 3D waifus, not 2D waifus!"
    "FanPu" "This is clearly worth the money!"
    "Ether" "(Sigh....)"
    "..."
    "Ok so I understood none of that, but do you have it under control?"
    "Ether" "Yeah, I think we should be able to handle the traffic."
    "Ether" "If FanPu stops streaming his games and actually does work for once."
    "FanPu" "Bruh, why do you keep calling me out like this?"
    "FanPu" "If you played this game, you'd understand!"
    "Ether" "I highly doubt that."
    "FanPu" "Rej rej!"
    "Ether" "Anyway, [player_name], you can tell Roxy we've got the situation handled."
    "Alright, sounds good."
    "Ether" "Enjoy the rest of your day!"
    "FanPu" "Noooo I got a Qiqi!!"
    "FanPu" "Wallet-kun doko da?!"
    "Ether" "(Sigh...)"
    "Ether" "You need serious help, man."
    "FanPu" "Nuuuu I need to grind more Freemogems now!"
    "FanPu" "Demo jikan ga nai!!"
    "Ether" "(Sigh...)"
    "Ether" "I'm gonna have to do most of this by myself, aren't I?"
    "Yeah, so I'm just gonna leave now..."
    hide fanpu normal with dissolve
    return

label cooking_club:
    scene black
    show text "After contacting the cooking club, you set up a time to talk during one of their meetings." with dissolve
    pause 1.5
    hide text with dissolve
    scene bg classroom
    "So the club president is someone named Jenny..."
    "I think it's this room, right?"
    "..."
    "Hello? Is Jenny here?"
    "Jenny" "Hewo!"
    "Jenny" "Are you [player_name]?"
    "Yeah, nice to meet you!"
    "Jenny" "Nice to meet you, too!"
    "You got the email from Roxy, right?"
    "Jenny" "The one about event space for the festival, right?"
    "Jenny" "I think we just finalized what we're planning to do, so we should be able to start looking for spaces now."
    "What's the cooking club doing?"
    "Jenny" "Oh, we're planning on doing a maid cafe!"
    "Jenny" "We just finalized the menu too, so we should be good to look at other logistics."
    "Ooh, that sounds fun!"
    "So do you have an expected number of customers?"
    "Jenny" "Yeah, lemme just ask Sandie."
    "Jenny" "Hey, Sandie, can you get the binder for last year's logistics?"
    "Sandie" "Yeah, sure, this bread's about to finish proofing so lemme stick it in the oven first..."
    "Sandie" "..."
    "Sandie" "Ok, there we go."
    "Sandie" "Alright, so last year we had about 400 customers total."
    "Jenny" "We should probably expect that to increase to at most 550 this time."
    "Sandie" "Yeah, that sounds good."
    "Sandie" "Do you know what places on campus can tolerate that crowd?"
    "Sandie" "I don't think a classroom is gonna cut it..."
    "Jenny" "We can also see if hosting outside is an option..."
    "Sandie" "..."
    "I don't think that's a good idea..."
    "I feel like allergies are gonna be a big concern if you host outside."
    "Jenny" "Ah shit, you're right."
    "???" "Sorry guys, my class ran late today!"
    "Jenny" "Oh hey, Maple!"
    "Jenny" "Do you happen to know any good locations on campus that we can use for the maid cafe?"
    "Sandie" "We're thinking we should expect about 550 people this year."
    "Maple" "Oh, if you're talking about that, then you must be [player_name]!"
    "Maple" "Nice to meet you!"
    "Haha, nice to meet you, too!"
    "Maple" "Hmmm... maybe somewhere in Tepper?"
    "Maple" "They have pretty big rooms, don't they?"
    "Jenny" "Oh yeah!"
    "You can probably talk to one of the admins to reserve it in advance."
    "\"beep boop!\""
    "Sandie" "Oh, I think that's my bread. Lemme go check on it."
    "Sandie" "It was nice meeting you, [player_name]!"
    "Maple" "So if we do somewhere in Tepper, we'll have to talk to the storage team to make sure they have enough tables, right?"
    "Jenny" "Yeah, I don't fully know how that process works."
    "I can give it a shot for you."
    "Roxy probably has some connections that we can use for that."
    "Jenny" "Oh, that would be great!"
    "Maple" "Thank you so much!"
    "How many tables do you think you'll need?"
    "Jenny" "Hmm... maybe about 9 or 10? We'll need enough chairs too."
    "Maple" "We can probably reuse the decorations and costumes from last year, so it should just be those two things."
    "Alright, sounds good!"
    "I'll go talk to the storage team, then."
    "Jenny" "Yeah!"
    "Maple" "Thanks for the help!"
    "Jenny" "You should also definitely come by our cafe during the festival if you have the chance!"
    "Yeah, definitely!"
    "I'll see you later!"
    "Jenny" "Bye!"
    "Maple" "See you!"
    return


label gaming_club:
    scene black
    show text "You make your way to the Graphics Lounge to find the contact Roxy provided you with." with dissolve
    pause 1.5
    hide text with dissolve
    scene bg classroom
    "Wow, this place is pretty nice.."
    "???" "Andy, what are you doing? Can you come help gank bot?"
    show andy normal with dissolve
    "Andy" "Bruh I just respawned! Lemme stock up on potion first."
    "???" "How did you die!? Did the chickens kill you?"
    "???" "No, it looks like he went AFK..."
    "???" "Dammit Andy, are you playing Herrscher on your phone while playing Legends again?"
    "Andy" "Legends gets too boring, man."
    "Andy" "No one ever wants to help me kill dragon so there's nothing to do here..."
    "What are they even talking about..."
    "Andy" "I already killed the wolves like five times!"
    "???" "If you'd help us push back, then maybe we'd have time to fight dragon!"
    "Andy" "..."
    "Andy" "Meh..."
    "???" "Oh, I think someone's here, Rae."
    "Rae" "Oh!"
    "Rae" "Gimme a sec, we're about to lose, anyway..."
    "Andy" "Haha gottem"
    "Andy" "I took their turret."
    "Rae" "Wait what"
    "Andy" "Oho we're boutta win now."
    "Rae" "I can't believe you've just done this..."
    "Rae" "Daniel, how is this happening?"
    show daniel normal at left with dissolve
    "Daniel" "He went and hid in a bush and then went AFK."
    hide daniel normal with dissolve
    "Rae" "How did they not catch him I don't understand..."
    "Andy" "I'm just too good at this game."
    "Andy" "Wow we won ez!"
    "Andy" "Peak komedy."
    "Rae" "Alright, don't troll next time, Andy..."
    "Andy" "Oho no promises."
    hide andy normal with dissolve
    "Rae" "..."
    "Rae" "Hello!"
    "Hey! I'm [player_name], I'm here from the student council. Did Roxy send you an email about what she wanted?"
    "Rae" "Oh, yeah. I got it."
    "Rae" "You needed a logo, right?"
    "Rae" "What's the theme for the festival this year?"
    "It's \"Light mode vs. Dark mode\"."
    show daniel normal at midleft with dissolve
    "Daniel" ":thinking:"
    hide daniel with dissolve
    "Rae" "Ooh interesting..."
    "Rae" "Yeah, I can probably come up with a logo for that."
    "Rae" "You just need the SCS dragon to be in it, right?"
    "Rae" "Do you need it by your next meeting?"
    "Yeah, I think the dragon needs to be in it."
    "We don't really need it by our next meeting, but we do need it so that we can send out emails and stuff."
    "No rush though."
    "We also need some poster designs."
    "Rae" "Oh, Daniel, can you make the posters?"
    show daniel normal at midleft with dissolve
    "Rae" "You still have that fancy generative script, don't you?"
    "Daniel" "Yeah, I still have it."
    "Daniel" "I'll probably have to reconfigure it, but it shouldn't take long :thinking:"
    "Daniel" "I can change it later after my Tetris class."
    "Rae" "Alright, sounds good."
    "Wait, you're taking a Tetris class?"
    "Daniel" "No, I'm teaching it actually haha."
    "Damn."
    "That's pretty cool."
    "Is that why you're wearing a Tetris costume?"
    "Daniel" "Yeah, today's their midterm, so I wanted to make the class more fun."
    "Ah ok, haha."
    "Alright, so I guess I'll check back in again to see how the posters and logo are coming along."
    "Rae" "Yeah sounds good!"
    "Daniel" "Pog"
    "Rae" "Maybe Andy will stop trolling us in every Legends game by then."
    show andy normal at right with dissolve
    "Andy" "No chance, this is peak komedy."
    hide andy normal with dissolve
    "Rae" "(Sigh...)"
    hide daniel normal with dissolve
    return

