# Makefile

# Define variables
SCALA_VERSION := 2.12
SPARK_VERSION := 3.5.0
JAR_NAME := death-office_$(SCALA_VERSION)-1.0.jar
SPARK_HOME := ./spark-$(SPARK_VERSION)-bin-hadoop3
SOURCE_FILE := src/main/scala/DeathOffice.scala

# Define targets and dependencies
all: package run

copy-csv:
	./copy_csv_files.sh

package: $(SOURCE_FILE)
	sbt package

run: $(SPARK_HOME)/bin/spark-submit
	$(SPARK_HOME)/bin/spark-submit --class "DeathOffice" --master local[4] target/scala-$(SCALA_VERSION)/$(JAR_NAME)

$(SPARK_HOME)/bin/spark-submit:
	@echo "Spark is not installed. Please download and extract Spark $(SPARK_VERSION) to $(SPARK_HOME)"
	@false
