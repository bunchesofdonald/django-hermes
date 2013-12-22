from django import test

from .. import renderers


class MarkdownRendererTestCase(test.TestCase):
    def test_render_to_html(self):
        """The Markdown Renderer should be able to translate Markdown to HTML"""
        expected = "<p><em>Markdown FTW!!</em></p>"
        self.assertEqual(expected, renderers.markdown("*Markdown FTW!!*"))


class ReStructuredTextRendererTestCase(test.TestCase):
    def test_render_to_html(self):
        """The RestructuredText Renderer should be able to translate ReStructuredText to HTML"""
        expected = "<p><em>ReStructuredText FTW!!</em></p>\n"
        self.assertEqual(expected, renderers.restructured_text("*ReStructuredText FTW!!*"))


class TextileRendererTestCase(test.TestCase):
    def test_render_to_html(self):
        """The Textile Renderer should be able to translate Textile to HTML"""
        expected = "\t<p><em>Textile FTW!!</em></p>"
        self.assertEqual(expected, renderers.textile("_Textile FTW!!_"))
