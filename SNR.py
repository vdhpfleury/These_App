import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## Définition des constantes
h   = 6.626e-34  # Constante de Planck (m^2 kg / s)
c   = 3e8        # Vitesse de la lumière (m / s)
k   = 1.381e-23  # Constante de Boltzmann (m^2 kg / s^2 K)
pi  = np.pi

# Définition des fonction : 

def fonction_porte(x, a, b):
    """
    Fonction porte : Retourne 0 si x est dans l'intervalle [a, b], sinon retourne 1.
    """
    return np.where((x >= a) & (x <= b), 1, 0) 


st.title("Rapport Signal Sur Bruit Appliqué à l'Interférométrie")

st.subheader("Sommaire", divider="gray")
col1, col2 = st.columns(2)
with col1 : 
    st.markdown(""" 
    - **I. Rapelle de probabilité - Loi de Poisson**
        - Rappels
        - Moyenne
        - Variance
        - Ecart type
        - Propriétés des estimateurs
    - **II. Calcul du rapport signal sur bruit (=SNR)**
        - Principe générale
        - Evolution en fonction du temps d'intégration
        - Source de bruit
            - Le bruit de photon  
            - Le bruit thermique  (=Sky)
            - Le bruit de recture (=Read Out Noise)
            - Le bruit de repliement spectrale
            - La fluctuation de phase (=Piston jitter)
            - Le bruit zodiacale
        - SNR d'un interféromètre à 2 télescope**
    - **III. Optimisation du SNR**
        - Principe de l'Apodisation
            - Apodisation appliqué à un interféromètre à 2 colelcteurs
    """)

with col2 : 
    st.markdown("""
    - **IV. SNR de MATISSE**
        - SNR du flux de cohérence
        - SNR de phase 
        - Apodisation appliqué à MATISSE

    - **V. SNR d'un interféromètre spatial à 2 téléscopes**

    - **VI. Simualteur de SNR d'un interféromètre spatiales à 2 teléscopes**
        - Paramètres de la cible
        - Paramètres du collecteurs
        - Calcul du SNR
            - Sans Apodisation
            - Avec Apodisation
    - **VII. Conclusions**
    """)

# Formalisme d'organisation du code
# N° de Section
################################################## Titre de Section
########################################## Sous titre de Section
################################## Sous Sous titre de Section
column_1, column_2 = st.columns(2) 
with column_1 : 
    test = 0
with column_2 : 
    test = 0


# I.
##################################################  Rapelle de probabilité
st.subheader("I. Rappels de probabilité - Loi de Poisson", divider="gray")

################################## Sous Sous titre de Section
st.markdown("**Rappels**")
st.markdown("""L'occurence de phénomènes discrétisables suit une distribution de probabilité de Poisson qui se formalise comme suit : """)
st.latex("p(X = k) = \\frac{e^{-\lambda} \cdot \lambda^k}{k!}")
st.markdown("""L'interprétation d'une tel loi de probabilité se fait tels que l'évènement $X$ à une probabilité $P(X=k)$ de se produire $k$ fois en sachant que cet évenement ce produit en moyenne $\lambda$ fois dans un interval de temps finit et connu.""")
st.markdown("La dualité onde-particule de la lumière nous permet la considérer comme une particule transportant de l'énergie, donc comme un phénomène discrétisable.")
st.markdown("Alors pour étudier les signaux lumineux, on utilise cette distribution ayant des indicateurs de la vrai valeur du nombre de particule detecté avec un certain degrès de confiance intrinsèque à la nature de la lumière.")
st.markdown("Autrement dit, on va chercher à determiner la moyenne et l'écart type de cette distributions pour retrouver la bonne valeur de notre signal. ")

################################## Sous Sous titre de Section
st.markdown("**Moyenne**")
st.markdown("Par définition, la moyenne, ou l'espérence noté $E$, d'une loi de probabilité s'exprime tels que : ")
st.latex("E(X) = \sum k \cdot p(X=k)")
st.markdown("""
$= \sum_i k \cdot \\frac{e^{-\lambda} \cdot \lambda^k}{k!}$

$= \sum_i  \cdot \\frac{e^{-\lambda} \cdot \lambda^k}{(k-1)!}$

$= e^{-\lambda} \cdot \sum_i  \cdot \\frac{\lambda \cdot \lambda^{k-1}}{(k-1)!}$

$= \lambda e^{-\lambda} \cdot \sum_i  \cdot \\frac{\lambda^{k-1}}{(k-1)!}$

$= \lambda e^{-\lambda} \cdot e^{\lambda}$

$= \lambda $

""")

st.markdown("On retrouve bien le résultat connue pour une loi de Poisson, l'espérance de cette dernière vaut : $E(X) = \lambda$")

################################## Sous Sous titre de Section
st.markdown("**Variance**")
st.markdown("De la même façon que pour l'espérance, on redéfinie la variance, noté $V(X)$ d'une loie de poisson : ")
st.latex("V(X) = E(X^2) - E(X)^2")
st.markdown("Nous venons de voir que $E(X) = \lambda$ donc $E(X)^2 = \lambda ^2.$" )
st.markdown("Il reste à déterminer $E(X^2):$")
st.latex("E(X^2) = \sum k^2 \cdot p(X = k)")


