import csv
def read_csv(url:str,title=True):
    data=list()
    with open(url,'r',encoding='utf-8')as f:
        reader = csv.reader(f)
        if title:
            next(reader)
        for item in reader:
            data.append(item)
        return data