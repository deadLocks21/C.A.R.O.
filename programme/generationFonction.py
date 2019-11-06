#! /usr/bin/env python374
# -*- coding: utf-8 *-

""", varConstF, jEF, principeF, vJEF, chem"""


def genFct(nomF, roleF, paramEF, typeValRF, varConstF, jEF, principeF, vJEF, chem):
    codeHTML = """<!doctype html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>%s</title>
        <link rel="stylesheet" href="style.css">
    </head>

    <body>
        <div>
            <h1><span class="souligner">Fonction :</span> <span id="nomProgramme">%s</span></h1>
        </div>


        <div>
            <h1><span class="souligner">Rôle :</span> <span id="role">%s</span></h1>
        </div>
        
        <div>
            <h1><span class="souligner">Glossaire :</span></h1>
            <ul>
                <li><span class="niveau1">Paramètres en entrée :</span></li>
                <ul>
""" % (nomF, nomF, roleF)

    paramE = str(paramEF).split("\n")
    for i in range(len(paramE)):
        if paramE[i] != '':
            codeHTML = codeHTML + "                    <li>" + paramE[i] + "</li>\n"

    codeHTML = codeHTML + """                </ul>

                <p></p>

                <li><span class="niveau1">Type de la valeur de retour :</span> %s </li>

                <p></p>

                <li><span class="niveau1">Variables et constantes :</span></li>
                <ul>
""" % typeValRF

    varConst = str(varConstF).split("\n")

    nbrR = len(varConst)-1

    for i in range(nbrR):
        if varConst[i] != '':
            codeHTML = codeHTML + "                    <li>" + varConst[i] + "</li>\n"


    codeHTML = codeHTML + """                </ul>
            </ul>
        </div>

        <div>
            <h1><span class="souligner">Algorithme :</span></h1>
            <ul>
                <li><span class="niveau1">Jeux d'essais :</span> %s</li>

                <p></p>

                <li><span class="niveau1">Principe :</span> %s</li>

                <p></p>

                <li><span class="niveau1">Diagramme d’activité :</span></li>
                <img src="images/fonction_%s.png"/>

                <p></p>

                <li><span class="niveau1">Validation sur jeux d’essais :</span> %s</li>
            </ul>
        </div>

        <div>
            <p>Designed by deadLocks21</p>
        </div>
    </body>
</html>""" % (jEF, principeF, nomF, vJEF)

    chemHTML = chem + nomF + ".html"
    chemCSS = chem + "style.css"

    with open(chemHTML, "a", encoding='utf-8') as f:
        f.write(codeHTML)
    with open(chemCSS, "w", encoding="utf-8") as f:
        f.write("""body {
    font-family: Comic Sans MS, Comic Sans, cursive;
    background-color: #1A1A1A;
    color: #C5C5C5;
    margin-top: 0px;
}

h1 {
    font-size: 30px;
    margin:0px;
    text-align: justify-all;
}

div {
    margin-bottom: 30px;
}

ul {
    margin: 0px;
}

#nomProgramme {
    font-size: 35px;
    color:red;
    text-decoration:underline;
}

#role {
    font-weight: normal;
    font-size: 25px;
}

.souligner {
    text-decoration:underline;
}

.bold {
    font-weight: bold;
}

.niveau1 {
    font-size: 25px;
    text-decoration:underline;
    text-align: justify;
}
""")
