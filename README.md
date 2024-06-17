This will allow you to check if your toll free numbers are working, 

Report in excel 

![image](https://github.com/RichardTelecomTech/solid-dollop/assets/153075593/6fa0b392-08b8-4ec9-862c-d67886cde413)


In Twilio

1. Log into Twilio
2. TwiML Bin
3. Create new
4. <?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say voice="alice">This is a status check only, please disregard</Say>
</Response>
5. Copy URL and copy it to app.py


![image](https://github.com/RichardTelecomTech/solid-dollop/assets/153075593/845f2aee-0ec0-4b74-8aaf-86d3a1f2efcc)


In PowerAutomate (to send data to excel)

1. Add when a new email arrives
2. Add 5 actions "initize variable"
first(split(last(split(string(triggerOutputs()?['body']), 'Call completed with status: ')), '\n'))
first(split(last(split(string(triggerOutputs()?['body']), 'Number Dialed: ')), '\n'))
first(split(last(split(string(triggerOutputs()?['body']), 'Call SID: ')), '\n'))
formatDateTime(convertTimeZone(utcNow(), 'UTC', 'AUS Eastern Standard Time'), 'dd-MM-yyyy')
formatDateTime(convertTimeZone(utcNow(), 'UTC', 'AUS Eastern Standard Time'), 'HH:mm')
3. add "add a row into a table"
4. ![image](https://github.com/RichardTelecomTech/solid-dollop/assets/153075593/0b718195-31f3-49e4-b62b-15ead795d22a)
