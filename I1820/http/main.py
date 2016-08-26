# In The Name Of God
# ========================================
# [] File Name : main.py
#
# [] Creation Date : 26-08-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from .route import app


def main():
    app.run(debug=True, host="0.0.0.0")
