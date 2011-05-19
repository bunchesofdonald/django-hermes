class Markdown(object):
	""" Abstract class wrapper for Markdown """
	def markup(self, text):
		from markdown import markdown
		return markdown(text)

class HTML(object):
	""" HTML Markup. """
	def markup(self, text):
		""" We're expecting the text to be html, so we just pass it back out. """
		return text
