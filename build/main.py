import os

def generate_gallery():
    html = """
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="UTF-8">
        <title>austin :: gallery</title>
        <link rel="stylesheet" href="css/styles.css">
        <link rel="preconnect" href="https://fonts.gstatic.com">
        <link href="https://fonts.googleapis.com/css2?family=Warnes&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Consolas&display=swap" rel="stylesheet">
      </head>
      <body>
        <header>
          <h1>austin</h1>
          <nav>
            <ul>
              <li><a href="index.html">Home</a></li>
              <li><span>&bull;</span></li>
              <li><a href="about.html">About</a></li>
              <li><span>&bull;</span></li>
              <li><a href="links.html">Links</a></li>
            </ul>
          </nav>
        </header>
        <div>
          <main>
            <h2>art gallery</h2>
            <div class="gallery">
              {}
            </div>
          </main>
        </div>
        <footer>
          <p>Copyright 2023 austin parker</p>
        </footer>
      </body>
    </html>
    """

    images = []
    for file in os.listdir("public/assets/art"):
        if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png") or file.endswith(".gif"):
            images.append('<img src="/assets/art/{}" alt="{}">'.format(file, file))

    gallery_html = html.format("\n".join(images))
    with open("public/gallery.html", "w") as f:
        f.write(gallery_html)

generate_gallery()