st.markdown("""
$= \sum k^2 \cdot \\frac{e^{-\lambda} \cdot \lambda^k}{k!}$

$= e^{-\lambda} \lambda \cdot \sum  k \\frac{\lambda^{k-1}}{(k-1)!}$

$= e^{-\lambda} \lambda \cdot  \sum \\frac{d}{d\lambda}(\\frac{\lambda^k}{(k-1)!}) $

$= e^{-\lambda} \lambda \cdot  \\frac{d}{d\lambda} [ \sum  \\frac{\lambda^k}{(k-1)!} ] $

$= e^{-\lambda} \lambda \cdot  \\frac{d}{d\lambda} [\lambda\cdot \sum  \\frac{\lambda^{k-1}}{(k-1)!} ] $

$= e^{-\lambda} \lambda \cdot  \\frac{d}{d\lambda} [ \lambda \cdot e^{\lambda} ] $

$= e^{-\lambda} \lambda \cdot  (e^{\lambda} + \lambda e^{\lambda} ) $

$= e^{-\lambda} \lambda \cdot  ( 1 + \lambda ) \cdot e^{\lambda} $

$= \lambda + \lambda^2 $

""")

st.markdown("""Finalement on obtient le résultat suivant pour la variance : """)
st.latex("V(X) = \lambda + \lambda^2 - \lambda^2 = \lambda")

################################## Sous Sous titre de Section
st.markdown("**Ecart type**")
st.markdown("Par définition l'écart type quantifie la disperssion moyenne carré des données autour de la moyenne d'une variable aléatoire. Il est définie comme la racine carré de la variance soit :")
st.latex("\sigma(X) = \sqrt{V(X)} = \sqrt{\\frac{1}{n} \cdot \sum^n_{i=1} (x_i - \\bar{x})^2} ")
st.markdown("Basé sur nos démonstrations précèdentes on trouve : $\sigma(X) = \sqrt{\lambda}$")



st.markdown("**Propriétés des estimateurs**")
st.markdown("Nous ne redémontrerons pas toute les propriétés de ces estimaneurs, i.e. $E$ et $V$, mais rappelons seulement quelque une d'entre elle lors de aléatoire type $Y= aX_1 + b X_2$ ou $X_1$ et $X_2$ sont des variables aléatoire suivant les la même distribution de probabilité :")
st.latex("E(Y) = E(aX_1 + b X_2) = a E(X_1) + b E(X_2)")
st.latex("V(X_1 + X_2) = V(X_1) +V(X_2) + 2 \cdot COV(X_1, X_2) ")
st.latex("\sigma(X_1 + X_2) = \sqrt{V(X_1 + X_2)} =  \sqrt{ V(X_1) + V(X_2) + 2 \cdot COV(X_1, X_2)} ")

st.markdown("*Rappel sur la Covariance*")
st.markdown("La covariance entre deux variables aléatoires $X$ et $Y$, noté $COV(X,Y)$, quantifie la variations commune de ces variables aléatoires. Elle s'interprète de la façon suivante : si elle est positive alors les VA évoluent dans la même direction. Autrement dit elle ont tendance à augmente/dimunier de façon simultané. A contrario, si la covariance est négative, cela signifie que l'une des VA augmente alors que l'autre diminue. Le cas particulier d'une covariance nulle indique simpelment qu'il n'y a pas de relation linaire entre les VA considérés, mais il peut exister une autre relation entre elles (loi de puissance par exemple). Par construction on comprend que deux variables aléatoires indépendantes auront une covariance nulle. On propose de rapeller la formule de la covariance pour deux VA $X$ et $Y$ ayant n observation :")
st.latex("COV(X, Y) = \\frac{1}{n} \cdot \sum_{i=1}^n (X_i - \\bar{X}) \cdot (Y_i - \\bar{Y}) ")



# II.
################################################## Calcul du rapport signal sur bruit (=SNR)
st.subheader("II. Calcul du rapport signal sur bruit (=SNR)", divider="gray")

########################################## Principe générale
st.markdown("**Principe générale**")
st.markdown("De la façon la plus élémentaire possible le rapport signal sur bruit (=SNR) et la division entre ce que nous appelerons signal noté $S$ et ce qui nous identifierons comme bruit $B$.")
st.latex("SNR = \\frac{S}{B}")
st.markdown("Dans notre cas, le signal est rien d'autre qu'un flux lumineux, donc un nombre de photon qui vient intéragir avec le detecteur. Comme nous l'avons introduit précèdemment dans la section *Rappels*, ce nombre de photon étant discrétisable, il peut être vue comme une variable aléatoire suivant une distribution de Poisson de paramètre $\lambda = n$ où $n$ est le nombre de photon moyen détecté dans un intervalle de temps connu.")
st.markdown("Ainsi grâce aux rappels de probabilité le formalisme le plus simple de ce ratio est le suivant :")
st.latex("SNR = \\frac{n}{\sigma_{photon}}")
st.markdown("""
Avec : 
-   $N$  : Le nombre de photon détecté

-   $\sigma_{photon}$ : La variance de la variable aléatoire $n$ : $\sigma_{photon}=\sqrt{n}$
""")
st.markdown("On vient alors de définir la source de bruit élémentaire : *Le bruit de photon*, qui est intrinsèque à la nature particulaire de la lumière. En remplaçant cela dans notre expréssion on trouve donc :")
st.latex("SNR = \\frac{n}{\sqrt{n}} = \sqrt{n}")

