from routes import app


if __name__ == '__main__':
    # SIGINT to stop (Ctrl + C)
    app.run(port=8000, debug=True)

    # Saves the data
