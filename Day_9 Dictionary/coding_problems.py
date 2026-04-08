# Create dictionary.
student = {
    "name":"nayan",
    "age":21,
    "favourite subject":"Operating System"
}
print(student)


# Add 3 key value pairs.
student = {
    "name":"nayan",
    "age":21,
    "favourite subject":"Operating System"
}
print(student)
student["marks"] = 87.23
student["mentor"] = 'Ajunkya Saniyal'
student["Course_fees"] = 75000
print(student)


# Access value.
student = {
    "name":"nayan",
    "age":21,
    "favourite subject":"Operating System"
}
print(student["favourite subject"])


# Print keys.
student = {
    "name":"nayan",
    "age":21,
    "favourite subject":"Operating System"
}
print(student.keys())


# Print values.
student = {
    "name":"nayan",
    "age":21,
    "favourite subject":"Operating System"
}
print(student.values())


# Update value.
student = {
    "name":"nayan",
    "age":21,
    "favourite subject":"Operating System"
}
print(student)
student["age"] = 23
print(student)


# Add new key.
student = {
    "name":"nayan",
    "age":21,
    "favourite subject":"Operating System"
}
print(student)
student["marks"] = 89.34
print(student)


# Remove key.
student = {
    "name":"nayan",
    "age":21,
    "favourite subject":"Operating System"
}
print(student)
student.pop("age")
print(student)


# Remove last item.
student = {
    "name":"nayan",
    "age":21,
    "favourite subject":"Operating System"
}
print(student)
student.popitem()
print(student)


# Copy dictionary.
student = {
    "name":"nayan",
    "age":21,
    "favourite subject":"Operating System"
}
print(student,id(student))
student_copy = student.copy()
print(student_copy,id(student_copy))


# Use get().
student = {
    "name":"nayan",
    "age":21,
    "favourite subject":"Operating System"
}
print(student.get("age"))


# Use update().
student = {
    "name":"nayan",
    "age":21,
    "favourite subject":"Operating System"
}
print(student)
student.update({"marks":89.34,"city":"Banglore"})
print(student)


# Use pop().
student = {
    "name":"nayan",
    "age":21,
    "favourite subject":"Operating System"
}
print(student)
student.pop("favourite subject")
print(student)


# Use popitem().
student = {
    "name":"nayan",
    "age":21,
    "favourite subject":"Operating System"
}
print(student)
student.popitem()
print(student)


# Use clear().
student = {
    "name":"nayan",
    "age":21,
    "favourite subject":"Operating System"
}
print(student)
student.clear()
print(student)


# Create nested dictionary.
students = {
    "student_1":{
        'name':'abhi',
        'age':23
    },
    "student_2":{
        'name':'kirti',
        'age':19
    }
}
print(students)


# Access nested value.
students = {
    "student_1":{
        'name':'abhi',
        'age':23
    },
    "student_2":{
        'name':'kirti',
        'age':19
    }
}
print(students)
print(students['student_2']['name'])


# Add nested value.
students = {
    "student_1":{
        'name':'abhi',
        'age':23
    },
    "student_2":{
        'name':'kirti',
        'age':19
    }
}
print(students)
students.update({"student_3":{"name":"John","age":23}})
print(students)


# Remove nested key.
students = {
    "student_1":{
        'name':'abhi',
        'age':23
    },
    "student_2":{
        'name':'kirti',
        'age':19
    }
}
print(students)
students['student_2'].pop("name")
print(students)


# Update nested value.
students = {
    "student_1":{
        'name':'abhi',
        'age':23
    },
    "student_2":{
        'name':'kirti',
        'age':19
    }
}
print(students)
students["student_1"].update({"marks":98.23})
print(students)


# Check key exists.
students = {
    "student_1":{
        'name':'abhi',
        'age':23
    },
    "student_2":{
        'name':'kirti',
        'age':19
    }
}
print(students)
print("student_2" in students)


# Count keys.
students = {
    "student_1":{
        'name':'abhi',
        'age':23
    },
    "student_2":{
        'name':'kirti',
        'age':19
    }
}
print(students)
print(len(students))


# Convert list to dictionary.
keys = [10,20,30,40,50]
result = dict.fromkeys(keys,12)
print(result)
