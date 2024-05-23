print('''

                                    _._
                                  _/,__\,
                               __/ _/o'o
                             /  '-.___'/  __
                            /__   /\  )__/_))\

 /_/,   __,____             // '-.____|--'  \\
e,e / //  /___/|           |/     \/\        \\
'o /))) : \___\|          /   ,    \/         \\
  -'  \\__,_/|             \/ /      \          \\
         \_\|              \/        \          \\
         | ||              <    '_    \          \\
         | ||             /    ,| /   /           \\
         | ||             |   / |    /\            \\
         | ||              \_/  |   | |             \\
         | ||_______________,'  |__/  \              \\
          \|/_______________\___/______\_             \\
           \________________________     \__           \\        ___
              \________________________    _\_____      \\ _____/
                 \________________________               \\
   ~~~~~~~~  b'ger /  ~~~~~~~~~~~~~~~~~~~~~~~~~~~  ~~ ~~~~\\~~~~
        ~~~~~~~~~~~~~~    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~    //
''')
print("It seems that you have died.")
print("Let's get you to the others, shall we?") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
first = int(input("You can either follow the mysterious man onto his barge (1), or turn around (2). Which path will you choose? "))

if first == 2:
   print("You turn from the odd man, and take a look around. You seem to be in some cave of a kind, but you don't seem to be able to see the top nor any side. A deep, tingy musk of decay and rot hangs in the air.")
   second = int(input("You come to a crossroads. You can either go up a set of slippery, stone stairs, glistening with some translucent fluid (1), or keep walking forward into the darkness (2). "))
   if second == 2:
      print("You keep going until you come to an opening in the cave. You look outside and see the sun, setting over the golden land. A very different view from what you've seen over the past few hours. Suddenly, you hear a woman's voice from behind you. You can't quite make out what she's saying...")
      third = int(input("Do you want to turn around and investigate the distressed voice (1), or keep going forward? (2) "))
      if third == 1:
         print('''
                            ,--.
          ,--.  .--,`) )  .--,
       .--,`) \( (` /,--./ (`
      ( ( ,--.  ) )\ /`) ).--,-.
       ;.__`) )/ /) ) ( (( (`_) )
      ( (  / /( (.' "-.) )) )__.'-,
     _,--.( ( /`         `,/ ,--,) )
    ( (``) \,` ==.    .==  \( (`,-;
     ;-,( (_) ~6~ \  / ~6~ (_) )_) )
    ( (_ \_ (      )(      )__/___.'
    '.__,-,\ \     ''     /\ ,-.
       ( (_/ /\    __    /\ \_) )
        '._.'  \  \__/  /  '._.'
            .--`\      /`--.
   jgs           '----' 
   ''')
         print("You turn around to investigate the situation. Once you turn around, you see a ghastly vision. A woman, who has snakes growing out of her head as if they were her hair, stares at you with her eyes wide open and her mouth twisted as she shrieks. You can sense your limbs slowly turning to stone. You can't run away. You can't scream, as your tongue has turned to stone. You have died.")
      else: 
         print("You don't let yourself be swayed from your mission and you walk out of the cave. You feel the sun shine onto your skin, the breeze tangle through your hair, and you can hear birds chirping in the sky. You have survived.")
   else:
      print('''
                                  /\_/\____,
                  ,___/\_/\ \  ~     /
                  \     ~  \ )   XXX
                    XXX     /    /\_/\___,
                       \o-o/-o-o/   ~    /
                        ) /     \    XXX
                       _|    / \ \_/
                    ,-/   _  \_/   \
                   
                   / (   /____,__|  )
                  (  |_ (    )  \) _|
                 _/ _)   \   \__/   (_
         b'ger  (,-(,(,(,/      \,),),)
         ''')
      print("You walk up the stairs, only to find out that the reason why they were slippery was a huge, three-headed dog, drooling onto the stairs. It spots you, opens all of its three maws, and devours you in a single bite. You have died.")
else:
   print("You step onto the barge. You pay the man a gold coin which you found in your pocket and take a seat. The man pushes the barge from the shore using a long pole and sets forth into the darkness of the unending cave. You have died.")