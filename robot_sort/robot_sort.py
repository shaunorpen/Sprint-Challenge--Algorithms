class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # # Pick up the first item
        # self.swap_item()
        # # Compare it to the next item, keep the biggest each time
        # while self.move_right():
        #     if self.compare_item() < 1:
        #         self.swap_item()
        # # Until you reach the end of the list, then swap with the item at the end
        # self.swap_item()
        # # Compare it to the next item, keep the smallest each time
        # while self.move_left() and not self.compare_item() == None:
        #     if self.compare_item() > 0:
        #         self.swap_item()
        # # Until you reach None, then drop the item, move right and pick up the next item
        # # Compare it to the next item, keep the biggest each time
        # self.swap_item()
        # self.move_right()
        # self.swap_item()
        # while self.move_right():
        #     if self.can_move_right():
        #         if self.compare_item() < 1:
        #             self.swap_item()
        # # Until you reach the end of the list. Then turn on the light.
        # self.set_light_on()
        # # Then compare the item carrying to the item at current position until you find 
        # # the first value less than the value you're carrying. Swap. Turn off light.
        # while self.move_left() and self.light_is_on() == True:
        #     if self.compare_item() > 0:
        #         self.swap_item()
        #         self.set_light_off()
        # # Go back down the list until you find none again.
        # while self.move_left() and not self.compare_item() == None:
        #     if self.compare_item() > 0:
        #         self.swap_item()
        # self.swap_item()

        # Pick up the first item
        self.swap_item()
        while True:
        # Carry it to the end, swapping for bigger as you go
            while self.can_move_right():
                self.move_right()
                if self.compare_item() == None:
                    self.swap_item()
                    self.move_right()
                if self.compare_item() < 1:
                    self.swap_item()
        # Turn on light
            self.set_light_on()
        # Find first value smaller than carried value, swap and turn off light
            while self.can_move_left() and self.light_is_on():
                if self.compare_item() > 0:
                    self.swap_item()
                    self.set_light_off()
                self.move_left()
        # Carry swapped value to 'None', swapping for smaller as you go, swap
            while self.can_move_left() and self.compare_item() != None:
                if self.compare_item() > 0:
                    self.swap_item()
                self.move_left()
            self.swap_item()
        # Move one right, pick up item, carry to end swapping for bigger as you go (step 2)
        # End when light is off and the last value swapped was just to the left of the previous one
        pass


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 4, 26]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)