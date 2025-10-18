import argparse
import importlib.util
import sys

from typing import Any
from collections.abc import Callable


def verify_py_file_exist(path_to_pyfile: str) -> None:
    try:
        with open(path_to_pyfile, "r"):
            pass
    except FileNotFoundError:
        with open(path_to_pyfile, "w"):
            pass


def get_function_object(path_to_pyfile: str, funcname: str) -> Callable[..., Any]:
    verify_py_file_exist(path_to_pyfile)
    spec = importlib.util.spec_from_file_location("tmpmodulename", path_to_pyfile)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module from {path_to_pyfile}")

    module = importlib.util.module_from_spec(spec)
    sys.modules["tmpmodulename"] = module
    spec.loader.exec_module(module)
    if not hasattr(module, funcname):
        raise AttributeError(f"Cannot find function '{funcname}'in imported module")

    function = getattr(module, funcname)
    if not isinstance(function, Callable):  # type: ignore
        raise TypeError(f"'{funcname}' is not a function")
    return function  # type: ignore


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str)
    parser.add_argument("--path", type=str)
    parser.add_argument("--function", default="puzzle", type=str)
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()

    inputList: list[str] = open(args.input, "r").readlines()
    puzzleFunc = get_function_object(args.path, args.function)

    if len(inputList) == 1:
        puzzleOutput = puzzleFunc(inputList[0])
    else:
        inputList = [x.rstrip() for x in inputList]
        puzzleOutput = puzzleFunc(inputList)

    print(f"Solution: {puzzleOutput}")