########################################## Evolution en fonction du temps d'intégration
st.markdown("**Evolution en fonction du temps d'intégration**")
st.markdown("Le temps d'intégration va avoir pour impact d'augmenter le nombre moyen de photon détecter de façon linéaire. Dans cette idée si on note $t$ ce temps le nombre de photon va augmenter comme $t \cdot n$ et le $SNR$ va être influencé comme suit :")
st.latex("SNR = \\frac{t \cdot n}{\sqrt{t \cdot n}} = \sqrt{t \cdot n}")
st.markdown("Cela signifie qu'on gagne un facteur $\sqrt{t}$ en précision dans nos mesures simplement en augmentant le temps d'acquisition.")

########################################## Sources de bruit
st.markdown("**Sources de bruit**")
st.markdown("""Avant de définir les sources de bruit, on introduit les paramètres, notament instrumentaux, qui vont influencer le nombre de photon detecté:

- $\\eta$  : Efficacité de transfert du systeme optique

- $F_i$    : Flux de photon de la source $i$

- $S_{coll}$ : Surface collectrice d'un miroir

- $\Delta \lambda$ : Largeur de bande spectrale observé

- $\Delta t$ : Temps d'intégration
""")

################################## Le bruit de photon
st.markdown("*Le bruit de photon* : $\sigma_{photon}$")
st.markdown("Comme expliqué ci dessus, le bruit de photon, ou bruit quantique, est une source fondamentale de bruit dans les observations astronomiques. Il provient de la nature discrète des photons et de leur arrivée aléatoire sur le détecteur. Ce bruit est décrit par une distribution de Poisson, où l'incertitude (l'écart type) est proportionnelle à la racine carrée du nombre total de photons détectés. Ainsi, plus le flux lumineux est élevé, plus le rapport signal/bruit s'améliore, mais jamais totalement exempt de cette incertitude fondamentale.")
st.latex("\sigma_{photon} = \sqrt{n} = \sqrt{\eta \cdot F_{\lambda} \cdot S_{coll} \cdot \Delta\lambda \cdot \Delta t}")

################################## Le bruit thermique  (=Sky)
st.markdown("*Le bruit thermique  (=Sky)* : $\sigma_{thermique}$")
st.markdown("Le bruit thermique, souvent appelé \"bruit du ciel\", provient du rayonnement infrarouge émis par l'atmosphère terrestre, le télescope et les instruments eux-mêmes. Ces sources émettent en continu un flux de photons, particulièrement dans les longueurs d'onde infrarouges, qui se superposent au signal astrophysique d'intérêt. Ce bruit est d'autant plus problématique que l'observation est effectuée à partir de la Terre ou dans des bandes spectrales où l'émission thermique est dominante. Il est généralement atténué par refroidissement des instruments ou par des observations en espace.")
st.latex("\sigma_{thermique} = \sqrt{ F_{instru} \cdot S_{coll} \cdot \Delta\lambda \cdot \Delta t}")

################################## Le bruit de recture (=Read Out Noise)
st.markdown("*Le bruit de recture (=Read Out Noise)* : $\sigma_{RON}$")
st.markdown("Le bruit de lecture est une source instrumentale de bruit qui survient lorsque le détecteur convertit le signal électronique en données numériques. Il provient des imperfections dans le processus de conversion analogique-numérique, des variations thermiques des circuits, et des bruits électroniques internes. Ce bruit est indépendant du signal détecté et constitue une limite fixe à la sensibilité des instruments. Il est souvent réduit en optimisant les performances des détecteurs et en réalisant des calibrations régulières.")
st.latex("\sigma_{RON} = \sqrt{ n_{pix} \cdot RON^2}")
st.markdown("""Avec:

- $n_{pix}$ : Nombre de pixels utilisé

- $RON$ : Bruit de lecture pour une seule lecture en électrons par pixel

""")

################################## Le bruit de repliement spectrale
st.markdown("*Le bruit de repliement spectrale* : $\sigma_{repliement}$")
st.markdown("Le bruit de repliement spectral, lorsqu'il est causé par le bruit thermique, résulte de l'incapacité d'un instrument à totalement éliminer ou rejeter les contributions lumineuses indésirables provenant de longueurs d'onde voisines ou multiples. Dans le cas du bruit thermique, ces signaux parasites proviennent souvent de l'émission infrarouge de l'atmosphère, du télescope, ou des instruments eux-mêmes. Si le facteur de rejet spectral de l'instrument (capacité à filtrer les longueurs d'onde indésirables) est insuffisant, une partie de ce rayonnement thermique se \"replie\" dans la bande spectrale d'intérêt, créant un bruit supplémentaire qui s'ajoute au signal astrophysique attendu.")
st.latex("\sigma_{repliement} = \sqrt{\gamma \cdot \sigma_{thermique}}")
st.markdown("""Avec:

- $\gamma$ : Facteur de rejet

""")


################################## Le bruit zodiacale
st.markdown("*Le bruit zodiacale* : $\sigma_{zodiacale}$")
st.markdown("Le bruit dû à la lumière zodiacale est causé par la diffusion de la lumière stellaire par les particules de poussière interplanétaire situées dans le plan du système solaire. Cette lumière forme une lueur diffuse observable dans le ciel, particulièrement intense le long de l'écliptique. Bien qu'il soit une source astrophysique, ce signal peut masquer des observations faibles ou lointaines, surtout dans les bandes visibles et infrarouges proches. Ce bruit est généralement atténué en évitant d'observer dans des régions du ciel proches du Soleil ou en utilisant des algorithmes de soustraction du fond.")
st.latex("\sigma_{zodiacale} = \sqrt{\eta \cdot F_{zodiacale, \lambda} \cdot S_{coll} \cdot \Delta \lambda \cdot \Delta t}")

