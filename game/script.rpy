# Déclarez les personnages utilisés dans le jeu.

image foret perdu = im.Scale("premiere_scene.png", 1280, 720)
image champs fleurs = im.Scale("champs_fleurs.png", 1280, 720)
image foret = im.Scale("foret.png", 1280, 720)
image taniere lapin = im.Scale("taniere_lapin.png", 1280, 720)
image chemin chat = im.Scale("chemin_chat.png", 1280, 720)
image jour = im.Scale("scene_finale_jour.png", 1280, 720)
image nuit = im.Scale("scene_finale_nuit.png", 1280, 720)
image perdu = im.Scale("perdu.png", 1280, 720)

image aelita triste = im.Scale("aelita_triste.png", 300 , 500)
image aelita impressionnee = im.Scale("aelita_impressionnee.png", 300, 500)
image aelita hesitante = im.Scale("aelita_hesitante.png", 300, 500)
image aelita frissonnante = im.Scale("aelita_frissonnante.png", 300, 500)
image aelita tracassee = im.Scale("aelita_tracassee.png", 300, 500)
image aelita heureuse = im.Scale("aelita_heureuse.png", 300, 500)
image aelita rassuree = im.Scale("aelita_rassuree.png", 300, 500)
image serpent = im.Scale("serpent.png", 300, 500)
image lapin = im.Scale("lapin.png", 300, 500)
image loup = im.Scale("loup.png", 300, 500)
image chat = im.Scale("chat.png", 300, 500)
image parents = im.Scale("parents.png", 300, 500)

define a = Character(_("Aelita"), color="#ffffff")
define l = Character(_("Lapin"), color="#ffffff")
define s = Character(_("Serpent"), color="#ffffff")
define lo = Character(_("Loup"), color="#ffffff")
define c = Character(_("Chat"), color="#ffffff")
define p = Character(_("Parents"), color="#ffffff")

# Le jeu commence ici
label start:
    play sound "Sons/coq.ogg"
    scene foret perdu
    show aelita triste at left
    
    "Une petite fille est perdue seule dans les bois. Les larmes aux yeux, elle est triste. Elle se demande si elle va réussir à retrouver son chemin."
    
    play music "Sons/rouge-gorge.ogg"
    
    a "Euh ... y a quelqu'un ? S'il vous plaît, aidez-moi"
    
    "Elle entend du bruit. Elle voit un serpent sortir de derrière les arbres."
    
    play music "Sons/snake.ogg"
    
    show serpent at right
    
    s "Ne pleure pas mon enfant."
    a "Tu parles ?"
    s "C'est étonnant, mais oui. Je connais bien cette forêt. Je peux t'aider à retrouver ton chemin."
    a "Vraiment ?"
    s "Biensûr ... Je tiens toujours mes promesses."
    
    "Soudainement, elle entend un bruit. Un lapin vient d'apparaître à ses côtés. Il défi le serpent du regard."

    hide serpent
    show lapin at right
    play music "Sons/rouge-gorge.ogg"
    
    l "Ne l'écoute pas petite fille. Ce serpent est un menteur né. Contrairement à ce qu'il dit, je connais vraiment tous les coins de cette forêt."
    
    hide aelita triste
    show serpent at left
    
    s "Ne choisi à pas à sa place. C'est son choix."
    l "Bien ... laissons la petite décider."
   
menu :
    "Suivre le Serpent" :
        jump scene_serpent
    "Suivre le Lapin":
        jump scene_lapin
        
label scene_serpent:
    play music "Sons/champs_fleurs.ogg"
    scene champs fleurs
    show aelita impressionnee at left
    
    a "Waouh ! C'est magnifique !"

    "Des bruits de pas se rapproche de la petite fille."
    
    hide aelita impressionnee
    show loup at right
    show aelita hesitante at left
    
    lo "J'ai entendu dire que tu cherchais ton chemin. Tu as besoin d'aide mon enfant ?"
    
    "La petite fille n'a pas le temps de réagir. Une boule de poils apparaît. C'est un chat."
    
    hide loup
    play music "Sons/cat.ogg"
    show chat at right
    
    c "Je peux aussi t'aider à retrouver ton chemin. À toi de choisir."
    
    hide aelita hesitante
    show aelita tracassee at left
    
    "Après avoir longtemps réfléchi, elle prend enfin sa décision."
    
    hide aelita tracassee
    hide chat
    
    a "Allons-y !"
    
menu :
    "Suivre le Chat" :
        jump scene_chat
    "Suivre le Loup":
        jump scene_loup

label scene_lapin:
    play music "Sons/scene_lapin.ogg"
    scene taniere lapin
    show aelita frissonnante at left
    
    a "On va où ?"
    
    "La petite fille se sent mal à l'aise et commence à regretter son choix."
    
    show lapin at right
    
    l "Dans un endroit sûr."
    
    "Pourtant la petite fille ne se sent pas bien. Personne n'est là."
    
    hide lapin
    show loup at right
    
    lo "J'ai entendu dire que tu cherchais ton chemin. Tu as besoin d'aide mon enfant ?"
    
    "La petite fille n'a pas le temps de réagir qu'une boule de poil apparaît. C'est un chat."
    
    hide loup
    show chat at right
    play music "Sons/cat.ogg"
    
    c "Je peux aussi t'aider à retrouver ton chemin. À toi de choisir."
    
    hide aelita frissonnante
    show aelita tracassee at left
    
    "Après avoir réfléchi pendant longtemps, elle fait enfin son choix."
    
    hide aelita tracassee
    hide chat
    
    a "Allons-y !"
    
menu :
    "Suivre le Chat" :
        jump scene_chat
    "Suivre le Loup":
        jump scene_loup
        
label scene_chat:
    play music "Sons/scene_cat.ogg"
    scene chemin chat
    show aelita rassuree at left
    
    a "C'est sympa ici. Tu habites ici ?"
    
    show chat at right
    
    c "Je vis un peu partout."
    
    "Les heures passent. Ils arrivent près d'une maison."
    
    hide chat
    hide aelita rassuree
    hide chemin chat
    play music "Sons/scene_cat.ogg"
    scene jour
    show parents at left
    
    p "Aelita !"
    
    show aelita heureuse at right
    
    a "Maman ! Papa !"
    
    hide parents
    hide aelita heureuse
    hide jour
    
    scene nuit
    
    play music "Sons/nuit.ogg"
    "La petite fille est heureuse de retrouver sa famille. Avant de se coucher,sa maman décide de lire son histoire préférée. Grace à son histoire préférée, elle comprend enfin qu'il faut faire attentions aux apparances."
    
    return
    
label scene_loup:
    scene foret
    show aelita frissonnante at left
    show loup at right
    play music "Sons/scene_chien.ogg"
    a "J'ai froid"
    
    lo "Ne t'inquiète pas ... On est bientôt arrivés."
    
    hide aelita frissonnante
    hide loup
    
    "Le chemin est sombre. Elle n'est pas rassurée."

    hide foret
  
    scene perdu

    "La petite fille a fait confiance à la mauvaise personne. Elle ne réussi pas à retrouver son chemin."
