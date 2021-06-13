import csv
import requests
import os

script_dir = os.path.dirname(__file__)
mode = 0o666

with open('list.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        code = row[0]
        name = row[1]

        name = name.replace(".", "")

        os.makedirs("./"+name, mode, exist_ok=True)

        for year in range(10,21,1):
            url = 'https://www.bseindia.com/bseplus/AnnualReport/'+code+'/'+code+'03'+str(year)+'.pdf'
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
            r = requests.get(url, headers=headers)
            rel_path = name+"/"+name+"_20"+str(year)+'.pdf'
            with open(os.path.join(script_dir, rel_path),"wb") as pdf:
                pdf.write(r.content)