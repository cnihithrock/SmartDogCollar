import os
from machine import UART
from notecard import *
port = UART(2, 9600)
port.init(9600, bits=8, parity=None, stop=1)

nCard = notecard.OpenSerial(port)

req = {"req": "hub.set"}
req["mode"] = "continuous"
req["product"] = "edu.purdue.nchaturv:smartcollar_53"
req["outbound"] = 30
req["inbound"] = 60
req["duration"] = 240
req["sync"] = True
nCard.Transaction(req)

req = {"req": "card.restore"}
req["delete"] = True
req["connected"] = True
nCard.Transaction(req)

req = {"req": "card.motion.mode"}
req["start"] = True
req["seconds"] = 10
req["sensitivity"] = 2
nCard.Transaction(req)

req = {"req": "card.location.mode"}
req["mode"] = "continuous"
rsp = nCard.Transaction(req)

req = {"req": "card.location.track"}
req["sync"] = True
req["heartbeat"] = True
req["hours"] = 2
rsp = nCard.Transaction(req)

req = {"req": "hub.sync"}
nCard.Transaction(req)
