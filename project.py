def main():
    people = []

    while len(people) < 5:
        name = input("Enter Name: ").strip()
        city = input("Enter City: ").strip()
        film = input("Have you ever made a short film? (yes/no): ").strip()
        role = input("Enter your role (actor/director/dop/writer/producer/music): ")
        while not valid_role(role):
            print("Invalid role. Please choose from the given options.")
            role = input("Enter your role (actor/director/dop/writer/producer/music): ")
        role = role.strip().lower()
        if valid_film_person(city, film):
            add_member(people, name, role)
            print("ADDED TO THE GUILD!")
        else:
            print("NOT ELIGIBLE.")
    display_team(people)
def valid_film_person(city, film):
    city = city.strip().lower()
    film = film.strip().lower()
    return city == "nagpur" and film == "yes"
def valid_role(role):
    roles = ["actor", "director", "dop", "writer", "producer", "music"]
    return role.strip().lower() in roles
def add_member(people, name, role):
    member = {
        "name": name,
        "role": role
    }
    people.append(member)
def display_team(people):
    print("\nFinal Team:")
    for i, member in enumerate(people, start=1):
        print(f"{i}. {member['name']} - {member['role']}")
    print(f"Total members: {len(people)}")
if __name__ == "__main__":
    main()

