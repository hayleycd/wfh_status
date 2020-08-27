## 🚀 Working from 127.0.0.1 🏠 with LauchDarkly Feature Flags 🚀
### 🦠 Working during the pandemic is a bit weird. 🦠

#### Exciting updates 8/27/20!!

I took the opportunity to dig into LaunchDarkly's API and am pleased to announce the following features.

1. I have set an Azure Functions timer to text me every morning to update my flags. 
2. Anyone with my twilio phone number can check my status via text. 
3. It is also possible to toggle flags via SMS 🤯 (in the future I may limit this functionality to texts from my cell number, but for now, I want people who have my twilio number to be able to try this feature themselves)

To accomplish this I used Azure Functions, Twilio SMS, and LaunchDarkly feature flags.

### Reminder Text
To create this I used a [time trigger for Azure Functions](https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-timer?tabs=csharp). At the specified time (9:00 Pacific every weekday--though you need to write the cron in UTC), my function runs, creating and sending a Twilio SMS to my cellphone to remind me to update my flags!

### Get Status Via Text
To create this functionality, I used an [HTTP trigger](https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-http-webhook) and set up my twilio number to hit the corresponding url when it recieves an incoming text. The default text gives you the current status of my flags and instructions on how to get more information. 

To get information about my flags, I used the [LaunchDarkly API](https://apidocs.launchdarkly.com/reference). I had to generate an [Personal Access Token](https://apidocs.launchdarkly.com/reference#authentication) (distinct from my SDK key). [Here](https://apidocs.launchdarkly.com/reference#list-feature-flags) is more information on how to make API calls to get info on your flags. 

### Toggle Flags Via Text
Updating an individual flag was a little trickier. It required using a json patch. The python `requests` library has a `patch` function. Once my JSON patch was formatted correctly (good information [here](https://apidocs.launchdarkly.com/reference#updates)), the request was a snap! By texting the flag key, you turn the flag on, and by texting flag key followed by an exclamation point turns the flag off! Easy!

### Conclusion

Hopefully these updates make my project more useful to myself and my family. It is easier for them to check my status, and I am able to update my status via a simple text message, without logging in to Slack or LaunchDarkly!
