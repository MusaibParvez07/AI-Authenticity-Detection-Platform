import tempfile
import unittest
from pathlib import Path

from backend.evaluation.manifest import build_record, load_manifest, write_manifest


class ManifestTests(unittest.TestCase):
    def test_jsonl_round_trip_preserves_declared_metadata(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "sample.txt"
            sample.write_text("verified sample", encoding="utf-8")
            record = build_record(
                sample,
                modality="text",
                label="real",
                source="curated-set-a",
                transformations=("normalized",),
            )
            manifest = write_manifest([record], Path(directory) / "manifest.jsonl")
            loaded = load_manifest(manifest)

            self.assertEqual(loaded, [record])
            self.assertEqual(loaded[0].group_id, loaded[0].sha256)

    def test_csv_round_trip_keeps_optional_fields_empty(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "sample.txt"
            sample.write_text("unlabelled", encoding="utf-8")
            record = build_record(sample, modality="text")

            loaded = load_manifest(write_manifest([record], Path(directory) / "manifest.csv"))

            self.assertIsNone(loaded[0].label)
            self.assertEqual(loaded[0].transformations, ())


if __name__ == "__main__":
    unittest.main()
