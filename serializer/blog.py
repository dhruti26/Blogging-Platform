def BlogEntity(doc) -> dict:
    return {
        "_id" : str(doc["_id"]) ,
        "title" : doc["title"] ,
        "description" : doc["description"] ,
        "author" : doc["author"] ,
        "date" : doc["date"] ,
    }

# all blogs 
def BlogEntities(docs) -> list:
    return [BlogEntity(doc) for doc in docs]


