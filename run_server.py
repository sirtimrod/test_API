from app import app, session


# This function close the session
@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()


# That "if" cycle starting server with debugging
if __name__ == "__main__":
    app.run(debug='True')