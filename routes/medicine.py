from flask import Blueprint, render_template, request, redirect, url_for, flash

from database import get_connection
from services.sns_service import send_low_stock_alert


medicine_bp = Blueprint("medicine", __name__)


# ==========================
# Home / Medicine List
# ==========================
@medicine_bp.route("/")
def home():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM medicines ORDER BY id DESC")

    medicines = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        "index.html",
        medicines=medicines
    )



# ==========================
# Dashboard
# ==========================
@medicine_bp.route("/dashboard")
def dashboard():

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute(
        "SELECT COUNT(*) AS total FROM medicines"
    )
    total = cursor.fetchone()["total"]


    cursor.execute(
        """
        SELECT COUNT(*) AS low_stock
        FROM medicines
        WHERE quantity <= threshold_quantity
        """
    )
    low_stock = cursor.fetchone()["low_stock"]


    cursor.execute(
        """
        SELECT COUNT(*) AS out_of_stock
        FROM medicines
        WHERE quantity = 0
        """
    )
    out_of_stock = cursor.fetchone()["out_of_stock"]


    cursor.execute(
        """
        SELECT SUM(price * quantity) AS inventory_value
        FROM medicines
        """
    )

    result = cursor.fetchone()

    inventory_value = result["inventory_value"] or 0



    cursor.execute(
        """
        SELECT *
        FROM medicines
        ORDER BY created_at DESC
        LIMIT 5
        """
    )

    medicines = cursor.fetchall()


    cursor.close()
    conn.close()


    return render_template(
        "dashboard.html",
        total=total,
        low_stock=low_stock,
        out_of_stock=out_of_stock,
        inventory_value=inventory_value,
        medicines=medicines
    )



# ==========================
# Add Medicine Page
# ==========================
@medicine_bp.route("/add-medicine")
def add_medicine_page():

    return render_template(
        "add_medicine.html"
    )



# ==========================
# Add Medicine
# ==========================
@medicine_bp.route("/add-medicine", methods=["POST"])
def add_medicine():


    medicine_name = request.form["medicine_name"]
    company = request.form["company"]
    price = request.form["price"]
    quantity = request.form["quantity"]
    threshold_quantity = request.form["threshold_quantity"]
    expiry_date = request.form["expiry_date"]



    conn = get_connection()
    cursor = conn.cursor()



    cursor.execute(
        """
        INSERT INTO medicines
        (
            medicine_name,
            company,
            price,
            quantity,
            threshold_quantity,
            expiry_date
        )
        VALUES
        (%s,%s,%s,%s,%s,%s)
        """,
        (
            medicine_name,
            company,
            price,
            quantity,
            threshold_quantity,
            expiry_date
        )
    )



    conn.commit()

    cursor.close()
    conn.close()


    flash("Medicine added successfully")


    return redirect(
        url_for("medicine.home")
    )



# ==========================
# Delete Medicine
# ==========================
@medicine_bp.route("/delete-medicine/<int:id>")
def delete_medicine(id):


    conn = get_connection()
    cursor = conn.cursor()



    cursor.execute(
        """
        DELETE FROM medicines
        WHERE id=%s
        """,
        (id,)
    )


    conn.commit()


    cursor.close()
    conn.close()


    flash("Medicine deleted")


    return redirect(
        url_for("medicine.home")
    )



# ==========================
# Sell Medicine Page
# ==========================
@medicine_bp.route("/sell-medicine/<int:id>")
def sell_medicine_page(id):


    conn = get_connection()
    cursor = conn.cursor()



    cursor.execute(
        """
        SELECT *
        FROM medicines
        WHERE id=%s
        """,
        (id,)
    )


    medicine = cursor.fetchone()



    cursor.close()
    conn.close()



    return render_template(
        "sell_medicine.html",
        medicine=medicine
    )



# ==========================
# Sell Medicine
# ==========================
@medicine_bp.route("/sell-medicine/<int:id>", methods=["POST"])
def sell_medicine(id):


    sold_quantity = int(
        request.form["sold_quantity"]
    )



    conn = get_connection()
    cursor = conn.cursor()



    cursor.execute(
        """
        SELECT *
        FROM medicines
        WHERE id=%s
        """,
        (id,)
    )


    medicine = cursor.fetchone()



    if sold_quantity > medicine["quantity"]:

        flash("Not enough stock")

        cursor.close()
        conn.close()

        return redirect(
            url_for("medicine.home")
        )



    new_quantity = (
        medicine["quantity"]
        -
        sold_quantity
    )



    cursor.execute(
        """
        UPDATE medicines
        SET quantity=%s
        WHERE id=%s
        """,
        (
            new_quantity,
            id
        )
    )



    conn.commit()


    cursor.close()
    conn.close()



    if new_quantity <= medicine["threshold_quantity"]:
        print ("sns triggered")

        send_low_stock_alert(
            medicine["medicine_name"],
            new_quantity,
            medicine["threshold_quantity"]
        )



    flash("Medicine sold successfully")


    return redirect(
        url_for("medicine.home")
    )



# ==========================
# Edit Medicine Page
# ==========================
@medicine_bp.route("/edit-medicine/<int:id>")
def edit_medicine(id):


    conn = get_connection()
    cursor = conn.cursor()



    cursor.execute(
        """
        SELECT *
        FROM medicines
        WHERE id=%s
        """,
        (id,)
    )


    medicine = cursor.fetchone()



    cursor.close()
    conn.close()



    return render_template(
        "edit_medicine.html",
        medicine=medicine
    )



# ==========================
# Update Medicine
# ==========================
@medicine_bp.route("/edit-medicine/<int:id>", methods=["POST"])
def update_medicine(id):


    medicine_name = request.form["medicine_name"]
    company = request.form["company"]
    price = request.form["price"]
    quantity = request.form["quantity"]
    threshold_quantity = request.form["threshold_quantity"]
    expiry_date = request.form["expiry_date"]



    conn = get_connection()
    cursor = conn.cursor()



    cursor.execute(
        """
        UPDATE medicines
        SET
        medicine_name=%s,
        company=%s,
        price=%s,
        quantity=%s,
        threshold_quantity=%s,
        expiry_date=%s
        WHERE id=%s
        """,
        (
            medicine_name,
            company,
            price,
            quantity,
            threshold_quantity,
            expiry_date,
            id
        )
    )



    conn.commit()


    cursor.close()
    conn.close()



    flash("Medicine updated successfully")


    return redirect(
        url_for("medicine.home")
    )
