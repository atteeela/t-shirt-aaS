# t-shirt-aaS

Use StackHut to deploy a service and get a free t-shirt !

## Steps to get yo' shirt fool :)

1. [Create a StackHut account](www.stackhut.com)
1. [Install the StackHut toolkit](https://stackhut.readthedocs.org/en/latest/getting_started/installation.html) and run `stackhut login`
1. Clone this git repo - https://github.com/StackHut/t-shirt-aaS
1. Deploy the service live under your own account
    * cd t-shirt-aaS; stackhut deploy
1. [Call your live service](https://stackhut.readthedocs.org/en/latest/using_service/index.html) with your address and how you'd use StackHut,

    * From Python or NodeJS/IoJS using the [client-libs](https://stackhut.readthedocs.org/en/latest/using_service/client_libs.html)

    * Edit `request.json` and send from the command-line using `curl`,
        * `curl -H "Content-Type: application/json" -X POST -d @request.json https://api.stackhut.com/run`
 
1. Receive awesome t-shirt in the post and look cool in front of your friends

