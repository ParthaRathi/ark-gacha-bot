"""
dedi inventory
"""


from pytesseract import pytesseract as tes # type: ignore[import]
from ark.exceptions import NoItemsDepositedError
from ark.inventories.inventory import Inventory
from ark.items import Item


class DedicatedStorageInventory(Inventory):
    """Represents the Dedicated Storage Box in ark.

    Contains dedi specific methods such as depositing.

    TO-DO: Add methods for withdrawing.
    """

    def __init__(self):
        super().__init__("Tek Dedicated Storage", "dedi")

    def can_be_opened(self) -> bool:
        """Checks if the dedi can be opened by attempting to do so"""
        c = 0
        max_time = 5

        while not self.is_open():
            c += 1
            # wait for 1s if the dedi opens
            self.press(self.keybinds.target_inventory)
            if self.await_open():
                break

            if c == 2:
                if not self.in_access_range():
                    return False
                print("Timer appears to be popping!")
                max_time = 30

            if c > max_time:
                return False
        return True