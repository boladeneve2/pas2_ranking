




with open('.idea/text_files/pas2_resultado_teste.txt', 'r') as infile, open('.idea/text_files/pas2_resultado_limpo.txt', 'w') as outfile:
    temp = infile.read().replace("", "")
    temp = temp.replace("\n", "")
    temp = temp.replace("/", "\n")
    outfile.write(temp)

