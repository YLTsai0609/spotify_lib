import abc


class _Task(abc.ABC):
    @property
    @abc.abstractclassmethod
    def inflow(self):
        """Input data"""
        raise NotImplemented

    @property
    @abc.abstractclassmethod
    def upstream(self):
        """upstream tasks"""
        raise NotImplementedError()

    @property
    @abc.abstractclassmethod
    def outflow(self):
        """outpur data"""
        raise NotImplementedError()

    @property
    @abc.abstractclassmethod
    def run(self):
        """Transformation logic of this operator"""
        raise NotImplementedError()

    def __call__(self, *args, **kwargs):
        return self.run(*args, **kwargs)
