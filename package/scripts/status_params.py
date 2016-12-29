from resource_management.libraries.functions import format
from resource_management.libraries.script.script import Script

config = Script.get_config()

data_dir = config['configurations']['schema-registry-env']['data_dir']
pid_dir = format("{data_dir}/run")
pid_file = format("{pid_dir}/schema_registry.pid")