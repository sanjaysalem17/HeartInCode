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
    scene black
    show text "Here we are again." with dissolve
    pause 1.0
    hide text with dissolve
    show text "You made sure to actually understand the material this time, so you're convinced that you can ace this midterm too." with dissolve
    pause 2.0
    hide text with dissolve
    show text "You get ready and start the test, only to find that..." with dissolve
    pause 1.5
    hide text with dissolve
    show text "Some of these questions are about C libraries that were not taught in class." with dissolve
    pause 1.5
    hide text with dissolve
    show text "Welp. Looks like it's time to pull out the Random Guess Generator." with dissolve
    pause 1.5
    hide text with dissolve 
    show text "Luckily for you, the questions you do know are about forks and spoons and pthreads." with dissolve
    pause 2.0
    hide text with dissolve
    show text "So you're guaranteed at least half of the points now!" with dissolve
    pause 2.0
    hide text with dissolve
    show text "Don't worry though, this midterm is only 10 percent of your final grade in the class. Extra credit go brrrr." with dissolve
    pause 2.5
    hide text with dissolve
    show text "By the time you finish the test, you only have 5 minutes left, so you decide it's better to just leave early and take your nap now." with dissolve
    pause 2.5
    hide text with dissolve
    show text "You get back home and once again crash on the couch. You don't have any assignments due in the near future, so you can destress for a bit." with dissolve
    pause 2.5
    hide text with dissolve
    if join_stuco:
        jump stuco_mtg2
    if join_vimclub:
        jump vim_club2
    jump science_lab

