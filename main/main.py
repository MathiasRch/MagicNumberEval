from controller.controller import Controller
from view.view import View
from model.model import Model


def main():
    model = Model()
    view = View()
    controller = Controller()

    controller.setModel(model)
    controller.setView(view)

    view.setModel(model)
    view.setController(controller)

    controller.start()


if __name__ == "__main__":
    main()
