MESSAGE = 'Python Twitter API Client Library'

class Banner:

    COLOR_TEMPLATE = '\x1b[{num1};{num2}m{text}\x1b[0m'

    def __init__(self, message):
        self.fill = '\u2593'
        self.horizontal = '#@'*40
        self.vertical = ('#@'*2)+'#'
        self.spanning = self.vertical + (self.fill*70) + self.vertical
        self.message = message

    def build(self):
        self.margins()
        self.construct_boarder()
        self.colorize_boarder()
        self.colorize_message()
        self.construct_banner()
        return self.banner

    def margins(self):
        pad = (80 - len(self.message) - (len(self.vertical)*2)) /2
        if int(pad) < pad:
            lmargin, rmargin = int(pad), int(pad)+1
        else:
            lmargin = rmargin = pad
        self.lmargin = self.fill*lmargin
        self.rmargin = self.fill*rmargin

    def construct_boarder(self):
        self.boarder_1 = '''{self.horizontal}
{self.spanning}
{self.vertical}{self.lmargin}'''.format_map(vars())
        self.boarder_2 = '''{self.rmargin}{self.vertical}
{self.spanning}
{self.horizontal}'''.format_map(vars())

    def colorize_boarder(self, num1=2, num2=96):
        text = self.boarder_1
        self.boarder_1 = Banner.COLOR_TEMPLATE.format_map(vars())
        text = self.boarder_2
        self.boarder_2 = Banner.COLOR_TEMPLATE.format_map(vars())

    def colorize_message(self, num1=5, num2=96):
        text = self.message
        self.message = Banner.COLOR_TEMPLATE.format_map(vars())

    def construct_banner(self):
        self.banner = self.boarder_1 + self.message + self.boarder_2

banner = Banner(MESSAGE)
banner = banner.build()
