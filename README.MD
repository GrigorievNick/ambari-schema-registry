confluentic-schema-registry-ambari
Ambari service package for schema registry http://docs.confluent.io/3.0.0/schema-registry/docs/intro.html#deployment 
Use sbt packaheBin to build zip file. 
Copy package to ambari resorces: 
`scp /target/universal/ambari-schema-registry-3.0.1.zip :/var/lib/ambari-server/resources/stacks/HDP/2.5/services/` 
Restart ambari service `ambari-service restart` 
Go ambaru UI and use add service button, find and  install Schema Registry
