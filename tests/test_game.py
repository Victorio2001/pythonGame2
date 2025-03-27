from Game.Game import Personnage

def test_one():
    personnage = Personnage("victorio",
                            "garcia",
                            100, "noire",
                            ["sword", "axe", "bow", "arrow", "augustine"])
    personnage2 = Personnage("victorio2",
                             "garcia",
                             100, "noire",
                             ["sword", "axe", "bow", "arrow", "augustine"])

    assert personnage.Nom_personnage == personnage2.Nom_personnage



