# Module: sqlReader.py
def createParansFromSql(sql):
    sqlArray = sql.split(':')
    sqlArray.pop(0)
    params = []
    for sqlPart in sqlArray:
        params.append(sqlPart.split(' ')[0].split(')')[0])
    return params

def formatParams(params):
    paramsFormated = []
    paramsAux = []
    for param in params:
        paramsAux.append(param)
        paramsFormated.append(param + str(paramsAux.count(param)))
    return paramsFormated

def main():
    sql = input('Digite o SQL: ')
    params = createParansFromSql(sql)
    paramsFormated = formatParams(params)
    print(paramsFormated)

if __name__ == '__main__':
    main()