# notation.py
# TODO : Version buggée — à corriger après exécution des tests unitaires
# TODO : Mettre des commentaires pour identifier les bugs trouvés et comment vous les avez corrigés.

def valider_notes(notes: list[float]) -> bool:
    """
    Vérifie que la liste de notes contient exactement 9 entiers entre -3 et +3.
    :param notes: liste de notes
    :returns: vrai si la liste et valide, sinon faux.
    """
    if len(notes) < 9:
        return False

    for n in notes:
        if n > 3 or n < -3 : # car on veut seulement les données de -3 à 3
            return False

    return True


def calculer_points(vbase: float, notes: list[float]) -> float:
    """
    Calcule la note finale d’un mouvement.
    :param vbase: valeur de base de la note
    :param notes: liste de notes
    :returns: valeur de la note finale
    """
    try:
        valider_notes(notes)

        note_max = max(notes)
        note_min = min(notes)

        for i in range(len(notes)):
            if notes[i] == note_max and note_min : # on mets and car cest la note minimale ET la note maximale
             notes.remove(notes[i])

        moyenne = sum(notes) / 7 # on divise par 7 car on prends la moyenne de seulement les notes restantes(7) car on a enlevé la note minimale et la note maximale
        total = vbase + moyenne
        return total

    except ValueError:
        print("Erreur")
        return False # on return false si il y a une erreur



