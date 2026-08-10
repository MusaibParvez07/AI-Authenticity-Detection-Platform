import unittest

from backend.evaluation.manifest import DatasetRecord
from backend.evaluation.splits import split_records


def _records():
    return [
        DatasetRecord(
            path=f"{label}-{index}.dat",
            modality="image",
            label=label,
            group_id=f"{label}-group-{index}",
        )
        for label in ("real", "fake")
        for index in range(4)
    ]


class SplitTests(unittest.TestCase):
    def test_split_is_deterministic_and_group_isolated(self):
        first = split_records(_records(), validation_size=0.25, test_size=0.25, seed=7)
        second = split_records(_records(), validation_size=0.25, test_size=0.25, seed=7)

        self.assertEqual(first, second)
        groups = [
            {record.group_id for record in split}
            for split in (first.train, first.validation, first.test)
        ]
        self.assertFalse(groups[0] & groups[1])
        self.assertFalse(groups[0] & groups[2])
        self.assertFalse(groups[1] & groups[2])

    def test_unlabelled_records_are_rejected(self):
        records = _records()
        records[0] = DatasetRecord(path="unknown.dat", modality="image", group_id="unknown")

        with self.assertRaisesRegex(ValueError, "reviewed labels"):
            split_records(records)


if __name__ == "__main__":
    unittest.main()
