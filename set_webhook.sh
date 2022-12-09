echo Please provide webhook url?
read webhookurl 
echo Please provide web token?
read bottoken
curl ${webhookurl}telegram_receipt_reader
curl https://api.telegram.org/bot$bottoken/setWebhook?url=${webhookurl}telegram_receipt_reader