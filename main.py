# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr



from bs4 import BeautifulSoup
import requests
import csv



# IN1 SCRAPPING
source = requests.get("https://data.brani.cz/tmp/backend-ukol/in1.xml")

if source.status_code != 200:
    print("něco je zle - source")
else:
    print("ACCESS GRANTED")

soup_nabidky = BeautifulSoup(source.text,"xml")
shop_item    = soup_nabidky.find_all("SHOPITEM")

in1_name = []
in1_code = []

for item in shop_item:
    name = item.find("NAME").text

    try:
        variants = item.find("VARIANTS")
        variants_result = "+"

    except:
        variants_result = "no variants"
    

    if variants == None:
        code = item.find_all("CODE")
        code = code[-1].text

        in1_name.append(name)
        in1_code.append(code)


    else:
        varaint = variants.find_all("VARIANT")
        
        varaint_length = len(varaint)
        variant_pos    = varaint_length

        variant_list = []
        a = -1
        for x in range(variant_pos):
            variant_list.append(a)
            a = a - 1


        codes = item.find_all("CODE")

        for prvek in variant_list:
            code = codes[prvek].text

            in1_name.append(name)
            in1_code.append(code)



# IN2 SCRAPPING
source = requests.get("https://data.brani.cz/tmp/backend-ukol/in2.xml")

if source.status_code != 200:
    print("něco je zle - source")
else:
    print("ACCESS GRANTED")

soup_nabidky = BeautifulSoup(source.text,"xml")
shop_item    = soup_nabidky.find_all("SHOPITEM")

in2_name = []
in2_code = []

for item in shop_item:
    name = item.find("NAME").text

    try:
        variants = item.find("VARIANTS")
        variants_result = "+"

    except:
        variants_result = "no variants"
    

    if variants == None:
        code = item.find_all("CODE")
        code = code[-1].text

        in2_name.append(name)
        in2_code.append(code)


    else:
        varaint = variants.find_all("VARIANT")
        
        varaint_length = len(varaint)
        variant_pos    = varaint_length

        variant_list = []
        a = -1
        for x in range(variant_pos):
            variant_list.append(a)
            a = a - 1


        codes = item.find_all("CODE")

        for prvek in variant_list:
            code = codes[prvek].text

            in2_name.append(name)
            in2_code.append(code)



# IN_MAIN SCRAPPING
source = requests.get("https://data.brani.cz/tmp/backend-ukol/in-main.xml")

if source.status_code != 200:
    print("něco je zle - source")
else:
    print("ACCESS GRANTED")

soup_nabidky = BeautifulSoup(source.text,"xml")
shop_item    = soup_nabidky.find_all("SHOPITEM")

in_main_name = []
in_main_code = []

for item in shop_item:
    name = item.find("NAME").text

    try:
        variants = item.find("VARIANTS")
        variants_result = "+"

    except:
        variants_result = "no variants"
    

    if variants == None:
        code = item.find_all("CODE")
        code = code[-1].text

        in_main_name.append(name)
        in_main_code.append(code)


    else:
        varaint = variants.find_all("VARIANT")
        
        varaint_length = len(varaint)
        variant_pos    = varaint_length

        variant_list = []
        a = -1
        for x in range(variant_pos):
            variant_list.append(a)
            a = a - 1


        codes = item.find_all("CODE")

        for prvek in variant_list:
            code = codes[prvek].text

            in_main_name.append(name)
            in_main_code.append(code)



# COMPARING IN1 VS IN2 LISTS
in1notin2_name = []
in1notin2_code = []

i = 0
for item in in1_code:
    if item not in in2_code:
        in1notin2_code.append(item)
        in1notin2_name.append(in1_name[i])

    i = i + 1



# COMPARING IN2 VS IN1 LISTS
in2notin1_name = []
in2notin1_code = []

i = 0
for item in in2_code:
    if item not in in1_code:
        in2notin1_code.append(item)
        in2notin1_name.append(in2_name[i])

    i = i + 1



# DIFF IN1 VS IN2 MERGED TO IN_MAIN
for i in range(len(in1notin2_code)):
    in_main_name.append(in1notin2_name[i])
    in_main_code.append(in1notin2_code[i])

for i in range(len(in2notin1_code)):
    in_main_name.append(in2notin1_name[i])
    in_main_code.append(in2notin1_code[i])



csv_file   = open("extra_products.csv", "w", encoding = "utf-8")
csv_writer = csv.writer(csv_file, delimiter = ",")

for prvek in range(len(in_main_code)):
    csv_writer.writerow([in_main_name[prvek], in_main_code[prvek]])
csv_file.close()



print("FINISHED")