################################## Fluctuation de phase : Piston jitter
st.markdown("*La fluctuation de phase* : $\sigma_{jitter}$")
st.markdown("Le piston jitter représentant les variations temporelles de la différence de chemin optique $\delta$ entre deux bras de l'interféromètre. Considéré comme aléatoire, elle sont de façon générale formalisé par une distribution statistique gaussienne, avec une variance $\sigma_{jitter}$ liée aux vibrations mécaniques et/ou instabilités des systemès optique.")

st.latex("P(\delta) = \\frac{1}{ \sqrt{2\pi \sigma_{jitter}^2} } \cdot e^{ -\\frac{\delta^2}{2 \sigma_{jitter}^2} }")
st.markdown("""
Tel que : 

- $\delta$ : Représente le décalage différentiel instentané 
- $\sigma_{jitter}$ : L'écart type du piston jitter
""")

st.markdown("Le piston de jitter introduit donc une fluctuation temporelle de la phase $\phi(t) = \\frac{2\pi}{\lambda}\cdot \delta(t)$")

st.latex("\phi (t) = \\frac{2\pi}{\lambda} \delta(t)")
st.markdown("""
Avec : 

- $\phi(t)$ : La fluctuation de phase
- $\lambda$ : La longueur d'onde
- $\delta(t)$  : La variation temporelle du chemin optique différentiel
""")

st.markdown("*Remarque*: par linéarité, que la phase $\phi$ suit également une loie normale.")



st.markdown("La variance des fluctuation de phase s'exprime donc comme:")
st.latex("\sigma_{\phi}^2 = (\\frac{2\pi}{\lambda})^2\cdot \sigma_{jitter}^2")




########################################## Somme des bruits
st.markdown("**Somme des bruits**")

st.markdown("""Additionner les erreurs en valeur absolue pour estimer l'erreur totale d'une mesure revient à considérer le scénario le plus défavorable : chaque variable est supposée atteindre simultanément sa valeur maximale, ce qui devient de moins en moins probable à mesure que le nombre de variables augmente. En revanche, la somme quadratique des erreurs évite ce biais en fournissant une estimation plus réaliste de l'erreur totale. Cette approche tient compte de la probabilité individuelle de chaque composant, en considérant que leurs contributions sont indépendantes et suivent une distribution normale. Ainsi, l'erreur totale calculée reflète mieux le comportement statistique des erreurs combinées. Selon ce principe on peut établie le bruit total comme :""")
st.latex("\sigma_{tot} = \sqrt{\sum_i \sigma^2_i}")
st.markdown("En fonction de la position de notre instrument (dans l'espace ou basé sur terre), les composante de bruit seront à intégrer ou nom. De plus ces expressions on été donné pour un unique collecteur. Dans le cas de l'interférométrie, le nombre de photon collecté est proportionnel au nombre de surface collectrice qui compose l'instrument.")

########################################## SNR d'un interféromètre à 2 télescope
st.markdown("**SNR d'un interféromètre à 2 télescope basé sur sol**")

st.markdown(" L'interférogramme d'une source circulaire spaialement étendue de diamètre angulaire $\Theta_{src}$ produit par une base $B(B_x, B_y)$ composé de deux télescope de diamètre $D$ définit la composante $I_{photon}$ de l'intensité total:")
st.latex("I_{photon}(x,y) = I_0 \cdot [1 + 2 \cdot \\frac{J_1(\pi \Theta_{src} \\frac{\sqrt{B_x^2 + B_y^2}}{\lambda})}{\pi \Theta_{src} \\frac{\sqrt{B_x^2 + B_y^2}}{\lambda}}  \cdot 2 \cdot \\frac{J_1(\pi \cdot \\frac{D\\rho}{\lambda})}{ \\frac{\pi D \\rho}{\lambda} } \cdot  cos(2\pi\cdot(ux + vy)+\phi)]")

st.markdown("*Termes de visibilité $V(u,v)$:*")
st.latex("V(u,v) = 2 \cdot \\frac{J_1(\pi \Theta_{src} \\frac{\sqrt{B_x^2 + B_y^2}}{\lambda})}{\pi \Theta_{src} \\frac{\sqrt{B_x^2 + B_y^2}}{\lambda}}  ")


st.markdown("*Enveloppe de diffraction $A(\\rho)$:*")
st.latex("A(\\rho) = 2 \cdot \\frac{J_1(\pi \cdot \\frac{D\\rho}{\lambda})}{ \\frac{\pi D \\rho}{\lambda} }")

st.markdown("*Termes d'interférence :*")
st.latex("cos(2\pi\cdot(ux + vy)+\phi)")

st.markdown("D'avantage de précision sur cette expréssion sont fournie dans le cours d'interféromatrie de ce même site. Toujours est-il qu'ici, $I_{photon}$ est pour le moment donné en $[J.s^{-1}.m^{-2}]$. Pour convertir cette quantité en nombre de photon il suffit de la diviser par l'énergie de ce dernier : $E_{photon} = \\frac{hc}{\lambda}$. On en déduit alors le nombre de photon dit scientifique collecté pendant une durée $\Delta t$ sur une surface $S_{Détection}$ :") 

