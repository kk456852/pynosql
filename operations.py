

def delete(field):
    def transform(doc):
        del doc[field]

    return transform

def add(field, n):
    def transform(doc):
        doc[field] += n

    return transform

def subract(field, n):
    def transform(doc):
        doc[field] -= n

    return transform

def set(field, val):
    def transform(doc):
        doc[field] = val

    return transform

def increment(field):
    def transform(doc):
        doc[field] += 1

    return transform

def decrement(field):
    def transform(doc):
        doc[field] -= 1

    return transform