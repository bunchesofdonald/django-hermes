def markdown(markup):
    import markdown as md
    return md.markdown(markup)


def restructured_text(markup):
    from docutils import core
    return core.publish_parts(markup, writer_name='html')['fragment']


def textile(markup):
    import textile as tex
    return tex.textile(markup, html_type='html')
