def calculate_metrics(filename):
    pass

## TESTS BELOW

actual = calculate_metrics("metrics.csv")

sample_solutions = [
    'Alley Grading-Unimproved (2018): Target=180, Average=438.22',
    'Bike Lane Post/Ped Xing Sign Repair (2017): Target=5, Average=1151.69',
    'CDOT Construction Complaints (2017): Target=14, Average=19.09',
    'Gym Shoe/Object On Electrical Wire (2016): Target=7, Average=110.63',
    'Landscape Median Maintenance (2011): Target=30, Average=3.93',
    'Pavement Cave-In Survey (2015): Target=3, Average=2.04'
]

issue_counter = 0
if actual == None or not len(actual) == 262:
    issue_counter += 1
    print("Looks like your output is not the correct length.")

else:

    for example in sample_solutions:
        if example not in actual:
            issue_counter += 1
            print(f"Looks like you're averages are not correct. Missing:{example}")

        if issue_counter == 0:
            print("Looks like your solutions pass our tests! Yay!")


