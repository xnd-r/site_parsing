import os, re, datetime, time

dir_ =  os.path.join(os.getcwd(), 'ipp_manual')
start_doc ='GUID-3DA6AD48-BFFF-4E7E-85A8-B25D3C2501F4.htm'
docs_array  = []
chained     = []
unchained   = []
external    = []
broken      = []

def search_docs(): #returns full list of docs
    directory = os.getcwd()+ '/ipp_manual'
    files = os.listdir(directory)
    docs_array = list(filter(lambda x: x.endswith('.htm'), files))
    return docs_array

def get_links(file):
    file_path = os.path.join(dir_, file)
    if os.path.exists(file_path) and os.path.isfile(file_path):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            reg = re.findall(r'(?<=href\=").+?(?=#)|(?<=href\=").+?(?=")', content)     
            for i in reg:
                if i.startswith('http'):
                    if i not in external:
                        external.append(i)
                        get_links(i)
                if i.endswith('.htm'):
                    if i in docs_array and i not in chained:
                        chained.append(i)
                        get_links(i)
                    if i not in docs_array and i not in broken:
                        broken.append(i)
                        get_links(i) 
                else:
                    pass
    else:
        pass
        return


if __name__ == '__main__':

    t1 = time.time()
    docs_array = search_docs()
    os.chdir("ipp_manual")
    get_links(start_doc)
    unchained = set(docs_array) - set(chained)
    t2 = time.time()

    time = t2 - t1
    today = datetime.datetime.today()
    dt = today.strftime("%Y-%m-%d-%H-%M")
    os.chdir("..")
    os.mkdir(dt)
    os.chdir(dt)
    f = open("!summary.log", 'a')
    
    f.write("amount of files: " + str(len(docs_array)) + "\n")
    f.write("amount of chained links: " + str(len(chained)) + "\n")
    f.write("amount of unchained links: " + str(len(unchained)) + "\n")
    f.write("amount of broken links: " + str(len(broken)) + "\n")
    f.write("amount of external links: " + str(len(external)) + "\n")
    f.write("time: " + str(time))
    f.close()

    f = open("docs_array.log", 'a')
    f.write("amount of files: " + str(len(docs_array)) + "\n")
    for i in docs_array:
        f.write(i + "\n")
    f.close()

    f = open("chained.log", 'a')
    f.write("amount of chained links: " + str(len(chained)) + "\n")
    for i in chained:
        f.write(i + "\n")
    f.close()

    f = open("unchained.log", 'a')
    f.write("amount of unchained links: " + str(len(unchained)) + "\n")
    for i in unchained:
        f.write(i + "\n")
    f.close()

    f = open("broken.log", 'a')
    f.write("amount of broken links: " + str(len(broken)) + "\n")
    for i in broken:
        f.write(i + "\n")
    f.close()
    
    f = open("external.log", 'a')
    f.write("amount of external links: " + str(len(external)) + "\n")
    for i in external:
        f.write(i + "\n")
    f.close()
   
