define d = Character("Bitsy")
define a = Character("Buffy")
define b = Character("Faye")
define gdb = Character("Blake")
define m = Character("Malek")
define c = Character("Cash")
define clc = Character("Kalik")
define s = Character("Shell")
define p = Character("Roxy")


label midterm2:
    if join_stuco:
        jump stuco_mtg2
    if join_vimclub:
        jump vim_club2
    jump science_lab

label stuco_mtg2:
    scene black
    show text "After a rough few weeks of work overload, you look forward to your next Student Council meeting." with dissolve
    pause 1.5
    hide text with dissolve
    scene bg classroom
    show proxy normal with dissolve
    p "Hello, [player_name]. How have you been doing?"
    "Welp, work is hard. Midterms are hard. Everything is hard."
    show reduction normal at left with dissolve
    "Halten" "I can confirm this is facts. Everything is NP-hard."
    "What?"
    show critical normal at right with dissolve
    "Graff" "I'm surprised he didn't say everything was trivial."
    "Halten" "I don't always say that, alright?"
    "How have you all been?"
    "Graff" "Everything is hard."
    "Packet" "nyan nyan"
    p "Same. But now all of my midterms are over, so it's not as stressful."
    p "Anyway, we have a few more things to discuss before the festival preparations kick up."
    p "Did you all finish the tasks you were assigned?"
    hide critical normal with dissolve
    hide reduction normal with dissolve
    show proxy normal at right with move
    show steven normal at left with dissolve
    "Steven" "What's up, losers?"
    p "..."
    "Graff" "You're the real loser here, Steven."
    "Halten" "That is also facts."
    p "Why are you here? Did you not get the email I sent you?"
    "Steven" "Well yes, but why would I just consent to being kicked out?"
    "Steven" "I have to at least defend myself."
    "Graff" "Yeah, but it's been like over a month since we kicked you out."
    "Halten" "Unfortunately, the regrade request deadline has passed."
    "Steven" "What does that even mean?"
    p "It means we're not letting you back in."
    "Steven" "Yo what"
    "Steven" "I just missed a few meetings!"
    "Steven" "It's not like I missed anything big!"
    "Halten" "No one tell him."
    "Packet" "nyan nyan"
    "Steven" "..."
    p "..."
    p "You forgot to do a lot of paperwork."
    "Steven" "Wha-"
    p "Graff had to cover for you."
    p "If it wasn't done, half of the clubs wouldn't have any funding for the festival."
    "Steven" "Wai-"
    p "Even [player_name] did more work than you despite being a completely new member."
    p "We're back on track now, but we don't have any space in the council for a lazy member who doesn't pull their own weight."
    p "Go have fun sitting in the corner of the Vim club."
    p "I told Shell to give you some extra punishment while you're there."
    "Halten" "(Oof.)"
    "Steven" "Then maybe I just won't go to Vim club, then!"
    "(That's what he got out of that reprimanding?)"
    p "Up to you."
    p "But remember, the student council is in charge of academic transcripts."
    p "Don't be surprised if your GPA tanks."
    "(Doesn't that seem a bit too cruel?)"
    "Packet" "purr purr"
    "Steven" "Lok"
    "Steven" "I'm gonna go tell my advisor I'm being bullied."
    "Steven" "This is a toxic environment now."
    hide steven normal with dissolve
    show proxy normal at center with move
    show reduction normal at left with dissolve
    show critical normal at right with dissolve
    "Halten" "I can't tell if he took that well or badly."
    "Graff" "I expected him to overreact a bit more."
    "..."
    p "Anyway, as I was saying before, did you all finish your tasks?"
    if stuco_task == 0:
        "Yeah, the sysadmin team made sure they'd verify the network specs before the festival, and buy any additional routers if they needed to."
        "I think we should be good on that end."
        "Graff" "I asked the person you mentioned about making a festival logo, and she said she could probably do it in time."
        "Graff" "I can go check in with her to see if she needs help printing out posters, too. Seems trivial"
        "Halten" "The cooking club has most of their utensils and materials ready for the cafe, but they're not sure about tables and chairs."
        "Halten" "We may need someone to go talk to the inventory management department."
        p "Ok cool. The only new task I have is that we need to go check on how the Poker club's Casino Night preparations are going."
        "Graff" "Is that what they're doing for the festival fundraiser?"
        p "Yup."
        "Graff" "Sounds dope."
        "Packet" "nyan nyan"
        "Halten" "Watch half the school get exposed for having a gambling addiction."
        p "So what tasks do you two want, [player_name] and Halten?"
        menu:
            "I can go talk to the Poker club.":
                $ stuco_task = 0
                p "Ok, sounds good."
                p "Halten, can you check in with the inventory department?"
                "Halten" "Sure."
                p "Alright, cool."
            "I can go talk to the inventory department.":
                $ stuco_task = 1
                p "Ok, sounds good."
                p "Halten, can you check in with the Poker club?"
                "Halten" "Sure."
                p "Alright, cool."
    elif stuco_task == 1:
        "The cooking club has most of their utensils and materials ready for the cafe, but they're not sure about tables and chairs."
        "We may need someone to go talk to the inventory management department."
        "Halten" "Yeah, the sysadmin team made sure they'd verify the network specs before the festival, and buy any additional routers if they needed to."
        "Halten" "I think we should be good on that end."
        "Graff" "I asked the person you mentioned about making a festival logo, and she said she could probably do it in time."
        "Graff" "I can go check in with her to see if she needs help printing out posters, too. Seems trivial"
        p "Ok cool. The only new task I have is that we need to go check on how the Poker club's Casino Night preparations are going."
        "Graff" "Is that what they're doing for the festival fundraiser?"
        p "Yup."
        "Graff" "Sounds dope."
        "Packet" "nyan nyan"
        "Halten" "Watch half the school get exposed for having a gambling addiction."
        p "So what tasks do you two want, [player_name] and Halten?"
        menu:
            "I can go talk to the Poker club.":
                $ stuco_task = 0
                p "Ok, sounds good."
                p "Halten, can you check in with the inventory department?"
                "Halten" "Sure."
                p "Alright, cool."
            "I can go talk to the inventory department.":
                $ stuco_task = 1
                p "Ok, sounds good."
                p "Halten, can you check in with the Poker club?"
                "Halten" "Sure."
                p "Alright, cool."
    else:
        $ stuco_task = 2
        "I asked the person you mentioned about making a festival logo, and she said she could probably do it in time."
        "I can go check in with her to see if she needs help printing out posters, too."
        "Halten" "The cooking club has most of their utensils and materials ready for the cafe, but they're not sure about tables and chairs."
        "Halten" "We may need someone to go talk to the inventory management department."
        "Graff" "Yeah, the sysadmin team made sure they'd verify the network specs before the festival, and buy any additional routers if they needed to."
        "Graff" "I think we should be good on that end."
        p "Ok cool. The only new task I have is that we need to go check on how the Poker club's Casino Night preparations are going."
        "Graff" "Is that what they're doing for the festival fundraiser?"
        p "Yup."
        "Graff" "Sounds dope."
        "Packet" "nyan nyan"
        "Halten" "Watch half the school get exposed for having a gambling addiction."
        p "So, Halten, can you go talk to the inventory department?"
        p "Graff, you can take the Poker club."
        "Halten" "Sounds good."
        "Graff" "Trivial."
        p "Alright, cool."
    p "I guess that concludes this meeting."
    p "I'll check back in with all of you to make sure your assignments are going smoothly."
    "Graff" "See you!"
    "Halten" "Bye!"
    "Packet" "meow"
    hide critical normal with dissolve
    hide reduction normal with dissolve
    hide proxy normal with dissolve
    jump stuco_tasks2

