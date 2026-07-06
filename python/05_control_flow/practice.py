# python/05_control_flow/practice.py

score = 72
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(grade)

n = 7
label = "even" if n % 2 == 0 else "odd"
print(label)


def describe(command):
    match command.split():
        case ["go", direction]:
            return f"moving {direction}"
        case ["stop"]:
            return "stopping"
        case [action, *rest] if action == "set":
            return f"setting {rest}"
        case _:
            return "unknown command"


print(describe("go north"))
print(describe("stop"))
print(describe("set volume 11"))


def show_count(count):
    if count:
        return f"count: {count}"
    return "nothing to show"


def show_count_fixed(count):
    if count is not None:
        return f"count: {count}"
    return "nothing to show"


print(show_count(0))          # "nothing to show" — the bug
print(show_count_fixed(0))    # "count: 0" — correct
