import json
from collections import OrderedDict

with open('csvjson.json', 'r') as f:
    data = json.load(f)

# map names to objects
departments = OrderedDict()
for employee in data:
    # process sills
    skills = [employee['skill1'], employee['skill2'], employee['skill3']]
    employee['skills'] = skills
    del employee['skill1']
    del employee['skill2']
    del employee['skill3']

    # process manager string
    employee['isManager'] = (employee['isManager'] == 'TRUE')

    #----

    # departments
    dept = employee['department']
    if (dept in departments):
        departments[dept]['employees'].append(employee)
    else:
        departments[dept] = OrderedDict()
        departments[dept]['name'] = dept
        departments[dept]['managerName'] = ''
        departments[dept]['employees'] = [employee]
    
    if (employee['isManager']):
        departments[dept]['managerName'] = employee['name']

organization = {'organization': {'departments': list(departments.values())}}
with open('organization.json', 'w') as f:
    json.dump(organization, f, indent=4)