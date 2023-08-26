label tol_start:


# Day 1
# Scene 1.1
# John is in his room fooling around, or to be more precise - making new spells. Some magic stuff happening.
# Sandra comes in and asks if John wants to eat. She can bring snacks. John replies that not now, later, now he is busy with something big. Sandra asks what it is. John replies that it's a new healing spell. Sandra leaves the room. John say that he probably need use "Verba obedy" less on his family.

# Comment
# This is like the episode from the original ST where John hypnotizes Sandra into thinking everything that happens in his room is normal.

# Narrative
    nvl clear
    nvl_narrator "Half a year ago, John Davis discovered that he is the offspring of a mighty wizard's dynasty. Unfortunately for him, all he inherited was a magical book, neither less nor more."
    nvl_narrator "As he began his experiments, he quickly realized that the book contained only a few useful spells." 
    nvl_narrator "In his search for someone from his ancestral line who could guide him, he was unsuccessful." 
    nvl_narrator "Determined to learn magic on his own, John decided to create his own spells. Since then, he has spent much time experimenting."

# Scene begins
    body john tol_john casual
    scene bg house_davis bedroom_john day_shut
    show john a_0 at center, faceright
    with dissolve

    "John stood in the middle of his room, testing the newly written spells."
    
    show john:
        easein .3 ypos 1.3
    pause 1.5
    outfit john underwear
    show john:
        easein .3 ypos 1.0
    "He took off his clothes and placed them on the bed, then took two steps back."

    show john a_13:
        ypos 1.0
    john "Let's see how it works."

    show john a_0
    "Clearing his throat, he confidently recited his new spell. Focusing on the clothes he just laid down."
    
    show john a_7
    show pentagram as pentagram behind john at Position(pos=(.77, 0.8))
    play sound sfx_spell
    john "{spell}Des Srem!{/spell}"

    show john a_2
    hide pentagram with dissolve
    "At first, nothing happened, but after a few seconds, his clothes started to move."
    
    show john a_15
    with hpunch
    "They slid off the bed, crawled across the floor, and began to put themselves on John." 
    
    outfit john topless
    show john a_16
    with wipeup
    "However, rather than being impressed, John Davis lets out a sigh of disappointment, making a note in one of his books."
    
    "John mutters in frustration."
    outfit john casual
    show john a_21
    with wipeup
    john "Not sliding, goddamnit, soaring!"

    show john a_15
    show text "{color=#A5A}{size=30}CROAK{/size}{/color}":
        xpos 0.3 ypos 0.15
#The best thing is find actuall sound of frog's croak, but before that please, can you make text CROAK without description in the box?
    "In the room, the sound of a frog croaking could be heard. "

    show john a_2 at faceleft
    hide text
    "John stared thoughtfully at the ceiling."
    
    show john a_0
    "Invisibility spell working as intended."

    show john a_15
    show text "{color=#964B00}{size=40}THUD{/size}{/color}":
        xpos 0.3 ypos 0.05
