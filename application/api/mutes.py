try:
    from twitter.application.api.superclass.abstract_module import AbstractModule
    from twitter.application.api._mutes.users import users
except ModuleNotFoundError as main:
    from application.api.superclass.abstract_module import AbstractModule
    from application.api._mutes.users import users

# encapsulate namespace
mutes = AbstractModule(globals())
setattr(mutes, 'users', users)

# enforce singleton
del (users,
     AbstractModule)
