from replit import db

def add_contact(name, phone_number):
  if name in db:
    print("Name already exists")
  else:
    db[name] = phone_number

def get_contact(name):
  number = db.get(name)
  return number

def delete_contact(name):
  del db[name]
  print("contact deleted")

def update_contact(oldname, newname, newnumber):
  db[newname] = newnumber
  del db[oldname]