label stuco_mtg2:
    $ proxy_points += 30
    scene black
    show text "After a nice few weeks of destressing, you look forward to your next Student Council meeting." with dissolve
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
    $ shell_points += 30
    scene black
    show text "After a nice few weeks of low stress, you look forward to your next Vim Club meeting, and you head to the meeting room." with dissolve
    pause 1.5
    hide text with dissolve
    scene bg classroom
    show shell normal with dissolve
    s "Hey everyone!"
    s "I hope these past few weeks haven't been too tough on you, with midterms and all."
    show adb normal at right with dissolve
    "ADB" "Midterms are easy gg"
    show rebecca normal at left with dissolve
    "Rebecca" "Alright, Albert, calm down."
    hide adb normal with dissolve
    hide rebecca normal with dissolve
    s "Ok, so we really need to start getting our mini golf booth set up for the Festival."
    show evelyn normal at left with dissolve
    "Evelyn" "I have a very important question."
    "Evelyn" "Where is sus Steven?"
    "..."
    s "..."
    s "Is he not here?"
    s "Hm..."
    s "He might be trying to fight for his position back on the student council."
    s "But he's probably not gonna get it."
    "Evelyn" "Lol"
    show rebecca normal at right with dissolve
    "Rebecca" "Imma bet he's gonna show up here at the very end and complain about Roxy again."
    "Evelyn" "Bet."
    hide rebecca normal with dissolve
    hide evelyn normal with dissolve
    s "..."
    "What is it?"
    s "I completely forgot to get the materials from last year from my sister!"
    "That is... unfortunate."
    s "Does anyone want to come with me to help carry the boards?"
    "Sure, I can come."
    show adb normal at left with dissolve
    "ADB" "wawa I can come too."
    hide adb normal with dissolve
    show rebecca normal at left with dissolve
    show evelyn normal at right with dissolve
    "Rebecca" "Evelyn and I have to finish up some regrade requests, so I think we'll just stay here haha."
    "Evelyn" "Wait, I finished mine already."
    "Rebecca" "Bestie how are you so fast?"
    hide rebecca normal with dissolve
    hide evelyn normal with dissolve
    scene black
    show text "You go with Shell and ADB to find Shell's sister and ask about the prior year's booth materials." with dissolve
    pause 1.5
    hide text with dissolve
    scene bg classroom
    show shell normal at left with dissolve
    s "Hey sis!"
    s "Are you busy right now?"
    show os normal at midright with dissolve
    "Emory" "Uh, I guess I should probably take a break now."
    "Emory" "This kernel is killing my brain cells."
    # show compilers normal at right with dissolve
    "Reg" "Hey, Shell! This SSA is also not fun."
    "Reg" "Watch them make us write this entire thing and then not even use it for the rest of the compiler..."
    "..."
    "ADB" "That sounds kinda stupid."
    "(Clearly these two are going through a bad semester right now.)"
    s "Do you know where the minigolf stuff from last year is?"
    "Emory" "..."
    "Emory" "It should be in a storage locker somewhere in the UC."
    "Emory" "I should have a key somewhere, lemme check."
    s "Thanks!"
    "Reg" "Ok, I'm giving up. This is too much work to do in 2 days. I hate this class."
    "Reg" "Em, I'm gonna go get a coffee, do you want anything?"
    "Emory" "Can you get me a matcha?"
    "Reg" "Sure."
    # hide compilers normal with dissolve
    "Emory" "Ok, I think I got it."
    "Emory" "Here it is."
    s "Thanks!"
    show shell sad at midleft with dissolve
    s "Don't overwork yourself!"
    "Emory" "I'll try, but my schedule is very hectic and does not leave time for breaks."
    "Emory" "Speaking of which, I should get back to kernel."
    "Emory" "See ya!"
    hide os normal with dissolve
    hide shell sad with dissolve 
    scene black 
    show text "You head to the UC to find the storage locker with the minigolf materials." with dissolve
    pause 1.5
    hide text with dissolve
    show text "It turns out to be bigger than you thought, but luckily ADB somehow manages to carry more than half of the panels himself." with dissolve
    pause 2.5
    hide text with dissolve
    show text "You carry the materials back to the club room, and take a break from heavy exercise." with dissolve
    pause 1.5
    hide text with dissolve
    scene bg classroom
    show adb normal at midleft with dissolve
    show shell normal at midright with dissolve
    "ADB" "That was a good workout."
    "I think my arms are broken."
    s "Haha, thanks for the help!"
    show shell star at midright with dissolve
    s "Looks like these panels are already labeled, so we don't need to figure out how to put together each minigolf hole. "
    "ADB" "baba"
    "Where did Rebecca and Evelyn go?"
    "ADB" "I think they had to leave for Office Hours."
    show shell normal at midright with dissolve
    s "Ah, makes sense."
    s "I think we should be good to go for the next meeting, then."
    s "It'll just be setting up the booth, which I don't think will take long if we know what we're doing."
    s "I'll see you guys in a few weeks!"
    "ADB" "Goodbye."
    hide adb normal with dissolve
    menu:
        "See you!":
            hide shell normal with dissolve
        "...":
            $ shell_points += 30
            s "What is it, [player_name]?"
            "Do you have any plans yet for the festival?"
            "Other than the booth, I mean."
            s "Hmm.."
            s "I don't think so?"
            "..."
            "Good to know."
            s "Huh? What's that supposed to mean?"
            "Haha, don't worry about it!"
            "See you!"
            hide shell normal with dissolve
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