#Same here
    "Suddenly, a loud smack echoed in the room, indicating that something small and soft had been forcefully slammed against the ceiling."

    hide text
    show john a_16
    think "Levitation spell still needs improvement..."
    
    show john a_2 at faceright
    show john at centerright with move
    "John started noting things down in his book."

    play sound sfx_knock
    show john at faceleft
    "A knock on the door interrupted John's thoughts."
    sandra "Honey, are you busy? Can I come in?"

    show john a_13
    john "Yes, mom, come in."

    show john a_0
    body sandra sayaka nude
    show sandra a_1 at left with easeinleft
    "John acted normal as a nude Sayaka entered his room."
    "He glanced at the prettiest girl in school's body, proud of his latest spell and a little turned on by the result."

    show john a_15
    show sandra a_27
    show text "{color=#A5A}{size=30}CROAK{/size}{/color}":
        xpos 0.3 ypos 0.05
    "His tough where interupted when he heard another croak coming from the celing of his room."

    hide text
    "Sayaka looked up at the ceiling in surprise."

    # Since im using Sandra with Sayaka's body, its only fair that Sayaka has Sandra's body for the glitch effect
    body sayaka sandra suit

    show sayaka a_0 behind sandra at left, faceright
    show sandra at Glitch()
    "Suddenly, as if in a video game, Sayaka transformed into Sandra Davis for a few moments before changing back."
    
    show john a_16 at faceright
    hide sayaka
    show sandra at left
    with dissolve
    "John, looking dissapointed, made another note, mumbling to himself."
    
    show john a_22
    john "Illusion spell needs a stability upgrade."

    show john a_16
    show sandra a_29
    sandra "What?"
    
    show sandra a_30
    show john a_22 at faceleft
    john "It's nothing. What do you want?"

    show john a_2
    show sandra b_8
    sandra "Dear, you've been sitting here all day, I'm worried you even missed lunch. Do you want me to bring you a snack?"

    show sandra b_11
    show john a_12
    "John chuckled."
    
    show john a_13
    john "Oh, come on, it's not that late. Thanks, mom, but I'm not hungry."

    show john a_15
    show sandra b_27
    show text "{color=#A5A}{size=30}CROAK{/size}{/color}":
        xpos 0.3 ypos 0.05
    "The croaking sound echoed in the room again."


    # Same pattern here 


    hide text
    show sandra b_28
    sandra "Son, is there a frog in your room?"

    show sandra b_27
    show john a_13
    john "Yep."
    
    show john a_0 
    show sandra a_0
    "Sandra's gaze shifted upwards towards the ceiling."
    
    show sandra a_8
    sandra "But there's-"
    
    show sandra a_27
    show john a_21
    with hpunch
    john "Of course, it's invisible!"

    show john a_2
    "Sandra's eyes widened in surprise."
    
    show sandra a_7
    sandra "Why, for the love of God, is there an invisible frog on the ceiling in my house?!"

    show sandra a_30
    "After her question, Sandra froze in place, as if she were listening to the sound of it."
    
    show sandra b_6
    sandra "What did I just say? I mean, that's, uh..."
    
    show sandra b_5
    "She trailed off, still trying to understand the situation."

    show john a_15
    "John started to panic."
    
    show john a_4
    john "M-Mom, it's okay. Remember, everything that's happening in my room is"
    play sound sfx_spell
    show john a_4
    extend " {b}FINE{/b}."

    show john a_13
    john "The frog is like that because I tried a levitation spell on it."

    show john a_0
    "Sandra, still bewildered, replied."
    
    show sandra a_8
    sandra "Oh, {i}fine{/i}... but that's not what I mentioned! Where did you even get it?"

    show sandra a_30
    show john a_10
    john "Ah, this is a flower from Holly's room!"

    show john a_0
    show sandra a_27
    "Sandra looked startled."
    
    show sandra a_8
    sandra "What?" 

    show sandra a_30
    show john a_14
    john "I turned Holly's flower into a frog, then levitated it, and finally made it invisible. It's easy!"

    show john a_0
    show sandra b_5
    "Sandra's expression turned concerned as she responded"
    
    show sandra b_8
    sandra "But dear, Holly loves this flower. Why did you do such things to it? You can't just-"

    show sandra b_27
    show john a_11 
    with hpunch
    john "Mom, I can do anything! "
    
    show john a_7
    extend "Especially when it's"
    play sound sfx_spell
    show john a_7
    extend " {b}necessary!{/b}"

    show john a_16
    show sandra b_20
    "Sandra spaced out for a moment, her thoughts processing."
    
    show sandra b_30
    show john a_2
    sandra "Yes, dear, this is {i}necessary{/i}..."

    show sandra b_1
    show john a_0
    "John was glad to see his mind control spell also worked. It had been annoying having to explain everything to his mom again and again, every time she caught him doing somehtung unnatural."

    show john a_16
    show sandra b_1 at Glitch(), left, faceright
    show sayaka a_0 behind sandra at left, faceright
    "But then, the same annoying issue happend to John's mother as her appearanced flipped between her original self and the one John tried to superimpose on her."
    
    body sandra yui nude
    hide sayaka
    show sandra b_6 at left, faceright
    with dissolve
    show john a_15:
        easein .2 xoffset 10
    "This time she changed into a naked Yui."
    "John clearly hadn't expected this. When he saw Yui's face, he flinched slightly and looked away."

    show sandra b_6 at Glitch(), left, faceright
    show sayaka a_0 at Glitch(), left, faceright
    "Then he made an subtle movement with his hand and Yui's image started to change again."

    body sandra connie nude
    hide sayaka
    show sandra a_0
    show john a_0
    with wipedown
    "The image settled on Connie Williams this time."
    john "Huh, I see the pattern." 
    "Sandra looked confused and asked:"

    show sandra a_18
    sandra "Ehm?"
    
    
    show sandra a_17
    "But John quickly dismissed her."
    
    show john a_22
    john "Don't pay attention."

    show john a_2

    show sandra a_18
    sandra "Son, you're scaring me. What's so important that you're not even going out to eat?"
    
    show sandra a_17
    show john a_17
    "John stood tall, his voice filled with self-confidence as he responded."
    
    show john a_3
    john "Well, for the past week, I've been passionately working on a special spell. It's a healing spell that I specifically created for Suna."

    show john a_0
    show sandra a_5
    "Connie's eyes softened as she though she understood what was really going on."
    
    show sandra a_14
    sandra "Oh, it's because of her condition. You believe you can cure her?" 

    show sandra a_5
    "The self-assured tone in John's voice was evident as he confidently replied."
    
    show john a_14
    john "I turned a mere house plant into an invisible flying frog. Of course, I do."
    
    show john a_20
    "Just imagine the sheer joy and happiness she will experience when I bring an end to her illness."

    show john a_0
    show sandra b_0 
    "A smile formed on Connie's face as she playfully teased."
    
    show sandra b_1
    sandra "If that's the case, maybe we'll discuss your next bold move, my bravest knight of the Round Table, for winning her heart?"

    show sandra b_0
    show john a_4
    john "Mom, why do you always bring that up?"
    
    show john a_7
    john "Your son is on the brink of outshining modern medicine by discovering a cure for a disease like hers. You should be in awe!" 

    show john a_2
    show sandra b_10
    "Sandra raised an eyebrow and replied"
    
    show sandra a_14
    show john a_15 blush
    sandra "Oh, is that all there is to it? I must say, my son's ambitions are truly limitless!"
    "John's face turned embarrassed as his mother teased him."

    show sandra a_0
    show john a_22 blush
    john "Mom, it's not... Ahem... It's for..."
    
    show john a_2 blush
    "John stammered, struggling to explain himself."

    show sandra b_1
    sandra "I see, Sir Lancelot, that you are ready to defeat a dragon, but not to kneel before a lady!"

    show sandra b_0
    show john a_11 blush
    john "Mom, stoooop!"
    
    show john a_21 blush
    john "You know what? You won. I'll go and eat something. Just spare me this talk."

    show john a_16 blush
    show sandra a_1 at faceleft
    sandra "Yay! It's not so difficult after all, is it?"

    show sandra a_0 at offscreenleft 
    show john a_2 at offscreenleft
    with easeoutleft
    "Sandra left the room, and John followed her."

    scene black with wipeleft
    pause 1.0
    scene bg house_davis hallway day with wipeleft

    show sandra a_0 at center, faceleft
    show john a_2 at right, faceleft
    with easeinright
    body sandra sandra suit
    show sandra b_0
    with wipedown
    "As they reached the stairs, Connie transformed back into Sandra."

    show john a_0
    "John observed the transformation and, with a playful lilt in his voice, said:"
    
    show sandra at offscreenleft with easeoutleft
    show john a_13
    john "Okay, the illusion seems to fade after she goes away from my room, "
    
    show john a_10
    extend "as-in-ten-ded!"

