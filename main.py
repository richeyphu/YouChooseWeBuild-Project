import sys
from Initialize import frm_splash as init
# from Login import frm_login
from PyQt5 import QtWidgets

if __name__ == '__main__':
    try:
        app = QtWidgets.QApplication(sys.argv)
        init.show()
        sys.exit(app.exec_())
        # init.exec_()
        # frm_login.exec_()
    except Exception as e:
        print(e)
