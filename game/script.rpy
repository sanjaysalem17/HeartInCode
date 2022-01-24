# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define d = Character("Bitsy")
define m = Character("Malek")
define s = Character(name="???")
define p = Character("Roxy")

init:
    $ player_name = ""
    $ join_stuco = False
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg nighttime

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    $ player_name = renpy.input("What is your name?", length=32)
    $ player_name = player_name.strip().capitalize()
    show malloc normal with moveinright
    $ vim_user = False
    # These display lines of dialogue.

    m "Hello, [player_name]."
    m "I heard you had some issues with your dynamic memory homework."
    m "I can take a look at it, but you'll need to answer my question first."
    
    show malloc eyes with dissolve
    m "Did you write a heap checker?"
    menu:
        "Yes.":
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
    "Hmm... my code still doesn't seem to work."
    "What the heck am I doing wrong here?"
    "..."
    
    menu:
        "Maybe I should just write a heapchecker...":
            jump shell_prologue_good
        "Maybe I should just give up...":
            "There's no way I forgot a semicolon or something stupid like that."
            "I'm too smart for those kind of mistakes."
            "..."
            jump shell_prologue_bad

label shell_prologue_good:
    "I have other work to finish anyway, so hopefully this finds the bugs..."
    "..."
    "...."
    "..."
    "Alright, time to test this out..."
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
            jump shell_intro_bad2
        "People who forget semicolons probably don't even use Vim, like me, an intellectual.":
            $ vim_user = True
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
    "..."
    m "..."
    m "Sorry about that."
    m "I tend to rant when I talk about things like this."
    m "That should fix your problem, but if not, I have faith in your programming abilities."
    m "Hope this helps!"
    hide malloc normal with dissolve

    "..."
    "What the heck was that?"
    "That guy probably has a few screws loose or something."
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
    m "All you \"pro-gamer\" scum are the same. Thinking you can get by watching recordings at 2x speed." 
    show malloc eyes with dissolve
    m "You may be happily cruising along now, but just wait until my buddy Roxy really makes you suffer."
    show malloc eyes2 with dissolve
    m "I look forward to seeing how that turns out."
    m "See you at the final exam."

    hide malloc eyes2 with dissolve

    "..."
    "What just happened?"
    "And who the fuck is Roxy?"
    "Am I supposed to be scared?"
    "..."
    "Nah, if I can sleep during lectures and still keep my A, there's nothing to be afraid of."
    menu:
        "After all, I don't use Vim.":
            $ vim_user = False
            $ join_vimclub = True
            jump shell_intro_bad2
        "After all, I set up my own fancy Vimrc all by myself.":
            "There's nothing that could possibly be more difficult than that."
            $ join_vimclub = True
            jump shell_intro_bad

label shell_intro_bad:
    show shell angry with dissolve
    s "Let me just stop you right there. Show me your Vimrc."
    "Huh?"
    s "I heard you bragging about your Vim setup, but you couldn't even get your heapchecker working."
    "How do you know that?"
    s "Miles seemed to be in a pretty bad mood after talking to you, and there's only one way that that can happen."
    "(I guess that dude really did have a few screws loose.)"
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
    jump proxy_bad_req_den

label shell_intro_bad2:
    show shell angry with dissolve
    s "Let me just stop you right there, [player_name]. What did you just say about Vim?"
    "Uhh.. that it's bad? Why do people even prefer it to other text editors? And how do you know my name?"
    s "You take that back!" with hpunch
    s "You can't just go around bashing Vim like this!"
    "(Okay, so this girl is clearly crazy too.)"
    "Alright, I'll keep that in mind."
    s "You think I'm just gonna let you go after you made fun of Vim?"
    "(Shit... She's not gonna slap me or something, is she?)"
    s "I'm signing you up to join my Vim club!"
    "Hold up, hold up. There's a club just for Vim?"
    "Why does that exist?"
    s "You take that back!" with hpunch
    "(Yup, I'm probably gonna get slapped.)"
    s "I'll see you in the activity room at 5. If you don't show up, I'll tell the student council president to expell you!"
    "(Welp, that's definitely worse than getting slapped.)"
    "(This day is going great.)"
    hide shell angry with dissolve
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
            s "So, what do you say? Do you want to join my club?"
        "Likewise.":
            s "So, what do you say? Do you want to join my club?"
    menu:
        "Sure!":
            $ join_vimclub = True
            show shell star with dissolve
            s "Oh that's great! I'll give you a club form, just give me a second..."
            show shell star at midleft with move
        "Nah, I'm good.":
            $ join_vimclub = False
            show shell sad with dissolve
            s "Aw man, another rejection..."
            s "Why does no one want to join? "
            show shell sad at midleft with move
    show data normal at midright with dissolve
    d "Shell, you're gonna be late for class!"
    show shell normal at midleft with dissolve
    s "Oh shoot, I gotta run!"
    if join_vimclub:
        s "Here's the club form. Fill it out and put it in the box at the end of the hallway."
        "Why can't I just give it to the student council directly?"
        s "They're typically very busy, so they make Packet deliver all their stuff to them from that box."
        s "Just so that they don't get too many people trying to talk to them all day."
        "(Who's Packet?)"
    s "See you later, [player_name]!"
    hide shell normal with dissolve
    hide data normal with dissolve
    "..."
    "The people here just keep getting weirder and weirder."
    if join_vimclub:
        jump proxy_good_req_den
    else:
        jump proxy_join_stuco

