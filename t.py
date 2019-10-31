res = str(resPG).split("\n")
    for i in range(len(res)):
        if res[i] != "":
            codeHTML = codeHTML + """                    <li>""" + res[i] + "</li>\n"
