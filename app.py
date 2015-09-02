#!/usr/bin/env python3
import stackhut
import stackhut_client as client

class Default(stackhut.Service):

    def getShirt(self, address, useCase): 

        # call the stackhut runtime to get the author of this service - i.e. you :)
        name = stackhut.get_service_author()

        # call another stackhut service to register your details (meta!)
        # first create a service reference
        service = client.SHService('stackhut', 'tshirt-love')
        # then call the service end-point
        service.Default.gimmeTheLoot(name, address, useCase)

        # exit the service and return to the client
        return ("Thanks {}, your t-shirt is in the post".format(name))

# export the services
SERVICES = {"Default": Default()}

