#script for the database inventory scene

label databases:
    scene black
    show text "You make your way to Tartan Ink to try and get festival supplies for the cooking club." with dissolve
    pause 1.5
    hide text with dissolve
    scene bg classroom
    "I think this is the right room."
    "Is this Tartan Ink?"
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
    "I'm helping the cooking club with the festival, and they're doing a cafe."
    "They sent me here to get the tables and chairs for it."
    "Database" "I see. Well, you've come to the right place."
    "Database" "If anyone would have them, it's us."
    "Database" "Oh! Did you see the new Request movie? It's my favorite series."
    "The what? I've never heard of a movie like that."
    "Database" "It's a great franchise about a team requesting items."
    "And the movies are good?"
    "Database" "Of course they are! There are so many cool scenes like the one where they SELECT things and-"
    "Oh, uh, I see. And a new one just came out?"
    "Database" "Yep! But now that it's out, they can make plans for the future."
    "Database" "I sure hope they get to work right away on the 'sequel' ;)."
    "-_-"
    "Let's talk about something else now."
    "Database" "Sure!"
    "So how did you end up working down here?"
    "Database" "Oh, thats quite simple, actually."
    "Database" "I love hanging out with Storage, and asking them to SELECT things."
    "Database" "Not to mention I get to help all the people who come here, which is also great."
    "You really like requesting things that much?"
    "Database" "Of course! I love saying SELECT and WHERE and HAVING and-"
    "Storage" "Alright that's enough. I'm back."
    show storage normal at left with dissolve
    "Storage" "I hope Database didn't bother you too much."
    "We had a nice chat."
    "Database" "Did you find if we have tables and chairs?"
    "Storage" "Yep, we got them right here."
    "Storage" "Here you go, uh-"
    "Oh, my name is [player_name]."
    "Storage" "Here are the tables and chairs [player_name]. Nice to meet you."
    "Nice to meet you too, and thank you for getting these for me."
    "Storage" "No problem."
    "Database" "I hope we see you around! I would love the chance to request more items for you!"
    "I'm sure I'll come back again to request more things in the future."
    "See you guys later!"
    "Database" "Bye!!!"
    "Storage" "See ya."
    #hide Database normal with dissolve
    hide storage normal with dissolve
    return