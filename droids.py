"""Droid classes"""

# David Barnes, Robert Depweg
# CIS 226
# 6-4-2023

# System Imports
import os
from abc import ABC, abstractmethod

# First-party Imports
from abstract_droid import AbstractDroid
import datastructures


class Droid(AbstractDroid, ABC):
    """Base Droid class. Also abstract as it does not make sense to allow it
    to be instantiated."""

    MODEL_COST = 0
    model_name = "Droid"

    def __init__(self, material, color, *args, **kwargs):
        """Constructor"""
        super().__init__(*args, **kwargs)
        self._material = material
        self._color = color

    def __str__(self):
        """String method"""
        return (
            f"Model: {self.model_name}{os.linesep}"
            f"Material: {self._material}{os.linesep}"
            f"Color: {self._color}{os.linesep}"
            f"{self._droid_info_str()}"
            f"Total Cost: ${self.total_cost:.2f}"
        )

    class Materials:
        """Storage of materials constants"""

        def __new__(cls):
            raise TypeError("Can not make instances of Materials class")

        CARBONITE = "Carbonite"
        VANADIUM = "Vanadium"
        QUADRANIUM = "Quadranium"
        TEARS_OF_A_JEDI = "Tears Of A Jedi"

    class Colors:
        """Storage of color constants"""

        def __new__(cls):
            raise TypeError("Can not make instance of Colors class")

        WHITE = "White"
        RED = "Red"
        GREEN = "Green"
        BLUE = "Blue"

    @abstractmethod
    def calculate_total_cost(self):
        """Calculate the total cost and store it in the total_cost attribute"""
        self.total_cost = self.MODEL_COST + self._get_material_cost() + self._get_color_cost()

    @abstractmethod
    def _droid_info_str(self):
        """Returns subclass specific attributes as a string"""
        raise NotImplementedError()

    def _get_material_cost(self):
        """Get the material cost based on value of instance's material"""
        material_cost = 50.00

        if self._material == self.Materials.CARBONITE:
            material_cost = 100.00
        elif self._material == self.Materials.VANADIUM:
            material_cost = 120.00
        elif self._material == self.Materials.QUADRANIUM:
            material_cost = 150.00
        elif self._material == self.Materials.TEARS_OF_A_JEDI:
            material_cost = 200.00
        else:
            raise ValueError("Unknown material type.")

        return material_cost

    def _get_color_cost(self):
        """Get the color cost based on value of instance's color"""
        color_cost = 5.00

        if self._color == self.Colors.WHITE:
            color_cost = 10.00
        elif self._color == self.Colors.RED:
            color_cost = 20.00
        elif self._color == self.Colors.GREEN:
            color_cost = 40.00
        elif self._color == self.Colors.BLUE:
            color_cost = 50.00
        else:
            raise ValueError("Unknown color")

        return color_cost


class ProtocolDroid(Droid):
    """Represent a Protocol Droid"""

    MODEL_COST = 120.00
    COST_PER_LANGUAGE = 25.00
    model_name = "Protocol"

    def __init__(self, material, color, number_of_languages):
        """Constructor"""
        super().__init__(material, color)

        # Set the number of languages
        self._number_of_languages = number_of_languages

    def _droid_info_str(self):
        """Return droid specific attributes as a string. Overrides parent."""
        return f"Number of Languages: {self._number_of_languages}{os.linesep}"

    def _calculate_language_cost(self):
        """Calculate and return the cost of languages"""
        return self._number_of_languages * self.COST_PER_LANGUAGE

    def calculate_total_cost(self):
        """Calculate the total cost and store it in the total_cost attribute"""
        super().calculate_total_cost()
        self.total_cost += self._calculate_language_cost()


class UtilityDroid(Droid):
    """Represents a Utility Droid"""

    MODEL_COST = 130.00
    COST_PER_OPTION = 35.00
    model_name = "Utility"

    def __init__(self, material, color, has_toolbox, has_computer_connection, has_scanner):
        """Constructor"""
        super().__init__(material, color)

        # Set the option bools
        self._has_toolbox = has_toolbox
        self._has_computer_connection = has_computer_connection
        self._has_scanner = has_scanner

    def _droid_info_str(self):
        """Return droid specific attributes as a string. Overrides parent."""
        return (
            f"Has Tool Box: {self._has_toolbox}{os.linesep}"
            f"Has Computer Connection: {self._has_computer_connection}{os.linesep}"
            f"Has Scanner: {self._has_scanner}{os.linesep}"
        )

    def _calculate_options_cost(self):
        """Calculate and return the cost of options selected for the droid"""
        options_cost = 0

        if self._has_toolbox:
            options_cost += self.COST_PER_OPTION
        if self._has_computer_connection:
            options_cost += self.COST_PER_OPTION
        if self._has_scanner:
            options_cost += self.COST_PER_OPTION

        return options_cost

    def calculate_total_cost(self):
        """Calculate the total cost and store it in the total_cost attribute"""
        super().calculate_total_cost()
        self.total_cost += self._calculate_options_cost()