# Scene's end.

# Scene 1.2.1
# Temple background. Day. Setsuna is in centre, she cleans the footpaths. There is other people at background. Setsuna hears young adults planning an all night party. She wants to reprimand them, but does not find the courage. Nemuru come in and scold them. Group don't want to conflict and leave the place. Setsuna watches them leave with a sad look. Phone ringing. It's a John, Setsuna is glad to hear him. John tells her that he will come in the evening. He has a big surprise for her. 

# Narrative
# Setsuna Otani, the miko of the local Shinto shrine, was extremely busy today. Her father, Nemuru, had announced that the shrine would be closed for repairs starting from tomorrow. 
# Despite the absence of holidays or special events, the temple was crowded with visitors. Consequently, Setsuna worked tirelessly, constantly moving from one task to another. 
# Adding to her burdens was her debilitating illness, making her already exhausted by noon. 
# It was for this reason that Setsuna decided to take a short break from the bustling crowd and retreated to sweep the pedestrian paths away from people.

# Scene begins
# Setsuna stood in front of the shrine, a broom in her hands, as she glanced towards the bustling crowd in the distance. 
# Slowly, she swept the paths, occasionally pausing to lean on the broom. 
# "I didn't expect such a turnout after the news of our sanctuary's temporary closure," she whispered to herself. 
# "It feels as crowded as it does on New Year's Eve. It's reassuring to see that our efforts are not in vain and that people truly want to support our sanctuary." 
# Setsuna's voice was soft as she muttered her thoughts. "I'm also grateful that a few other girls agreed to be miko with me today. I don't think I could have managed it alone."

# "Maiden, maiden!" Setsuna heard someone calling out to her. She let out a soft sigh. "Here we go," she whispered under her breath. "All I wanted was a moment of peace and quiet."

# A lonely nerd approached Setsuna with hesitation. "Hello, what do you need?" Setsuna mustered a tired smile. 
# "I... I want you to... you know... love," the guy babbled nervously. Setsuna's eyes widened in surprise. "Whaat?" she exclaimed. 
# "N-no, I mean, uh... I wrote a poem..." he stammered. "For me?" Setsuna marveled. 
# "N-no, it's for a certain girl. A beautiful one. Oh, I mean, you're pretty too..." he replied, avoiding eye contact with Setsuna.

# Suddenly, he took in a deep breath and held it for half a minute. Setsuna looked at him with a puzzled expression. "Are you okay?" she asked cautiously. 
# And then the guy blurted out without pause, "IwroteapoemforagirlIlovepleaseforetellmeifwellbetogether," then stared at the ground. 
# "Ah, so you need an omikuji!" Setsuna smiled, understanding his intent. "Sure, let's see what the Kami will foretell for you."

# They walked together towards the Omikuji corner, and on the way, Setsuna inquired, "Does the girl know about your feelings?" 
# Nervously, he replied, "She doesn't know yet, but if the foretell is good, I'll confess to her." 
# Setsuna found his awkwardness endearing and decided to uplift his spirits. "Even if the divination turns out to be unfavorable, it's still worth taking a chance," she reassured him. 
# "The deities sometimes enjoy playing games with mortals. Often, a victory snatched from the clutches of bad luck holds more value than one bestowed by good fortune." 
# "Thank you, miko," he murmured, his voice barely audible.

