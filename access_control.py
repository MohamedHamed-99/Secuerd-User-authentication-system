roleUdict = { #list of users vs roles
    "Rahul Garza" :["Patient"],
    "Arjun Singh" :["Patient"],
    "Heather Anderson" : ["Administrator"],
    "Keikilana Kapahu": ["Administrator"],
    "Winston Callahan": ["Physician"],
    "Leslie Stewart": ["Physician"],
    "Howard Linkler": ["Radiologist"],
    "Veronica Perez": ["Radiologist"],
    "Kelsey Chang": ["Nurse"],
    "James Preston": ["Nurse"],
    "Harold Zakara":["Technical"],
    "Malina Romanova": ["Technical"],
}
roleOdict={ #list of roles vs objects
    "Patient": ["READ patient profile","READ patient history","READ Physcians contact details"], 
    "Administrator": ["MODIFY patient profile","Access system between 9:00am-5:00pm ONLY"],
    "Physician": ["READ patient profile","MODIFY patient history","READ patient medical images"],
    "Radiologist": ["READ patient profile","MODIFY patient history","READ patient medical images"],
    "Nurse": ["READ patient profile","READ patient history","READ patient medical images"],
    "Technical": ["READ patient medical images"],
}

