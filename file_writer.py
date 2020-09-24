import json


directory = {}

directory['projects'] = []
directory['projects'].append({
    "proj_name" : "List Writer",
    "due_date" : "24/09/2020 7:05",
    "description" : "A Software That Writes Lists",
    "urgent" : False,
    "important" : True,
    "tasks" : [
        {
            "task_name" : "Pick a Language",
            "due_date" : "12/09/2020 8:00",
            "description" : "Python, Java, C#, C++",
            "urgent" : True,
            "important" : True,
        },
        {
            "task_name" : "Design",
            "due_date" : "10/12/2020 23:59",
            "description" : "What is this software going to look like",
            "urgent" : False,
            "important" : False,
        },
{
            "task_name" : "Code",
            "due_date" : "20/12/2020 12:00",
            "description" : "Write the software",
            "urgent" : False,
            "important" : True,
        },
        {
            "task_name" : "Refactor",
            "due_date" : "25/12/2020 20:00",
            "description" : "Refactor so it looks nice",
            "urgent" : True,
            "important" : False,
        }
    ]
})

directory['projects'].append({
    "proj_name" : "Get A Job",
        "due_date" : "31/12/2020 23:59",
        "description" : "Get a Job for January",
        "urgent" : True,
        "important" : True,
        "tasks" : [
            {
                "task_name" : "Update Resume",
                "due_date" : "18/07/2020 23:59",
                "description" : "Update Resume to include current job",
                "urgent" : True,
                "important" : True,
            },
            {
                "task_name" : "Cover Letter Overview",
                "due_date" : "25/09/2020 8:00",
                "description" : "Create an Overview of Skills for Cover Letter",
                "urgent" : False,
                "important" : False,
            },
{
                "task_name" : "Apply For Jobs",
                "due_date" : "01/10/2020 8:00",
                "description" : "Put In Those Resumes",
                "urgent" : False,
                "important" : True,
            }
        ]
    }
)

with open('file.txt', 'w') as outfile:
    json.dump(directory, outfile)
