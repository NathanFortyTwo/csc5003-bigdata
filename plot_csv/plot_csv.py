import matplotlib.pyplot as plt
import json
from tabulate import tabulate


def deco(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            load_path = "./data/" + filename + ".csv"
            save_path = "./img/" + filename + ".png"
            with open(load_path) as f:
                func(f)
            plt.xticks(rotation=30, ha="right")
            plt.title(func.__doc__)
            plt.tight_layout()
            plt.savefig(save_path)
            plt.clf()

        return wrapper

    return decorator


def get_true_value(col_name, encoded_value):
    JSON_PATH = "/mnt/d/csc5003data/2005_codes.json"

    with open(JSON_PATH) as f:
        json_file = json.load(f)
        return json_file[col_name].get(encoded_value)


@deco("ageRecode")
def age(f):
    """Number of deaths by age group"""
    _age = []
    deaths = []
    header = f.readline().split(",")
    for line in f:
        line = line.strip().split(",")
        value = get_true_value(header[0], line[0])
        value = value.split("year")[0]  # avoid overlap
        _age.append(value)
        deaths.append(int(line[1]))
        plt.bar(_age, deaths)


@deco("autopsy")
def autopsy(f):
    """Percentage of deaths with autopsy by age manner of death"""
    header = f.readline().split(",")
    manners = []
    percentages = []
    for line in f:
        line = line.strip().split(",")
        manner = get_true_value(header[0], line[0])
        autopsy = line[1]
        if manner and autopsy == "Y":
            percentage = float(line[-1])
            manners.append(manner)
            percentages.append(percentage)
    plt.bar(manners, percentages)


@deco("causeRecode")
def cause(f):
    """Most frequent causes of death"""
    header = f.readline().split(",")
    causes = []
    deaths = []
    table = []
    for line in f:
        line = line.strip().split(",")
        count = int(line[1])
        causes.append(line[0])
        table.append([line[0], get_true_value(header[0], line[0])])
        deaths.append(count)
    # print(tabulate(table, headers=["Code", "Cause"], tablefmt="github"))
    plt.bar(causes, deaths, width=0.7)


def education():
    with open("./data/educationPercentage.csv") as f:
        header = f.readline().split(",")
        percentages = []
        _all = dict()
        for line in f:
            line = line.strip().split(",")
            education = get_true_value(header[0], line[0])
            manner = get_true_value(header[1], line[1])
            percentage = float(line[-1])
            if not education or not manner:
                continue

            if not education in _all:
                _all[education] = ([], [])
            _all[education][0].append(manner)
            _all[education][1].append(percentage)

        figid = 0
        for education, (manners, percentages) in _all.items():
            plt.figure(figid)
            plt.bar(manners, percentages)
            figid += 1
            plt.title(education)
            plt.xticks(rotation=25, ha="right")
            plt.tight_layout()

            plt.savefig("./img/education/" + education + ".png")
            plt.clf()


def educationV2():
    with open("./data/educationPercentage.csv") as f:
        header = f.readline().split(",")
        percentages = []
        _all = dict()
        for line in f:
            line = line.strip().split(",")
            education = get_true_value(header[0], line[0])
            manner = get_true_value(header[1], line[1])
            percentage = float(line[-1])
            if not education or not manner:
                continue

            if not manner in _all:
                _all[manner] = ([], [])
            _all[manner][0].append(education)
            _all[manner][1].append(percentage)

        figid = 0
        for manners, (education, percentages) in _all.items():
            plt.figure(figid)
            plt.bar(education, percentages)
            figid += 1
            plt.title(manners)
            plt.xticks(rotation=25, ha="right")
            plt.tight_layout()
            plt.savefig("./img/manners/" + manners + ".png")
            plt.clf()


def manner_by_day():
    with open("./data/mannerOfDeathByDay.csv") as f:
        header = f.readline().split(",")
        percentages = []
        _all = dict()
        for line in f:
            line = line.strip().split(",")
            day = get_true_value(header[0], line[0])
            manner = get_true_value(header[1], line[1])
            percentage = float(line[-1])
            if not day or not manner:
                continue

            if not manner in _all:
                _all[manner] = ([], [])
            _all[manner][0].append(day)
            _all[manner][1].append(percentage)

        figid = 0
        for manners, (day, percentages) in _all.items():
            plt.figure(figid)
            plt.bar(day, percentages)
            figid += 1
            plt.title(manners)
            plt.xticks(rotation=25, ha="right")
            plt.tight_layout()
            plt.savefig("./img/manners_day/" + manners + ".png")
            plt.clf()


def manner_by_marital():
    with open("./data/mannerOfDeathByMaritalStatus.csv") as f:
        header = f.readline().split(",")
        percentages = []
        _all = dict()
        for line in f:
            line = line.strip().split(",")
            status = get_true_value(header[0], line[0])
            manner = get_true_value(header[1], line[1])
            percentage = float(line[-1])
            if not status or not manner:
                continue

            if not manner in _all:
                _all[manner] = ([], [])
            _all[manner][0].append(status)
            _all[manner][1].append(percentage)

        figid = 0
        for status, (manner, percentages) in _all.items():
            plt.figure(figid)
            plt.bar(manner, percentages)
            figid += 1
            plt.title(status)
            plt.xticks(rotation=25, ha="right")
            plt.tight_layout()
            plt.savefig("./img/marital_status/" + status + ".png")
            plt.clf()


@deco("racePercentage")
def race(f):
    deaths = dict()
    header = f.readline().split(",")
    for line in f:
        line = line.strip().split(",")
        race = get_true_value(header[0], line[0])
        manner = get_true_value(header[1], line[1])

        if manner and manner != "Natural":
            count = int(line[2])
            total = int(line[3])
            percentage = float(line[4])
            deaths[race + "_" + manner] = percentage
    plt.bar(deaths.keys(), deaths.values())


def main():
    age()
    autopsy()
    cause()
    education()
    manner_by_day()
    manner_by_marital()
    race()
    educationV2()


if __name__ == "__main__":
    main()
