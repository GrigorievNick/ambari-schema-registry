import com.typesafe.sbt.packager.MappingsHelper._

name := "ambari-schema-registry"

version := "3.0.1"

scalaVersion := "2.12.1"

lazy val `ambari-schema-registry` = project
  .in(file("."))
  .enablePlugins(UniversalPlugin)
  .settings(
    topLevelDirectory := Some("SCHEMAREGISTRY"),
    mappings in(Universal, packageBin) ++= directory("configuration"),
    mappings in(Universal, packageBin) ++= directory("package"),
    mappings in(Universal, packageBin) += file("metrics.json") -> "metrics.json",
    mappings in(Universal, packageBin) += file("widgets.json") -> "widgets.json",
    mappings in(Universal, packageBin) += file("metainfo.xml") -> "metainfo.xml"
  )
