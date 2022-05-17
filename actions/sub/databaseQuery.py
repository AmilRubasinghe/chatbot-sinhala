import logging
def getMohDetails(dbQuery,dbConection):
    x   = []
    mohDetails = dbConection.mohs.find(dbQuery)
    for i in mohDetails:
        x.append(i)
    logging.info("fetch the document from the data base")
    return x

def getPhiDetails(dbQuery,dbConection):
    x   = []
    phiDetails = dbConection.phis.find(dbQuery)
    for i in phiDetails:
        x.append(i)
    logging.info("fetch the phi document from the data base")
    return x