# Near the Omikuji corner, Setsuna asks if he has the fee. The boy assures her that he does and reaches into his pocket, only to find it empty. Each pocket he checks yields the same result.
# Frustration takes hold as he exclaims, "Oh, no. How could this happen? I didn't forget..." He pats his pockets in disbelief. 
# "Oh, I'm such a fool. I'm here with Inari, my sister. She wanted to buy an omamori for both of us, and I gave her the money. 
# I'll be right back to get it." "Wait," Setsuna interjects, shaking her head. "Don't worry, I have enough for the offering. 
# But make sure to bring the fee later, otherwise, the Kami might become displeased. Agreed?"

# "Yeah," he nods his head. "That's good," Setsuna smiles. "Now let's get started." 
# She places the offering in the donation box and instructs him, "Now, take the box of tubes and shake it. When one stick falls out, tell me the number written on its tip, and I will give you a divination that corresponds to that number, without looking."
# He follows her instructions, and after a moment, he says, "It's four." Setsuna looks surprised at the number. "W-well..." she stammers, gathering her thoughts.

# Author's Note: In Japan, the number 4 is considered to be unlucky, so Setsuna was confused about it

# "Is everything okay?" he asks, his anxiety evident. Setsuna hesitates for a moment, then forces a smile. "Yeah, yeah, everything's fine. Here's your fortune." 
# She covers her eyes and lets out a subtle sigh before taking a divination from the box without looking. "Let me see," the guy eagerly takes the fortune paper from Setsuna's hands. 
# "Daikyou. What does it mean?" he asks with concern. 
# Setsuna's voice is quiet as she responds, "Great misfortune."

# "That's a shame," he shakes his head. "And I still owe you. It's better for me to go get the money." Disappointed, he slips the paper into Setsuna's hand, turns, and walks away swiftly. 
# "Wait!" Setsuna calls out to him. "To prevent the bad prediction from coming true..." But he has already disappeared amidst the crowd. 
# "... it should be tied to a tree," the girl finishes her sentence, slightly quieter, and hides the paper in her pocket.

# "Suna, what are you doing here?" she heard a familiar voice to her right. It was Sakura, one of the girls who was part-time Miko today. 
# "Dear, you're white as a sheet" Sakura asked anxiously, "Is something wrong?". "Really? I must have missed taking my pills" Setsuna put her palm to her forehead "It's also pounding in my ears"
# Setsuna briefly recounted to her what had happened, but forgot to mention that he didn't take the paper. 
# "What a gentle lad" smirked Sakura "On the contrary, let him be happy - the deities tell to wait for a better time". 
# She glanced at Setsuna again "Let me wait for him and you better go because you look, to be honest, not good". "I'm fi..." Setsuna starting to protest.
# "Don't worry" Sakura winked "It's not a big deal to me, besides other people will want to do the fortune telling too. And you better get some rest."
# "You think so? Okay, thanks, I'll be off then" nodded Setsuna with relief. "You'll owe me a favor!" she heard Sakura's cheerful voice behind her.

# "Suna, what are you doing here?" she heard a familiar voice to her right. It was Sakura, one of the girls who was also a part-time miko that day.
# "Dear, you're as pale as a sheet," Sakura asked anxiously "Is something wrong?"
# Setsuna put her palm to her forehead. "Really? I must have missed taking my pills. It's also pounding in my ears." 
# Setsuna briefly recounted to her what had happened, but conveniently omitted the fact that the boy didn't have the fortune paper.
# "What a gentle lad," Sakura remarked, her tone dripping with sarcasm. "On the contrary, let him be happy. Perhaps the deities are telling him to wait for a more favorable time."
# Sakura glanced at Setsuna again. "Let me wait for him, and you better go because, honestly, you don't look good."

# "I'm fine," Setsuna started to protest.
# "Don't worry," Sakura interrupted with a sly smirk. "It's not a big deal for me. 
# Besides, I'm sure there will be plenty of people who will want their fortunes told. You should get some rest."
# "You think so? Okay, thanks. I'll be on my way then," nodded Setsuna, quietly relieved.
# "And remember, you'll owe me a favor!" she heard Sakura's cheerful voice behind her.

# However, Setsuna was reluctant to go to her room due to the bustling crowd that still filled the shrine. 
# Instead, she decided to return to sweeping the paths in an attempt to avoid the crowded areas. 
# Determined to find solace amidst the chaos, Setsuna focused on her task, diligently sweeping and clearing the pathways, finding a moment of peace amidst the commotion.  

# Scene 1.2.2

# However, an unpleasant surprise awaited Setsuna. As she returned to the area where she had been sweeping, she noticed a group of young people nearby. 
# They appeared to be college students, engaged in a rather boisterous discussion. Their voices filled the air, disrupting the tranquility of the shrine. 
# Setsuna sighed inwardly, knowing that her task would now be even more challenging with their presence.

