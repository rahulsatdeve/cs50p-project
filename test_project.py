from project import valid_film_person, valid_role, add_member

def test_valid_film_person():
    assert valid_film_person("Nagpur", "yes") == True

def test_valid_film_person_case_insensitive():
    assert valid_film_person("nAgPuR", "YES") == True

def test_invalid_city():
    assert valid_film_person("Mumbai", "yes") == False

def test_invalid_film_experience():
    assert valid_film_person("Nagpur", "no") == False

def test_city_with_spaces():
    assert valid_film_person("  Nagpur  ", "yes") == True



def test_valid_roles():
    assert valid_role("actor") == True
    assert valid_role("director") == True
    assert valid_role("dop") == True
    assert valid_role("writer") == True
    assert valid_role("producer") == True
    assert valid_role("music") == True

def test_valid_role_case_insensitive():
    assert valid_role("AcToR") == True

def test_invalid_role():
    assert valid_role("dancer") == False

def test_invalid_role_empty():
    assert valid_role("") == False


def test_add_member():
    people = []
    add_member(people, "Aakash", "actor")

    assert len(people) == 1
    assert people[0]["name"] == "Aakash"
    assert people[0]["role"] == "actor"

def test_add_multiple_members():
    people = []

    add_member(people, "A1", "actor")
    add_member(people, "A2", "director")

    assert len(people) == 2

