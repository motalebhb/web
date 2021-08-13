import csv
from typing import Counter

import pandas as pd
from flask import Flask, render_template, request

app=Flask(__name__)

with open (r'H:\flask-vscode\datatable1\static\file\example.csv', encoding='utf-8') as infile:
    result=csv.DictReader(infile)
    rowlist=[]
    for row in result:
       rowlist.append(dict(row))
       name=rowlist

@app.route('/')
def  pagi_nation():
  
    return render_template('index.html', name=name)


# city code counts satart
countf=pd.read_csv(r'H:\flask-vscode\datatable1\static\file\example.csv', encoding="utf-8")
df=pd.DataFrame(countf)
grouped=df.groupby('city')['city_code'].value_counts(ascending=True)

#city count start
@app.route("/count")
def count_list():
    with open(r'H:\flask-vscode\datatable1\static\file\example.csv',encoding='utf-8') as like:
        result=csv.DictReader(like)
        list=[]
        for row in result:
            list.append(row['city'])
            total=Counter(list)
        return render_template('count.html',total=total, grouped=grouped)



# city count and city code counts end




if __name__=='__main__':
    app.run(debug=True)     