# "Okay, one more time, what are we doing here?" asked one of them, dressed in a leather jacket. 
# "Honoring ancestors, spirits, and making wishes," the guy with glasses immediately responded. 
# "Toshi, I didn't ask what we've already done here," the first one said with pressure, "I asked what we're doing here right now." 
# "Waiting for Samantha and Mitsuru," intervened the biggest guy in the group. "Sam wanted to see what the priest would do."

# "Oh, right, ass and tits" chuckled the jacket "Wait, are they not coming right now?" 
# "Probably not," Toshi replied. "Jay, what did you expect from a Shinto shrine anyway?"
# "Honestly? That we'd finish up here real quick and go to Ron's. We still have alcohol to buy. Instead of sticking around until the local priest says a few ritual words," Jay grumbled.
# "Well, show some respect," the big guy's voice interjected. "It's important to Mitsuru. Sam's been wanting to see some ceremony for a long time, and here's an occasion like this."
# "Cut it," Toshi interrupted. "What do you mean we still have to buy the booze? You should have bought it yesterday!"

# "I've... been busy-y," Jay stretched out the phrase.
# "Doing what, exactly?" the big guy asked him coldly. 
# "Important things," Jay retorted defiantly. "Uh... a lot of important things."
# "Dalgur's Gate 3," Toshi spelled out, staring directly into his eyes. 
# "You can't blame me!" exclaimed Jay.
# "I can and I will," Toshi replied in a cold-blooded manner. "You know, calling you an idiot is giving you a compliment."
# "But now I know why he's in such a hurry," the big guy grinned broadly. "He can't get any sober chick."

# "Shut the fuck up Brock!" Jay hissed at him viciously. "I don't have this kind of problems. "Okay, here's an idea! Let's pick up some chicks and go to Ron's right now!"
# "And what about Sam and Mitsu?" asked Toshi politely
# "We'll figure something out on the way," Jay waved him off
# "Alright Casanova, we're ready to go at any moment, but you owe us the ladies" Brock said still grinning.
# "Easy! Look how it's done! Show any one of them and she'll ride with us" Jay raised his head proudly
# "That one" Toshi pointed out with a glance
# "B-But it's..." Jay muttered uncertainly.
# "Any one means ANY one. The choice is made" Brock said predatorily.
# "Okay, get the car ready" sighed Jay

# Once Jay moved away from them a bit, Toshi turned to Brock and said "I bet you twenty bucks he fucks up"
#"Sneaky little jap" Brock fake indignant "Let me bet on her punching him in the face".
#"I'll take that bet" smirked Toshi.

# Setsuna stood half-turned, listening to their conversation, occasionally glancing at the group of three. 
# A part of her wanted to intervene and give them a warning or even kick them out of the shrine. 
# However, as she looked in their direction, they appeared imposing and intimidating, dissuading her from confronting them. 

# So when Jay approached her, she tightened her grip on the broom, increased her sweeping speed, and purposely avoided making eye contact with him.

# "Hey, sweetie," Setsuna heard Jay's obnoxious voice calling out. "What are you doing?"
# "Working," Setsuna replied curtly, still avoiding eye contact. Her heart raced with unease.
# "Ha, so you're just a part-time worker, huh? Well, I've got a better offer," Jay continued. 
# "Me and the guys are heading to an awesome hangout right now, and we've got some prime seats for cool girls like you."
# Setsuna thoughtfully mumbled under her breath, "Cool girls?"
# "Yeah, you know, you've got that cool look," Jay remarked. "I bet you're always at the coolest parties. Trust me, this one we have lined up is gonna be amazing."
# Setsuna's voice carried a hint of sadness as she responded, "Sir, I can sell you an omamori amulet or assist with omikuji fortune-telling. 
# If you have any other requests, I probably won't be able to help you."
# "Did I say something wrong?" Jay asked, noticing the disappointment in Setsuna's eyes. "I can tell you're interested."
# Setsuna sighed softly. "I just can't," she said quietly.
# "You don't worry, we're not going to do anything bad, we're just having fun" Jay increased the pressure.
# He stood directly in front of Setsuna and put his hands on her shoulders. 
# Setsuna shuddered, trembled, and clutched the broom so tightly that her fingers turned white
# "You know, sometimes you have to face your fear to get a taste of life," Jay said in a confident tone of voice
# As if in a dream, Setsuna raised her eyes open with fear and met Jay's gaze
# "S-Sir, p-please..." she spoke quietly "I already t-told you..."
# "Oh, come on," Jay interrupted her. "Do you really think the priest will care? There are other mikos here. The old man won't even notice."

# "What won't the old man notice?" came Nemuru's voice. "I have been informed that there are three young men here disturbing the order, swearing and distracting the miko. I suppose you are one of them."
# "Oh, sir, it's okay. We're just chatting," Jay's eyes raced, "My friends and I are waiting for our girlfriends." He hurriedly removed his hands from Setsuna's shoulders and hid them behind his back.
# "Then I will ask you to leave the shrine grounds. {b}Now{/b}" Nemuru said confidently.
# "It's true father, they were talking loudly, but they didn't do anything wrong" Setsuna said in a very quiet and tired voice.
# "Father? Оh..." Jay whistled
# "On a normal day you'd get off with a warning, but today I want to minimize problems. So please {b}leave{/b} this place." There was steel in Nemuru's usually calm, peaceful voice.
# Jay looked first at him, then at Setsuna, and said. "I see, excuse me. My friends and I were just leaving."

