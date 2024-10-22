def httpStatusCode(status) :
    match status:
        case 200 :
            return "Success"
        case 201 :
            return "Ok"
        case 404 :
            return "Not Found"
        case _ :
            return "Unknown status code"

print(httpStatusCode(201))