st.latex("n_{photon} = \Delta t \cdot \int_{S_{détection}} \\frac{I_{photon}(x,y)}{E_{photon}} dx dy ")

st.markdown("""
$ =  \\frac{\Delta t \cdot \lambda}{hc} \cdot \int_{S_{détection}} I_{photon}(x,y) \cdot dx dy $

$ =  \\frac{\Delta t \cdot \lambda}{hc} \cdot \int_{S_{détection}} I_0 \cdot [1 + V(u,v) \cdot A(x, y) \cdot cos(2\pi \cdot (ux + vy) + \phi)] \cdot dx dy $

$ =  \\frac{\Delta t \cdot \lambda}{hc} I_0 S_{détection}+ \\frac{\Delta t \cdot \lambda}{hc} I_0 \cdot \int_{S_{détection}}  V(u,v) A(x, y) \cdot cos(2\pi (ux + vy) + \phi)  dx dy $

$ =  \\frac{\Delta t \cdot \lambda}{hc} I_0 S_{détection}+ \\frac{\Delta t \cdot \lambda}{hc} I_0 V(u,v) \cdot \int_{S_{détection}} A(x, y) \cdot cos(2\pi (ux + vy) + \phi)  dx dy $

""")

st.markdown("""On interprète ce nombre de photon de la façon suivante : 

- Le premier terme : $ \\frac{\Delta t \cdot \lambda}{hc} I_0 S_{détection}$  ; représente le nombre de photon participant à la contribution uniforme du flux lumineux detecté.

- Le second terme :  $ \\frac{\Delta t \cdot \lambda}{hc} I_0 V(u,v) \cdot \int_{S_{détection}} A(x, y) \cdot cos(2\pi (ux + vy) + \phi)  dx dy $  ; quantifie le nombre de photon participant à la formation des franges. 

""")

st.markdown("En intégrant sur une surface suffisament petite $\Delta x \cdot \Delta y$ au sein de laquel les variation de x et de y soit nul dans cette surface, alors localement on a $x = x_0$ et $y = y_0$. Cela nous permets de faire les approxiamtions suivante :  ")

st.latex("cos(2\pi\cdot(ux + vy)+\phi) = cos(2\pi\cdot(ux_0 + vy_0)+\phi)")
st.latex("A(\\rho) = A(\\rho_0)")

st.markdown("On obtient alors l'expression suivante du nombre de photon détecté : ")
st.latex("n_{photon} = \Delta t \cdot \\frac{\lambda}{hc} \cdot I_0 \cdot S_{Détection} + \Delta t \cdot \\frac{\lambda}{hc} \cdot V(u,v) \cdot A(\\rho_0) \cdot cos(2\pi(ux_0 + vy_0) + \phi) ")

st.markdown("On propose une simulation dynamique, en fonction du diamètre des deux collecteurs, de leur base et de la longueur d'onde d'observation, d'un tel interférogramme avec le graphe ci dessous. ")



###
col1, col2 = st.columns(2)
with col1 :
    D = st.number_input("Diamètre des miroirs $D$ [m]", value=1.0, min_value=0.1, max_value=10.0, step=0.1)
    B = st.number_input("Ligne de base $B$  [m]", value=3.0, min_value=1.0, max_value=100.0, step=1.0)
    Lambda = st.number_input("Longueur d'onde $\lambda$ [m]", value=100, min_value=100, max_value=20000, step=100) * 1E-9

    # Calculs pour l'interférogramme
    x_max =  Lambda/(2*D) 
    x = np.linspace(-5*x_max, 5*x_max, 2048)  
    Enveloppe   = np.sinc((D / Lambda) * x) ** 2
    Frange      = np.cos(2 * np.pi * B * x / Lambda)**2
    Interferogramme = Frange  * Enveloppe 

with col2 :
    fig, axes = plt.subplots(figsize=(10, 8))

    axes.plot(x, Enveloppe, label="Enveloppe (Sinc^2)", color="blue")
    axes.plot(x, Interferogramme, label="Interférogramme²", color="orange")
    axes.set_title("Interferogramme")
    axes.set_ylabel("Amplitude")
    axes.grid(True)
    axes.legend()

    fig.tight_layout()
    st.pyplot(fig)
###
st.code("""
        # Programm Python servant à afficher le graphe de l'interférogramme
        x_max =  Lambda/(2*D) 
        x = np.linspace(-5*x_max, 5*x_max, 2048)  
        Enveloppe   = np.sinc((D / Lambda) * x) ** 2
        Frange      = np.cos(2 * np.pi * B * x / Lambda)**2
        Interferogramme = Frange  * Enveloppe 
        """, language="python")


st.markdown("Avec l'estimation du nombre de photon d'un tels interféromètre et les rappels de probabilité et ceux sur les bruits, on est en mesure de proposer une première valeur du SNR du flux cohérent d'un tel observatoire à 2 télescopes basé sur Terre dont le formalisme de ce rapport dans ces conditions est présenté ci dessous : ")

st.latex("SNR = \\frac{2 \cdot n_{photon} \cdot V}{\sqrt{\sigma_{photon}^2 + \sigma_{thermique}^2 + \sigma_{RON}^2 + \sigma_{repliement}^2 }}")

