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

    show malloc eyes
    e "Did you write a heap checker?"
    menu:
        "Yes":
            jump heapcheck
        "...":
            jump no_heapcheck

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
    show malloc normal
    e "Looks like you actually know what you're doing."
    e "The number of people who answer \"no\" to that question is astounding."
    e "..."
    e "Well anyway, you may want to check that you're freeing variables."
    e "Memory leaks are one of the most prominent threats to freedom these days."
    e "Everyone wants to take up memory, but no one wants to give it up."
    e "Don't be one of those scummy people, taking what's not yours and refusing to give it up."
    show malloc eyes
    e "Free the memory!!" with hpunch
    show malloc normal
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
