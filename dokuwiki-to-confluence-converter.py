# This code takes a list of txt files extracted from dokuwiki, creates a folder called Confluence 
# generating new files with the same names as the old files converted to txt file with Confluence formatting.
# Note: it has no treatment for images and links

# Amanda Fernandes May 17, 2022

import os

# Make sure there are no files of other extensions in this folder besides txt
# List all txt files in the indicated folder
allFiles = os.listdir('D:/Projetos/DokuWiki/All wiki pages extracted/')

oldFilePath = "D:/Projetos/DokuWiki/All wiki pages extracted/"

path = os.path.join("D:/Projetos/DokuWiki/", "Confluence/")
os.mkdir(path)

empty = ''
for file in allFiles:

  fileName = file
  oldFile = open(oldFilePath + fileName, "r", encoding="UTF-8")
  rows = oldFile.readlines()
  
  newFile = open(path + fileName, "w+", encoding="UTF-8")

  print(fileName)

  for row in rows:
    # Título início h1
    if(row.startswith("======")):
      row = row.replace("======", "h1.", 1)
      row = row.replace("======", empty)

    # Título início h2
    if(row.startswith("=====")):
      row = row.replace("=====", "h2.", 1)
      row = row.replace("=====", empty)

    # Título início h3
    if(row.startswith("====")):
      row = row.replace("====", "h3.", 1)
      row = row.replace("====", empty)

    # Título início h4
    if(row.startswith("===")):
      row = row.replace("=== ", "h4.", 1)
      row = row.replace(" ===", empty)

    # Numeração
    if(row.startswith("  - ")):
      row = row.replace("- ", "# ")

    # Itálico
    index = row.find("//")
    if(index >= 0 and (row.startswith("//") or row[index-1] == " ")):
        row = row.replace("//", "_")

    # Negrito
    row = row.replace("**", "*")

    # Cabeçalho tabela
    row = row.replace("^", "||")

    # Links
    row = row.replace("[[", "[")
    row = row.replace("]]", "]")

    # Codigo
    row = row.replace("<code>", "{code}")
    row = row.replace("</code>", "{code}")

    # Botão fix me
    row = row.replace("FIXME", empty)

    newFile.write(row)

oldFile.close();
newFile.close();
