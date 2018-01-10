from django.test import TestCase
from website.models import Board
from django.utils import timezone


class BoardAttributeTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Board.objects.create(title="test_title", text="test_title",
                             writer="test_writer", hit=0)

    def setUp(self):
        self.board = Board.objects.get(id=1)

    def test_field_label(self):
        """
        Test Board model's field label
        """
        field_label = self.board._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')
        field_label = self.board._meta.get_field('text').verbose_name
        self.assertEqual(field_label, 'text')
        field_label = self.board._meta.get_field('created_date').verbose_name
        self.assertEqual(field_label, 'created date')
        field_label = self.board._meta.get_field('writer').verbose_name
        self.assertEqual(field_label, 'writer')
        field_label = self.board._meta.get_field('hit').verbose_name
        self.assertEqual(field_label, 'hit')

    def test_field_max_length(self):
        """
        Test Board model's field max_length
        :return:
        """
        max_length = self.board._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)
        max_length = self.board._meta.get_field('writer').max_length
        self.assertEqual(max_length, 20)

    def test_string_representation(self):
        """
        __str__ function test for Board Model
        """
        board = Board(title="String Test")
        self.assertEqual(str(board), board.title)