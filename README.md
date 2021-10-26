# chalice-twitter-demo
Demo to explain how to use AWS Chalice to connect to twitter API and change profile picture at scheduled times.


### Video Demo

[![تغيير صورة بروفايل تويتر باستخدام سيرفرليس](https://media-exp1.licdn.com/dms/image/sync/C4D27AQGhRRLLt1uRig/articleshare-shrink_800/0/1635109904026?e=1635318000&v=beta&t=XK3JiXmepgi05u6sqsi3M-nsmkx973RCt7XwMmnpslo)](https://www.youtube.com/watch?v=oCWC3bYqRLA "تغيير صورة بروفايل تويتر باستخدام سيرفرليس")

[Click to subscribe for similar tutorials.](http://learn.me2resh.com)

### Setup
```bash
virtualenv /tmp/chalice-twitter-demo
. /tmp/chalice-twitter-demo/bin/activate 
pip install -r requirements.txt
```

### Deploy to AWS
```bash
chalice deploy
```

### Remove from AWS
```bash
chalice delete
```