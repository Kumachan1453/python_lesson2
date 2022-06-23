import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("/Firebase/newexpofirebase2-a3a70-firebase-adminsdk-19fel-fedc56fb04.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

db = firestore.client()
docs = db.collection('users').get()
for doc in docs:
    print(doc.to_dict())