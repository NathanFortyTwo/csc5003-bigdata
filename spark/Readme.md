# DeathOffice Scala Project

The DeathOffice Scala project is designed to analyze and extract insights from a comprehensive dataset containing information about deaths in the United States from 2005 to 2015. Leveraging Apache Spark, the project employs Scala to conduct various analyses on the dataset and subsequently visualizes the results using Python's Matplotlib library.

## Prerequisites
- Apache Spark installed and configured
- Scala (sbt) installed

## Usage

### 1. Data Loading
Before running the Scala project, ensure that the dataset is available in CSV format within the specified input path. The project expects CSV files with a consistent structure.

### 2. Running the Scala Project
Execute the following commands to run the Scala project:

```bash
make all
```

This command will trigger the build, packaging, and execution of the Scala project. The results will be saved as CSV files in the project directory.

## Project Structure

### Scala Code Explanation

The `DeathOffice` Scala object defines the main logic for data analysis. It loads the dataset, performs various aggregations, and calculates percentages for different attributes. The results are then saved as CSV files.

### Makefile

The Makefile simplifies the project workflow by providing convenient targets for copying CSV files, building the Scala project and running it on Spark.

### Additional Files

- `copy_csv_files.sh`: Shell script to copy CSV files to the input directory.