# "What won't the old man notice?" came Nemuru's commanding voice. 
# "I have been informed that there are three young men here disturbing the order, swearing, and causing a commotion around the miko. I assume you are one of them."
# Jay's confidence wavered as he faced Nemuru's authoritative presence. "Oh, sir, it's just harmless conversation," he stuttered, avoiding eye contact. 
# "My friends and I are just waiting for our girlfriends."

# Nemuru's voice held a steely determination. 
# "On any other day, you may have received a warning," he stated firmly, his words laced with an intimidating tone. 
# "But today, I want to uphold the sanctity of this shrine. I insist that you leave this place immediately."

# "Father?" Jay whistled.
# He glanced hesitantly at Nemuru, then at Setsuna, before capitulating. 
# "I see. Excuse me. My friends and I were just leaving."

# Jay then rejoined his friends, sharing a few words that Setsuna couldn't discern. 
# With a heavy heart, Setsuna watched as the group walked away, moving farther from the shrine grounds.

# "Suna, are you okay? Did he do anything to you?" Nemuru looked at his daughter with concern and care. 
# Setsuna reassured him, "I'm fine, father. He just wanted to talk, and I was able to finish sweeping the walkways while we were conversing." 
# Nemuru let out a sigh of relief. "That's good to hear. Now, go and get some rest. You have been working tirelessly today." 
# Setsuna hesitated. "But, Dad, there's still so much work left to be done." 
# Nemuru smiled reassuringly. "Don't worry, I and the other girls will take care of it. You have done more than enough. Rest is important too." 
# Setsuna expressed her gratitude to her father and slowly, pausing occasionally to catch her breath, made her way to her room.

# Scene's end.


# Scene 1.3
# Inside of the temple. Setsuna tells her father that she has finished cleaning the paths.Nemuru tells her to go and rest as she is overtired. Setsuna is surprised because there is still work to be done, but Nemuru is adamant. Setsuna goes to her room and calls Izuna there. Izuna wants to come to the temple, but Setsuna says that it's not an option. Lots of people here today. And in the evening John promised to come and asked her to be alone. Izuna jokes that John has finally made up his mind to reach second base. Setsuna is embarrassed. The girls decide to meet tomorrow at the mall.
# Comment
# Izuna is an extremely important character. When Sirenasu suppresses Setsuna's consciousness, it is Izuna who will be able to reach out to Setsuna.

# Scene 1.4
# Timeskip. Temple (night/ evening). Wind howling. Thunder sounds. Setsuna is sad. Even the weather is against her as it prevents her from getting her surprise. Nemuru is busy somwhere else. John enters the door. Setsuna is both very happy and worried about John. John replies that it's okay, just the wind. Setsuna is touched by his words.They talk like old friends and in conversation John avoids the subject of surprise all the time. At some point, Setsuna breaks down and directly asks him what surprise he was talking about. It's starting to rain. John looks at her and then casts "Verba obedy" and orders her to believe his words implicitly. He tells her that he is a magician and has developed a healing spell especially for her. She believes him (hypnosis), but doubts. In all the stories she knows, magic is an evil thing. John says he designed the spell especially for her. Setsuna flattered. She agrees. Outside sounds  a loud clap of thunder. They write a note to Nemuru and leave.
# Comment
# He wants Setsuna to believe him quickly, and the hypnosis spell has the least mana cost.

# Scene 1.5
# To perform the ritual, they need to find a secluded place. Setsuna says he knows something like this nearby. They go there. John asking what is the place. Setsuna replies that this is their family crypt. John is surprised. Setsuna replies that it only sounds scary, it's actually a quiet, peaceful place where she goes almost every day. She clarifies that for the ritual, you don’t need to draw signs on the walls with someone’s blood. John replies that it is not necessary, he will give her a small bundle in her hand and when he gives her a signal, she will have to squeeze it. The wind is howling, but the rain is no longer falling. Before entering the crypt, John notices ritual inscriptions in ancient Japanese. He doesn't like them, but he doesn't say anything to Setsuna. Inside crypt, as Setsuna said, it is really dry, warm, and even has a sense of safety. Setsuna talks a little about her family. After that, they begin the ritual. Thunder sounds for the last time.
# Comment
# "Subsequently, John will think that it was in these inscriptions that the reason for failure was.
# I will try to find background, but scene can be done at the temple stair background."

