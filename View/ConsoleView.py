from ProjectPiouPiou.View.AbstractView import AbstractView


class ConsoleView(AbstractView):
    def displayLand(self, representation):
        print(representation)