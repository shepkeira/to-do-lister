import json


directory = {}

directory['projects'] = []
directory['projects'].append({
    "proj_name" : "Proj 1",
    "due_date" : "29/11/1997 7:05",
    "description" : "this is the description",
    "urgent" : True,
    "important" : False,
    "tasks" : [
        {
            "task_name" : "Task 1",
            "due_date" : "29/11/1997 7:05",
            "description" : "this is the description",
            "urgent" : True,
            "important" : False,
        },
        {
            "task_name" : "Task 2",
            "due_date" : "29/11/1997 7:05",
            "description" : "this is the description",
            "urgent" : True,
            "important" : False,
        }
    ]
})

directory['projects'].append({
    "proj_name" : "Proj 2",
        "due_date" : "29/11/1997 7:05",
        "description" : "this is the description",
        "urgent" : True,
        "important" : False,
        "tasks" : [
            {
                "task_name" : "Task 1",
                "due_date" : "29/11/1997 7:05",
                "description" : "this is the description",
                "urgent" : True,
                "important" : False,
            },
            {
                "task_name" : "Task 2",
                "due_date" : "29/11/1997 7:05",
                "description" : "this is the description",
                "urgent" : True,
                "important" : False,
            }
        ]
    }
)

with open('file.txt', 'w') as outfile:
    json.dump(directory, outfile)
