# Copyright 2022 Amethyst Reese
# Licensed under the MIT License

from unittest import expectedFailure, TestCase


class MainTest(TestCase):
    def test_one(self) -> None:
        self.assertTrue(True)

    @expectedFailure
    def test_two(self) -> None:
        self.assertListEqual([1, 2, 3], [1, 2, 3, 4])
