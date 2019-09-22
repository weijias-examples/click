import click

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
def run():
    pass

@run.command()
@click.option("-c", '--count', default=1, help='Number of greetings.')
@click.option('-n', '--name', default='world', help='The person to greet.')
def hello(**kwargs):
    """Say hello"""
    count = kwargs["count"]
    name = kwargs["name"]
    for i in range(count):
        print("Hello %s." % name)


@run.command()
@click.option('-n', '--name', default='world', help='The person to goodbye.')
def goodbye(**kwargs):
    """Say goodbye"""
    print('Goodbye, {0}!'.format(kwargs['name']))

if __name__ == '__main__':
    run()