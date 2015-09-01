#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tshirts Service
"""
import stackhut
import stackhut_client as client

class Default(stackhut.Service):

    def getShirt(self, address, useCase): 
        name = stackhut.get_service_author()
        service = client.SHService('stackhut', 'tshirt-love')
        service.Default.gimmeTheLoot(name, address, useCase)
        return True

# export the services
SERVICES = {"Default": Default()}