label proxy_good_req_den:
    # the next day
    show shell normal with dissolve
    s "Hey, [player_name]! Did you submit your club form?"
    "Yeah, I'm just going to check it now."
    s "Cool, I'll come with you!"
    s "So did you fix your issue with your dynamic memory homework?"
    "..."
    "Yeah, I just forgot a semicolon. Dumb mistakes go brrr.."
    s "Oh don't worry about that!"
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
    "I thought you said they don't like random people barging in, though."
    s "Don't worry, Roxy's a good friend of mine. She'll talk to us if I'm with you."
    s "There's gotta be some reason why she would reject your form, though. Maybe something on here is wrong."
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
    p "Yes, I just came back from the storage closet to refill Packet's food bowl."
    "(So Packet is a cat...)"
    s "Ah, that makes sense..."
    p "So, who's this with you?"
    show shell normal at midright with dissolve
    s "This is [player_name]. We wanted to ask you why his request to join my Vim club got denied."
    p "Oh, you're [player_name]? I wanted to talk to you about something, anyway."
    p "Your club member request got denied? That's odd."
    p "Let's go back to the council room and talk there."

    p "Hmm... let me see..."
    p "Ah, here it is."
    p "Hmm... looks like Steven accidentally rejected it."
    p "I'll have to yell at him later..."
    p "Anyway, what I wanted to ask you was..."
    p "Are you interested in joining the student council?"
    p "I know this is very sudden, but you seem to be in good academic standing, and have good interpersonal skills."
    p "Malek especially was very impressed by your programming skills."
    s "Oooh that's great! You should definitely join! I've heard it's super fun!"
    s "You also get to plan the school festival!"
    p "That is correct. But keep in mind, it's not all fun."
    p "The student council does have to deal with important matters as well."
    p "It will involve a lot of time committment, but I do believe the rewards are worth it."
    p "So, what do you say?"
    menu:
        "I'm definitely interested!":
            $ join_stuco = True
            p "Great! Let me fill out the relevant paperwork."
        "Actually, I think I'm good. Thanks for the offer.":
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
    if not join_stuco: 
        jump vim_club
    return
    

label proxy_join_stuco:
    show malloc normal with dissolve
    m "Hello, [player_name], are you doing well?"
    "Yeah, how about you?"
    m "Likewise."
    "So why'd you ambush me first thing in the morning today?"
    m "Haha, there's a friend of mine who'd like to meet you."
    "Oh really? Who?"
    m "Roxy, the student council president. She wants to ask you if you're interested in joining the student council."
    menu:
        "(Hmm, I'm not really interested, but I'll hear her out.)":
            "So where is the student council room?"
        "(Yes! Something to add to my LinkedIn profile!)":
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
        "I'd love to join!"
    else:
        "Hmm... I'm not really sure if I want to..."
        "What do I get out of being on the student council?"
        p "You get to help us plan the School Festival."
        "Hmmm....."
        p "You also get free food vouchers for the festival. Does that interest you?"
        menu:
            "Yes!":
                $ join_stuco = True
                p "Great!"
            "Yes! (but it's the second option)":
                $ join_stuco = True
                p "Great!"
            "Actually, I'm good, thanks.":
                p "No worries, I understand."
    
    if join_stuco: 
        p "Let me get the paperwork sorted out, then."
    else:
        p "Let me approve your club membership form, then."
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
    if not join_stuco: 
        jump vim_club
    return




label proxy_bad_req_den:
    show shell angry with dissolve
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
    return


label vim_club:
    return

    

