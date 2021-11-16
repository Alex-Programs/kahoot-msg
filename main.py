from kahoot import client
import time

clients = []
messages = ["Never gonna", "give you", "up, never", "gonna let", "you down,", "going to", "make a", "bot for", "this", "I can't", "be bothered", "to write", "the rest"]

messages.reverse()

code = 9618739

for msg in messages:
    time.sleep(0.2)
    print(msg + " client made")
    clients.append(client())

i = 0
for client in clients:
    print("Joining with " + messages[i])
    time.sleep(0.5)
    client.join(code, messages[i])
    i += 1