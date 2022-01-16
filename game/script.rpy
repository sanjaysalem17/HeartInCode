# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("MallocLab")

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

    e "Hello, [player_name]."
    e "I heard you had some issues with your memory allocation homework."
    e "I can take a look at it, but you'll need to answer my question first."

    show malloc eyes with dissolve
    e "Did you write a heap checker?"
    menu:
        "Yes.":
            jump heapcheck
        "No...":
            jump no_heapcheck
        "What's that?":
            jump unsure_hpcheck

    # This ends the game.

    return

label no_heapcheck:
    e "A Segmentation Fault is too kind of a punishment for scum like you."
    e "Come back when you've learned how to debug your code yourself."
    "Bam!!" with vpunch
    hide malloc normal with dissolve
    "D...Did he just punch me?"
    "Who needs a heap checker when I have my own two eyes?"
    "Whatever. That guy needs serious help..."
    return

label heapcheck:
    show malloc normal with dissolve
    e "Looks like you actually know what you're doing."
    e "The number of people who answer \"no\" to that question is astounding."
    e "..."
    e "Well anyway, you may want to check that you're freeing variables."
    e "Memory leaks are one of the most prominent threats to freedom these days."
    e "Everyone wants to take up memory, but no one wants to give it up."
    e "Don't be one of those scummy people, taking what's not yours and refusing to give it up."
    show malloc eyes with dissolve
    e "Free the memory!!" with hpunch
    show malloc normal with dissolve
    "..."
    e "..."
    e "Sorry about that."
    e "I tend to rant when I talk about things like this."
    e "That should fix your problem, but if not, I have faith in your programming abilities."
    e "Hope this helps!"
    hide malloc normal with dissolve

    "..."
    "What the heck was that?"
    "That guy probably has a few screws loose or something."
    "I should look at my code though, just to check what he said."
    "..."
    "...."
    "..."
    "Ah shit, I just forgot a semicolon."
    return

label unsure_hpcheck:
    show malloc normal with dissolve
    e "Are you serious?"
    e "How do you not know what that is?"
    e "Do you not pay attention during lecture or something?"
    "..."
    e "Ah, I get it. You must be one of those people who think they're too good to go to lectures, aren't you?"
    e "All you \"pro-gamer\" scum are the same. Thinking you can get by watching recordings at 2x speed." 
    show malloc eyes with dissolve
    e "You may be happily cruising along now, but just wait until my buddy Proxy really makes you suffer."
    e "I look forward to seeing how that fragmentation turns out."
    e "See you at the final exam."

    hide malloc eyes with dissolve

    "..."
    "What just happened?"
    "And who the fuck is Proxy?"
    "Am I supposed to be scared?"
    "..."
    "Nah, if I can sleep during lectures and still keep my A, there's nothing to be afraid of."
    return
