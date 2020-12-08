from flask import Blueprint, request, redirect, url_for, session, render_template




product = Blueprint("product", __name__, template_folder="templates")



@product.route("/")
def product_page():
    is_login = session.get("is_login", False)
    if is_login == True:
        return render_template("product.html")
    else:
        return render_template("login.html")