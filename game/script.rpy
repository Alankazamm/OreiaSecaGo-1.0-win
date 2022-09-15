# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Professor")
init:
    transform entrance_left:
        yalign 1.0
        xanchor 1.0
        xpos 0.0
        linear 1.0 xanchor 0.0
    
    transform entrance_right:
        yalign 1.0
        xanchor 0.0
        xpos 1.0
        linear 1.0 xanchor 1.0

# The game starts here.

label start:
    $ round = 0
    $ vitoria = 0
    $ derrota =0
   

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    


    image prof animated:
        "fala1"
        pause .5
        "fala2"
        pause .5
        repeat
    
    show prof animated
    with dissolve

   
    

  
  
    # These display lines of dialogue.

    p "Então você estava dormindo na aula novamente é?"

    play music "fundofx.mp3"  loop

    p "Continuando assim você vai arranjar encrenca!"


    python:
            name = renpy.input("Qual o seu nome?")

            name = name.strip() or "Aluno"

    p "Muito bem, [name],"

    p "Segundo o que eu pude interceptar dos seus dados trafegados, pois eu tenho 500 anos de experiência com REDES,"
    p "Inclusive os índios dormiam no chão antes de eu apresentá-los à rede..."
    p "Mas enfim, prosseguido..."
    p "Você já maratonou três séries, incluindo Grey's Anatomy, durante a aula!"
    p "E ainda por cima PIRATEADO!"
    p "Segundo a legislação, aplicada às REDES de interwebs, você vai ficar de DP e pode ter que pagar indenização à Netflix!"      
    p "Seu OREIA SECA!"

    p "Mas pra sua sorte, [name], você pode se safar dessa!"
    p "SE..."
    p "Me derrotar no Jo Ken Po!"
    p "Sim, eu hackeei o pedra papel tesoura com meu conhecimento e experiencia em REDES! E quero testar isso."
    p "Duvida? Mas é claro que é possível, se você for mestre sênior pica das REDES, igual eu..."
    
    p "Mas chega de enrolação, vamos começar logo isso."
    
    $round+=1
    jump jokenpo


    label jokenpo:
        image profesperando ="esperando1.png"

        default escolha = 0
        hide prof animated
    
        
        image profesperando = "fight1.png"
        show profesperando

        

    
    
        p "Faça sua escolha:"

        

        window hide

        screen bar_nav():
            imagebutton auto "pedraicon_%s.png":

                focus_mask True
                xanchor 1
                yanchor 1
                xpos 0.25
                ypos 0.75
                
                action Jump ("escolha1" )
               
               
            
            imagebutton auto "papelicon_%s.png":
                    focus_mask True
                    xanchor 1
                    yanchor 1
                    xpos 0.5
                    ypos 0.75
                    
                    action Jump ("escolha2" )
                
            imagebutton auto "tesouraicon_%s.png":
                focus_mask True
                xanchor 1
                yanchor 1
                xpos 0.75
                ypos 0.75
                
                action Jump ("escolha3" ) 


        call screen bar_nav
        "a"
        
    label escolha1:
    $ escolha = 1
    
    jump resultado

    label escolha2:
    $ escolha = 2
    
    jump resultado

    label escolha3:
    $ escolha = 3
    
    jump resultado


    label resultado:
    $ profmao = renpy.random.randint(1, 3)
    

    if escolha == 1:
       
        if  profmao == 1:
            show pedra1
            with dissolve
            pause 0.5
            p "Sua escolha foi:"
            p "Pedra!"
            "..."
            p"Eu também hehe!"
            hide pedra1
            with dissolve
            
        
        if  profmao == 2:
            show papel1
            with dissolve
            pause 0.5
            p "Sua escolha foi:"
            p "Pedra!"
            "..."
            hide papel1
            show vangloriando1
            
            p"Venci! Papel!"
            $ derrota +=1
            hide vangloriando1 with dissolve


        if profmao == 3:
            show tesoura1
            with dissolve
            pause 0.5
            p "Sua escolha foi:"
            p "Pedra!"
            "..."
            hide tesoura1
            show busted1
            
            p"Droga!"
            $ vitoria +=1
            hide busted1 with dissolve
    
    if(escolha==2):

       
        if profmao == 1:
            show pedra2
            with dissolve
            pause 0.5
            p "Sua escolha foi:"
            p "Papel"
            "..."
            hide pedra2
            show busted2
            
            p"Oh não! escolhi pedra!"
            $ vitoria +=1
            hide busted2 with dissolve
           
        if  profmao == 2:
            show papel2
            with dissolve
            pause 0.5
            p "Sua escolha foi:"
            p "Papel!"
            "..."
            p"Empatou, papel"
           
            hide papel2 with dissolve
        if  profmao == 3:
            show tesoura2
            with dissolve
            pause 0.5
            p "Sua escolha foi:"
            p "Papel!"
            "..."
            hide tesoura2
            show vangloriando2
            p"Ganhei haha! Tesoura!"
            $ derrota +=1
            hide vangloriando2 with dissolve
    
    if (escolha==3):
       
        if  profmao == 1:
            show pedra2
            with dissolve
            pause 0.5
            p "Sua escolha foi:"
            p "Tesoura!"
            "..."
            hide pedra2
            show vangloriando1
            p"Toma, oreia seca! Haha!"
            $ derrota +=1
            hide vangloriando1 with dissolve
        if  profmao == 2:
            show papel2
            with dissolve
            pause 0.5
            p "Sua escolha foi:"
            p "Tesoura!"
            "..."
            hide papel2
            show busted3
            p"Deu sorte desta vez, [name]!"
            $ vitoria +=1
            hide busted3 with dissolve
        if  profmao == 3:
            show tesoura2
            with dissolve
            pause 0.5
            p "Sua escolha foi:"
            p "Tesoura!"
            "..."
            hide tesoura2
            show kawai1
            p"Empatou, hihi *w*"
            hide kawai1 with dissolve
           
    p "cotinuando"
    if vitoria>=3:
        jump hapend
    
    if derrota >=3:
        jump sadend

    if derrota<=2:
        if vitoria<=2:
            $ round+=1
            jump jokenpo

    label hapend:
        hide profesperando
        image professurpreso = "surpreso1.png"
        image gameover = "gameover1.png"
        image cidade = "cidade1.jpg"
        image profechorando = "busted2.png"
        show professurpreso with dissolve

        p"Não acredito!"
        p "Em todos esses anos adquirindo conhecimento em Redes."
        p"Diversas vezes capa da revista Somelliers das Operadoras de Internet..."
        p"Campeão pra caralho em ligar pra cornetar a Vivo, Oi, dentre outras!"
        hide professurpreso with dissolve
        show profechorando with dissolve
        p"Tudo bem seu oreia seca..."
        p"...desculpe uh..."
        p"mestre [name]"
        p"Você não precisa assistir às aulas!"
        p"Afinal, acabou de me provar aqui que pode me superar no conhecimento pica das galaxias em Redes!"
        p"Ok, Ok!"
        p"Você pode usar minhas videoaulas e comercializar como ASMR contra a insônia!"
        hide profechorando with fade
        stop music
        show cidade with fade
        "* Você abre um canal no YouTube, logo em seguida. *"
        "* Seus ASMRs bombam instantaneamente, muitos afirmam que milagrosamente não conseguem ficar acordados ouvindo*"
        "* Você fica muito rico e cria uma cidade, seguindo os preceitos das REDES *"
        "Graças à essa cultura, a cidade se desenvolve e se torna a Wuakanda da fibra ótica!"

        hide cidade with fade
        show vitoria1 with fade
        pause 1.0
        jump start





    label sadend:
        hide profesperando
        image professor = "ligando1.png"
        show professor with dissolve

        p "Você perdeu, estou ligando aqui pra polícia federal e..."
        p "...infelizmente, [name], você está preso por falta de lubrificação das cartilagens auriculares."
        p "Alou, é da swat?"
        p "Pode invadir a casa do Oreia Seca!"
        hide professor with fade

        "..."

        "* Você ouve um barulho dentro de sua casa *"
        "* E decide se virar para trás para ver *"

        image swat = "swat1.jpg"
        show swat at offscreenright
        with None
        show swat at left
        
        with move

        "O Andrézão x9vou a localização do seu IP vagabundo!"
        "Isso é pra pensar duas vezes antes de dormir na aula!"

        hide swat with fade
        stop music
        play sound "gameoverfx.mp3"
        show gameover with fade
        pause 1.0
        jump start

        

    # This ends the game.

    return
