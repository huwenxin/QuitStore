from rdflib.plugin import register
from rdflib.query import Processor, UpdateProcessor, ResultSerializer

register(
    'sparql', Processor,
    'quit.processor', 'SPARQLProcessor')

register(
    'sparql', UpdateProcessor,
    'quit.processor', 'SPARQLUpdateProcessor')

register(
    'html', ResultSerializer,
    'quit.htmlresults', 'HTMLResultSerializer')