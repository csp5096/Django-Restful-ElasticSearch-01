from django.conf import settings

from elasticsearch_dsl import DocType, Index, Integer, Search
from elasticsearch_dsl.connections import connections

connections.create_connection(hosts=settings.ELASTICSEARCH_HOSTS)


class ProfileDocType(DocType):
    brand_ids = Integer()

    class Meta(object):
        index = 'profiles'
        doc_type = 'profiles'

    @classmethod
    def reset(cls):
        index = Index(cls._doc_type.index)
        if index.exists():
            index.delete()
        cls.init()

    @classmethod
    def flush(cls):
        Index(cls._doc_type.index).flush()