label databases:
    scene black
    show text "You make your way to the inventory room to try and get festival supplies for the cooking club." with dissolve
    pause 1.5
    hide text with dissolve
    scene bg classroom
    "I think this is the right room."
    "Is this the Inventory Department?"
    "???" "Yep. What can I help you with?"
    #show Database normal with dissolve
    "Oh, uh, I need some tables and chairs."
    "Do you guys have anything like that?"
    "???" "Let's find out. Hey Storage, can you SELECT some tables and chairs for me?"
    show storage normal at left with dissolve
    "Storage" "Database, you know you don't have to yell everytime you ask a question, right?"
    "Database" "Ah, I'm sorry. I just get so excited when requesting items."
    "Database" "So, do we have the tables and chairs?"
    "Storage" "You're gonna have to be more specific than that."
    "Storage" "I'll check in the back with specific instructions only."
    "Database" "Oh, right. Can you check our supplies WHERE the labels are 'table' or 'chair'?"
    "Storage" "You're so weird. But ok, I can look for that."
    "Storage" "I'll be back."
    hide storage normal with dissolve
    "Database" "While we wait, what do you need a bunch of tables and chairs for?"
    "The cooking club is doing a maid cafe for the school festival."
    "I'm here to make sure they have enough tables and chairs beforehand."
    "Database" "I see. Well, you've come to the right place."
    "Database" "If anyone would have them, it's us."
    "Database" "Oh! Did you see the new Request movie? It's my favorite series."
    "The what? I've never heard of a movie like that."
    "Database" "It's a great franchise about a team requesting items."
    "Interesting."
    "Are the movies good?"
    "Database" "Of course they are! There are so many cool scenes like the one where they SELECT things and-"
    "Oh, uh, I see. And a new one just came out?"
    "Database" "Yep! But now that it's out, they can make plans for the future."
    "Database" "I sure hope they get to work right away on the 'sequel' ;)."
    "..."
    "Let's talk about something else now."
    "Database" "Sure!"
    "So how did you end up working down here?"
    "Database" "Oh, thats quite simple, actually."
    "Database" "I love hanging out with Storage, and asking them to SELECT things."
    "Database" "Not to mention I get to help all the people who come here, which is also great."
    "You like requesting things that much?"
    "Database" "Of course! I love saying SELECT and WHERE and HAVING and-"
    "Storage" "Alright that's enough. I'm back."
    show storage normal at left with dissolve
    "Storage" "I hope Database didn't bother you too much."
    "We had a nice chat."
    "Database" "Did you find out if we have enough tables and chairs?"
    "Storage" "Yep, we got them right here."
    "Storage" "Here you go, uh-"
    "Oh, my name is [player_name]."
    "Storage" "Nice to meet you, [player_name]."
    "Storage" "Here are the item numbers for the tables and chairs."
    "Storage" "I reserved the amount you said you needed, so you can tell the cooking club to come pick them up whenever they want."
    "Nice to meet you too, and thank you for getting these for me."
    "Storage" "No problem."
    "Database" "I hope we see you around! I would love the chance to request more items for you!"
    "I'm sure I'll come back again to request more things in the future. Maybe"
    "See you guys later!"
    "Database" "Bye!!!"
    "Storage" "See ya."
    #hide Database normal with dissolve
    hide storage normal with dissolve
    jump matchmaker


