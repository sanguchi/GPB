from Plugin import Plugin

class Echo(Plugin):
        
    def on_message(self, message):
        super().on_message(message)
        if(message.text[1:] == self.get_name()):
            self.bot.send_message(self.cid, self.get_help())
            return
        self.bot.send_message(self.cid, self.rest)
        
    def get_help(self):
        return "A Simple Echo Plugin."
