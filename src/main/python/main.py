from fbs_runtime.application_context.PyQt5 import ApplicationContext
import sys
from main_window import MainWindow

if __name__ == '__main__':
    appctxt = ApplicationContext()
    main_window = MainWindow()
    main_window.show()
    exit_code = appctxt.app.exec_()  # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
