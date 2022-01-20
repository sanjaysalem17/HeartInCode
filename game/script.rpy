# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Malek")
define s = Character(name="???")
define p = Character("Roxy")

init:
    $ player_name = ""
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
    m "A Segmentation Fault is too kind of a punishment for scum like you."
    m "Come back when you've learned how to debug your code yourself."
    m "Or maybe I should tell Roxy to deal with you somehow."
    "Bam!!" with hpunch
    hide malloc normal with dissolve
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
    m "I look forward to seeing how that turns out."
    m "See you at the final exam."

    hide malloc eyes with dissolve

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
    "(Shit... She's not gonna slap me or something right?)"
    s "I'm signing you up to join my Vim club!"
    "Hold up, hold up. There's a club just for Vim?"
    "Why does that exist?"
    s "You take that back!" with hpunch
    "(Yup, I'm probably gonna get slapped.)"
    s "I'll see you in the activity room at 5. If you don't show up, I'll tell the student council president!"
    "(Yeah, that's definitely worse than getting slapped.)"
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
    show malloc normal at midright with dissolve
    m "Shell, you're gonna be late for class!"
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
    hide malloc normal with dissolve
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
    s "Don't worry, Roxy's a good friend. She'll talk to us about this."
    s "There's gotta be some reason why she personally would reject your form, though. It's probably important."
    s "Since this apparently didn't go through Steven."
    "..."
    s "Let's go talk to her!"
    

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
    p "Oh, you're [player_name]? I wanted to talk to you about something anyway."
    p "Let's go back to the council room and talk there."
    return

label proxy_join_stuco:
    $ join_stuco = False
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
    p "Malek here was pretty outspoken about your interpersonal skills, so I thought I'd ask you to join, since we need an additional member."
    "(Why does this feel like some kind of anime plot...?)"
    p "So, what do you say?"
    if join_stuco:
        "I'd love to join!"
    else:
        "Hmm... I'm not really sure if I want to..."
        "What do I get out of being on the student council?"
        p "You get to help us plan the Tech Festival."
        "Hmmm....."
        p "You also get free food at council meetings. Does that interest you?"
        menu:
            "Yes!"
            "Yes, but it's the second option."
        
    p "Great!"
    p "Let me get the paperwork sorted out."
    p "(Damn that Steven, he's probably off stealing food from other clubs somewhere...)"
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
    s "Nope, we're gonna go talk to the student council president."
    "(Damn, I should've known it wouldn't be that easy!)"
    s "Roxy probably had some reason for rejecting your member form."
    s "We can just ask her directly."
    "(Roxy? Is this the person Malek was talking about?)"
    "(Welp, time to find out how exactly she'll make me \"suffer\"...)"
    return



    

