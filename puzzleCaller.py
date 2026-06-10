import argparse
import importlib.util
import sys
from collections.abc import Callable
from typing import Any


def load_function(path_to_pyfile: str, funcname: str) -> Callable[..., Any]:
    spec = importlib.util.spec_from_file_location("puzzle_module", path_to_pyfile)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module from {path_to_pyfile}")

    module = importlib.util.module_from_spec(spec)
    sys.modules["puzzle_module"] = module
    try:
        spec.loader.exec_module(module)

        if not hasattr(module, funcname):
            raise AttributeError(f"Function '{funcname}' not found in {path_to_pyfile}")

        function = getattr(module, funcname)
        if not callable(function):
            raise TypeError(f"'{funcname}' in {path_to_pyfile} is not callable")
        return function
    finally:
        sys.modules.pop("puzzle_module", None)


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run an AoC puzzle function against an input file."
    )
    parser.add_argument("-i", "--input", type=str, required=True)
    parser.add_argument("-p", "--path", type=str, required=True)
    parser.add_argument("--function", default="puzzle", type=str)
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()

    with open(args.input) as f:
        lines = [line.rstrip() for line in f]

    puzzle_func = load_function(args.path, args.function)
    puzzle_input: str | list[str] = lines[0] if len(lines) == 1 else lines
    print(f"Solution: {puzzle_func(puzzle_input)}")
