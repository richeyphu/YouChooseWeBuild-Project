import sys
from Initialize import frm_splash as init
from PyQt5 import QtWidgets


def run():
    try:
        app = QtWidgets.QApplication(sys.argv)
        init.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(e)


if __name__ == '__main__':
    run()
