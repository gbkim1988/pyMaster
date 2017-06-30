from twisted.internet.protocol import Protocol, ClientFactory

class PoetryProtocol(Protocol):
    poem = ''

