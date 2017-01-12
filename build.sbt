import com.typesafe.sbt.packager.MappingsHelper._

name := "ambari-schema-registry"

version := "3.0.1"

scalaVersion := "2.12.1"

val buildVersion = version + "-build-" + sys.env.getOrElse("BUILD_NUMBER", "local")

val metaInfoConfig: String = "metainfo.xml"

lazy val `ambari-schema-registry` = project
  .in(file("."))
  .enablePlugins(UniversalPlugin)
  .settings(
    topLevelDirectory := Some("SCHEMAREGISTRY"),
    mappings in(Universal, packageBin) ++= directory("configuration"),
    mappings in(Universal, packageBin) ++= directory("package"),
    mappings in(Universal, packageBin) += file("metrics.json") -> "metrics.json",
    mappings in(Universal, packageBin) += file("widgets.json") -> "widgets.json",
    mappings in(Universal, packageBin) += {
      val content =
        IO.read(file(metaInfoConfig)).replaceAll("<version>.*</version>", s"<version>$buildVersion</version>")
      val templateFile = file(target.value.getAbsolutePath + "/" + metaInfoConfig)
      IO.write(templateFile, content)
      templateFile
    } -> metaInfoConfig
  )