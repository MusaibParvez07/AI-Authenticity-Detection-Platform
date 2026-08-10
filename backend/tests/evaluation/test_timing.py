import unittest

from backend.evaluation.timing import measure_latency


class TimingTests(unittest.TestCase):
    def test_measurement_runs_exactly_warmup_plus_repeats(self):
        calls = 0

        def operation():
            nonlocal calls
            calls += 1

        result = measure_latency(operation, repeats=3, warmup=2)

        self.assertEqual(calls, 5)
        self.assertEqual(len(result.samples_ms), 3)
        self.assertGreaterEqual(result.min_ms, 0.0)
        self.assertGreaterEqual(result.max_ms, result.min_ms)


if __name__ == "__main__":
    unittest.main()
