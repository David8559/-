from __future__ import annotations

import sys
import unittest
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from joint_coverage import joint_sightline_margin
from problem1_model import point_to_segment_distance


class JointCoverageTests(unittest.TestCase):
    def test_two_clouds_can_cover_different_sight_lines(self) -> None:
        missile = np.array([0.0, 0.0, 0.0])
        targets = np.array([[10.0, -1.0, 0.0], [10.0, 1.0, 0.0]])
        clouds = np.array([[5.0, -0.5, 0.0], [5.0, 0.5, 0.0]])
        radius = 0.1

        individual_worst = []
        for cloud in clouds:
            distances, _ = point_to_segment_distance(cloud, missile, targets)
            individual_worst.append(float(np.max(distances)))

        self.assertTrue(all(value > radius for value in individual_worst))
        self.assertLessEqual(
            joint_sightline_margin(missile, targets, clouds, radius), 0.0
        )

    def test_single_cloud_matches_worst_sightline_distance(self) -> None:
        missile = np.array([0.0, 0.0, 0.0])
        targets = np.array([[10.0, -1.0, 0.0], [10.0, 1.0, 0.0]])
        cloud = np.array([5.0, 0.0, 0.0])
        radius = 0.25
        distances, _ = point_to_segment_distance(cloud, missile, targets)
        expected = float(np.max(distances) - radius)
        self.assertAlmostEqual(
            joint_sightline_margin(
                missile, targets, np.asarray([cloud]), radius
            ),
            expected,
        )

    def test_empty_cloud_set_is_not_effective(self) -> None:
        margin = joint_sightline_margin(
            np.zeros(3),
            np.array([[1.0, 0.0, 0.0]]),
            np.empty((0, 3)),
            1.0,
        )
        self.assertTrue(np.isinf(margin))


if __name__ == "__main__":
    unittest.main()
