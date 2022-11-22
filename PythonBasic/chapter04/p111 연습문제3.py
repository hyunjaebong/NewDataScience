message =['spam','ham','spam','ham','spam']

dummy = [1 if msg=='spam' else 0 for msg in message]
print(dummy)

spam_list=[msg for msg in message if msg=='spam']
print(spam_list)