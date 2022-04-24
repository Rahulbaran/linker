from linker import app


# RUNNING APP IN PYTHONIC WAY
if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True, load_dotenv=True)
