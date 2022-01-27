from apps.models import Model


class Loan(Model):
    __table__ = 'digitals'
    __primary_key__ = 'loanid'
