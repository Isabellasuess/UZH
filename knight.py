#!/usr/bin/env python3

# Implement this class. Extend Character and adopt the combat
# mechanics that are defined in the description. Do not change the
# class name and stick to the method signatures of Character
# or the automated grading won't work.

from public.character import Character

class Knight(Character):

    def _get_caused_dmg(self, other: Character) -> int:
        dmg = super()._get_caused_dmg(other)
        return round(0.8 * dmg)


    def _take_physical_damage(self, amount: int) -> None:
        super()._take_physical_damage(round(0.75 * amount))