# Scene 1.2
# Temple background. Day. Setsuna is in centre, she cleans the footpaths. There is other people at background. Setsuna hears young adults planning an all night party. She wants to reprimand them, but does not find the courage. Nemuru come in and scold them. Group don't want to conflict and leave the place. Setsuna watches them leave with a sad look. Phone ringing. It's a John, Setsuna is glad to hear him. John tells her that he will come in the evening. He has a big surprise for her.

label tol_part_1_2:
    define audio.rustle="scenario/Taste of life/sound/rustle.wav"
    define audio.crowd="scenario/Taste of life/sound/crowd.wav"
    define audio.lock="scenario/Taste of life/sound/lock.wav"
    define shivernig= "shivernig.rpy"
    define shake= "shake.rpy"

    scene black with dissolve
    "Meanwhile, at a nearby shrine..."
    scene bg shrine exterior day
    play sound tol_sfx_crowd
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
    #I know you are very busy, but could you please add some sprites to the background. At first I thought full sprites were needed, but now I see that just silhouettes would work even better.

    show setsuna b_4 at faceright
    show setsuna at offscreenright with easeoutright
    scene black with wiperight
    stop sound fadeout 3
    "It was for this reason that Setsuna decided to take a short break from the bustling crowd and retreated to sweep the pedestrian paths away from people."

    play music bgm_summer_day
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
    play sound tol_sfx_rustle volume 0.5
    setsuna "I didn't expect such a turnout after the news of our sanctuary's temporary closure."
    setsuna "It feels as crowded as it does on New Year's Eve. It's reassuring to see that our efforts are not in vain and that people truly want to support our sanctuary."
    show setsuna b_4
    play sound tol_sfx_rustle volume 0.5
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

    stop music
    play music bgm_vivacity
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
    with hpunch
    tol_chris "{sc}IwroteapoemforagirlIlovepleaseforetellmeifwellbetogether!{/sc}"
    
    show tol_chris a_2
    "Then stared at the ground."

    show setsuna a_2
    setsuna "Ah..."
    extend "So you need an omikuji!"

    show setsuna a_1
    "Setsuna smiled, understanding his intent."

    show setsuna a_2
    setsuna "Sure, let's see what the Kami will foretell for you."
    stop music

    show setsuna a_0 at faceright
    show setsuna at offscreenright
    show tol_chris at offscreenright
    with easeoutright

    play music bgm_summer_day
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
    stop music

    scene black with wiperight
    pause .5
    scene tol_bg shrine
    with wiperight

    play music bgm_ensolarado
    play sound tol_sfx_crowd loop volume 0.3
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
    show tol_chris a_3 at shake

    "He tried to do what she was telling him."
    tol_chris "Nothing is happening. It's stuck"
    show tol_chris a_3 at reset_transform_shake_right
    setsuna "It's literally can't be. Try again"

    show tol_chris a_3
    show setsuna a_7
    tol_chris "It is. Try yourself if you don't belive me"
    setsuna "But..."
    extend "That's against the rules, Kami..."

    show tol_chris a_6
    "However, the boy's miserable expression made Setsuna feel sorry and she decided to help him out a little bit"

    show setsuna a_7:
        zoom 1.0
    pause 0.5
    show setsuna a_4:
        linear 1.0 zoom 1.01
    pause 1.5
    show setsuna a_6:
        linear 1.0 zoom 1.0
    show setsuna a_1
    setsuna "{i}Sigh{/i}... Alright, look, you need carefully shake it. Like this"
    "With those words, Setsuna reached out and gently touched the box."
    play sound tol_sfx_lock volume 0.5
    "As soon as she had done so, there was a click and a stick fell out of it."
    play sound tol_sfx_crowd loop volume 0.3
    # Now it's obvious that the fortune telling was for her, not for a third rate character.

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
    stop music
    play music bgm_blue_feather
    play sound tol_sfx_crowd volume 0.15
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
    stop music
    play music bgm_easy_lemon
    play sound tol_sfx_crowd volume 0.3
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
    show tol_mikoto a_9
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

    scene black with wiperight
    stop sound fadeout 2.0
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
    "However, an unpleasant surprise awaited Setsuna."
    stop music
    "As she returned, she noticed a group of young people nearby." 
    "They appeared to be college students, engaged in a rather boisterous discussion. Their voices filled the air, disturbing the so desired tranquility of the sanctuary." 
    "Setsuna sighed inwardly, knowing that her task would now be even more challenging with their presence."
    
    show setsuna at offscreenleft with easeoutleft
    play music bgm_early_riser

    $tol_henry.name = "Jacket guy"
    outfit tol_henry casual

    $tol_toshi.name = "Glasses guy"
    outfit tol_toshi casual
    
    $tol_bruce.name = "Big guy"
    outfit tol_bruce uniform_c

    show tol_henry a_1 at centerleft, faceright with easeinright: 
        xalign 0.10
    show tol_toshi a_2 at center, faceright with easeinright
    show tol_bruce a_7 at centerright, faceleft with easeinright:
        xalign 0.90
    
    show tol_henry a_4 
    tol_henry "Okay, one more time, what are we doing here?"

    show tol_toshi a_6 at faceleft
    show tol_bruce a_2
    tol_toshi "Honoring ancestors, spirits, and making wishes"

    show tol_henry a_6
    tol_henry "Toshi, I didn't ask what we've already done here. " 
    extend "I asked what we're doing here right now."
    $tol_toshi.name = "Toshi"

    show tol_bruce a_1
    tol_bruce "Waiting for Samantha and Mitsuru. "
    extend "Sam wanted to see what the priest would do."

    show tol_henry a_0
    tol_henry "{i}chuckle{/i}"
    extend "...oh, right, ass and tits. "
    extend "Wait, are they not coming right now?"

    show tol_toshi a_3
    tol_toshi "Probably not. "
    extend "Jay, what did you expect from a Shinto shrine anyway?"
    extend " Finish everything in fifteen minutes?"
    
    $tol_henry.name = "Jay"
    show tol_henry a_5
    tol_henry "Honestly? That we'd finish up here real quick and go to Ron's."
    extend "We still have alcohol to buy. Instead of sticking around until the local priest says a few ritual words"

    show tol_bruce a_17
    tol_bruce "Well, show some respect. "
    extend "It's important to Mitsuru and Sam's been wanting to see some ceremony for a long time, and here's an occasi-"

    show tol_toshi a_7 with hpunch
    tol_toshi "Cut it!"
    extend " What do you mean we still have to buy the booze? You should have bought it yesterday!"

    show tol_bruce a_8
    show tol_henry a_2
    tol_henry "I've... " 
    extend "be-e-en "
    extend "busy-y"

    show tol_bruce a_18
    tol_bruce "Doing what, exactly?"

    tol_henry "Important things. "
    extend "Uh... "
    extend "a lot of important things."

    show tol_toshi a_6
    tol_toshi "Dalgur's Gate 3"
    "Saying this, he looked Jay straight in the eye"

    show tol_henry a_4 with hpunch
    tol_henry "You can't blame me!"

    show tol_bruce a_31
    show tol_toshi a_4
    tol_toshi "I can and I will."
    extend "{i} ...sigh{/i} "
    extend "You know, calling you an idiot is giving you a compliment."

    show tol_bruce a_13
    tol_bruce "But now I know why he's in such a hurry. "
    extend "He can't get any sober chick!"

    show tol_toshi a_2
    show tol_bruce a_22 with hpunch
    tol_toshi "{sc}HAhaHaHAhaHaHhaHahAHhaHaHA{/sc}" (multiple=2)
    tol_bruce "{sc}hAHhaHAHhAHaHAHHAHAHHAhaaH{/sc}" (multiple=2)

    show tol_henry a_3 with hpunch
    tol_henry "Shut the fuck up Bruce!"
    $tol_bruce.name = "Bruce"

    show tol_bruce a_10
    show tol_toshi a_5

    show tol_henry a_6
    tol_henry "I don't have this kind of problems. "
    extend "Okay, here's an idea! Let's pick up some chicks and go to Ron's right now!"

    tol_toshi "And what about Sam and Mitsu?"

    show tol_henry a_4
    tol_henry "We'll figure something out on the way."

    show tol_bruce a_20
    tol_bruce "Alright {i}{b}Casanova{/b}{/i}, we're ready to go at any moment, but you owe us the ladies"

    show tol_henry a_1
    tol_henry "Easy! Look how it's done! Show any one of them and she'll ride with us"

    "Toshi glanced around"

    show tol_toshi a_7 at faceright
    pause 0.5
    show tol_toshi a_7 at faceleft
    pause 0.5
    show tol_toshi a_7 at faceright
    pause 0.5
    show tol_toshi a_7 at faceleft

    show tol_toshi a_2
    tol_toshi "That one!"

    show tol_henry a_5 at faceleft
    tol_henry "B-but "
    extend "it's a-"

    show tol_bruce a_15
    tol_bruce "Any one means " 
    extend "{b}ANY ONE.{/b} "
    extend "The choice is made."
    
    show tol_toshi a_2
    show tol_henry a_5
    tol_henry "Okay, get the car ready."
    show tol_henry at offscreenleft with easeoutleft

    show tol_toshi a_0 at centerleft, faceright with easeinright: 
        xalign 0.10
    tol_toshi "I bet you twenty he can't do it."

    show tol_bruce a_20
    tol_bruce "Good thinking, you little sneak. "
    extend "Not accepted. It's too obvious. "
    extend "Let me bet she'll hit him with a broom."

    show tol_toshi a_2
    tol_toshi "Ha, got it. I'll take that bet."

    show tol_bruce at offscreenright
    with easeoutleft
    show tol_toshi at offscreenright
    with easeoutleft


    show setsuna a_0 at centerright, faceright:

    "Setsuna stood half-turned, listening to their conversation, occasionally glancing at the group of three." 
    "A part of her wanted to intervene and give them a warning or even kick them out of the shrine." 
    "However, as she looked in their direction, they appeared imposing and intimidating, dissuading her from confronting them."

    play music bgm_pulse_rock
    show tol_henry a_1 at centerleft, faceleft with easeinleft: 
        xalign 0.15
   
    show setsuna a_4 at centerright, faceright:
    play sound tol_sfx_rustle volume 0.6
    pause 1
    play sound tol_sfx_rustle volume 0.6
    pause 1
    play sound tol_sfx_rustle volume 0.6
    pause 1

    "So when Jay approached her, she tightened her grip on the broom, increased her sweeping speed, and purposely avoided making eye contact with him"
    
    tol_henry "Hey, sweetie. "
    extend "What are you doing?"

    show setsuna a_4 at faceleft
    think "Go away, please."
    setsuna "Working."
    "Politeness demanded to speak by facing him, but Setsuna still couldn't raise her eyes to look up at him"

    show tol_henry a_0
    tol_henry "Ha, so you're just a part-time worker, huh?"
    extend " Well, I've got a better offer"
    tol_henry "Me and the guys are heading to an awesome hangout right now, and we've got some prime seats for cool girls like you."

    show setsuna a_7
    setsuna "{size=-5}Cool girls?{/size}"

    show tol_henry a_2 
    tol_henry "Yeah, you know, you've got that cool look"
    extend "I bet you're always at the coolest parties. Trust me, this one we have lined up is gonna be amazing!"

    "Setsuna's voice carried a hint of sadness as she responded"
    show setsuna a_4 
    setsuna "Sir, I can sell you an omamori amulet or assist with omikuji fortune-telling. If you have any other requests, I probably won't be able to help you."

    show tol_henry a_4
    tol_henry "Did I say something wrong?"
    extend " I can tell you're interested."

    think "If you only knew."
    setsuna "{i}Sigh{/i}...{size=-5}I just can't.{/size}"

    show tol_henry a_6 at centerleft, faceleft with easeinleft:
        xalign 0.45

    tol_henry "He stood directly in front of Setsuna and put his hands on her shoulders."

    show setsuna a_4 at shivering_left(duration=0.5)

    "Setsuna shuddered, trembled, and clutched the broom so tightly that her fingers turned white."

    show setsuna a_9
    think "Don't touch me, please"
    
    show tol_henry a_0
    tol_henry "You know, sometimes you have to face your fear to get a taste of life."

    "As if in a dream, Setsuna raised her eyes open with fear and met Jay's gaze"
    show setsuna a_4 at faceleft
    
    show setsuna b_7 at shivering_left(duration=0.5)
    setsuna "S-Sir, p-please..."
    extend "I already t-told y-"

    show tol_henry a_3 with hpunch
    tol_henry "Oh, come on! "
    extend "Do you really think the priest will care? There are other mikos here. The old man won't even notice!"
    
    nemuri "What won't the old man notice?"
    
    play music bgm_radio_martini
    show nemuri a_4 at left

    with easeinleft
    nemuri "I have been informed that there are three young men here disturbing the order, swearing and distracting the miko. I suppose you are one of them."

    show tol_henry a_1 at faceright, with easeinleft:
        xalign 0.4
    
    show setsuna b_1 at reset_transform_shivering_left
    think "Thanks Dad"

    "Jay's confidence wavered as he faced Nemuru's authoritative presence."
    tol_henry "Oh, sir, it's just harmless conversation. "
    extend "My friends and I are just waiting for our girlfriends."

    show setsuna a_6
    setsuna "It's true father, they were talking loudly, but they didn't do anything wrong."

    show tol_henry a_4
    tol_henry "Father? Оh..."
    "Jay whistled"

    show nemuri a_0
    nemuri "On a normal day you'd get off with a warning, but today I want to minimize problems."
    nemuri "So please {b}leave{/b} this place."
    "There was steel in Nemuri's usually calm, peaceful voice."

    show tol_henry a_3
    show tol_henry a_3 at faceright
    pause 0.5
    show tol_henry a_3 at faceleft
    pause 0.5
    show tol_henry a_3 at faceright 
    pause 0.5
    show tol_henry a_3 at faceleft
    pause 0.5
    tol_henry "I see, excuse me. My friends and I were just leaving."
    
    show tol_henry at offscreenleft with easeoutleft
    "Jay then rejoined his friends, sharing a few words that Setsuna couldn't discern."
    "With a heavy heart, Setsuna watched as the group walked away, moving farther from the shrine grounds."

    show nemuri a_1
    show setsuna a_4
    nemuri "Suna, are you okay? Did he do anything to you?"
    "Nemuri looked at his daughter with concern and care."
    setsuna "I'm fine, father. He just wanted to talk, and I was able to finish sweeping the walkways while we were conversing."

    "Nemuru let out a sigh of relief."
    nemuri "That's good to hear. Now, go and get some rest. You have been working tirelessly today."

    show setsuna b_5
    setsuna "But, Dad, there's still so much work left to be done."

    show nemuri a_0
    nemuri "Don't worry, I and the other girls will take care of it. You have done more than enough. Rest is important too."

    "Setsuna expressed her gratitude to her father and slowly, pausing occasionally to catch her breath, made her way to her room."
    
    show nemuri at offscreenleft with easeoutleft
    
    show setsuna at offscreenleft with easeoutleft

    placeholder
