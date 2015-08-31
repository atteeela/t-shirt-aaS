#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tshirts Service
"""
import stackhut
import stackhut_client as client

class Default(stackhut.Service):

    def getShirt(self, address): 
        author = stackhut.service_author()
        service = client.SHClient('stackhut', 'tshirt-love')
        service.Default.gimmeTheLoot(author, address)
        return None

# export the services
SERVICES = {"Default": Default()}
