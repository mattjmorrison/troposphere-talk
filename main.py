#!python
import click
import json
import glob
from pathlib import Path


def load_config(config_path):
    defaults = {}
    for default in glob.glob('{}/*.json'.format(config_path)):
        p = Path(default)
        defaults[p.name.replace('.json', '')] = json.loads(p.read_text())
    return defaults


@click.command()
@click.option('--environment', default="staging")
def main(environment):
    defaults = load_config('defaults')
    for name, project in load_config('projects').items():
        env = project['environments'][environment]
        beanstalk = dict(defaults['beanstalk'], **env['beanstalk'])
        cloudfront = dict(defaults['cloudfront'], **env['cloudfront'])
        print(beanstalk)
        print(cloudfront)


if __name__ == '__main__':
    main()
