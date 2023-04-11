[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/hayleycd/wfh_status/badge)](https://api.securityscorecards.dev/projects/github.com/hayleycd/wfh_status)

## 🚀 Working from 127.0.0.1 🏠 with LauchDarkly Feature Flags 🚀
### 🦠 Working during the pandemic is a bit weird. 🦠

#### Update Sep 2020
This project is no longer deployed, as my LaunchDarkly trial expired and it is pricier than I would like. _However,_
I am leaving up the source code because I am proud of it, and it is an example project and might be interesting to those wanting to learn more about LaunchDarkly, Azure Functions, or Twilio. 

#### August 2020 Update: [Toggle Feature Flags with Twilio SMS](https://github.com/hayleycd/wfh_status#august-update)

----------------

### The Problem
Working from home has been difficult, but important during the epidemic. I have been looking for Developer Advocate/Develepor Relations jobs during quarantine. This has meant that I have taken many high stakes video calls. I also have done some video recording and editing as conferences have moved online and are more likely than ever to request a pre-recorded talk.

My husband is working from home, and my retired mother lives with us. I have found that it is important to let people know when I am okay being interrupted and when an interruption is really costly. 

### My Solution

You can think of this project as a digital "do not disturb" sign on my office door. I am utilizing LaunchDarkly feature flags to easily update my statuses. My family has the URL for my website, and can check to see what they can expect from my workday. I also threw in helpful info about our dog's status and a couple of things that are important to me from a more personal perspective. 

#### Flags off
Here is a peek at what the website looks like when all of the feature flags are off. 
![This is what the text on the website looks like when all of the flags are off](https://raw.githubusercontent.com/hayleycd/wfh_status/master/screenshots/flagsoffscreenshot.png)
![Dashboard showing feature flags are off](https://raw.githubusercontent.com/hayleycd/wfh_status/master/screenshots/flags%20off.png)
##### Flags are turned off.

#### Flags on
And here you can see the changes to the page when the feature flags are on. 
![Statuses have changed compared to picture above.](https://raw.githubusercontent.com/hayleycd/wfh_status/master/screenshots/flagsonscreenshot.png)
Notice how the text has changed. 
![I have turned flags on](https://raw.githubusercontent.com/hayleycd/wfh_status/master/screenshots/flagson.png)
##### Flags are turned on. 

__You don't need to have all the flags on or all the flags off. Flags are toggled individually based on what I am trying to convey. This was just an easy way for you to see the difference in the content shown on the website.__

### Get your Own
You will need:
- A Microsoft Azure [account](https://azure.microsoft.com/en-us/free/)
- Azure VS Code extension
- A LaunchDarkly account ([30-day](https://launchdarkly.com/start-trial/) trial available)
- LaunchDarkly's [Python SDK](https://docs.launchdarkly.com/sdk/server-side/python)

Optional:
- Install the [LaunchDarkly Slack App](https://docs.launchdarkly.com/integrations/slack) into a Slack community that you log into during your work day

### Feature Flags
A feature flag allow devs to turn on and off bits of code. They are important for feature rollout, testing in production, user targeting and more. Including feature flags in your project is considered an industry "best practice", but can be really difficult to manage flags at scale. 

LaunchDarkly makes it really easy to create flags. (I had my first flag working in about a minute!) I used simple Booleans, but the flags can be much more flexible and complex. 
![Showing the form to create a new flag](https://raw.githubusercontent.com/hayleycd/wfh_status/master/screenshots/create_a_flag.png)
This is the form to create a flag. 

Managing my flags is also really easy. The dashboard lets you search for and filter flags with a snap.  
![Showing dashboard with feature flags](https://raw.githubusercontent.com/hayleycd/wfh_status/master/screenshots/flags.png)
This is my flag dashboard. 

I also appreciate that when you turn a flag on or off, there is a confirmation screen that confirms the flag and environment. 

Because my project is generally about my work day and work habits, I wanted to make use of the LaunchDarkly's Slack App. It was easy to install it and provided more features than I was expecting.

You can subscribe to flags and see the updates as they happen. 
![Showing flag updates in Slack](https://raw.githubusercontent.com/hayleycd/wfh_status/master/screenshots/launchdarklyslack.png)

You can see the details of a specific flag. 
![Showing flag details in Slack](https://raw.githubusercontent.com/hayleycd/wfh_status/master/screenshots/ldslackflag.png)

And you can turn flags on and off in Slack. 
![Showing turning flag on through Slack](https://raw.githubusercontent.com/hayleycd/wfh_status/master/screenshots/ldupdateflag.png)

It is also possible to set reminders in Slack to update your flags. 
![Slackbot reminds me to update flags](https://raw.githubusercontent.com/hayleycd/wfh_status/master/screenshots/Slackbot.png)

## August Update
I took the opportunity to dig into LaunchDarkly's API and am pleased to announce the following features.

1. I have set an Azure Functions timer to text me every morning to update my flags. 
2. Anyone with my Twilio phone number can check my status via text. 
3. It is also possible to toggle flags via SMS 🤯 (in the future I may limit this functionality to texts from my cell number, but for now, I want people who have my Twilio number to be able to try this feature themselves)

To accomplish this I used Azure Functions, Twilio SMS, and LaunchDarkly feature flags.

### Reminder Text
To create this I used a [time trigger for Azure Functions](https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-timer?tabs=csharp). At the specified time (9:00 Pacific every weekday--though you need to write the cron in UTC), my function runs, creating and sending a Twilio SMS to my cellphone to remind me to update my flags!

![Every weekday at 9am, I get a text reminding me to update my flags.](https://raw.githubusercontent.com/hayleycd/wfh_status/master/screenshots/reminder.jpg)

### Get Status Via Text
To create this functionality, I used an [HTTP trigger](https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-http-webhook) and set up my Twilio number to hit the corresponding url when it recieves an incoming text. The default text gives you the current status of my flags and instructions on how to get more information. 

To get information about my flags, I used the [LaunchDarkly API](https://apidocs.launchdarkly.com/reference). I had to generate an [Personal Access Token](https://apidocs.launchdarkly.com/reference#authentication) (distinct from my SDK key). [Here](https://apidocs.launchdarkly.com/reference#list-feature-flags) is more information on how to make API calls to get info on your flags. 

![A text that details all my statuses.](https://raw.githubusercontent.com/hayleycd/wfh_status/master/screenshots/status.jpg)

### Toggle Flags Via Text
Updating an individual flag was a little trickier. It required using a json patch. The python `requests` library has a `patch` function. Once my JSON patch was formatted correctly (good information [here](https://apidocs.launchdarkly.com/reference#updates)), the request was a snap! By texting the flag key, you turn the flag on, and by texting flag key followed by an exclamation point turns the flag off! Easy!

I can request a list of flag keys in case I don't remember them. 

![List of flag keys](https://raw.githubusercontent.com/hayleycd/wfh_status/master/screenshots/keys.jpg)

I can easily toggle my keys via text. 

![Demonstrates how to toggle flags over text. If I text the key, the flag is turned on. If I text the key followed by an exclamation point, it turns the flag off. ](https://raw.githubusercontent.com/hayleycd/wfh_status/master/screenshots/toggle.jpg)

If I ever forget how this works, or someone needs more instructions, texting 'wfhinfo' gives you all the info you need!

![Information on how to navigate the functionality.](https://raw.githubusercontent.com/hayleycd/wfh_status/master/screenshots/wfhinfo.jpg)

### Conclusion

Hopefully these updates make my project more useful to myself and my family. It is easier for them to check my status, and I am able to update my status via a simple text message, without logging in to Slack or LaunchDarkly. 
