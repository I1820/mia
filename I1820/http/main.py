# In The Name Of God
# ========================================
# [] File Name : main.py
#
# [] Creation Date : 26-08-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from .route import app
from .route import socketio


def main():
    socketio.run(app, host="0.0.0.0", port=8080, debug=False)
