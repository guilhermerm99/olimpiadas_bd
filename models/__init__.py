from sqlalchemy.ext.declarative import declarative_base

# Definição da base
Base = declarative_base()

# Importação dos modelos
from .pais import Pais
from .confederacao import Confederacao
from .atleta import Atleta
