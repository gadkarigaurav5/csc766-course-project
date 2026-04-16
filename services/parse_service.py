import ast
import json
from fastapi import FastAPI, Request, Body


app = FastAPI(title="Parser")




@app.post("/parse")
def parse_code(data: dict = Body(...)):
# def parse_code(request: Request):
#     body_bytes = request.scope["body"]
#     data = json.loads(body_bytes)
    src = data["source_code"]
    include_extras = data.get("include_extras", True)
    tree = ast.parse(src)

    functions = []
    classes = []
    for node in ast.walk(tree):
        if isinstance(node,ast.FunctionDef):
            args =[]
            for arg in node.args.args :
                args.append(arg.arg)
            func_info ={}
            func_info["name"]= node.name
            func_info["args"]= args
            functions.append(func_info)

        
        
        elif isinstance(node,ast.ClassDef):
            class_info = {}
            class_info["name"] =node.name
            classes.append(class_info)

    result = {}
    result["functions"] = functions
    result["classes"] = classes


# I am addinfg randomn data gere which will not be used anywhere in the pipeline
#jsut for demonstration of increase in payload size resuling from useless data
    if include_extras:
        extra_data =""
        for i in range(3000):
            extra_data = extra_data + "X"
        result["extra_data"] = extra_data

    
    return result