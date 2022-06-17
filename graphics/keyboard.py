import pygame


class KeyBoard(object):
    def __init__(self):
        # the following list hold the key states
        self.keyboard_down_list = []
        self.keyboard_pressed_list = []
        self.keyboard_up_ist = []
        self.quit = False

    def update(self):
        self.keyboard_down_list = []
        self.keyboard_up_ist = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            # here we check for key is down or up
            # we get the name of the key
            if event.type == pygame.KEYDOWN:
                keyName = pygame.key.name(event.key)
                self.keyboard_down_list.append(keyName)
                self.keyboard_pressed_list.append(keyName)
            if event.type == pygame.KEYUP:
                keyName = pygame.key.name(event.key)
                self.keyboard_pressed_list.remove(keyName)
                self.keyboard_up_ist.append(keyName)

    def is_key_down(self, key_code):
        return key_code in self.keyboard_down_list

    def is_key_pressed(self, key_code):
        return key_code in self.keyboard_pressed_list

    def is_Key_up(self, key_code):
        return key_code in self.keyboard_up_ist
