# variables and constants
name = "Manuel"
age = 34
current_week = 1
completed_progress = False

COURSE_NAME = "AI Engineer Roadmap"

# lists - mutable
lists = [1,2,3]
# tuple - inmutable
tuples = (1,2,3)
# set - desordered and unique values
sets = {1,2,3}
# dictionary
dictionary = { "dictionary": name, "age": age, "course": "AI Engineer Roadmap" }

# array and set
repetitive_tech = ["Python", "JavaScript", "Python", "Docker", "Docker"]
unique_tech = set(repetitive_tech)
print(repetitive_tech)
print(unique_tech)

team_a = {"Python", "Docker", "Git"}
team_b = {"Python", "React", "TypeScript"}

# intersection
print(team_a & team_b)

# union without repetitive items
print(team_a | team_b)


# Functions - def
def welcome(nam, week):
    return f"Hi {nam}, You are in the week {week}"

message = welcome(name, current_week)
print(message)


if __name__ == "__main__":
    print(f"---Welcome to the course {COURSE_NAME} ---")
    print(f"Current week: {current_week}")
    print(f"Developer name: {name}")
    print(f"Developer age: {age}")
    print(f"Is the proyect completed?: {completed_progress}")
    print("")
    print(name)
    print(age)
    print(type(name))