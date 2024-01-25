import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions.Window
import org.apache.spark.sql.SaveMode
import org.apache.spark.sql.Dataset
import org.apache.spark.sql.Row

object DeathOffice {
  def main(args: Array[String]): Unit = {
    val spark = SparkSession.builder.appName("DeathOffice").getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")

    println("Starting ... \n")
    val filename = "./input/*_data.csv"
    val deathData = spark.read.option("header", "true").csv(filename)

    // show the day of the week with the most deaths
    val dayofweek = deathData
      .groupBy("day_of_week_of_death")
      .agg(count("day_of_week_of_death"))

    // show the manner of death with the most deaths
    val mannerofDeath = deathData
      .groupBy("manner_of_death")
      .agg(count("manner_of_death"))

    // I want the percentage of deaths for each manner of death for each day of the week
    val mannerofDeathByDay = deathData
      .groupBy("day_of_week_of_death", "manner_of_death")
      .agg(count("manner_of_death").alias("count"))
      .withColumn(
        "total",
        sum("count").over(Window.partitionBy("day_of_week_of_death"))
      )
      .withColumn("percentage", col("count") / col("total") * 100)
      .orderBy("day_of_week_of_death", "manner_of_death")

    // show the percentage of deaths for each manner of death for each day of the week
    mannerofDeathByDay.show(100)
    saveDataset(mannerofDeathByDay, "./mannerofDeathByDay.csv")

    // I want the percentage of autopsy for each manner of death
    val autopsy = deathData
      .groupBy("manner_of_death", "autopsy")
      .agg(count("autopsy").alias("count"))
      .withColumn(
        "total",
        sum("count").over(Window.partitionBy("manner_of_death"))
      )
      .withColumn("percentage", col("count") / col("total") * 100)
      .orderBy("manner_of_death", "autopsy")

    // Show the percentage of autopsy for each manner of death
    autopsy.show(100)
    saveDataset(autopsy, "./autopsy.csv")

    // Show the top 20 358_cause_recode
    val causeRecode = deathData
      .groupBy("358_cause_recode")
      .agg(count("358_cause_recode").alias("count"))
      .orderBy(desc("count"))
      .limit(20)

    // Show the top 20 358_cause_recode
    causeRecode.show()
    saveDataset(causeRecode, "./cause.csv")

    // I want the percentage of manner_of_death fro each race
    val racePercentage = deathData
      .groupBy("race", "manner_of_death")
      .agg(count("manner_of_death").alias("count"))
      .withColumn(
        "total",
        sum("count").over(Window.partitionBy("race"))
      )
      .withColumn("percentage", col("count") / col("total") * 100)
      .orderBy("race", "manner_of_death")

    // Show
    racePercentage.show()
    saveDataset(racePercentage, "./racePercentage.csv")

    // Maner of death by marital_status
    val mannerOfDeathByMaritalStatus = deathData
      .groupBy("marital_status", "manner_of_death")
      .agg(count("manner_of_death").alias("count"))
      .withColumn(
        "total",
        sum("count").over(Window.partitionBy("marital_status"))
      )
      .withColumn("percentage", col("count") / col("total") * 100)
      .orderBy("marital_status", "manner_of_death")

    // Show
    mannerOfDeathByMaritalStatus.show()
    saveDataset(
      mannerOfDeathByMaritalStatus,
      "./mannerOfDeathByMaritalStatus.csv"
    )

    // I want the percentage of manner_of_death for each education_2003_revision
    val educationPercentage = deathData
      .groupBy("education_2003_revision", "manner_of_death")
      .agg(count("manner_of_death").alias("count"))
      .withColumn(
        "total",
        sum("count").over(Window.partitionBy("education_2003_revision"))
      )
      .withColumn("percentage", col("count") / col("total") * 100)
      .orderBy("education_2003_revision", "manner_of_death")

    // Show
    educationPercentage.show()
    saveDataset(educationPercentage, "./educationPercentage.csv")

    // I want the number of death by age_recode_12
    val ageRecode = deathData
      .groupBy("age_recode_12")
      .agg(count("age_recode_12").alias("count"))
      .orderBy(desc("count"))

    // Show
    ageRecode.show()
    saveDataset(ageRecode, "./ageRecode.csv")

    // I want the percentage of 39_cause_recode for each month_of_death
    val causeRecodeByMonth = deathData
      .groupBy("39_cause_recode", "month_of_death")
      .agg(count("month_of_death").alias("count"))
      .withColumn(
        "total",
        sum("count").over(Window.partitionBy("39_cause_recode"))
      )
      .withColumn("percentage", col("count") / col("total") * 100)
      .orderBy("39_cause_recode", "month_of_death")

    // Show
    causeRecodeByMonth.show(40)
    saveDataset(causeRecodeByMonth, "./causeRecodeByMonth.csv")
  }

  def saveDataset(dataset: Dataset[Row], name: String) {
    dataset
      .coalesce(1)
      .write
      .mode(SaveMode.Overwrite)
      .option("header", "true")
      .csv(name)
  }
}
