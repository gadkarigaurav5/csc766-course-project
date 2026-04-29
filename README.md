Overview:
    I have implemented a code analysis pipeline for Python code using HTTP with FastAPI.

    The code analysis has 3 components:

    Parser:
        Extracts function names, arguments, and class names. My parser also returns the AST and tokens to the caller. It also returns a set of tokens. The tokens are classified as variable, keyword, value, operator, or Other. The AST and token data are never used in the pipeline.

    Lint:
        Tool that checks the structure. Specifically, I am checking if the class name starts with an uppercase letter. Functions should start with lowercase and should have a maximum of 4 arguments.

    Doc:
        Generates output in plain English. It reports the class name, function name, and function arguments.


    Directory Structure:

    client : the client codes for basic and optimized version

    profiler_logs: profiler logs that will be generated

    services: code for each of the tools

    tests : the sample Python code that will be fed to the pipeline

    profiler_utils.py : I have used the file provided to generate logs

    perf_measure.py : This runs the pipeline 5 times and does analysis.


Workflow:

    InEfficient Basic pipeline:
        inefficiencies:
            adds extra data 
            a useless call
        pipeline:
            parse -> lint -> parse again -> doc

    Efficient Optimized pipeline:
        Optimizations:
            removes extra data
            removes redundant call
        pipeline:
            parse -> lint -> doc


To Run:
    
    Open 3 terminals and paste the below command in each.
    cd to services folder in all the 3 terminals. 
    Copy one command in every terminal.

    uvicorn parse_service:app --port 8000
    uvicorn lint_service:app --port 8001
    uvicorn doc_service:app --port 8002 

   
    Open a new terminal
    cd client

    *********run basic client***********
    python basic.py --source ../tests/sample.py
   

    *********run optimized client***********
    python optimized.py --source ../tests/sample.py

    cd ../profiler_logs
    basic logs : basic_logs
    optimized logs: optimized_logs

    If you want to run the pipelines and collect data over multiple runs, run perf_measure.py from the program root directory.


Observations:

    (venv) gauravgadkari@Mac client % python basic.py --source ../tests/sample.py
    ========== Summary =======
    TRACE_ID: tr_4bf514c1dfdb
    Parser 1 latency: 57 ms
    Lint latency: 29 ms
    Parser 2 latency: 1 ms
    Doc latency: 69 ms
    Total latency: 157 ms
    RPC calls: 4

    (venv) gauravgadkari@Mac client % python optimized.py --source ../tests/sample.py
    =========== Summary ========
    TRACE_ID: tr_b97e27ae9341
    Parser latency: 6 ms    
    Lint latency: 3 ms
    Doc latency: 2 ms
    Total latency: 11 ms
    RPC calls: 3


    After running 5 times the summary is:

    ======================================= FINAL RESULTS==================================
    Basic latency mean: 121.30851679248735
    Basic latency std: 29.65596076612746
    Basic RPC count: 20
    Basic total data transferred: 738260
    Optimized latency mean: 97.48969996580854
    Optimized latency std: 2.827430417703615
    Optimized RPC count: 15
    Optimized total data transferred: 87625
    ======================================= FINAL RESULTS==================================


                                Basic      Optimized
    Latency mean                121.3 ms   97.5 ms
    Latency std deviation       29         2.82
    RPC                         20         15
    Data transferred            738260     87625


    As you can see, the latency of each component has gone down. The total latency (mean of 5 runs) decreased from 121 ms to 97 ms. An unnecessary call to the parser has been eliminated, reducing the RPC calls over 5 runs from 20 to 15. This reduces unnecessary computation.

    The individual payload size has also been reduced. For example in one individual run, the parser in the basic flow outputs 3103 bytes and the lint tool takes 3103 bytes as input. On the other hand, the output of the parser in the optimized version is just 87 bytes and the input to the lint is 87 bytes. cross 5 runs, the totalm data transferred reduces from 738260 to 87625 bytes in the optimized. 




Hardware configuration:
    Apple M2
    CPU core count: 8
    RAM: 8 GB