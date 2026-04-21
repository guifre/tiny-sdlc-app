import os
import time

from flask import Flask, jsonify, redirect, render_template_string, request, url_for
from sqlalchemy import Column, Integer, String, create_engine, text
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_DB_URL = f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}"
DATABASE_URL = os.getenv("DATABASE_URL", DEFAULT_DB_URL)

app = Flask(__name__)
engine = create_engine(DATABASE_URL, future=True, pool_pre_ping=True)
Session = scoped_session(sessionmaker(bind=engine, autoflush=False, autocommit=False))
Base = declarative_base()


class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True)
    title = Column(String(120), nullable=False)


def init_db():
    retries = int(os.getenv("DB_CONNECT_RETRIES", "1"))
    delay = float(os.getenv("DB_CONNECT_DELAY", "2"))
    last_error = None

    for attempt in range(1, retries + 1):
        try:
            Base.metadata.create_all(engine)
            return
        except OperationalError as exc:
            last_error = exc
            if attempt == retries:
                raise
            time.sleep(delay)

    if last_error is not None:
        raise last_error


PAGE_TEMPLATE = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Tiny SDLC App</title>
    <style>
      body {
        font-family: sans-serif;
        margin: 2rem auto;
        max-width: 42rem;
        padding: 0 1rem;
      }
      form, ul {
        margin-top: 1.5rem;
      }
      input, button {
        font-size: 1rem;
        padding: 0.6rem;
      }
      input {
        width: 70%;
      }
    </style>
  </head>
  <body>
    <h1>Tiny SDLC App</h1>
    <p>This app is intentionally small so we can containerize it, deploy it, and scan it.</p>

    <form method="post" action="{{ url_for('create_note') }}">
      <input name="title" placeholder="Add a note title" required>
      <button type="submit">Save</button>
    </form>

    <ul>
      {% for note in notes %}
      <li>{{ note.title }}</li>
      {% else %}
      <li>No notes yet.</li>
      {% endfor %}
    </ul>
  </body>
</html>
"""


@app.teardown_appcontext
def shutdown_session(exception=None):
    Session.remove()


@app.get("/healthz")
def healthcheck():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    return jsonify({"status": "ok", "database": "ok"})


@app.get("/api/notes")
def list_notes():
    session = Session()
    notes = session.query(Note).order_by(Note.id.desc()).all()
    return jsonify([{"id": note.id, "title": note.title} for note in notes])


@app.get("/")
def home():
    session = Session()
    notes = session.query(Note).order_by(Note.id.desc()).all()
    return render_template_string(PAGE_TEMPLATE, notes=notes)


@app.post("/notes")
def create_note():
    title = request.form.get("title", "").strip()
    if not title:
        return redirect(url_for("home"))

    session = Session()
    session.add(Note(title=title))
    session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")))
