def application(environ, start_response):
    status = '200 OK'
    output = b"""
        {
            "name": "hoge",
            "age": "26"
        }
    """
        # <!DOCTYPE html>
        # <html>
        # <head>
        # <title>Page Title</title>
        # </head>
        # <body>

        # <h1>This is a Heading</h1>
        # <p>This is a paragraph.</p>

        # </body>
        # </html>

    response_headers = [
        # ('Content-type', 'application/json'),
        ('Content-type', 'text/html'),
        ('Content-Length', str(len(output)))
    ]
    start_response(status, response_headers)
    return [output]
