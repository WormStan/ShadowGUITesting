import random
import json

actions = ["set", "click", "select", "input", "open", "close", "delete",
           "update", "move", "resize", "highlight", "disable", "enable", "hover",
           "maximize", "minimize", "restore", "scroll", "drag", "drop",
           "copy", "paste", "cut", "undo", "redo", "search", "refresh",
           "save", "print", "export", "import", "lock", "unlock", "sync"]

objects = [
    "Textbox",
    "Button",
    "Dropdown",
    "Checkbox",
    "Menu",
    "Window",
    "Panel",
    "Slider",
    "RadioButton",
    "Label",
    "Image",
    "Link",
    "Table",
    "Row",
    "File",
    "Folder",
    "Toolbar",
    "StatusBar",
    "Notification",
    "Dialog Box",
    "Progress Bar",
    "Calendar",
    "Clock",
    "Taskbar",
    "Desktop",
    "Shortcut",
    "Icon",
    "Tool Tip",
    "Context Menu",
    "Breadcrumb",
    "Tab Control",
    "Tree View",
    "List View",
    "Grid",
    "Alarm",
    "Trend",
    "Data Log",
    "Recipe",
    "Tag",
    "PLC",
    "HMI",
    "SCADA",
    "OPC Server",
    "Historian",
    "Alarm Banner",
    "Alarm Summary",
    "Trend Chart",
    "Data Grid",
    "Recipe Manager",
    "Tag Browser",
    "PLC Program",
    "HMI Project",
    "SCADA Project",
    "OPC Connection",
    "Historical Data",
    "Alarm Viewer",
    "Trend Viewer",
    "Data Logger",
    "Recipe Editor",
    "Tag Editor",
    "PLC Editor",
    "HMI Editor",
    "SCADA Editor",
    "OPC Configurator",
    "Historian Viewer"
]

locations = [
    "Desktop",
    "Taskbar",
    "Start Menu",
    "System Tray",
    "Control Panel",
    "File Explorer",
    "Recycle Bin",
    "Quick Access",
    "Network",
    "Devices and Printers",
    "Settings",
    "Notification Area",
    "Action Center",
    "Task Manager",
    "Search Bar",
    "Sidebar",
    "Toolbar",
    "Status Bar",
    "Title Bar",
    "Menu Bar",
    "Context Menu",
    "Dialog Box",
    "Properties Window",
    "Help Menu",
    "About Window",
    "Preferences Window",
    "Options Menu",
    "Navigation Pane",
    "Ribbon",
    "Breadcrumb Bar"
]

values = ["test value", "example text", "sample input", "demo value",
          "1", "2", "3","40000","default setting", "user input", "system value", "configuration", "custom value", "preset", "template", "default path", "file name", "folder name", "URL", "email address", "password", "username", "search query", "filter", "option", "preference", "setting"]

contexts = [
    "Before proceeding to the next step.",
    "After completing the previous task.",
    "Till the system finishes loading.",
    "Wait for the confirmation message.",
    "Before making any changes.",
    "After saving the current settings.",
    "Till the data is fully synchronized.",
    "Wait for the update to complete.",
    "Before accessing the new feature.",
    "After reviewing the notifications.",
    "Till the application is ready.",
    "Wait for the system to respond.",
    "Before closing the window.",
    "After opening the file.",
    "Till the process is finished.",
    "Wait for the installation to complete.",
    "Before starting the configuration.",
    "After adjusting the preferences.",
    "Till the changes are applied.",
    "Wait for the validation to finish.",
    "Before navigating to the next section.",
    "After organizing the content.",
    "Till the backup is done.",
    "Wait for the download to complete.",
    "Before initiating the task.",
    "After verifying the inputs.",
    "Till the connection is established.",
    "Wait for the analysis to complete.",
    "Before confirming the action.",
    "After inspecting the elements."
]

# Defined the promote key word
promote_keyword = "Generate Test:"

def generate_data_pair():
    action = random.choice(actions)
    obj = random.choice(objects)
    context = random.choice(contexts)

    include_value = random.choice([True, False])
    include_location = random.choice([True, False])

    keyword_position = random.choice(["start", "middle"])

    if include_value:
        value = random.choice(values)
        input_text = f"{action} {obj} to ${value}$"
        output_json = {"action": action, "object": obj, "value": value}
    else:
        input_text = f"{action} {obj}"
        output_json = {"action": action, "object": obj}

    if include_location:
        location = random.choice(locations)
        input_text += f" from #{location}#"
        output_json["location"] = location

    if keyword_position == 'start':
        input_text = f"{promote_keyword} {context} {input_text}"
    else:
        input_text = f"{promote_keyword} {input_text} {context}"

    return input_text, output_json


def generate_dataset(num_examples):
    dataset = []
    for _ in range(num_examples):
        input_text, output_json = generate_data_pair()
        dataset.append({
            "input": input_text,
            "output": output_json
        })
    return dataset


dataset = generate_dataset(1000)

with open("training_data.json", "w") as f:
    json.dump(dataset, f, indent=4)

print("generated - 'training_data.json' ")