label poker_club:
    scene black
    show text "You make your way to the Poker Club room to discuss the fundraiser for the upcoming festival." with dissolve
    pause 1.5
    hide text with dissolve
    scene bg classroom
    "I think this is the right room."
    "Is Joelle in here?"
    "???" "I think I have you now, Isabella. You'll never win."
    show pnc normal at midright with dissolve
    "Isabella" "Abby, you're not supposed to talk this much during a game of poker."
    show random normal at midleft with dissolve
    "Abby" "I can't help it. Plus, you'll never know if I'm bluffing or not."
    "Isabella" "You are."
    "Abby" "Are you sure?"
    "Isabella" "Yes. I'm all in."
    "Abby" "I'm all in too."
    "Isabella" "Bold move for someone who is bluffing!"
    "Abby" "Since you are so sure, then check this out!"
    "Isabella" "No way."
    "Abby" "Ha! I wasn't bluffing!"
    "Isabella" "No. Way."
    "... Hello...?"
    "Abby" "Looks like I win this time."
    "Isabella" "Agh, you actually beat me."
    "Abby" "Yes!"
    "Abby" "Oh, someone's here."
    "Isabella" "Huh?"
    "Abby" "You're [player_name], right?"
    "Yeah, nice to meet you!"
    "Abby" "Nice to meet you too."
    "Isabella" "At least you're here now. We need help planning for Casino Night."
    "Why do you need my help? I'm just here to make sure your plans are coming along smoothly for the Student Council."
    "Isn't Joelle the club president?"
    "Abby" "Well yes, but Joelle's really been slacking in the planning so far."
    "Isabella" "She pulls all nighters playing MMORPGs and then sleeps all day."
    "Abby" "Classic pro gamer move. I don't understand how she has time to game and still do work for classes."
    "Isabella" "Yes somehow she had the time to secure the club budget and set up financial accounts for the fundraiser. She's too OP."
    #"Abby" "It's what we're doing for the festival!"
    #"Oh, that's really cool! What were you thinking of having there?"
    "Isabella" "Anyway, we basically just need some outside opinions on what games to have going."
    "(Looks like a planning speedrun is happening now...)"
    "Hmm, well, what are your favorite gambling games?"
    "Abby" "Oh! Oh! I love blackjack!"
    "Isabella" "I prefer poker, so I'm able to beat everyone."
    "But didn't you lose that game earlier?"
    "Isabella" "Forget about that game! I usually win."
    "Okay then. Well, we can add those games as a start."
    "What about the dealers for those games?"
    "Isabella" "I wanna deal for the blackjack table, since I won't be able to play poker myself."
    "Isabella" "I'll love watching them lose!"
    "Well, that settles that. Abby, are you gonna deal for poker then?"
    "Abby" "Yeah, I can do that."
    "Has gambling been a popular thing for the festival in the past?"
    "Isabella" "Yeah, it's really popular. We might need more volunteers for managing the games."
    "Abby" "I guess we can try and find some volunteers."
    "Abby" "They could manage a roulette wheel, if we could get our hands on one."
    "Isabella" "Could we even find one?"
    "Abby" "It would be really cool."
    "Abby" "I can try and look into getting one for the festival."
    "Isabella" "I can easily get the cards and chips that people would be using."
    #"Isabella" "What are you going to do to help?"
    "What else does the gambling night need?"
    "Abby" "It could probably use some nice decorations for that extra flair."
    "Isabella" "Maybe Joelle knows if there's anything in storage somewhere. Since the club has thrown a Casino Night before."
    #"It could look like a real casino. Well, as much as we could at the festival, anyway."
    "Abby" "I think that's a great idea!"
    "Isabella" "This Casino Night is going to turn out so well!"
    #"Isabella" "You better come through on that idea."
    "Abby" "Thank you for all of your help!"
    "I'll see you guys later."
    "Abby" "See you later!"
    "Isabella" "Bye."
    hide pnc normal with dissolve
    hide random normal with dissolve
    jump matchmaker

