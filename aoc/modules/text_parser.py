import re
from collections.abc import Iterable

type PatternLike = str | re.Pattern[str]

INT_PATTERN: re.Pattern[str] = re.compile(r"-?\d+")


class ParseError(ValueError):
    """Raised when a line of puzzle input does not match the expected format."""

    def __init__(self, message: str, line: str, pattern: re.Pattern[str] | None = None) -> None:
        details = f"{message}\n  line:    {line!r}"
        if pattern is not None:
            details += f"\n  pattern: {pattern.pattern!r}"
        super().__init__(details)

        self.line = line
        self.pattern = pattern


def _compile(pattern: PatternLike) -> re.Pattern[str]:
    return pattern if isinstance(pattern, re.Pattern) else re.compile(pattern)


def match_line(pattern: PatternLike, line: str, *, full: bool = True) -> re.Match[str]:
    """Match a line against a pattern, raising ParseError instead of returning None.

    By default the whole line must match; set full=False to only anchor at the start.
    """
    compiled = _compile(pattern)
    re_match = compiled.fullmatch(line) if full else compiled.match(line)
    if re_match is None:
        raise ParseError("Line does not match pattern", line, compiled)
    return re_match


def parse(pattern: PatternLike, line: str, *, full: bool = True) -> tuple[str, ...]:
    """Match a line and return its groups as strings; convert them at the call site.

    Example:
        >>> command, x = parse(r"(\\w+) (\\d+)", "up 3")
        >>> command, int(x)
        ('up', 3)
    """
    re_match = match_line(pattern, line, full=full)
    groups = re_match.groups()
    if None in groups:
        raise ParseError("Optional group did not participate in the match", line, re_match.re)
    return groups


def parse_lines(
    pattern: PatternLike, lines: Iterable[str], *, full: bool = True
) -> list[tuple[str, ...]]:
    """Apply parse() to every line."""
    return [parse(pattern, line, full=full) for line in lines]


def parse_ints(text: str) -> list[int]:
    """Extract every (optionally negative) integer from a string."""
    return [int(value) for value in INT_PATTERN.findall(text)]
