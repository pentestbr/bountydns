class BaseCommand:
    name = ''
    aliases = []
    description = ''

    def __init__(self, options):
        self.options = options

    def run(self):
        raise NotImplementedError()
    
    @classmethod
    def make(cls, args):
        return cls(dict(vars(args)))
    
    @classmethod
    def parser(cls, parser):
        if not cls.name:
            raise NotImplementedError()
        return parser

    @classmethod
    def apply_parser(cls, sub_parser):
        parser = sub_parser.add_parser(cls.name, aliases=cls.aliases, help=cls.description)
        return cls.parser(parser)

    @classmethod
    def has_command(cls, command):
        return command in [cls.name] + cls.aliases
    
    def option(self, key, default='dne'):
        if default == 'dne':
            return self.options.get(key)
        return self.options.get(key, default)