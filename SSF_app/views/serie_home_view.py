from django.http import HttpResponse

def home_view4(request):
    from SSF_app.routers.series_router import serie_router  # Delay the import
    base_url = request.build_absolute_uri('/api/api_series/')

    html_output = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SSF Serie API</title>
        <!-- Bootstrap CSS -->
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {
                background-color: #f8f9fa;
                font-family: 'Arial', sans-serif;
                color: #333;
            }
            .container {
                max-width: 800px;
                padding: 30px;
                background-color: #fff;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                margin-top: 50px;
            }
            .header {
                text-align: center;
                margin-bottom: 30px;
            }
            .header h1 {
                font-size: 2.5em;
                color: #007bff;
            }
            ul {
                list-style-type: none;
                padding: 0;
            }
            li {
                margin: 10px 0;
                transition: transform 0.3s ease, background-color 0.3s ease;
                border-radius: 5px;
            }
            li:hover {
                background-color: #f1f1f1;
                transform: scale(1.02);
            }
            a {
                text-decoration: none;
                color: #007bff;
                font-weight: 500;
                display: block;
                padding: 10px 15px;
            }
            a:hover {
                text-decoration: underline;
                color: #0056b3;
            }
            .btn-container {
                text-align: center;
                margin-top: 20px;
            }
            .btn {
                background-color: #007bff;
                border: none;
                padding: 10px 20px;
                font-size: 16px;
                border-radius: 5px;
                color: #fff;
                transition: background-color 0.3s ease, transform 0.3s ease;
            }
            .btn:hover {
                background-color: #0056b3;
                transform: scale(1.05);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>SSF Serie API</h1>
            </div>
            <ul class="list-group">
    """

    # Generate the list items for each registered route in serie_router
    for prefix, viewset, basename in serie_router.registry:
        url = f"{base_url}{prefix}/"
        html_output += f"<li class='list-group-item'><a href='{url}'>{prefix.capitalize()} API</a></li>\n"

    html_output += """
            </ul>
            <div class="btn-container">
                <form action="/home/" method="get">
                    <button type="submit" class="btn btn-primary">Community API</button>
                </form>
                <br>
                <form action="/home2/" method="get">
                    <button type="submit" class="btn btn-primary">Competition API</button>
                </form>
                <br>
                <form action="/home3/" method="get">
                    <button type="submit" class="btn btn-primary">Scoring API</button>
                </form>
            </div>
        </div>
        <!-- Bootstrap JS and dependencies -->
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    </body>
    </html>
    """
    return HttpResponse(html_output)
