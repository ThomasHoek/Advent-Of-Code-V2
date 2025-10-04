from __future__ import annotations
from dataclasses import dataclass
from typing import Any, NoReturn, Optional


@dataclass
class user_file:
    """File"""

    name: str
    weight: int

    def weight_search(self) -> NoReturn:
        raise RuntimeError("Weight of File searched")

    def get_all_info(self, depth: int = 0) -> str:
        info: str = "│\t" * (depth - 1) + "├───"
        info += f"{self.name}, (file {self.weight}) \n"
        return info

    def __repr__(self) -> str:
        return f"{self.name}, (file, {self.weight})"


@dataclass
class folder:
    """Tree structure"""

    name: str
    weight: int
    parent: Optional[folder]
    children: list[user_file | folder]

    def add_weight(self, weight: int) -> None:
        """
        add_weight Adds new weight to itself and every parent folder

        Args:
            weight (int): weight of newly added
        """
        self.weight += weight
        parent: folder | None = self.get_parent_folder()
        if parent is not None:
            parent.add_weight(weight)

    def add_folder(self, name: str) -> None:
        """
        add_folder Adds a folder to children

        Args:
            name (str): folder name
        """
        self.children.append(folder(name=name, parent=self, weight=0, children=[]))

    def add_file(self, name: str, weight: int) -> None:
        """
        add_file adds a file to the current folder
        Args:
            name (str): name of the file
            weight (int): file size
        """
        self.add_weight(weight=weight)
        self.children.append(user_file(name=name, weight=weight))

    def get_parent_folder(self) -> Optional[folder]:
        """
        get_parent_folder get the folder of the parent, if it exists

        Returns:
            folder : pointer
        """
        return self.parent

    def get_child_folder(self, name: str) -> folder:
        """
        get_child_folder Finds the child folder with name

        Args:
            name (str): Name of folder to be found


        Returns:
            folder: returns folder
        """
        for item in self.children:
            if isinstance(item, folder):
                if item.name == name:
                    return item

        raise Exception(f"Code should never reach this, error in {self.children}")

    def root(self) -> folder:
        if self.name == "\\":
            return self
        else:
            return self.get_parent_folder().root()

    def get_all_info(self, depth: int = 0) -> str:
        """
        pprint gives back the underlaying folders in a pretty format

        Args:
            depth (int, optional): depth compared to root. Defaults to 0.

        Returns:
            str: string formatted
        """
        if depth == 0:
            string: str = f"{self.name}, (dir {self.weight}) \n"
        else:
            string = "│\t" * (depth - 1) + "├───"
            string += f"{self.name}, (dir {self.weight}) \n"

        for child in self.children:
            child_info: str = child.get_all_info(depth + 1)
            if child == self.children[-1]:
                child_info = child_info.replace("├", "└")
            string += child_info

        return string

    def weight_search(self) -> int:
        """
        weight_search Function to solve the puzzle

        Returns:
            int: returns the sum
        """
        value: int = 0
        if self.weight <= 100000:
            value += self.weight

        for child in self.children:
            if isinstance(child, folder):
                value += child.weight_search()

        return value

    def __repr__(self) -> str:
        return self.get_all_info()


def parse_data(input_str: list[Any]) -> list[Any]:
    """
    parse_data Parses the data into lists of a single command

    Args:
        input_str (list): puzzle input

    Returns:
        list: List of lists parsed into seperate commands
    """
    commands: list[Any] = []
    commands_index: int = -1
    for line in input_str:
        if line[0] == "$":
            commands.append([])
            commands_index += 1
        commands[commands_index].append(line)

    return commands


def puzzle(puzzle_input: list[Any]) -> int:
    puzzle_input_parsed: list[Any] = parse_data(puzzle_input)[1:]

    folder_pointer: folder = folder(name="\\", weight=0, parent=None, children=[])

    for line in puzzle_input_parsed:
        if "cd" in line[0]:
            name: str = line[0].split("cd ")[-1]
            if name == "..":
                folder_pointer = folder_pointer.get_parent_folder()  # type: ignore
                # should never be None
            else:
                folder_pointer = folder_pointer.get_child_folder(name)

        elif "ls" in line[0]:
            for content in line[1:]:
                info, name = content.split(" ")

                if info == "dir":
                    folder_pointer.add_folder(name=name)
                else:
                    folder_pointer.add_file(name=name, weight=int(info))

    return folder_pointer.root().weight_search()
