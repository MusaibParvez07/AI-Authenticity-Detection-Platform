import unittest

from backend.evaluation.image_baseline import evaluate_image_baseline
from backend.evaluation.manifest import DatasetRecord


def _records():
    return [
        DatasetRecord(path="real-1.jpg", modality="image", label="real", group_id="r1"),
        DatasetRecord(path="real-2.jpg", modality="image", label="real", group_id="r2"),
        DatasetRecord(path="fake-1.jpg", modality="image", label="fake", group_id="f1"),
        DatasetRecord(path="fake-2.jpg", modality="image", label="fake", group_id="f2"),
    ]


class ImageBaselineTests(unittest.TestCase):
    def test_evaluates_a_predictor_without_loading_a_model(self):
        outputs = {
            "real-1.jpg": {"prediction": "real", "confidence": 0.9},
            "real-2.jpg": {"prediction": "fake", "confidence": 0.8},
            "fake-1.jpg": {"prediction": "real", "confidence": 0.8},
            "fake-2.jpg": {"prediction": "fake", "confidence": 0.9},
        }

        result = evaluate_image_baseline(_records(), outputs.__getitem__)

        self.assertEqual(result.records_evaluated, 4)
        self.assertEqual(result.metrics.confusion_matrix, ((1, 1), (1, 1)))
        self.assertEqual(result.metrics.roc_auc, 0.75)
        self.assertEqual(len(result.fake_scores), 4)
        for actual, expected in zip(result.fake_scores, (0.1, 0.8, 0.2, 0.9)):
            self.assertAlmostEqual(actual, expected)
        self.assertEqual(len(result.latency.samples_ms), 4)

    def test_rejects_unreviewed_labels(self):
        records = _records()
        records[0] = DatasetRecord(path="unknown.jpg", modality="image", group_id="unknown")

        with self.assertRaisesRegex(ValueError, "reviewed real/fake labels"):
            evaluate_image_baseline(records, lambda _: {"prediction": "real", "confidence": 0.9})


if __name__ == "__main__":
    unittest.main()
