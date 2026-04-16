from fastapi import FastAPI, Body, Request
import json

app =FastAPI(title="Doc Service")




@app.post("/doc")
def doc_code(data: dict = Body(...)):
# def parse_code(request: Request): 
    # body_bytes = request.scope["body"] 
    # data = json.loads(body_bytes)
    
    
    functions = data.get("functions", [])
    classes = data.get("classes",[])
    documentation=[]

    
    for cls in classes:
        name = cls.get("name","")
        if name:
            documentation.append("Class "+ name + " is defined.")

   
   
    for func in functions:
        name = func.get("name", "")
        args = func.get("args",[])
        if len(args) ==0:
            sentence = "Function " +name+" takes 0 arguments."
        else:
            arg_text = ", ".join(args)
            sentence = "Function " + name+ " takes arguments " + arg_text +"."
        
        
        
        documentation.append(sentence)

    
    
    result = {}
    result["documentation"] =documentation
    return result