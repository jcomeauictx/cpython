import tempfile
import unittest
import sys
from unittest.mock import patch
from test import support

try:
    from _pyrepl.console import Event
    from _pyrepl import base_eventqueue
except ImportError:
    pass

try:
    from _pyrepl import unix_eventqueue
except ImportError:
    pass

try:
    from _pyrepl import windows_eventqueue
except ImportError:
    pass

class EventQueueTestBase:
    """OS-independent mixin"""
    def make_eventqueue(self) -> base_eventqueue.BaseEventQueue:
        raise NotImplementedError()

    def test_get(self):
        eq = self.make_eventqueue()
        event = Event("key", "a", b"a")
        eq.insert(event)
        self.assertEqual(eq.get(), event)

    def test_empty(self):
        eq = self.make_eventqueue()
        self.assertTrue(eq.empty())
        eq.insert(Event("key", "a", b"a"))
        self.assertFalse(eq.empty())

    def test_flush_buf(self):
        eq = self.make_eventqueue()
        eq.buf.extend(b"test")
        self.assertEqual(eq.flush_buf(), b"test")
        self.assertEqual(eq.buf, bytearray())

    def test_insert(self):
        eq = self.make_eventqueue()
        event = Event("key", "a", b"a")
        eq.insert(event)
        self.assertEqual(eq.events[0], event)

    @patch("_pyrepl.base_eventqueue.keymap")
    def test_push_with_key_in_keymap(self, mock_keymap):
        mock_keymap.compile_keymap.return_value = {"a": "b"}
        eq = self.make_eventqueue()
        eq.keymap = {b"a": "b"}
        eq.push("a")
        mock_keymap.compile_keymap.assert_called()
        self.assertEqual(eq.events[0].evt, "key")
        self.assertEqual(eq.events[0].data, "b")

    @patch("_pyrepl.base_eventqueue.keymap")
    def test_push_without_key_in_keymap(self, mock_keymap):
        mock_keymap.compile_keymap.return_value = {"a": "b"}
        eq = self.make_eventqueue()
        eq.keymap = {b"c": "d"}
        eq.push("a")
        mock_keymap.compile_keymap.assert_called()
        self.assertEqual(eq.events[0].evt, "key")
        self.assertEqual(eq.events[0].data, "a")

    @patch("_pyrepl.base_eventqueue.keymap")
    def test_push_with_keymap_in_keymap(self, mock_keymap):
        mock_keymap.compile_keymap.return_value = {"a": "b"}
        eq = self.make_eventqueue()
        eq.keymap = {b"a": {b"b": "c"}}
        eq.push("a")
        mock_keymap.compile_keymap.assert_called()
        self.assertTrue(eq.empty())
        eq.push("b")
        self.assertEqual(eq.events[0].evt, "key")
        self.assertEqual(eq.events[0].data, "c")
        eq.push("d")
        self.assertEqual(eq.events[1].evt, "key")
        self.assertEqual(eq.events[1].data, "d")

    @patch("_pyrepl.base_eventqueue.keymap")
    def test_push_with_keymap_in_keymap_and_escape(self, mock_keymap):
        mock_keymap.compile_keymap.return_value = {"a": "b"}
        eq = self.make_eventqueue()
        eq.keymap = {b"a": {b"b": "c"}}
        eq.push("a")
        mock_keymap.compile_keymap.assert_called()
        self.assertTrue(eq.empty())
        eq.flush_buf()
        eq.push("\033")
        self.assertEqual(eq.events[0].evt, "key")
        self.assertEqual(eq.events[0].data, "\033")
        eq.push("b")
        self.assertEqual(eq.events[1].evt, "key")
        self.assertEqual(eq.events[1].data, "b")

    def test_push_special_key(self):
        eq = self.make_eventqueue()
        eq.keymap = {}
        eq.push("\x1b")
        eq.push("[")
        eq.push("A")
        self.assertEqual(eq.events[0].evt, "key")
        self.assertEqual(eq.events[0].data, "\x1b")

    def test_push_unrecognized_escape_sequence(self):
        eq = self.make_eventqueue()
        eq.keymap = {}
        eq.push("\x1b")
        eq.push("[")
        eq.push("Z")
        self.assertEqual(len(eq.events), 3)
        self.assertEqual(eq.events[0].evt, "key")
        self.assertEqual(eq.events[0].data, "\x1b")
        self.assertEqual(eq.events[1].evt, "key")
        self.assertEqual(eq.events[1].data, "[")
        self.assertEqual(eq.events[2].evt, "key")
        self.assertEqual(eq.events[2].data, "Z")


@unittest.skipIf(support.MS_WINDOWS, "No Unix event queue on Windows")
class TestUnixEventQueue(EventQueueTestBase, unittest.TestCase):
    def setUp(self):
        self.enterContext(patch("_pyrepl.curses.tigetstr", lambda x: b""))
        self.file = tempfile.TemporaryFile()

    def tearDown(self) -> None:
        self.file.close()

    def make_eventqueue(self) -> base_eventqueue.BaseEventQueue:
        return unix_eventqueue.EventQueue(self.file.fileno(), "utf-8")


@unittest.skipUnless(support.MS_WINDOWS, "No Windows event queue on Unix")
class TestWindowsEventQueue(EventQueueTestBase, unittest.TestCase):
    def make_eventqueue(self) -> base_eventqueue.BaseEventQueue:
        return windows_eventqueue.EventQueue("utf-8")
