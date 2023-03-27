messages_to_send = ["Hey", "you,there", "how long is it?", "not today", "watch out.",
                    "i'm done", "ok, last one for real." ]
messages_received = []

def send_messages(msg_to_send, msg_received):
    """Send messages then prove it."""
    print(f"\nMessages to send: {msg_to_send}")
    print(f"Messages received: {msg_received}")

    while msg_to_send:
        sending = msg_to_send.pop()
        print(f"\nSending message . . . .  {sending.title()}")
        msg_received.append(sending)

    print(f"\nMessages to send: {msg_to_send}")
    print(f"Messages received: {msg_received}")


send_messages(messages_to_send[:], messages_received)

print(f"Original list : {messages_to_send}")