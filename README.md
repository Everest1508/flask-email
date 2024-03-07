## API Reference

Send a POST request to `https://sendmail.pythonanywhere.com/send_mail` with the following JSON payload:
```json
{
  "recipient": "recipient@example.com",
  "subject": "Drowsiness Alert",
  "body": "Alert message here..."
}
```
Replace "recipient@example.com" with the recipient's email address and "Alert message here..." with the desired alert message.
