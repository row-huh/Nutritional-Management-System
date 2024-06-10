import database as db

def format_data_as_html_table(data):
    html_table = """
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
            border: 1px solid #ddd;
        }
        th, td {
            padding: 8px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
    <table>
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Age</th>
            <th>Gender</th>
            <th>Email</th>
        </tr>
    """

    for row in data:
        html_table += "<tr>"
        for item in row:
            html_table += "<td>{}</td>".format(item)
        html_table += "</tr>"

    html_table += "</table>"
    return html_table



# other functions
def html_data(connection):
    all_patients = db.fetch_patients(connection)
    all_nutritionists = db.fetch_nutritionists(connection)
    all_food_items = db.fetch_food_items(connection)
    all_meal_plans = db.fetch_meal_plans(connection)
    all_fitness_data = db.fetch_fitness_data(connection)

    all_patients = format_data_as_html_table(all_patients)
    all_nutritionists = format_data_as_html_table(all_nutritionists)
    all_fitness_data = format_data_as_html_table(all_fitness_data)
    all_food_items = format_data_as_html_table(all_food_items)
    all_meal_plans = format_data_as_html_table(all_meal_plans)

    return all_patients, all_nutritionists, all_fitness_data, all_food_items, all_meal_plans