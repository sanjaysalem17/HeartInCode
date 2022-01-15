# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("MallocLab")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show malloc normal

    # These display lines of dialogue.

    e "Hello, new student."

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
    e "May your dreams be haunted by memory leaks for all eternity."
    return

label heapcheck:
    e "Looks like your code gets to live another day."
    e "At least, until ProxyLab kicks your ass."
    return