label printing:
    scene black
    show text "You head back to the Graphics Lounge to check on Rae's logos for the festival." with dissolve
    pause 1.5
    hide text with dissolve
    scene bg classroom
    show graphics normal at midleft with dissolve
    show daniel normal at midright with dissolve
    "Rae" "Oh, hey, [player_name]!"
    "Rae" "You have great timing! I have to go to a staff meeting now, so I asked Daniel to help with printing the logos and posters."
    "Rae" "I managed to finish them in time, which is very surprising, haha."
    "Rae" "Sorry, I have to run now since I'm already a few minutes late."
    "Rae" "I gave Daniel all the dimension info, so he should be able to help you. See you!"
    hide graphics normal with dissolve
    show daniel normal at center with move
    "Daniel" "So I had a script that would convert all the files to something printable, but it doesn't work sadly."
    "Did you write the script yourself?"
    "Daniel" "No, I got them from Max and changed them to work for this, but I think the scripts were already broken."
    "Oh. Did you ask him to fix the scripts?"
    "Daniel" "I did, but his sprite hasn't been drawn yet so he can't come and help."
    "Daniel" "He just responded with \"works for me\" and then left me on read."
    "Interesting."
    "Daniel" "I guess we have to go to the printing department now gg."
    hide daniel normal with dissolve
    scene black
    show text "You go to the printing department to find the monitor furiously editing some Python files." with dissolve
    pause 1.5
    hide text with dissolve
    scene bg classroom
    show daniel normal at midright with dissolve
    "Daniel" "Hey, CompPhoto, can you help us print out some posters for the festival?"
    "CompPhoto" "Hold on, hold on. This assignment is due in like 30 minutes."
    "Daniel" "Is this Comp Photo?"
    "CompPhoto" "Perhaps."
    "CompPhoto" "My bilateral filter is still very broken for some unknown reason..."
    "Is it ok if we just print ourselves then?"
    "CompPhoto" "Sure sure. Hmm.. maybe my intensity kernel is wrong..."
    hide daniel normal with dissolve
    scene black
    show text "With some experimentation, you figure out how to calibrate the printer so that you waste the least amount of paper." with dissolve
    pause 2.0
    hide text with dissolve
    show text "Yes, you've just solved a practical optimization problem called MIN-WASTED-SPACE. Good for you!" with dissolve
    pause 1.5
    hide text with dissolve
    scene bg classroom
    show daniel normal at center
    "Daniel" "So if we spread them out like this, I think it should work."
    "Oh, I think we also needed some pins and stickers with the logo."
    "Daniel" "I think stickers aren't too bad, if we use the sticker sheets."
    "Daniel" "We just have to format the logo to fit in a circle."
    "I don't think CompPhoto can help us since she's still busy."
    "CompPhoto" "Yes, now my joint bilateral is broken. Everything is pain."
    "I can probably do it then. Just need some resizing."
    "Daniel" "We should probably order the pins instead of making them manually."
    "Daniel" "Manual labor is pain."
    "Yup."
    "CompPhoto" "Yup."
    "Daniel" "I think we should be good to go then."
    "CompPhoto, do you have a good site for pin ordering?"
    "CompPhoto" "Uhh.. they should all be on that sheet over there."
    "Ah, ok. I can place an order through the first site after I edit the logos."
    "Daniel" "Sounds good."
    "Daniel" "I'll let you know once the posters are finished being printed."
    "Alright."
    "Good luck on your Comp Photo assignment, CompPhoto."
    "CompPhoto" "aaaaaaaaaa"
    "Daniel" "Those do not sound like good noises lol."
    "CompPhoto" "My joint bilateral finally works! Time to do detail transfer."
    "CompPhoto" "Someone give me an epsilon value."
    "Uh.."
    "Daniel" "Uh.."
    "CompPhoto" "Nevermind, numpy probably has something built in..."
    "..."
    "Ok, I guess we're all good then?"
    "See you!"
    "Daniel" "Bye!"
    hide daniel normal with dissolve
    jump matchmaker