class JanitorDroid(UtilityDroid):
    """Represents a Janitor Droid"""

    MODEL_COST = 160.00
    model_name = "Janitor"

    def __init__(
        self,
        material,
        color,
        has_toolbox,
        has_computer_connection,
        has_scanner,
        has_broom,
        has_vacuum,
    ):
        """Constructor"""
        super().__init__(material, color, has_toolbox, has_computer_connection, has_scanner)

        # Set the option bools
        self._has_broom = has_broom
        self._has_vacuum = has_vacuum

    def _droid_info_str(self):
        """Return droid specific attributes as a string. Overrides parent."""
        return (
            f"{super()._droid_info_str()}"
            f"Has Broom: {self._has_broom}{os.linesep}"
            f"Has Vacuum: {self._has_vacuum}{os.linesep}"
        )

    def _calculate_options_cost(self):
        """Calculate and return the cost of options selected for the droid"""
        options_cost = super()._calculate_options_cost()

        if self._has_broom:
            options_cost += self.COST_PER_OPTION
        if self._has_vacuum:
            options_cost += self.COST_PER_OPTION

        return options_cost


class AstromechDroid(UtilityDroid):
    """Represents a Astromech Droid"""

    MODEL_COST = 200.00
    COST_PER_SHIP = 45.00
    model_name = "Astromech"

    def __init__(
        self,
        material,
        color,
        has_toolbox,
        has_computer_connection,
        has_scanner,
        has_navigation,
        number_of_ships,
    ):
        """Constructor"""
        super().__init__(material, color, has_toolbox, has_computer_connection, has_scanner)

        # Set the option bools
        self._has_navigation = has_navigation
        self._number_of_ships = number_of_ships

    def _droid_info_str(self):
        """Return droid specific attributes as a string. Overrides parent."""
        return (
            f"{super()._droid_info_str()}"
            f"Has Navigation: {self._has_navigation}{os.linesep}"
            f"Number Of Ships: {self._number_of_ships}{os.linesep}"
        )

    def _calculate_options_cost(self):
        """Calculate and return the cost of options selected for the droid"""
        options_cost = super()._calculate_options_cost()

        if self._has_navigation:
            options_cost += self.COST_PER_OPTION

        return options_cost

    def _calculate_ships_cost(self):
        """Calculate and return the cost of ships"""
        return self.COST_PER_SHIP * self._number_of_ships

    def calculate_total_cost(self):
        """Calculate the total cost and store it in the total_cost attribute"""
        super().calculate_total_cost()
        self.total_cost += self._calculate_ships_cost()


class DroidCollection:
    """Stores droids that have been created"""

    def __init__(self):
        """Constructor"""
        self._collection = []

    def add_protocol(self, material, color, number_of_languages):
        """Add protocol droid to internal collection"""
        self._collection.append(
            ProtocolDroid(material, color, number_of_languages),
        )

    def add_utility(self, material, color, toolbox, computer_connection, scanner):
        """Add Utility droid to internal collection"""
        self._collection.append(
            UtilityDroid(material, color, toolbox, computer_connection, scanner),
        )

    def add_janitor(self, material, color, toolbox, computer_connection, scanner, broom, vacuum):
        """Add Janitor droid to internal collection"""
        self._collection.append(
            JanitorDroid(
                material,
                color,
                toolbox,
                computer_connection,
                scanner,
                broom,
                vacuum,
            ),
        )

    def add_astromech(
        self,
        material,
        color,
        toolbox,
        computer_connection,
        scanner,
        navigation,
        number_of_ships,
    ):
        """Add Astromech droid to internal collection"""
        self._collection.append(
            AstromechDroid(
                material,
                color,
                toolbox,
                computer_connection,
                scanner,
                navigation,
                number_of_ships,
            )
        )

    def is_empty(self):
        """Whether the collection is empty or not"""
        return len(self._collection) <= 0

    def __str__(self):
        """String method"""

        # Init the return string.
        return_string = ""
        # Loop through all droids and form the return string.
        for droid in self._collection:
            # Calculate the total cost of the droid. Since we are using inheritance
            # an polymorphism, the program will automatically know which version
            # of calculate_total_cost it needs to call based on which particular
            # type it is looking at during the for loop.
            droid.calculate_total_cost()
            # Create the string now that the total cost has been calculated
            return_string += f"****************************{os.linesep}"
            return_string += f"{str(droid)}{os.linesep}"
            return_string += f"****************************{os.linesep}"
            return_string += f"{os.linesep}"
        # Return completed string.
        return return_string
    
    def droid_model_sort(self):
        """Categorizes the droids by model"""
        stack_protocol = datastructures.Stack()
        stack_utility = datastructures.Stack()
        stack_janitor = datastructures.Stack()
        stack_astromech = datastructures.Stack()
        queue = datastructures.Queue()

        # Loops through collection
        for droid in self._collection:
            if self.instance_checker(droid, AstromechDroid):
                stack_astromech.push(droid)
            elif self.instance_checker(droid, JanitorDroid):
                stack_janitor.push(droid)
            elif self.instance_checker(droid, UtilityDroid):
                stack_utility.push(droid)
            elif self.instance_checker(droid, ProtocolDroid):
                stack_protocol.push(droid)
        
        # Add stack instance droids to enqueue by stack data removal
        queue.enqueue(stack_astromech.pop)
        queue.enqueue(stack_janitor.pop)
        queue.enqueue(stack_utility.pop)
        queue.enqueue(stack_protocol.pop)

        # Replace original list of droids with queue droids
        for i in range(self._collection):
            self._collection.replace(droid, queue.dequeue)

    def instance_checker(self, checked_instance, classinfo):
        """Checks what class instance the instance is"""
        return isinstance(checked_instance, classinfo)
    
    def droid_total_cost_sort(self):
        """"""
        pass