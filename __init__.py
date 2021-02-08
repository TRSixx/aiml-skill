from mycroft import MycroftSkill, intent_file_handler


class Aiml(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('aiml.intent')
    def handle_aiml(self, message):
        self.speak_dialog('aiml')


def create_skill():
    return Aiml()

