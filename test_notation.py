# test_notation.py
# Tests unitaires pour le module notation.py

import pytest
from notation import valider_notes, calculer_points

# -----------------------------
# TODO : Tests unitaires pour valider_notes()
# -----------------------------
# Arrange
@pytest.mark.parametrize("notes, resultat_attendu", [
    ([3,2,1,2,3,3,2,2,3], True),
    ([3,2,3,2,1,3,2,1,1], True),
    ([-2,-2,-1,-3,-3,-2,-1,-2,-3], True),
    ([2,1,3,2,2,1,3,2,1,1,3,3,2,1,2], False),
    ([4,5,6,4,6,5,4,5,6],False)

])
def test_notation(notes, resultat_attendu):


    # Act
    resultat_obtenu = valider_notes(notes)

    # Assert
    assert isinstance(resultat_obtenu, str)
    assert resultat_obtenu == resultat_attendu


# -----------------------------
# TODO : Tests unitaires pour calculer_points()
# -----------------------------
# Arrange
@pytest.mark.parametrize("notes, vbase, resultat_attendu", [
    ([3,2,1,2,3,3,2,2,3], 3.2, True),
    ([3,2,3,2,1,3,2,1,1], 2.5, True),
    ([-2,-2,-1,-3,-3,-2,-1,-2,-3], 1.0, True),
    ([2,1,3,2,2,1,3,2,1,1,3,3,2,1,2], 3.0, False),
    ([4,5,6,4,6,5,4,5,6], 2.5, False)

])
def test_calculer_points(notes, vbase, resultat_attendu):


    # Act
    resultat_obtenu = calculer_points(notes, vbase)

    # Assert
    assert isinstance(resultat_obtenu, str)
    assert resultat_obtenu == resultat_attendu

