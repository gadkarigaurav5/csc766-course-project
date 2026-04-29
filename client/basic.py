import argparse
import json
import sys
import uuid
import requests
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
LOG_PATH = os.path.join(BASE_DIR,"profiler_logs","basic_logs.jsonl")
import profiler_utils as pu

PARSER_URL ="http://127.0.0.1:8000/parse"
LINT_URL ="http://127.0.0.1:8001/lint"
DOC_URL = "http://127.0.0.1:8002/doc"



def read_source(path):
    with open(path) as f:
        return f.read()




def make_meta(value,value_type):
    if isinstance(value,str):
        content =value
    else:
        content = json.dumps(value,sort_keys=True)

    return {"id": pu.obj_id_from_str(content, kind="txt"),
    "type": value_type,
    "bytes": pu.guess_bytes(value)
    }





def main():
    parser =argparse.ArgumentParser()
    parser.add_argument("--source",required=True)
    args = parser.parse_args()
    source_code = read_source(args.source)
    trace_id = "tr_"+ uuid.uuid4().hex[:12]
    rpc_calls =0
    
    parser_payload_1 = {"source_code": source_code,"include_extras": True}
    t0 =pu.now_ms()
    parser_output_1 = requests.post(PARSER_URL, json=parser_payload_1).json()
    t1 = pu.now_ms()
    rpc_calls += 1
    parser_record_1 = pu.build_exec_op_record(trace_id=trace_id,
        node_id="parser_1",
        op="tool.parser",
        t_start_ms=t0,
        t_end_ms=t1,
        payload_in_bytes=pu.guess_bytes(parser_payload_1),
        payload_out_bytes=pu.guess_bytes(parser_output_1),
        inputs_meta={ "source_code": make_meta(source_code, "str"),"include_extras": make_meta(True, "bool")},
        outputs_meta={"functions": make_meta(parser_output_1.get("functions", []), "json"),"classes": make_meta(parser_output_1.get("classes", []), "json"),"extra_data": make_meta(parser_output_1.get("extra_data", ""), "str")})
    pu.append_jsonl(LOG_PATH, parser_record_1)
    
    
    
    
    
    
    lint_payload = {"functions": parser_output_1.get("functions", []),"classes": parser_output_1.get("classes", []),"extra_data": parser_output_1.get("extra_data", "")}
    t2 = pu.now_ms()
    lint_output = requests.post(LINT_URL, json=lint_payload).json()
    t3=pu.now_ms()
    rpc_calls +=1
    lint_record=pu.build_exec_op_record(trace_id=trace_id,
        node_id="lint_1",
        op="tool.lint",
        t_start_ms=t2,
        t_end_ms=t3,
        payload_in_bytes=pu.guess_bytes(lint_payload),
        payload_out_bytes=pu.guess_bytes(lint_output),
        inputs_meta={"functions":make_meta(lint_payload["functions"], "json"),"classes": make_meta(lint_payload["classes"], "json"),"extra_data": make_meta(lint_payload["extra_data"], "str")
        },
        outputs_meta={ "warnings": make_meta(lint_output.get("warnings", []), "json")}
    )
    pu.append_jsonl(LOG_PATH,lint_record)





    parser_payload_2 = {"source_code": source_code, "include_extras": True}
    t4=pu.now_ms()
    parser_output_2 = requests.post(PARSER_URL, json=parser_payload_2).json()
    t5 = pu.now_ms()
    rpc_calls += 1
    parser_record_2 = pu.build_exec_op_record(trace_id=trace_id,
        node_id="parser_2",
        op="tool.parser",
        t_start_ms=t4,
        t_end_ms=t5,
        payload_in_bytes=pu.guess_bytes(parser_payload_2),
        payload_out_bytes=pu.guess_bytes(parser_output_2),
        inputs_meta={"source_code": make_meta(source_code, "str"),"include_extras": make_meta(True, "bool")},
        outputs_meta={"functions": make_meta(parser_output_2.get("functions", []), "json"),"classes": make_meta(parser_output_2.get("classes", []), "json"),"extra_data": make_meta(parser_output_2.get("extra_data", ""), "str")})
    pu.append_jsonl(LOG_PATH, parser_record_2)


    
    
    
    doc_payload ={"functions": parser_output_2.get("functions", []),"classes": parser_output_2.get("classes", []),"extra_data": parser_output_2.get("extra_data", "")}
    t6 = pu.now_ms()
    doc_output = requests.post(DOC_URL,json=doc_payload).json()
    t7 = pu.now_ms()
    rpc_calls += 1
    doc_record = pu.build_exec_op_record(trace_id=trace_id,
        node_id="doc_1",
        op="tool.doc",
        t_start_ms=t6,
        t_end_ms=t7,
        payload_in_bytes=pu.guess_bytes(doc_payload),
        payload_out_bytes=pu.guess_bytes(doc_output),
        inputs_meta={"functions": make_meta(doc_payload["functions"], "json"),"classes": make_meta(doc_payload["classes"], "json"),"extra_data": make_meta(doc_payload["extra_data"], "str")},
        outputs_meta={"documentation":make_meta(doc_output.get("documentation", []), "json")})
    pu.append_jsonl(LOG_PATH, doc_record)
    
    
    total_latency = t7 - t0
    
    
    print("========== Basic Summary =======")
    print("TRACE_ID:", trace_id)
    print("Parser 1 latency:", t1-t0, "ms")
    print("Lint latency:", t3-t2, "ms")
    print("Parser 2 latency:", t5-t4, "ms")
    print("Doc latency:", t7-t6, "ms")
    print("Total latency:",total_latency, "ms")
    print("RPC calls:",rpc_calls)




if __name__ == "__main__":
    main()