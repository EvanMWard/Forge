from dataclasses import dataclass


class Recipe(dataclass):
    name = None
    difficulty = None
    quality = None
    durability = None
    recipe_yield = 1


class Stats(dataclass):
    craftsmanship = None
    control = None
    cp = None


class GearItem(dataclass):
    name = None
    slot = None
    stats = Stats
