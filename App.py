from appbuilder import AppBuilder as Builder


def start():
    app = Builder().build().run()


if __name__ == "__main__":
    start()
