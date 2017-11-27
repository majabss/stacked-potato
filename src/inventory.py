""" Logic for inventory """

import pygame


class Inventory(pygame.sprite.DirtySprite):

    def __init__(self):
        pygame.sprite.DirtySprite.__init__(self)
        self.rect = pygame.Rect(0, 0, 200, 100)
        self.image = pygame.Surface([200, 100])
        self.image.fill((120, 30, 40))
        self.selected_img = pygame.Surface([48, 48])
        self.selected_img.fill((255, 16, 27))

        self.slots = []
        for i in range(8):
            x = i * 50 if i < 4 else (i % 4) * 50
            y = 0 if i < 4 else 50
            new_rect = Slot(x, y)
            self.slots.append(new_rect)
        
        self.visible = 0
        self.selected_slot = 0
        self.next_slot = 0


        self.items = [ None for _ in range(8) ]
    
    def update(self, input, delta):

        if "up" in input:
            if self.selected_slot > 3:
                self.selected_slot -= 4
        if "down" in input:
            if self.selected_slot < 4:
                self.selected_slot += 4
        if "left" in input:
            if self.selected_slot != 0 and self.selected_slot != 4:
                self.selected_slot -= 1
        if "right" in input:
            if self.selected_slot != 3 and self.selected_slot != 7:
                self.selected_slot += 1
        if "inv" in input:
            if self.visible == 1:
                self.hide_inventory()
            else:
                self.show_inventory()
                
    
    def add_item(self, new_item):

        self.item[self.next_slot] = new_item

    
    # Set all slots/item icons, to visible
    def show_inventory(self):
        self.visible = 1
        for item in self.items:
            if item is not None:
                item.visible = 1
        for slot in self.slots:
            if slot is not None:
                slot.visible = 1
    
    def hide_inventory(self):
        self.visible = 0
        for item in self.items:
            if item is not None:
                item.visible = 0
        for slot in self.slots:
            if slot is not None:
                slot.visible = 0

        

class Slot(pygame.sprite.DirtySprite):

    def __init__(self, x, y):
        pygame.sprite.DirtySprite.__init__(self)

        self.rect = pygame.Rect(x, y, 48, 48)
        self.visible = 0
        self.image = pygame.Surface([48, 48])
    

class Item(pygame.sprite.DirtySprite):

    def __init__(self, x, y):
        pygame.sprite.DirtySprite.__init__(self)
        self.visible = 0
        self.dirty = 1
        self.image = pygame.Surface([10, 10])
        self.image.fill((255, 255, 255))
        self.rect = pygame.Rect(x, y, 10, 10)




