# serverless-example
Project 4 for ECE 590: Data Analytics at Scale in the Cloud. 

## Steps
I created a new project in the Google Cloud environment. After that, I went to Cloud Functions and chose Create Function. Unauthenticaed invocation was allowed, and Runtime was changed to Python 3.7.

You may need to set up authentication in order to use google AI/ML services. Follow this link for how to set it up: https://cloud.google.com/natural-language/docs/reference/libraries

You will also need to enable the Cloud Natural Language API. If you do not enable it, you will be pointed to do so while testing the function. 

Copy requirements.txt and main.py to Google Cloud Function. Make sure to change the "Function to execute" field so that it matches the function name in the code. Click "Create".

Once the function is created succesfully, we can test it by clicking the three dots under "Actions", and click "test function". We can test the function by passing it a payload, such as ```{"entity": "google"}```. Click "TEST THE FUNCTION" and we should see the output. Note that we can view any output from ```print``` statement in logs.

We can also invoke the function via the GCP console. Use ```gcloud functions describe [function-name]``` to describe the function, and invoke it with ``` gcloud functions call [function-name] --data '{"entity":"google"}' ```




## Reference
https://noahgift.github.io/cloud-data-analysis-at-scale/topics/faas