label stuco_tasks2:
    if stuco_task == 0:
        jump poker_club
    elif stuco_task == 1:
        jump databases
    else:
        jump printing

label vim_club2:
    jump matchmaker

label science_lab:
    scene black
    show text "On your way home from the midterm, you hear a loud explosion from the Science building." with dissolve
    pause 1.5
    hide text with dissolve
    show text "Worried that something bad may have happened in some kind of fight between two students, you head over to check it out."
    pause 2.0
    hide text with dissolve
    scene bg classroom
    "???" "If you say that one more time, name, I'm gonna throw this at you."
    "???" "What's wrong with strong induction, name?"
    "???" "All you're doing is combining random stuff together."
    "???" "Aaaahhhh!"
    "THUD" with hpunch
    "..."
    "???" "Why are you mad? You know I'm right."
    "???" "You can't just n choose 2 your way out of this!"
    "???" "You have to use strong induction!"
    "???" "How does that even make sense in this situation?"
    "???" "You can't just say strong induction for everything!"
    "???" "You've activated my trap card!"
    "???" "Here goes my induction hypothesis!"
    "..."
    "THUD" with hpunch
    "Aight, Imma head out. This is too degenerate for me."
    jump matchmaker

label printing:
    jump matchmaker

label matchmaker:
    return