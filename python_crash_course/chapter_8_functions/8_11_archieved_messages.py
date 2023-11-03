import time

def send_messages(to_send, sent):
    while to_send:
        current_message = to_send.pop()
        print(current_message)
        sent.append(current_message)

        time.sleep(1)

messages = [
    "Some Text",
    "Let's go shopping.",
    "He failed his French test.",
    "Odds are that he is cheating on her.",
]

sent = []

send_messages(messages[:], sent=sent)

print('to send:', messages)
print('sent:', sent)