st.markdown("""
Les bruits *de photon*; *thermique* et *de repliement* peuvent être exprimé en nombre de photon proportionnel au nombre de télescope :

- $\sigma_{photon}^2     = 2 \cdot n_{photon} $

- $\sigma_{thermique}^2  = 2 \cdot n_{thermique} $

- $\sigma_{repliement}^2 = (2 \gamma \cdot  n_{thermique})^2 $

Dans l'expression du SNR, $V$ représente le contraste des franges. En développant les bruits on trouve : """)

st.latex("SNR = \\frac{2 \cdot n_{photon} \cdot V }{\sqrt{2 \cdot n_{photon} + 2 \cdot n_{thermique} + n_{pixels} \cdot RON^2 + (2\gamma \cdot n_{thermique})^2}}")

st.markdown("""*Note*

En interférométrie, les porteurs de l'information sont :

- *La visibilité*

- *Le flux cohérent*

- *La cloture de phase*

Il est donc possible de calculer un SNR pour chacune de ces quantité mesuré. Elles seront plus étudier dans la section de cette page intitulé : **IV. SNR de MATISSE**.
""")
# III
################################################## Optimisation du SNR
st.subheader("III. Optimisation du SNR", divider="gray")

st.markdown("Avec ce qu'on a vue jusqu'a présent, on remarque que les leviers dont nous disposons pour augmenter le $SNR$ est soit de réduire la composante du bruit, notament thermique, au d'augmenter le temps d'intégration. Pour répondre à cet objectif, des techniques de traitement du signal permettent cela, comme l'apodisation. On se propose de décrire cet effet sur le $SNR$ dans la section suivante.  ")

################################## Principe de l'Apodisation
st.markdown("**Principe de l'Apodisation**")
st.markdown("Etant donné que le terme d'interférence est nécessairement de la forme d'un cosinus, la technique d'apodisation se résumera à appliquer un filtre de même nature sur les franges avant intégration du des photons collecté par les pixels afin de réduire la part de bruit dans ces dernièrs.")
st.markdown("On définit alors la fenêtre d'apodisation suivante :")
st.latex("w(x) = [ cos²(\\frac{\pi x}{L_a}) \cdot \Pi(\\frac{x}{L_a}) ] \\ast \sum_i  \delta(x - x_i)  ")

st.markdown("""
Avec : 
- $L_a$                 : La largeur d'un pic frange
- $\Pi(\\frac{x}{L_a})$ : La fonction porte qui vaux 1 sur la largeur $L_a$
- $\delta(x)$           : La distribution de dirac
- $x_i$                 : Les positions des pics d'interférences
""")

st.markdown("""En somme, on applique un filtre cos² qui prendra ces valeurs sur une largeur $L_a$ centré en $x_i$. On comprends alors qu'avec les bons paramètres $L_a$ et $x_i$ on va être en mesure de filtrer les pics franges. On propose la représentation élémentaire de ce filtre avec le graphe dynamique ci dessous : """)

col1, col2 = st.columns(2)
with col1:
    Largeur_Porte = st.slider("Largueur de la porte = $L_a$", 0.1, 10.0, 4.5)
    Centre_Porte  = st.slider("Centre de la porte = $x_i$", 0.0, 10.0, 0.0)
   
with col2 :
    L = 10
    wavelength = 0.5
    x = np.linspace(-5 , 5 ,1024)
    P = Largeur_Porte
    C = Centre_Porte
    y = fonction_porte(x, C-P/2, C+P/2)
    cos = np.cos(pi * x / (wavelength * L))**2
    filtre = y * cos
    # Création du graphique
    fig, ax = plt.subplots()
    ax.plot(x, y, color='blue', label="Porte")
    ax.plot(x, cos, color='orange', label="cos²")
    ax.plot(x, filtre, color='red', label=r"Filtre")
    ax.set_title("Définition de la fenêtre de filtrage")
    ax.set_xlabel("x")
    ax.set_ylabel("Amplitude")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)


################################## Apodisation appliqué à un interféromètre à 2 collecteurs
st.markdown("**Apodisation appliqué à un interféromètre à 2 collecteurs**")

st.markdown("Qu'il s'agisse du signal scientifique ou des photons thermiques, chaque élement de résolution du detecteurs va percevoir un nombre de photon modulé par la fenêtre d'apodisation $w(x,y)$. En considérant les intensité de ces sources de photons, $I_{photon}$ et $I_{thermique}$, comme deux variables aléatoires indépendantes, on pose, en rapellant que les variable $x$ et $y$ définissent les positions sur le détecteur : ")
st.latex("I_{apod}(x,y) = (I_{photon}(x,y) + I_{thermique}(x,y)) \cdot w(x,y)")
st.markdown("""
$ = I_{photon}(x,y) \cdot w(x,y) + I_{thermique}(x,y) \cdot w(x,y) $

$ = I_{photon}(x,y) \cdot w(x,y) + I_{thermique}(x,y) \cdot w(x,y) $

""")

