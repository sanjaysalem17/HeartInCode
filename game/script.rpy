# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Miles Locke")
define s = Character(name="???")

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
    "Bam!!" with vpunch
    hide malloc normal with dissolve
    "D...Did he just punch me?"
    "Who needs a heap checker when I have my own two eyes?"
    "Whatever. That guy needs serious help..."
    jump debug_code

label debug_code:
    # few hours later
    "Hmm... my code still doesn't seem to work."
    "What the heck am I doing wrong here?"
    "..."
    "There's no way I forgot a semicolon or something stupid like that."
    "I'm too smart for those kind of mistakes."
    "People who forget semicolons probably don't even use Vim, like me, an intellectual."
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
    "Well, this is what I get for not using Vim."
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
    m "You may be happily cruising along now, but just wait until my buddy Proxy really makes you suffer."
    m "I look forward to seeing how that turns out."
    m "See you at the final exam."

    hide malloc eyes with dissolve

    "..."
    "What just happened?"
    "And who the fuck is Proxy?"
    "Am I supposed to be scared?"
    "..."
    "Nah, if I can sleep during lectures and still keep my A, there's nothing to be afraid of."
    "After all, I set up my own fancy Vimrc all by myself."
    "There's nothing that could possibly be more difficult than that."
    jump shell_intro_bad
    

label shell_intro_good:
    s "Did someone say Vim?"
    "Uh...yes?"
    s "No one likes Vim more than I do!"
    s "Do you want to join my Vim club?"
    "(Vim \"club\"?)"
    "(Why is there a club focusing entirely on a text editor?)"
    "(Is everyone here this crazy?)"
    s "So, what do you say?"
    "Wait, but I don't even know you!"
    s "..."
    s "Sorry about that. I've been trying to get people to join my club for a long time, 
        but no one's really interested."
    s "I guess everyone's using different editors now."
    "..."
    $ s.name = "Michelle Tausch"
    s "Anyway, I'm Michelle, but you can call me Shell. What's your name?"
    "I'm [player_name]."
    s "Well, nice to meet you, [player_name]!"
    menu:
        "Nice to meet you too!":
            s "So, what do you say? Do you want to join my club?"
        "Likewise.":
            s "So, what do you say? Do you want to join my club?"
    menu:
        "Sure!":
            s "Oh that's great! I'll email you the info, hang on a second."
        "Nah, I'm good.":
            s "Aw man, I failed again..."
    "Also, what's with the penguin hoodie?"
    "Are you some kind of penguin enthusiast?"
    s "Well, that's because..."
    m "Sheryl, you're gonna be late for class!"
    s "Oh shoot, I gotta run! See you later, [player_name]!"
    "..."
    "The people here just keep getting weirder and weirder."
    return

label shell_intro_bad:
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
    s "Maybe you should join my Vim club. Someone like you could clearly use the help."
    "..."
    "(So this girl just showed up in a penguin hoodie, trashed my Vimrc, and now she wants me to join her club?)"
    "(She can't be serious...)"
    "Actually, I think I'll pass."
    s "Hahaha! You thought you had a choice?"
    "(Ah shit, I should have guessed. The ones with the weird hoodies are always like this.)"
    s "See you at 5 in the activity room. If you don't show up, I know where to find you, [player_name]."
    "(Alright, so she knows my name too. This day is going great)."
    "(...)"
    return
