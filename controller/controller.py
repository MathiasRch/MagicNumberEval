from common.imodel import IModel
from common.iview import IView
from common.icontroller import IController


class Controller(IController):

    def __init__(self):
        self._view: IView = None
        self._model: IModel = None

    def setView(self, view: IView) -> None:
        self._view = view

    def setModel(self, model: IModel) -> None:
        self._model = model

    def start(self) -> None:
        self._view.showMessage("Bienvenue dans le jeu du nombre magique !")

        while self._model.getProposalCount() < self._model.getMaxNumberOfProposals():
            num = self._view.askProposal()
            result = self._model.compareToMagicNumber(num)
            self.performProposeNumber(result)

            if result == 0:
                return

        self._view.showMessage("Vous avez atteint le nombre maximum de tentatives.")

    def performProposeNumber(self, result: int) -> None:
        if result == 0:
            self._view.showMessage("Bravo, vous avez trouvé le nombre magique !")
        elif result < 0:
            self._view.showMessage("Trop petit.")
        else:
            self._view.showMessage("Trop grand.")

        remaining = self._model.getMaxNumberOfProposals() - self._model.getProposalCount()
        self._view.showMessage(f"Tentatives restantes : {remaining}")
