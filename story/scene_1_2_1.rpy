# Scene 1.2.1
# Temple background. Day. Setsuna is in centre, she cleans the footpaths. There is other people at background. Setsuna hears young adults planning an all night party. She wants to reprimand them, but does not find the courage. Nemuru come in and scold them. Group don't want to conflict and leave the place. Setsuna watches them leave with a sad look. Phone ringing. It's a John, Setsuna is glad to hear him. John tells her that he will come in the evening. He has a big surprise for her. 

label tol_part_1_2_1:
    define audio.rustle="scenario/Taste-of-life-main/sound/rustle.wav"
    define audio.crowd="scenario/Taste-of-life-main/sound/crowd.wav"
    define audio.lock="scenario/Taste-of-life-main/sound/lock.wav"
    scene black with dissolve
    "Meanwhile, at a nearby shrine..."
    scene bg shrine exterior day
    show setsuna b_4 at center, faceleft:
        pause 3.0
        block:
            faceleft
            easein 2.0 xpos .7
            pause 1.5
            faceright
            easein 2.0 xpos .3
            pause 1.5
            repeat
    with dissolve

    # Narrative
    "Setsuna Otani, the miko of the local Shinto shrine, was extremely busy today. Her father, Nemuru, had announced that the shrine would be closed for repairs starting from tomorrow." 
    "Despite the absence of holidays or special events, the temple was crowded with visitors. Consequently, Setsuna worked tirelessly, constantly moving from one task to another." 
    "Adding to her burdens was her debilitating illness, making her already exhausted by noon."
    show setsuna b_4 at faceright
    show setsuna at offscreenright with easeoutright
    scene black with wiperight
    "It was for this reason that Setsuna decided to take a short break from the bustling crowd and retreated to sweep the pedestrian paths away from people."

    scene bg shrine steps day
    show setsuna b_0 at center, faceright with easeinleft
    "Setsuna stood in front of the shrine, a broom in her hands, as she glanced towards the bustling crowd in the distance."

    show setsuna b_5:
        faceleft
        easein 1.5 xpos .45
        pause 1.5
        faceright
        easein 1.5 xpos .65
        pause 1.5
        repeat
    "Slowly, she swept the paths, occasionally pausing to lean on the broom."
    
    show setsuna b_6
    play sound rustle
    setsuna "I didn't expect such a turnout after the news of our sanctuary's temporary closure."
    setsuna "It feels as crowded as it does on New Year's Eve. It's reassuring to see that our efforts are not in vain and that people truly want to support our sanctuary." 
    show setsuna b_4
    play sound rustle
    "Setsuna's voice was soft as she muttered her thoughts."
    
    show setsuna b_6
    setsuna "I'm also grateful that a few other girls agreed to be miko with me today. I don't think I could have managed it alone."
    $tol_chris.name = "???"
    show setsuna b_7:
        faceleft
        easein .5 xpos .5
    tol_chris "Maiden, maiden!"
    "Setsuna heard someone calling out to her."
    
    show setsuna b_6
    setsuna "*sigh*, Here we go..."

    show setsuna a_6 at faceleft
    setsuna "All I wanted was a moment of peace and quiet."

    outfit tol_chris casual
    show setsuna a_1
    show tol_chris a_0 at centerleft, faceright with easeinleft
    "A lonely nerd approached Setsuna with hesitation."
    
    show setsuna a_2
    setsuna "Hello, what do you need?"

    show setsuna a_1
    show tol_chris  b_3
    tol_chris "I... I want you to... you know... {size=-5}love{/size}"
    
    show tol_chris b_0
    show setsuna a_7
    "The guy babbled nervously. Setsuna's eyes widened in surprise."
    
    show setsuna a_8
    setsuna "Whaat?"

    show setsuna a_7
    show tol_chris a_6
    tol_chris "N-no, I mean, uh... {size=-5}I wrote a poem...{/size}"
    
    show tol_chris a_3
    show setsuna a_8
    setsuna "For me?"

    show setsuna a_5
    show tol_chris b_3 
    tol_chris "N-no, it's for a certain girl. A beautiful one."
    
    show tol_chris b_6
    show setsuna b_7
    tol_chris "Oh, {size=-5}I mean{/size}, {size=-10}you're p-pretty too{/size}..."

    show tol_chris a_2
    "Suddenly, he took in a deep breath and held it for half a minute. Setsuna looked at him with a puzzled expression."
    
    show setsuna b_8
    setsuna "Are you okay?"

    show setsuna b_3 
    "And then the guy blurted out without pause:"
    
    show tol_chris a_1
    tol_chris "{size=+10}IwroteapoemforagirlIlovepleaseforetellmeifwellbetogether!{/size}"
    
    show tol_chris a_2
    "Then stared at the ground."

    show setsuna a_2
    setsuna "Ah..."
    extend "So you need an omikuji!"
    
    show setsuna a_1
    "Setsuna smiled, understanding his intent."
    
    show setsuna a_2
    setsuna "Sure, let's see what the Kami will foretell for you."


    show setsuna a_0 at faceright
    show setsuna at offscreenright
    show tol_chris at offscreenright
    with easeoutright

    scene black with wiperight
    "They walked together towards the Omikuji corner and on the way, Setsuna inquired: "

    scene tol_bg forest_shrine with wiperight

    show setsuna a_1 at centerright, faceright
    show tol_chris a_0 at center, faceright
    with easeinleft
    
    show tol_chris at walk_right
    pause .35
    show setsuna b_2 at walk_right
    setsuna "Does the girl know about your feelings?"

    show setsuna b_1
    show tol_chris b_3
    tol_chris "She doesn't know yet, but if the foretell is good, I'll confess to her."

    show tol_chris b_0 
    "Setsuna found his awkwardness endearing and decided to uplift his spirits."
    
    show setsuna b_2
    setsuna "Even if the divination turns out to be unfavorable, it's still worth taking a chance."

    show setsuna a_2 
    setsuna "The deities sometimes enjoy playing games with mortals. Often, a victory snatched from the clutches of bad luck holds more value than one bestowed by good fortune." 

    show setsuna a_1
    show tol_chris a_3
    tol_chris "{size=-5}Thank you, Ms. miko{/size}"

    show setsuna at offscreenright
    show tol_chris a_0 at offscreenright
    with easeoutright

    scene black with wiperight
    pause .5
    scene tol_bg shrine
    with wiperight

    show setsuna a_1 at centerright, faceright
    show tol_chris a_0 at centerleft, faceright
    with easeinleft

    show setsuna at faceleft
    show tol_chris a_0
    "Near the Omikuji corner, Setsuna asks if he has the fee. The boy assures her that he does and reaches into his pocket, only to find it empty. Each pocket he checks yields the same result."

    show tol_chris a_1
    tol_chris "Oh, no. How could this happen? I didn't forget..."

    show tol_chris a_6 
    tol_chris "Oh, I'm such a fool. I'm here with Inari, my sister. She wanted to buy an omamori for both of us, and I gave her the money."

    show tol_chris a_1 at faceleft 
    tol_chris "I'll be right back to get it."
    
    show tol_chris a_3
    show setsuna b_7:
        linear .2 xoffset -40
    setsuna "Wait! "
    extend "Don't worry, I have enough for the offering."

    show setsuna b_7 
    show tol_chris a_0 at faceright
    setsuna "But make sure to bring the fee later, otherwise, the Kami might become displeased. Agreed?"

    show tol_chris a_4
    show setsuna b_1
    tol_chris "Yeah!"
    
    show tol_chris a_0
    show setsuna a_2
    setsuna "That's good. Now let's get started." 

    show setsuna a_1
    "She places the offering in the donation box and instructs him:"
    
    show setsuna a_2
    setsuna "Now, take the box of tubes and shake it. When one stick falls out, tell me the number written on its tip, and I will give you a divination that corresponds to that number, without looking."
      
    show setsuna a_1
    show tol_chris a_3
    # Please, insert here guy's shaking. I don't understand why, but "linear .2 xoffset 10" is not working as a command

    "He tried to do what she was telling him."
    tol_chris "Nothing is happening. It's stuck"
    setsuna "It's literally can't be. Try again"

    show tol_chris a_3
    show setsuna a_7
    tol_chris "It is. Try yourself if you don't belive me"
    setsuna "But..."
    extend "That's against the rules, Kami..."

    show tol_chris a_6
    "However, the boy's miserable expression made Setsuna feel sorry and she decided to help him out a little bit"

    show setsuna a_5
    "Sigh... Alright, look, you need carefully shake it. Like this"
    play sound lock
    "With those words, Setsuna reached out and gently touched the box."
    "As soon as she had done so, there was a click and a stick fell out of it."
    # Now it's obvious that the fortune telling was for her, not a third rate character.

               #show setsuna a_1
               #"He follows her instructions, and after a moment, he says, \"It's four\"."
   
    show tol_chris a_5
    "He take the stick, and after a moment, he says, \"It's four\"."

    show setsuna a_7
    "Setsuna looks surprised at the number."
    
    show setsuna a_8
    setsuna "W-well..."
    
    show setsuna a_7
    "She stammers, gathering her thoughts."
    # Author's Note: In Japan, the number 4 is considered to be unlucky, so Setsuna was confused about it

    show tol_chris a_3
    tol_chris "Is everything okay?"

    show tol_chris a_2
    "He asks, his anxiety evident. Setsuna hesitates for a moment, then forces a smile."
    
    show setsuna b_2
    setsuna "Yeah, yeah, everything's fine. Here's your fortune." 

    show setsuna b_1
    "She covers her eyes and lets out a subtle sigh before taking a divination from the box without looking."
    
    show tol_chris a_6:
        linear .2 xoffset 40
        linear .2 xoffset 0
    tol_chris "Let me see!"
    
    show tol_chris a_0
    "The boy eagerly takes the fortune paper from Setsuna's hands."

    show tol_chris a_3
    show setsuna b_7
    tol_chris "\"Daikyou\". What does that mean?"

    "Setsuna's voice is quiet as she responds:"
    show tol_chris a_2
    show setsuna b_8
    setsuna "{size=-5}Great misfortune{/size}"

    show setsuna a_4
    show tol_chris a_3
    tol_chris "That's a shame. And I still owe you. It's better for me to go get the money." 
    
    show tol_chris a_2 at faceleft
    show tol_chris at offscreenleft with easeoutleft
    "Disappointed, he slips the paper into Setsuna's hand, turns, and walks away swiftly."

    show setsuna a_8:
        easein .5 xpos .4
    setsuna "{size=+7}W-Wait!{/size}" 
    setsuna "To prevent the bad prediction from coming true..."
    
    show setsuna a_4
    "But the boy had already disappeared amidst the crowd."

    show setsuna a_6 
    setsuna "{size=-3}... it should be tied to a tree.{/size}"
    
    show setsuna a_4
    "She finished her sentence, slightly quieter, and hid the paper in her pocket."

    # Re-using DnD character Mikoto since she has a similar Miko outfit
    $tol_mikoto.name = "Sakura"
    outfit tol_mikoto miko

    show setsuna a_0
    show tol_mikoto a_1 at right, faceleft with easeinright
    tol_mikoto "Suna, what are you doing here?"
    
    show tol_mikoto a_0
    show setsuna at faceright
    "Setsuna heard a familiar voice to her right. It was Sakura, one of the girls who was part-time Miko today."

    show tol_mikoto a_8 
    tol_mikoto "Dear, you're white as a sheet. Is something wrong?"
    
    show tol_mikoto a_4
    show setsuna a_6
    setsuna "Really? I must have missed taking my pills."
    
    show setsuna a_9
    "Setsuna put her palm to her forehead."
    
    show setsuna a_6
    setsuna "And my ears are pounding..."

    show setsuna a_4
    "Setsuna briefly recounted to Sakura what had happened, but forgot to mention that he didn't take the paper."

    show setsuna a_6
    tol_mikoto "What a {i}snowflake{/i} "

    show tol_mikoto a_11
    show setsuna a_4
    tol_mikoto "On the contrary, he should be grateful - the deities tell to wait for a better time"

    show tol_mikoto a_4
    show setsuna a_9
    "She glanced at Setsuna again."
    
    show tol_mikoto a_8
    tol_mikoto "Let me wait for him and you better go because you look, to be honest, not good."
    
    show tol_mikoto a_4
    show setsuna b_6 
    setsuna "I'm fi--"
    
    show setsuna b_9
    show tol_mikoto a_8
    tol_mikoto "Don't worry, it's not a big deal to me, besides other people will want to do the fortune telling too. And you better get some rest."

    show tol_mikoto a_4
    show setsuna b_6
    setsuna "You think so? "
    extend "Okay, thanks, I'll be off then."
    
    show setsuna a_9 at faceleft
    show tol_mikoto a_6

    show tol_mikoto a_0
    show setsuna at offscreenleft with easeoutleft
    "Setsuna heard Sakura's cheerful voice behind her."
    tol_mikoto "You'll owe me a favor!"
    
    show tol_mikoto a_0
    show setsuna at offscreenleft with easeoutleft
    "Setsuna heard Sakura's cheerful voice behind her."
    
    scene black with wiperight
    "However, she was reluctant to go to her room due to the bustling crowd that still filled the shrine." 

    scene bg shrine steps day
    show setsuna b_4 at center, faceleft:
        pause 3.0
        block:
            faceleft
            easein 2.0 xpos .55
            pause 1.5
            faceright
            easein 2.0 xpos .45
            pause 1.5
            repeat
    with dissolve
    "Instead, she decided to return to sweeping the paths in an attempt to avoid the crowded areas." 
    "Determined to find solace amidst the chaos, Setsuna focused on her task, diligently sweeping and clearing the pathways, finding a moment of peace amidst the commotion."


    placeholder
