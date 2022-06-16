import pygame


class KeyBoard(object):
    def __init__(self):
        self.key_down_list = []
        self.key_pressed_list = []
        self.key_up_ist = []
        self.quit = False

    def update(self):
        self.key_down_list = []
        self.key_up_ist = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            if event.type == pygame.KEYDOWN:
                keyName = pygame.key.name(event.key)
                self.key_down_list.append(keyName)
                self.key_pressed_list.append(keyName)
            if event.type == pygame.KEYUP:
                keyName = pygame.key.name(event.key)
                self.key_pressed_list.remove(keyName)
                self.key_up_ist.append(keyName)

    def is_key_down(self, key_code):
        return key_code in self.key_down_list

    def is_key_pressed(self, key_code):
        return key_code in self.key_pressed_list

    def is_Key_up(self, key_code):
        return key_code in self.key_up_ist
