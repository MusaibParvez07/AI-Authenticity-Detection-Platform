import unittest

from backend.evaluation.metrics import evaluate_binary_classification


class MetricsTests(unittest.TestCase):
    def test_binary_metrics_are_calculated_from_supplied_results(self):
        result = evaluate_binary_classification(
            ["real", "real", "fake", "fake"],
            ["real", "fake", "real", "fake"],
            scores=[0.1, 0.8, 0.2, 0.9],
        )

        self.assertEqual(result.confusion_matrix, ((1, 1), (1, 1)))
        self.assertEqual(result.accuracy, 0.5)
        self.assertEqual(result.precision, 0.5)
        self.assertEqual(result.recall, 0.5)
        self.assertEqual(result.f1, 0.5)
        self.assertEqual(result.false_positive_rate, 0.5)
        self.assertEqual(result.false_negative_rate, 0.5)
        self.assertEqual(result.roc_auc, 0.75)

    def test_roc_auc_is_unavailable_for_single_class_ground_truth(self):
        result = evaluate_binary_classification(
            ["fake", "fake"],
            ["fake", "real"],
            scores=[0.9, 0.1],
        )

        self.assertIsNone(result.roc_auc)


if __name__ == "__main__":
    unittest.main()
