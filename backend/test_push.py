from notifications.push import send_push

DEVICE_TOKEN = "PUT_YOUR_DEVICE_TOKEN_HERE"

result = send_push(
    "Bot Test",
    "Push system is working",
    DEVICE_TOKEN
)

print(result)