import json
with open("equipments_events.json") as file :
    data = json.load(file)

print(data)

# A7. Load equipment_events.json and print event_id, asset type, site and severity for every event.
for event in data:
    print(f"Event_ID :",event["event_id"])
    print(f"Asset Type :",event["asset"]["type"])
    print(f"Asset Site :",event["asset"]["site"])
    print(f"Severity :",event["severity"])
    print("\n")
# A8. Display JSON records with temperature above 70. If actions is missing, display 'No actions recorded'

result = []

for event in data:
    if event.get("temperature",0) > 70:
        event.get("action","No action recorded")
        result.append(event)

print(result)


