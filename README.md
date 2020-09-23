## 🚀 Working from 127.0.0.1 🏠 with LauchDarkly Feature Flags 🚀
### 🦠 Working during the pandemic is a bit weird. 🦠

## Exciting updates 8/27/20!! See [Part 2](https://github.com/hayleycd/wfh_status/blob/master/PART2_README.md) now!

#### ~~See my [WFH Status]website~~ Not currently deployed because LaunchDarkly trial ended
#### See the [demo](https://youtu.be/J1nD3lzldnY)

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