# Scene 1.6
# The ritual itself is boring. John walks around Setsuna in circles and monotonously mumbling some incomprehensible abracadabra for about 10 minutes. Setsuna even starts to fall asleep it was quite a hard day to her. At the end John suddenly shouts loudly "Grahana aadaa p`ara praana". And gives a signal. Then Setsuna squeezes her hand. It turns out that there was an egg in the package. Regular chicken egg. Setsuna thinks she hears a quiet whispers and feminine giggles for a second. But what worries her much more is that now her clothes and the floor are dirty. Setsuna gets mad at John - he should have warned her. John tells her it's for the ritual (lie), but she doesn't believe him. John is surprised because he did not remove the hypnosis spell from her yet.
# Comment
# "Take the life of another for yourself" Sanscrit. John didn't figure the translation.  And instead of the word "rebirth" it turned out wrong

# Scene 1.7
# They clean up in the crypt and leave it. At the way home they are silent for a some time. Setsuna thinks that John is playing some joke at her. John ask her how she feel. She replies that she is dissapointed in him. And even though it's late enough she asks him to leave. John wants to stay, but he sees that Setsuna is not in the mood, so he obeys.
# Comment
# How late is it happening? Approximately between 00.00 and 01.00 so it's relatively early. He did not come home drunk at 4 in the morning ... on the third day.

# Scene 1.8
# Setsuna returning at the temple. Nemuru is worried about her, but she tell him it's ok. She just walk with John Davis. Nemuru scolds her, but calms down after a tirade. Offers to drink tea, and then go to bed. Setsuna agrees. They go to their rooms. Nemuru fall asleep, but Setsuna have insomnia. She decide to take a walk around. During the walk, she calms down and decides to forgive John for his inappropriate joke. Although, of course, to tease him a little. Than she return to her room and fall asleep.
# Comment
# Here, when Setsuna walks near the temple, is need to insert CG (Day Zero).

# John gets home without incident, so there isn't even a special scene.

# Day 2
# Scene 2.1
# John's room. Morning. The alarm clock is ringing. John hardly wake up (slow animation). Mumbling that he feel like he been hit by a truck. Good thing is today is day off and he don't need to go to Tina Koya. He has a migraine. He slowly go to the bathroom. Second good thing is Holly gone on her college trip for a whole month, so there is no one in the bathroom. While doing his morning routine, John begins to notice that something is wrong with him. He didn't just "didn't get enough sleep" something else is wrong. John return to his room. After a bit of research, John realizes that his mana hasn't been restored. He shocked. But he reassures himself by the fact that he must have really had little rest. He just needs to wait and the mana will be replenished.
# Comment
# "There is potential here for a second storyline about John and his mana pool.
# I just thought that the wizard is absolutely OP on Setsuna until about halfway through the story, when she starts using supernatural powers. So now John is focused not on Setsuna, but on his mana and doesn't see beyond his own nose."

# Scene 2.2
# Temple. Morning. Setsuna waking up in her room. Feels as usual. Do her morning routine and go to the kitchen. Her father is already here. She feel urge to kiss him, but doesn't take mind on it. Nemuru tell her that the temple is closed for scheduled maintenance, so it turns out that she is free for about a week. Since yesterday was quite difficult, Setsuna is glad. She tell Nemuru that she have plan for today to go to the mall with Izuna. Nemuru agrees to let her go there. Setsuna smiles and kiss him on the cheek. She feels a little energized and Nemuru feels pleasure. After, Setsuna leave the place.
# Comment
# It doesn't mean she's grounded or Nemuru controls her every move. It rather means that he will deal with the affairs himself, without his daughter

# Scene 2.3
# John's room. He takes headache pills (insert name here) and studuing the book, but find nothing. He decide do not use mana today. He thinks it's because the ritual inscriptions from yesterday. John decides to take a break and also find out how Setsuna is doing. He try to call her, but she drop the call. John think that Setsuna is still mad at him. The phone ring in John's hand. That's Kat. She suggests going to the movie, the prequel to "The Baron of the Triangles" is still on. John don't think movie will be good, but for a distraction of his current situation is agree to go. 

# Scene 2.4
# Setsuna and Izuna meet in front of the mall. Izuna remarks that Setsuna looks very cheerful. Izuna ask what happened yesterday with surprise and Setsuna answer that it was just a prank. She again feel urge to kiss, now Izuna. But again don't pay attention. She doesn't say bad things about John, but remark his childish behavior. After that they go to the mall. They hang out there for some time. Izuna notices that Setsuna doesn't get tired like usual.

# Scene 2.5
# The girls leave the mall, move away from it a little. Izuna remembers that she left something important at the mall and returns there. Setsuna stays waiting outside. Next to her is a man with a big dog (German Shepherd, Doberman or something like that (what kind of sprite can I find). The phone rings, it's John, but the Setsuna doesn't have time to answer.Suddenly the dog tries to attack Setsuna. The beast tries to get off the leash, growls loudly, barks with all her might, tries to bite Setsuna. the owner barely restrains the dog. Setsuna is frozen with fear. At this moment, a girl unknown to her stands between her and the dog. The girl chases the dog away. The girl introduces herself as Flavia Lucca. Izuna runs up, she saw everything, but could not run in time. Setsuna and Izuna hug and Setsuna kisses Izuna on the cheek. 
# Comment
# "Is it possible to interrupt the animation of a conversation on the phone?
# Setsuna is afraid of dogs. This will be important in the future. Sirenasu is a completely separate person, moreover, Setsuna will remain. And they will have dialogues among themselves. But some things they have in common"

