from dependency_injector import containers, providers


from books.models.publisher_model import Publisher
from books.repositories.publisher_repository import PublisherRepository
from books.services.publisher_service import PublisherService
from books.models.aba_model import Aba
from books.repositories.aba_repository import AbaRepository
from books.services.aba_service import AbaService


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


container = Container()
