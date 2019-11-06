#! /usr/bin/env python374
# -*- encoding: utf-8 *-


def genProc(nomPC, rolePC, paramEPC, pSESPC, varConstPC, jEPC, principePC, vJEPC, chem):
    codeHTML = """<!doctype html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>%s</title>
        <link rel="stylesheet" href="style.css">
    </head>

    <body>
        <div>
            <h1><span class="souligner">Procédure :</span> <span id="nomProgramme">%s</span></h1>
        </div>


        <div>
            <h1><span class="souligner">Rôle :</span> <span id="role">%s</span></h1>
        </div>


        <div>
            <h1><span class="souligner">Glossaire :</span></h1>
            <ul>
                <li class="niveau1">Paramètres en entrée :</li>
                <ul>
""" % (nomPC, nomPC, rolePC)

    paramE = str(paramEPC).split("\n")
    for i in range(len(paramE)):
        if paramE[i] != "":
            codeHTML = codeHTML + """                    <li>""" + paramE[i] + "</li>\n"

    codeHTML = codeHTML + """                </ul>

                <p></p>

                <li class="niveau1">Paramètres en Sortie et en Entrée/Sortie :</li>
                <ul>
"""

    pSES = str(pSESPC).split("\n")
    print(pSES)
    print(pSESPC)
    for i in range(len(pSES)):
        if pSES[i] != "":
            codeHTML = codeHTML + """                    <li>""" + pSES[i] + "</li>\n"

    codeHTML = codeHTML + """                </ul>

                <p></p>

                <li class="niveau1">Variables et constantes :</li>
                <ul>
"""

    varConst = str(varConstPC).split("\n")
    for i in range(len(varConst)):
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
                <img src="images/procedure_%s.png"/>

                <p></p>

                <li><span class="niveau1">Validation sur jeux d’essais :</span> %s</li>
            </ul>
        </div>

        <div>
            <p>Designed by deadLocks21</p>
        </div>
    </body>
</html>""" % (jEPC, principePC, nomPC, vJEPC)

    chemHTML = chem + nomPC + ".html"
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