st.markdown("Alors, part la nature discrète de la lumière, la variance de cette variable aléatoire ($I_{apod}$), et la sommes quadratique des variances des VA qui la compose :")
st.latex("\sigma_{apod}^2 = \sigma_{source}^2(I_{photon} \cdot w(x,y)) + \sigma_{th}^2(I_{th}(x,y) \cdot w(x,y)) ")
st.markdown("""
$ = \sigma_{source}^2(I_{photon}(x,y))  \cdot \int_{S_{Detection}} w(x,y)^2 dxdy + \sigma_{th}^2(I_{th}(x,y)) \cdot \int_{S_{Detection}} w(x,y)^2 dxdy $

$ = \sigma_{photon}^2 \cdot \int_{S_{Detection}} w(x,y)^2 dxdy + \sigma_{th}^2 \cdot \int_{S_{Detection}} w(x,y)^2 dxdy $

$ = n_{photon} \cdot \int_{S_{Detection}} w(x,y)^2 dxdy + n_{thermique} \cdot \int_{S_{Detection}} w(x,y)^2 dxdy $

""")

st.markdown("On en déduit le rapport **SNR après apodisation** pour un interféromètre basé sur Terre à deux collecteurs : ")
st.latex("SNR = \\frac{n_{photon} \cdot V \cdot W }{\sqrt{2 \cdot n_{photon} \cdot W + 2 \cdot n_{thermique} \cdot W + n_{px} RON^2 + (2\gamma\cdot n_{thermique} W)^2}}")
st.markdown("Tel que : $W = \int_{S_{Detection}} w(x,y)^2 dxdy$")


# IV. 
################################################## SNR de MATISSE
st.subheader("IV. SNR de MATISSE", divider="gray")

################################## SNR du flux de cohérence
st.markdown("**SNR du flux de cohérence**")

################################## SNR de phase
st.markdown("**SNR de phase**")

################################## Apodisation appliqué à MATISSE
st.markdown("**Apodisation appliqué à MATISSE**")



# V.
################################################## SNR d'un interféromètre spatial à 2 téléscopes
st.subheader("V. SNR d'un interféromètre spatial à 2 téléscopes", divider="gray")


# VI.
################################################## VII. Simualteur de SNR d'un interféromètre spatiales à 2 teléscopes
st.subheader("VI. Simualteur de SNR d'un interféromètre spatiales à 2 teléscopes", divider="gray")

################################## Paramètres de la cible
st.markdown("**Paramètres de la cible**")

################################## Paramètres du collecteurs
st.markdown("**Paramètres du collecteurs**")

################################## Calcul du SNR
st.markdown("**Calcul du SNR**")


# VII.
################################################## Conclusion
st.subheader("VII. Conclusion", divider="gray")

# Annexe.
################################################## Conclusion
st.subheader("Annexe. Calcul SNR $\\beta$ pictoris b", divider="gray")



################################################## Section Apodisation
################################### Rapelle Interférométrie
st.header("Formalisme de SNR après apodisation", divider="gray")
st.subheader("Cas simple d'un interferomètre à 2 collecteurs monochromatiques")

st.markdown("On rapelle l'expression de l'interférogrammes d'un interféromètre composé de deux mirroirs collecteurs, sans considération du terme de phase :") 

st.latex("I_{tot} = (I_1 + I_2) \cdot [1 + 2 \cdot \\frac{\sqrt{I_1 \cdot I_2}}{I_1 + I_2} \cdot cos(\\frac{2 \pi}{\lambda} \cdot \\frac{ax}{L})]")

st.markdown("""
Avec les notations suivantes : 
- $a$ :   La distance séparant les deux collecteurs
- $L$ :   La distance entre le plan des collecteurs et le detecteur
""")

################################### Définition apodisation

st.subheader("Simulation dynamiques dans le cas d'un interferomètres à 2 collecteurs")

st.markdown("""
L'idée de l'apodisation est que derrière chaque pic frange du lobe principale on applique une fenêtre de type cosinus. en reprennant l'interferogramma ci dessus on peu définir les fenêtre qui vont nous interesser : 

""")

col1, col2 = st.columns(2)

with col1:
    Nombre_de_pics = int(B/D) * 4 + 1
    st.markdown(f"""Nombre de pics dans le lobe principale : {Nombre_de_pics:.0f}. 
    Il faut donc définir le positionnement de {Nombre_de_pics:.0f} fonction porte.
    """)
    
    y = 0
    P   = Lambda / (4*B)
    for i in range(0,int(Nombre_de_pics/2)) :         
        if i == 0 : 
            C = 0
            y   += fonction_porte(x, C-P, C+P)
        else : 
            C   =  Lambda / (i * B)
            y   += fonction_porte(x, C-P, C+P) + fonction_porte(x, -C-P, -C+P)
    
with col2:
    A = Lambda / (D)
    E = Lambda / (4*B)
    test    = fonction_porte(x, -A, A)
    test_2  = fonction_porte(x, A/3-E, A/3+E)
    
    fig, axes = plt.subplots(2,1,figsize=(10, 8))

    axes[0].plot(x, test, label="Enveloppe (Sinc^2)", color="blue")
    axes[0].plot(x, test_2, label="Interférogramme²", color="red")
    axes[0].plot(x, interferogramme, label="Interférogramme²", color="orange")
    axes[0].set_title("Interferogramme")
  
    axes[0].set_ylabel("Amplitude")
    axes[0].grid(True)
    axes[0].legend()
    
    axes[1].plot(x, y, label="Interférogramme²", color="orange")
    axes[1].plot(x, interferogramme, label="Interférogramme²", color="orange")
    axes[1].set_title("Interferogramme")
    axes[1].set_ylabel("Amplitude")
    axes[1].grid(True)
    axes[1].legend()

    fig.tight_layout()
    st.pyplot(fig)

