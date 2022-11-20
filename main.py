from view import View
from model import Model
from controller import Controller

if __name__ == '__main__':
    model = Model()
    view = View()
    control = Controller(model, view)
