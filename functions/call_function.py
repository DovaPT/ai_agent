from google.genai import types
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.write_file import write_file
from functions.run_python import run_python_file

VALID_FUNCTIONS = [
    "get_file_content",
    "run_python_file",
    "write_file",
    "get_files_info",
]
WORKING_DIR = "./calculator"


def call_function(function_call_part, verbose=False):
    function_name = function_call_part.name
    function_args = function_call_part.args

    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
    if function_name not in VALID_FUNCTIONS:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    match function_name:
        case "get_files_info":
            function_result = get_files_info(WORKING_DIR, **function_args)
        case "get_file_content":
            function_result = get_file_content(WORKING_DIR, **function_args)
        case "write_file":
            function_result = write_file(WORKING_DIR, **function_args)
        case "run_python_file":
            function_result = run_python_file(WORKING_DIR, **function_args)
        case _:
            function_result = ""
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )
