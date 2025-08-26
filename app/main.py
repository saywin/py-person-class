class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    people_instance = []

    for person_info in people:
        person = Person(
            name=person_info["name"],
            age=person_info["age"]
        )
        people_instance.append(person)

    for person_info in people:
        person_name = Person.people[person_info["name"]]
        if person_info.get("husband"):
            person_name.husband = Person.people[person_info["husband"]]
        if person_info.get("wife"):
            person_name.wife = Person.people[person_info["wife"]]

    return people_instance
