dict = { 
    "class": { 
        "student": { 
            "name": "Mike", 
            "marks": { 
                "physics": 70, 
                "history": 80 
            } 
        } 
    } 
} 

print(dict.get("class").get("student").get("marks").get("history"))
dict.update({"class": {"student": {"name": "Mark"}}})
print(dict.get("class").get("student").get("name"))