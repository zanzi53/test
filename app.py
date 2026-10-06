from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
app.json.ensure_ascii = False


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/api/hello")
def hello():
    name = request.args.get("name", "世界").strip() or "世界"
    if len(name) > 100:
        return jsonify(error="名前は100文字以内にしてください"), 400
    return jsonify(message=f"こんにちは、{name}！", framework="Flask")


@app.get("/healthz")
def health():
    return jsonify(status="ok")
