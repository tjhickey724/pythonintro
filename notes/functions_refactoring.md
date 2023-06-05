# Refactoring
This is a technique to remove redundance.
For example, we can refactor the following function
``` python
def poem():
    ''' print the poem "Do not go gentle" '''
    print("")
    print("Do not go gentle into that good night,")
    print("Old age should burn and rave at close of day;")
    print("Rage, rage against the dying of the light.")
    print("")
    print("Though wise men at their end know dark is right,")
    print("Because their words had forked no lightning they")
    print("Do not go gentle into that good night.")
    print("")
    print("Good men, the last wave by, crying how bright")
    print("Their frail deeds might have danced in a green bay,")
    print("Rage, rage against the dying of the light.")
    print("")
    print("Wild men who caught and sang the sun in flight,")
    print("And learn, too late, they grieved it on its way,")
    print("Do not go gentle into that good night.")
    print("")
    print("Grave men, near death, who see with blinding sight")
    print("Blind eyes could blaze like meteors and be gay,")
    print("Rage, rage against the dying of the light.")
    print("")
    print("And you, my father, there on the sad height,")
    print("Curse, bless, me now with your fierce tears, I pray.")
    print("Do not go gentle into that good night.")
    print("Rage, rage against the dying of the light.")
    print("")

poem()

```

as follows:
``` python
def do_not_go():
    print("Do not go gentle into that good night.")

def rage_rage():
    print("Rage, rage against the dying of the light.")

def poem():
    ''' print the poem "Do not go gently" '''

    print()
    do_not_go()
    print("Old age should burn and rave at close of day;")
    rage_rage()
    print()

    print("Though wise men at their end know dark is right,")
    print("Because their words had forked no lightning they")
    do_not_go()
    print()

    print("Good men, the last wave by, crying how bright")
    print("Their frail deeds might have danced in a green bay,")
    rage_rage()
    print()

    print("Wild men who caught and sang the sun in flight,")
    print("And learn, too late, they grieved it on its way,")
    do_not_go()
    print()

    print("Grave men, near death, who see with blinding sight")
    print("Blind eyes could blaze like meteors and be gay,")
    rage_rage()
    print()

    print("And you, my father, there on the sad height,")
    print("Curse, bless, me now with your fierce tears, I pray.")
    do_not_go()
    rage_rage()
    print()


poem()

```
