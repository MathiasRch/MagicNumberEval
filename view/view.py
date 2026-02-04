from common.iview import IView
from common.imodel import IModel
from common.icontroller import IController


class View(IView):

    def __init__(self):
        self._controller: IController = None
        self._model: IModel = None

    def setActionPerformer(self, actionPerformer: IController) -> None:
        self._controller = actionPerformer

    def setModel(self, model: IModel) -> None:
        self._model = model

    def setController(self, controller: IController) -> None:
        self._controller = controller

    def showMessage(self, message: str) -> None:
        print(message)

    def askProposal(self) -> int:
        while True:
            try:
                return int(input("Votre proposition : "))
            except ValueError:
                print("Veuillez entrer un nombre entier.")
