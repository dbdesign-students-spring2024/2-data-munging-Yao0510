import csv


def calculate_decadal_averages(file_path):
    decadal_averages = {}
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            year = int(row['Year'])
            anomaly_fahrenheit = float(row['J-D'])
            decade = (year // 10) * 10
            if decade in decadal_averages:
                decadal_averages[decade].append(anomaly_fahrenheit)
            else:
                decadal_averages[decade] = [anomaly_fahrenheit]

    for decade, anomalies in decadal_averages.items():
        average_anomaly = sum(anomalies) / len(anomalies)
        print(f'{decade}s: {average_anomaly:.2f} F')


if __name__ == '__main__':
    file_path = 'data/clean_data.csv'
    calculate_decadal_averages(file_path)