col1, col2 = st.columns(2)
with col1 :
    wavelength         = st.slider("Longueur d'ondes [nm]:", 100, 20000, 100)*1E-9
    Collecteur_Diameter= st.number_input("Diamètre des collecteurs [m]:", 0.1, 10.0, 0.1)
    Ligne_De_Base      = st.number_input("Base interférométrique [m] :",  min_value=max(int(2*Collecteur_Diameter),1))
    Distance_Collecteur_Ecran = st.number_input("Distance Collecteur Ecran [m] :",  1, 10, 1)
    X_Scale = st.number_input("Echelle des $x$ en $\lambda \cdot L / B$:", 1, 100,1)
    
with col2 :
    L = Distance_Collecteur_Ecran
    U_graphe = wavelength** L / (2*Collecteur_Diameter)
    x = np.linspace(-X_Scale*U_graphe , X_Scale*U_graphe ,2048)
    Nombre_De_Pic = int(Ligne_De_Base / Collecteur_Diameter)
    P   = wavelength** L / (2*Ligne_De_Base)
    y = 0
    for i in range(0,Nombre_De_Pic) : 
        C   = 2 * i * wavelength** L / (2*Ligne_De_Base)
        if i == 0 : 
            y   += fonction_porte(x, C-P/2, C+P/2)
        else : 
            y   += fonction_porte(x, C-P/2, C+P/2) + fonction_porte(x, -C-P/2, -C+P/2)
    cos = np.cos(pi * x * Ligne_De_Base / (wavelength * L)) * np.cos(pi * x * Collecteur_Diameter / (wavelength * L))
    
    filtre = y * cos**2
    

   # Création des subplots (un par courbe)
    fig, axes = plt.subplots(3, 1, figsize=(8, 12), sharex=True)  # 3 lignes, 1 colonne, partage de l'axe x

    # Premier plot : Filtre
    axes[0].plot(x, y, color='blue', label="Filtre")
    axes[0].set_title("Filtre")
    axes[0].set_ylabel("Amplitude")
    axes[0].grid(True)
    axes[0].legend()

    # Deuxième plot : Flux corrélé au carré
    axes[1].plot(x, cos**2, color='orange', marker=".", label="Flux corrélé au carré")
    axes[1].set_title("Flux corrélé au carré")
    axes[1].set_ylabel("Amplitude")
    axes[1].grid(True)
    axes[1].legend()

    # Troisième plot : Filtre (rouge)
    axes[2].plot(x, filtre, color='red', linestyle="-.", label="Filtre")
    axes[2].set_title("Filtre (apodisation)")
    axes[2].set_xlabel("x")  # Axe commun en x
    axes[2].set_ylabel("Amplitude")
    axes[2].grid(True)
    axes[2].legend()

    # Ajustement de l'espace entre les subplots
    fig.tight_layout()

    # Affichage avec Streamlit
    st.pyplot(fig)



################################################## Section FKSI
st.header("FKSI - SNR estimation", divider="gray")
st.subheader("Rapelle sur les corps noirs - La fonction de planck")
st.latex("B (\\nu, T_{Surf}) = 2 \cdot \\frac{h c^2}{\\nu^3} \cdot \\frac{1}{e^{\\frac{h  \\nu}{k_b T_{Surf}}}-1}")


################################################## Graphe Fonction de Planck
col1, col2 = st.columns(2)
with col1 :
    wavelength = st.slider("Selectionner un domaine de longueur d'onde [nm]", 0.0, 20000.0, (400.0, 800.0))
    temp = st.number_input("Température (K)", value = 400.0)
    
    # Conversion des longueurs d'onde en mètres
    wavelengths_nm = np.linspace(wavelength[0], wavelength[1], 500)
    wavelengths_m = wavelengths_nm * 1e-9

    def planck(wavelength, temperature):
        """
        Calcule la fonction de Planck pour une longueur d'onde et une température données.
        wavelength : Longueur d'onde en mètres (array ou scalaire)
        temperature : Température en Kelvin (scalaire)
        Retourne : Intensité spectrale (W/m^2/sr/m)
        """
        return (2 * h * c**2 / wavelength**5) / (np.exp(h * c / (wavelength * k * temperature)) - 1)
    # Calcul de la fonction de Planck
    intensities = planck(wavelengths_m, temp)
    
with col2 : 
    # Création du graphique
    fig, ax = plt.subplots()
    ax.plot(wavelengths_nm, intensities, color='blue', label=f"T = {temp} K")
    ax.set_title("Fonction de Planck")
    ax.set_xlabel("Longueur d'onde (nm)")
    ax.set_ylabel("Intensité spectrale (W/m²/sr/m)")
    ax.grid(True)
    ax.legend()

    # Affichage du graphique dans Streamlit
    st.pyplot(fig)


################################# Calcule du FLUX #########################

#Flux total d'une étoile

st.subheader("Calcul du flux d'une étoile recupéré par un mirroir circulaire")

def Aire_Collectrice():
    """
    Air de la surface collectrice d'un miroire sphérique
        - r : Rayon du miroir
    """
        
    return 0
    
def Stellar_Flux(frequence, Temps_Surface, Aire_Collectrice, Theta_s, Bandwith):
    wavelength = frequence * c
    return pi * Theta_s**2 * Bandwith * Aire_Collectrice * planck(wavelength, temperature)

# Flux apparent

