import ast
import keyword
import tokenize
import io
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


#I had used random data as unused data in the intial submission
#according to the feedback I modified it so that now my parser 
#passes ast and token
#I have classified tokens into variable, keyword, value, operator, or some other
    if include_extras:
        # extra_data =""
        # for i in range(3000):
        # extra_data = extra_data + "X"
        result["ast"]= ast.dump(tree,indent=3)
        tokens = []
        reader = io.StringIO(src).readline
# Note : I did not know about tokenize . hence i have used ChatGpt here since I have used 
# flex tool for this before which I was not sure how to integrate here.
# it would have been very difficult to write a tokenizer of my own due to time constraints.    
        for tok in tokenize.generate_tokens(reader):
            token_str = tok.string
            token_info = {}

            if token_str in keyword.kwlist:
                token_info["type"] = "keyword"

            elif token_str.isidentifier():
                token_info["type"] = "variable"

            elif token_str.isdigit() or token_str.startswith(("'", '"')):
                token_info["type"] = "value"

            elif token_str in ["+", "-", "*", "/", "%", "=", "==", "!=", "<", ">", "<=", ">=", "(", ")", ":", ","]:
                token_info["type"] = "operator"

            else:
                token_info["type"] = "other"

        token_info["string"] = token_str
        tokens.append(token_info)
        result["tokens"] = tokens
    
    return result