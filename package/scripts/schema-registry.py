import sys

from resource_management import *

class SchemaRegistry(Script):
    def install(self, env):
        import params
        env.set_params(params)
        self.install_packages(env)
        Directory(params.data_dir,
                  mode=0755,
                  owner=params.user,
                  group=params.group,
                  create_parents=True,
                  recursive_ownership=True
                  )
        Directory(params.log_dir,
                  mode=0755,
                  owner=params.user,
                  group=params.group,
                  create_parents=True,
                  recursive_ownership=True
                  )
        Directory(params.pid_dir,
                  mode=0755,
                  owner=params.user,
                  group=params.group,
                  create_parents=True,
                  recursive_ownership=True
                  )
        Directory(params.logsearch_conf_dir,
                  mode=777,
                  create_parents=True,
                  recursive_ownership=True
                  )
        Execute("rpm --import http://packages.confluent.io/rpm/1.0/archive.key")
        Execute("yum -y install yum-utils")
        Execute("yum-config-manager --add-repo http://packages.confluent.io/rpm/3.0")
        Execute("yum -y clean all")
        Execute("yum -y install confluent-schema-registry")
        File(format("{params.schema_registry_conf_file_location}"),
             content=InlineTemplate(params.schema_registry_conf),
             owner=params.user,
             group=params.group
             )

    def start(self, env, upgrade_type=None):
        import params
        env.set_params(params)
        File(format("{params.schema_registry_conf_file_location}"),
             mode=0755,
             group=params.group,
             owner=params.user,
             content=InlineTemplate(params.schema_registry_conf)
             )
        File(format("{params.log4j_file_location}"),
             mode=0755,
             group=params.group,
             owner=params.user,
             content=InlineTemplate(params.log4j_props)
             )
        start_cmd = """nohup /usr/bin/schema-registry-start {params.schema_registry_conf_file_location}
>> {params.log_file} 2>&1 &"""
        process_cmd = format(start_cmd.replace("\n", " ") + "\necho $! > {params.pid_file}")
        try:
            Execute(process_cmd,
                    user=params.user,
                    logoutput=True,
                    wait_for_finish=True,
                    timeout=300
                    )
        except:
            show_logs(params.log_file, params.user)
            raise

    def stop(self, env):
        import params
        env.set_params(params)
        Execute(format("/usr/bin/schema-registry-stop"), user=params.user)
        Execute(format("rm -f {params.pid_file}"), user=params.user)

    def status(self, env):
        import status_params
        env.set_params(status_params)
        check_process_status(status_params.pid_file)


if __name__ == "__main__":
    SchemaRegistry().execute()
