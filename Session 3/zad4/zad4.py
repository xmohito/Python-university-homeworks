import csv
import statistics
import webbrowser
import random

def get_valid_year_input():
    while True:
        try:
            sets_year = int(input("Enter sets production year (1949 - 2024): "))
            if 1949 <= sets_year <= 2024:
                return str(sets_year)
            else:
                print('Out of range. Try again')
        except ValueError:
            print('That\'s not a number')

def open_random_image_url(img_url_list):
    if img_url_list:
        webbrowser.open_new_tab(random.choice(img_url_list))

def process_sets_for_year(csv_reader, sets_year):
    sets_from_year = [row for row in csv_reader if row['year'] == sets_year]
    img_url_list = [row['img_url'] for row in sets_from_year]
    return sets_from_year, img_url_list

def calculate_statistics(sets_from_year):
    num_parts_list = [int(row['num_parts']) for row in sets_from_year]
    median = statistics.median(num_parts_list) if num_parts_list else 0
    average = statistics.mean(num_parts_list) if num_parts_list else 0
    return len(sets_from_year), median, average

def main():
    sets_year = get_valid_year_input()

    with open('sets.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        sets_from_year, img_url_list = process_sets_for_year(csv_reader, sets_year)

    open_random_image_url(img_url_list)
    number_of_sets, median, average = calculate_statistics(sets_from_year)

    print(f'Number of sets from this year: {number_of_sets}')
    print(f'Median number of elements (of all sets from that year): {int(round(median))}')
    print(f'Average number of elements in these sets: {int(round(average))}')

if __name__ == "__main__":
    main()