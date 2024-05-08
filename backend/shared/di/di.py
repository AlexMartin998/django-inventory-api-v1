from dependency_injector import containers, providers


from books.models.publisher_model import Publisher
from books.repositories.publisher_repository import PublisherRepository
from books.services.publisher_service import PublisherService
from books.models.aba_model import Aba
from books.repositories.aba_repository import AbaRepository
from books.services.aba_service import AbaService
from books.models.aaran_model import Aaran
from books.repositories.aaran_repository import AaranRepository
from books.services.aaran_service import AaranService


class Container(containers.DeclarativeContainer):
    # ### Publisher ========================
    # Manager isn't accessible via Publisher instances - Error cuando se inyecta la instancia y no el modelo (sol. Object)
    publisher_model = providers.Object(
        Publisher  # como value/class sin instanciarlo (orm manager) - igual q en awilix
    )
    publisher_repository = providers.Singleton(
        PublisherRepository, model=publisher_model
    )
    publisher_service = providers.Singleton(
        PublisherService, repository=publisher_repository
    )
    aba_model = providers.Object(Aba)
    aba_repository = providers.Singleton(AbaRepository, model=aba_model)
    aba_service = providers.Singleton(AbaService, repository=aba_repository)

    aaran_model = providers.Object(Aaran)
    aaran_repository = providers.Singleton(AaranRepository, model=aaran_model)
    aaran_service = providers.Singleton(AaranService, repository=aaran_repository)


container = Container()
