import pg

def loaddata():
    con=pg.connect('redsa','localhost',5432,None,'mec14','pass@word123')

    result= con.query('select * from reviews')
    alldata=result.getresult()
    transformdata =list()
    for data in alldata:
        transformdata.append({'id_review':data[1],'label':data[2],'review':data[3],'date':data[4]})
    return transformdata