from itertools import product

type Point = tuple[int, ...]
type Point2D = tuple[int, int]
type Shape = tuple[int, ...]
type GridBounds2D = tuple[int, int, int, int]

CARDINAL_OFFSETS: tuple[Point2D, ...] = (
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
)

DIAGONAL_OFFSETS: tuple[Point2D, ...] = tuple(
    (x, y) for x, y in product((-1, 0, 1), repeat=2) if (x, y) != (0, 0)
)


class grid_helper:
    """Backward-compatible namespace for grid helpers."""

    CARDINAL_DIRECTIONS: dict[str, Point2D] = {
        "N": (-1, 0),
        "E": (0, 1),
        "S": (1, 0),
        "W": (0, -1),
    }

    XY_DIRECTIONS: dict[str, Point2D] = {
        "U": (0, -1),
        "D": (0, 1),
        "L": (-1, 0),
        "R": (1, 0),
    }

    @staticmethod
    def add(a: Point, b: Point) -> Point:
        """Add two coordinate tuples element by element."""
        return tuple(map(sum, zip(a, b, strict=True)))

    @staticmethod
    def add_2d(a: Point2D, b: Point2D) -> Point2D:
        """Add two 2D coordinate tuples."""
        return a[0] + b[0], a[1] + b[1]

    @staticmethod
    def scale(vector: Point, amount: int) -> Point:
        """Scale every component of a coordinate tuple."""
        return tuple(value * amount for value in vector)

    @staticmethod
    def move(point: Point, direction: Point, amount: int = 1) -> Point:
        """Move a point by a direction vector and an optional distance."""
        return grid_helper.add(point, grid_helper.scale(direction, amount))

    @staticmethod
    def move_2d(point: Point2D, direction: Point2D, amount: int = 1) -> Point2D:
        """Move a 2D point by a direction vector and an optional distance."""
        return grid_helper.add_2d(
            point,
            (direction[0] * amount, direction[1] * amount),
        )

    @staticmethod
    def move_by_key_custom(
        point: Point2D,
        key: str,
        direction_mapping: dict[str, Point2D],
        amount: int = 1,
    ) -> Point2D:
        """Move a 2D point using a direction vector looked up by key.

        ``direction_mapping`` can be any ``str``-keyed mapping of direction
        vectors, such as a puzzle-specific direction dict. Raises
        ``KeyError`` if ``key`` is not present.
        """
        return grid_helper.move_2d(point, direction_mapping[key], amount)

    @staticmethod
    def move_by_key_xdy(point: Point2D, key: str, amount: int = 1) -> Point2D:
        """Move a 2D point using ``XY_DIRECTIONS`` (U/D/L/R) looked up by key."""
        return grid_helper.move_by_key_custom(point, key, grid_helper.XY_DIRECTIONS, amount)

    @staticmethod
    def move_by_grid_cardinal(point: Point2D, key: str, amount: int = 1) -> Point2D:
        """Move a 2D point using ``CARDINAL_DIRECTIONS`` (N/E/S/W) looked up by key."""
        return grid_helper.move_by_key_custom(point, key, grid_helper.CARDINAL_DIRECTIONS, amount)

    @staticmethod
    def in_bounds(
        point: Point2D,
        shape: Shape | None = None,
        grid_bounds: GridBounds2D | None = None,
    ) -> bool:
        """Return whether a point is inside a rectangular grid.

        ``shape`` uses zero-based, exclusive upper bounds. ``grid_bounds``
        uses explicit inclusive bounds in ``(min_x, max_x, min_y, max_y)``
        order. If both are provided, ``grid_bounds`` takes precedence.
        """
        if grid_bounds is not None:
            min_x, max_x, min_y, max_y = grid_bounds
            x, y = point
            return min_x <= x <= max_x and min_y <= y <= max_y

        if shape is None or len(shape) != 2:
            raise ValueError("shape must contain exactly two dimensions")

        return all(0 <= value < limit for value, limit in zip(point, shape, strict=True))

    @staticmethod
    def in_bounds_between(
        point: Point,
        lower: Point,
        upper: Point,
    ) -> bool:
        return all(
            low <= value <= high for value, low, high in zip(point, lower, upper, strict=True)
        )

    @staticmethod
    def neighbors(point: Point2D, diagonals: bool = False) -> list[Point2D]:
        """Return 2D cardinal neighbors, optionally including diagonal neighbors."""
        directions = DIAGONAL_OFFSETS if diagonals else CARDINAL_OFFSETS
        return [grid_helper.add_2d(point, direction) for direction in directions]

    @staticmethod
    def bounded_neighbors(
        point: Point2D,
        shape: Shape | None = None,
        diagonals: bool = False,
        grid_bounds: GridBounds2D | None = None,
    ) -> list[Point2D]:
        """Return neighbors that are inside a rectangular grid."""
        return [
            neighbor
            for neighbor in grid_helper.neighbors(point, diagonals=diagonals)
            if grid_helper.in_bounds(neighbor, shape=shape, grid_bounds=grid_bounds)
        ]

    @staticmethod
    def offsets(dimensions: int, include_origin: bool = False) -> list[Point]:
        """Return all adjacent offsets for an N-dimensional grid."""
        if dimensions < 1:
            raise ValueError("dimensions must be positive")

        return [
            offset
            for offset in product((-1, 0, 1), repeat=dimensions)
            if include_origin or any(value != 0 for value in offset)
        ]

    @staticmethod
    def manhattan_distance(a: Point, b: Point) -> int:
        """Return the Manhattan distance between two points."""
        return sum(abs(left - right) for left, right in zip(a, b, strict=True))

    @staticmethod
    def line_points(
        start: Point2D,
        direction: Point2D,
        amount: int,
    ) -> list[Point2D]:
        """Return points visited from start, excluding the endpoint."""
        if amount < 0:
            raise ValueError("amount must be non-negative")
        return [grid_helper.move_2d(start, direction, step) for step in range(amount)]
