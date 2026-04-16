from fastapi import FastAPI, Body, Request
import json
app = FastAPI(title="Lint")


@app.post("/lint")
def lint_code(data: dict =Body(...)):
# def parse_code(request: Request): 
#     body_bytes = request.scope["body"] 
#     data = json.loads(body_bytes)
    functions = data.get("functions",[])
    classes = data.get("classes", [])

    
    
    warnings =[]


    
    for cls in classes :
        name = cls.get("name","")
        if len(name) >0:
            if not name[0].isupper():
                msg = "Class '" +name+ " should start with uppercase"
                warnings.append(msg)


    for func in functions:
        name =func.get("name", "")
        args =func.get("args",[])
        if len(name) >0:
            if not name[0].islower():
                msg = "Function "+name + " should start with lowercase"
                warnings.append(msg)


        if len(args) >4:
            msg = "Function " +name+ " has too many arguments"
            warnings.append(msg)



    result = {}
    result["warnings"]= warnings
    return result