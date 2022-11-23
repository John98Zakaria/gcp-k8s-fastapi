from general_types.exeption_base import DomainExceptionBaseError


class UsernameTakenException(DomainExceptionBaseError):
    pass


class UserNotFoundException(DomainExceptionBaseError):
    pass
