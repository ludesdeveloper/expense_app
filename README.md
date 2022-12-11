# Expense Chat Bot App
<p align="center">
<img src="pic/ludes.png" width="500">
</p>

### **Diagram**
<!-- ![test](pic/diagram.png) -->
```mermaid
flowchart LR
    Start --> Stop
    Telegram Bot-- text -->Lambda Function
```
### **Requirements**
1. [Serverless Framework](https://www.serverless.com/framework/docs/getting-started) installed
2. [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html) configured
3. [Telegram Bot](https://core.telegram.org/bots/tutorial) configured
### **Create S3 Bucket**
1. Before we begin, please create S3 Bucket
### **Deploy With Serverless Framework**
1. Clone repository
```
git clone https://github.com/ludesdeveloper/expense_app.git
```
2. Please update your organization inf serverless.yml file
```
org: PLEASE_CHANGE_THIS_WITH_YOUR_ORGANIZATION
app: expense-app
service: expense-app
```
3. Install wsgi plugin 
```
serverless plugin install -n serverless-wsgi
```
4. Install python requirements plugins
```
serverless plugin install -n serverless-python-requirements
```
5. Init & deploy serverless framework, and follow instruction
```
sls
```
### **Configure Telegram Bot Webhook**
1. Run script below, enter your lambda url and telegram bot token 
```
./set_webhook.sh
```
### **Update Lambda Environment Variable**
1. Open your AWS Lambda Console, and go to Function -> Your Function -> Configuration -> Environment Variable
2. Create new Environment Variable with key TELEGRAMAPI, and for value is your bot api token
3. Create new Environment Variable with key BUCKET_NAME, and for value is your bucket name
4. Create new Environment Variable with key TELEGRAMUSERID, and for value is your userid
### **Interraction With Bot**
1. You can say hi to and bot will return "Hello!!"
```
hi
```
2. You can upload your receipt to be parse by bot 
3. You can get information about total within date range
```
range 2022-12-11 2022-12-12
```
> This example to get range in 11 December 2022
