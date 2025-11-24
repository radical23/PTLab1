# -*- coding: utf-8 -*-
from Types import DataType
from DataReader import DataReader


class TextDataReader(DataReader):

    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as file:
            for line in file:
                stripped = line.strip()
                if not stripped:
                    continue

                # если строка содержит ":" — это предмет и балл
                if ":" in stripped:
                    subj, score = stripped.split(":", maxsplit=1)
                    self.students[self.key].append(
                        (subj.strip(), int(score.strip()))
                    )
                else:
                    # иначе это ФИО
                    self.key = stripped
                    self.students[self.key] = []

        return self.students
