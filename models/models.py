# -*- encoding: utf-8 -*-
from google.appengine.ext import ndb
import operator
import datetime

class Claseunidad(ndb.Model):
    codigo = ndb.StringProperty(required = True)
    nombre = ndb.StringProperty(required = True)

    def _pre_put_hook(self):
        if not self.key.id():
            if Claseunidad.query(Claseunidad.codigo == self.codigo).count() > 0:
                raise CodigoClaseunidadDuplicado('Código claseunidad ya existe')

    def get_claseunidadkey(self, codigo):
        return ndb.gql("SELECT __key__ FROM Claseunidad WHERE codigo = :1", codigo).get()