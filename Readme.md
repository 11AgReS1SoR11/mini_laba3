<!DOCTYPE html>
<html>

<head>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }

    h1 {
      text-align: center;
    }

    h3 {
      text-align: center;
    }

    ul {
      list-style-type: none;
      padding: 0;
    }

    li {
      margin-bottom: 10px;
    }
  </style>
</head>

<body>

  <h1 align="center">Laba#3</h1>
  <h3 align="center">My own backend app</h3>

  <h2>Animals searcher</h2>
  <p>This is a simple Python application that display images of cute pets. The application has GUI and makes requests to APIs</p>

  <h2>Prerequisites</h2>
  <ul>
    <li>Python installed (version 3.x recommended)</li>
  </ul>

  <h2>Setup and Configuration</h2>
  <ul>
    <li>Clone the Repository:
      <br>
      <code>git clone https://github.com/11AgReS1SoR11/mini_laba3.git</code>
    </li>
    <li>
      Change to the Repository Directory:
      <br>
      <code>cd mini_laba3</code>
    </li>
    <li>
      Install Dependencies:
      <br>
      <code>pip install -r requirements.txt</code>
    </li>
    <li>
      Run the Application:
      <br>
      <code>python main.py</code>
    </li>
  </ul>

  <h2>Application Logic</h2>
  <p>The main window displays three buttons: "CAT," "DOG," and "FOX."</p>
  <ul>
    <li>Each button triggers an HTTP request to a different API that provides random images of cats, dogs, and foxes.</li>
    <li>The "Exit" button closes the application.</li>
  </ul>

  <h2>Error Handling</h2>
  <p>If an error occurs during the HTTP request or image processing, an error message is displayed using Tkinter's messagebox.</p>

  <h2>Postman Documentation</h2>
  <p>
    Check out the Postman documentation for the API requests:
    <br>
    <a href="https://documenter.getpostman.com/view/31400045/2s9YeD9DRu">Postman Documentation</a>
  </p>

</body>

</html>
