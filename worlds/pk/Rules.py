from BaseClasses import MultiWorld, CollectionState

from . import Items, ParadiseKillerOptions

def set_rules(multiworld: MultiWorld, world, player: int, options: ParadiseKillerOptions):
    multiworld.completion_condition[player] = lambda state: (
        state.has("LLD Upgrade: Double Jump", player, 1)
    )