label matchmaker:
    scene black
    show text "A few days later..." with dissolve
    pause 1.0
    hide text with dissolve
    show text "While aimlessly walking around campus, you come across an intriguing table in the UC." with dissolve
    pause 2.0
    hide text with dissolve
    show text "Also, PSA. Go take a walk. Overworking yourself is not a good plan." with dissolve
    pause 2.5
    hide text with dissolve
    scene bg classroom
    "???" "Hey! Are you interested in finding out who your best match is?"
    "Are you talking to me?"
    "???" "Yup! What's your name?"
    "Uh, I'm [player_name]."
    "???" "I'm ParenLab! Nice to meet you!"
    "ParenLab" "So, are you interested in matchmaking?"
    "Sure, but it this a bit late?"
    "Valentine's Day already happened."
    "ParenLab" "Huhuhuhu. What a simpleton."
    "ParenLab" "Love has no expiration date!"
    "..."
    "Sounds like a line out of a romance manga."
    "ParenLab" "Just stick your hands out and I'll run it through my matchmaker algorithm."
    "Interesting."
    "ParenLab" "Weewooweewoo"
    "What are those noises?"
    "ParenLab" "It's for extra flair!"
    $ match = ''
    if proxy_points > shell_points:
        if proxy_points > malloc_points:
            if proxy_points > attack_points:
                if proxy_points > data_points:
                    $ match = 'Roxy'
                else:
                    $ match = 'Bitsy'
            else:
                if attack_points > data_points:
                    $ match = 'Buffy'
                else:
                    $ match = 'Bitsy'
        else:
            if malloc_points > attack_points:
                if malloc_points > data_points:
                    $ match = 'Malek'
                else:
                    $ match = 'Bitsy'
            else:
                if attack_points > data_points:
                    $ match = 'Buffy'
                else:
                    $ match = 'Bitsy'
    else:
        if shell_points > malloc_points:
            if shell_points > attack_points:
                if shell_points > data_points:
                    $ match = 'Shell'
                else:
                    $ match = 'Bitsy'
            else:
                if attack_points > data_points:
                    $ match = 'Buffy'
                else:
                    $ match = 'Bitsy'
        else:
            if malloc_points > attack_points:
                if malloc_points > data_points:
                    $ match = 'Malek'
                else: 
                    $ match = 'Bitsy'
            else:
                if attack_points > data_points:
                    $ match = 'Buffy'
                else: 
                    $ match = 'Bitsy'
    scene black
    show text "As you wait for this fancy algorithm to compute your best match, you reminisce about the experiences you've had this semester." with dissolve
    pause 2.5
    hide text with dissolve
    show text "You're glad to have met so many cool people here, even if some of them were weirder than others." with dissolve
    pause 1.5
    show text "Even so, it's been a good semester." with dissolve
    pause 1.0
    show text "Okay you're right, I may be stalling. We now return to our regularly scheduled program." with dissolve
    pause 2.0
    hide text with dissolve
    scene bg classroom
    "ParenLab" "Alright, looks like it's done!"
    "ParenLab" "Drum roll please!"
    "Uh..."
    "ParenLab" "dadadadadadadada"
    "ParenLab" "Your best match is [match]!"
    "ParenLab" "I think you two would make a cuwute couple!"
    "(Damn... that algorithm was a bit too accurate...)"
    "Haha, thanks!"
    "ParenLab" "Thanks for stopping by!" 
    "No problem! It was pretty fun."
    if join_stuco:
        jump proxy_asleep
    jump handin_malloc

label handin_malloc:
    scene black
    show text "In all of the confusion that has happened in the past few weeks, you forgot that MallocLab Final is due tonight." with dissolve
    pause 1.5
    hide text with dissolve
    show text "Spring Break also starts this weekend! You've already planned out a Las Vegas trip with some of your friends, which you're looking forward to." with dissolve
    pause 2.5  
    hide text with dissolve
    show text "Don't worry. For the sake of plot, you don't have to suffer through trying to finish MallocFinal before tomorrow, because you frontload all of your schoolwork." with dissolve
    pause 2.5
    hide text with dissolve
    show text "In other words, you're already done! Imagine that." with dissolve
    pause 1.5
    show text "Where did you find the time to optimize your implementation?" with dissolve
    pause 1.5
    hide text with dissolve
    show text "No, seriously. I need to know." with dissolve
    pause 1.0
    hide text with dissolve
    show text "Anyway, enjoy your Spring Break!" with dissolve
    pause 1.0
    hide text with dissolve
    show text "And with that, we come to the end. Of Part 1." with dissolve
    pause 1.5
    hide text with dissolve
    show text "Part 2 of this insanely twisty (and possibly low quality) visual novel dating sim will come out Soon TM." with dissolve
    pause 1.5
    hide text with dissolve
    show text "Whenever I have time to write it :P" with dissolve
    pause 1.0
    hide text with dissolve
    show text "Thanks for playing!" with dissolve
    pause 4.0
    hide text with dissolve
    return

