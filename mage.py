#!/usr/bin/env python3

# Implement this class. Extend Character and adopt the combat
# mechanics that are defined in the description. Do not change the
# class name and stick to the method signatures of Character
# or the automated grading won't work.

from public.character import Character

class Mage(Character):

    def attack(self, other: Character) -> None:
        assert isinstance(other, Character)
        assert self is not other

        if not self.is_alive():
            raise Warning("Character is dead!")

        other._take_magical_damage(self._get_caused_dmg(other))

    def _get_caused_dmg(self, other: Character) -> int:
        dmg = super()._get_caused_dmg(other)
        return round(1.25 * dmg)

    def _take_physical_damage(self, amount: int) -> None:
        super()._take_physical_damage(round(1.5 * amount))

    def _take_magical_damage(self, amount: int) -> None:
        super()._take_magical_damage(round(1.5 * amount))