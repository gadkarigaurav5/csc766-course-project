I have implemented the code analysis pipeline for pythin codes using HTTP using FastApi(referred the caption_survey)

The code analysis has 3 components
Parser:
    extracts function names and arguments and class names. I am also adding random data here to demonstarte the increase in data transfer size that can happen if we have lot of useless data. this extra data is never used in the pipeline

Lint:
    Tool that checks the structure. Specifically, I am cheking if the Classname starts with upper case. Functions should start with lower case and should habe a max of 4 arguments.

Doc:
    Geberates ouput in plain english. tells the class name, function name and function arguments.


Directory Structure
client : the client codes for basi and optimized version

profiler_logs: profilers logs that will be generated

services: code for each of the tool

tests : the sample python code that will be fed to the pipelin

profiler_utils.py : I have used the file provided to generate logs.

InEfficient Basic pipeline:
    inefficiencies:
        adds extra data 
        a useless call
    pipeline:
        parse->int->parse again->doc

Efficient Opitmized pipeline:
    Optimizations:
        removes extra data
        removes redundant call
    pipeline:
        parse->lint->doc

To Run:
    
    Open 3 terminals and paste the below command in each
    cd to services folder in all the 3 terminals.
    uvicorn parse_service:app --port 8000
    uvicorn lint_service:app --port 8001
    uvicorn doc_service:app --port 8002 

    open a new terminal
    cd client
    run basic client


    python basic.py --source ../tests/sample.py
    sample.py is a test simple test case

    run optimized
    python optimized.py --source ../tests/sample.py

    cd ../profiler_logs
    basic logs : basic_logs
    optimized logs: optimized_logs


    Basic Summary :
    TRACE_ID: tr_cfcd08fd84c0
    Parser 1 latency: 76 ms
    Lint latency: 55 ms
    Parser 2 latency: 2 ms
    Doc latency: 27 ms
    Total latency: 160 ms
    RPC calls: 4

    Optimized Sumamry:
    TRACE_ID: tr_9ced684f97be
    Parser latency: 23 ms
    Lint latency: 11 ms
    Doc latency: 7 ms
    Total latency: 41 ms
    RPC calls: 3

    As you can see lateny of each component has gone down. total latency is reduced. An unnecessary call to parser has been eliminated bringing down the rpc calls to 3.
    This reduces unnecessary computation.

    The payload size has also been reduced:
    e.g. in doc you can see input payload to be payload_in_bytes":3103 in basic  vs payload_in_bytes":87. This demonstrates the reduction caused by transfer of unnecessary data between calls.

    Hardware configuration:
    Apple M2
    cpu core_count: 8
    RAM: 8Gb
