import logging

def getMohDetails(dbQuery,dbConection):
    x   = []
    mohDetails = dbConection.mohOffice.find(dbQuery)
    for i in mohDetails:
        x.append(i)
    logging.info("fetch the document from the data base")
    return x