# Scene 2.6
# All three girls go away of this place. They go to the food court, they decided to eat. Setsuna is surprisingly fine, but Izuna is dizzy. She must have been worried about her friend. Flavia turns out to be a very pleasant, albeit somewhat boastful, personality. They start to feel symphaty to each other.Izuna says he doesn't feel well and goes home.Setsuna initially tries to go after her, but Izuna stops her. Says it's nothing to worry about. And even to some of her surprise, Setsuna stays with Flavia. The conversation turns to John. Upon hearing of his prank, Flavia proposes a plan for revenge.
# Comment
# Izuna is fine. She just needs to rest.

# Scene 2.7
# Evening. John and Kat are at the cinema. The phone rings. Call from Setsuna. Much to Kat's annoyance, John answers the phone. Setsuna greets him cheerfully. Kat doesn't like this. John asks how she feels. Setsuna reports that apparently being angry at John gives her strength. But if he wants to be forgiven, then today she is waiting for him in a nightclub. John is surprised. Setsuna explains that she has wanted to go to a place like this for a long time. But there is one condition - she is with a friend, so let John take some guy with him. And drop the call. Katrina stares at John. John invites her to go to a nightclub. Katrina sighs but agrees. But she sets a condition - let Kiyoshi go with them. John agrees.

# Scene 2.8
# "Night. In front of the doors of the nightclub. They meet. John, Kat, Setsuna, Flavia and Kiyoshi. Seen two beautiful girls Kiyoshi start being Kiyoshi. But the girls do not behave hostile, on the contrary, they accept his inept compliments.Kat is starting to get suspicious. 
# They enter the club. They walk into the club and sit on the couch. Kiyoshi finds himself between Flavia and Setsuna. 
# They chat for a while. Kat acts somewhat cold towards Setsuna. Flavia offers to go to the dance floor. John refuses and also Kat. Kiyoshi, fascinated by the two girls, agrees. And during the dance, a plan of revenge is executed. Setsuna was supposed to give Kiyoshi a demonstrative kiss. But being in front of Kiyoshi, she felt an incredible, irresistible, brutal craving to kiss him. And she kisses him hard on the lips for about a minute. Everybody shocked."
# Comment
# Finally, the "kiss of the vampire". In general, this is the transfer of life. In this case, the victim feels euphoria

# Scene 2.9
# After ending the kiss, Setsuna gets a huge boost of energy. She does not know what happened, she is terribly ashamed and she runs to the toilet. In the toilet she starts masturbating furiously. The heart is beating like crazy, some kind of rhythm is pounding in the ears, all the senses are heightened. Setsuna doesn't know what's happening to her, but she can't stop.In ecstasy she bites her tongue until it bleeds. With a loud moan she cums. Catching her breath, on shaky legs, she leaves the toilet stall to wash. At this time, a girl comes out of the next stall. Setsuna is very ashamed. The girl while giggling tells Setsuna have a beautiful voice and jokingly calls her "Siren". Than she leaves the toilet.

# Scene 2.10
# Meanwhile Kat makes a scene. She blames Flavia and tries to leave with John. John hasn't been feeling very well all day. Therefore, he, seeing that everything is in fine with Setsuna (naive), leaves with Kat. Flavia think that revenge is complete, though Setsuna overdid it. Kiyoshi feels very strange. Feeling as if he drank a lot of alcohol or swallowed some forbidden pills. Setsuna returns. John and Kat are gone. Setsuna doesn't know what came over her. She didn't want it to turn out like this.

# And here is the choice
# a) Stay in the club (Thrall Kiyoshi)
# b) Go to Flavia's place (Thrall Flavia)

# Scene 2.11a
# Having dealt with excitement, Setsuna returns to the couch. She feel great, best feeling of her life. The most intense at least. She starts flirting with Kiyoshi. She has little experience, it does not work very well. But Kiyoshi doesn't need much. Seeing it. Flavia leaves, realizing that they will figure it out without her. Setsuna kisses Kiyoshi again, this time he swallows her blood with saliva. (Setsuna, conditionally, is full. So the same effect does not occur). And Kiyoshi breaks the whole mood - he calls her a slut. Setsuna slaps him. Setsuna slaps him and goes to Izuna. In the morning she wakes up in the first stage of transformation.
# Comment
# No, the guy can be understood, he seems to be under cocaine now and not quite in control of himself, but still ...

# Scene 2.11b
# Consumed by shame, Setsuna approaches Flavia and asks her to leave and take Setsuna with her. Leaving the club, Setsuna realizes that the excitement has not yet passed. She approaches Flavia and kisses her on the lips. Flavia is surprised, pulls away, about manages to swallow Setsuna's blood. She says that she likes boys, and Setsune seems to have had enough adventures today. They come to Flavia and go to bed. The next morning, Setsuna and Flavia wake up in the first stage of transformation.



placeholder
