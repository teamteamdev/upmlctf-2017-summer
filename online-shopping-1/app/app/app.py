from flask import Flask, render_template, abort, request, redirect

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('main.html')


@app.route('/goods/<int:good_id>/')
def good(good_id):
    good_data = {}
    if good_id == 1:
        good_data = {
            "item": "Флаг Франции",
            "id": 1,
            "price": 0
        }
    elif good_id == 2:
        good_data = {
            "item": "Флаг CTF",
            "id": 2,
            "price": "29.99"
        }
    else:
        abort(404)
    if request.args.get("error"):
        good_data["error"] = request.args.get("error")
    return render_template("buy.html", **good_data)


@app.route('/process/')
def process():
    id = 0
    price = 0
    try:
        id = int(request.args["id"])
    except:
        abort(403)
    try:
        price = float(request.args["price"])
    except:
        abort(403)
    card_number = request.args.get("card", "")
    if len(card_number) != 16 or not card_number.isdigit():
        return redirect("/goods/{}/?error=Wrong+card+number".format(id))

    if id < 1 or id > 2:
        abort(403)

    if price == 0:
        if id == 1:
            url = "https://otvet.imgsmail.ru/download/0112648fc905ace76cb9407ea9528d2c_i-1978.jpg"
        else:
            url = "/static/hadhy3yj9034y09er0heq0n.txt"
        return render_template("success.html", url=url)

    good_data = {
        "id": id,
        "price": price,
        "card_number": card_number
    }
    if request.args.get("error"):
        good_data["error"] = request.args.get("error")
    return render_template("check_code.html", **good_data)


@app.route('/check_sms/')
def check_code():
    id = request.args.get("id", "")
    price = request.args.get("price", "")
    card = request.args.get("card", "")
    return redirect("/process/?id={}&price={}&card={}&error=Wrong+SMS+code".format(id, price, card))


if __name__ == '__main__':
    app.run()
