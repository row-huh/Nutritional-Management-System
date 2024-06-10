import database as db
import datetime

patient_columns = ('patient_id', 'name', 'age', 'gender', 'contact_info')
nutritionist_columns = ('nutritionist_id', 'name', 'specialty', 'contact_info')
meal_plan_columns = ('meal_plan_id', 'patient_id', 'nutritionist_id', 'start_date', 'end_date', 'description')
food_item_columns = ('food_item_id', 'name', 'calories', 'protein', 'carbs', 'fats')
fitness_data_columns = ('fitness_data_id', 'patient_id', 'weight', 'height', 'bmi', 'measurement_date')

def format_data_as_html_table(data):
    if not data:
        return "<p>No data available</p>"

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
    """

    # Generating table headers
    for key in data.keys():
        html_table += f"<th>{key}</th>"
    html_table += "</tr>"

    # Generating table row
    html_table += "<tr>"
    for value in data.values():
        html_table += "<td>{}</td>".format(value)
    html_table += "</tr>"

    html_table += "</table>"
    return html_table

# used to generate a table for displaying
def html_data(connection):
    all_patients = db.fetch_patients(connection)
    all_nutritionists = db.fetch_nutritionists(connection)
    all_meal_plans = db.fetch_meal_plans(connection)
    all_food_items = db.fetch_food_items(connection)
    all_fitness_data = db.fetch_fitness_data(connection)

    all_patients = generate_html_table_from_data("Patients", patient_columns, all_patients)
    all_nutritionists = generate_html_table_from_data("Nutritionists", nutritionist_columns, all_nutritionists)
    all_meal_plans = generate_html_table_from_data("Meal Plans", meal_plan_columns, all_meal_plans)
    all_food_items = generate_html_table_from_data("Food Items", food_item_columns, all_food_items)
    all_fitness_data = generate_html_table_from_data("Fitness Data", fitness_data_columns, all_fitness_data)


    return all_patients, all_nutritionists, all_fitness_data, all_food_items, all_meal_plans

# used for getting html form for updating data
def get_update_html(title, data):
    if title.lower() == 'food_item':
        html = row_to_html(title, food_item_columns, data)
        print(html)
        return html
    elif title.lower() == 'patient':
        html = row_to_html(title, patient_columns, data)
        print(html)
        return html
    elif title.lower() == 'meal_plan':
        html = row_to_html(title, meal_plan_columns, data)
        print(html)
        return html
    elif title.lower() == 'nutritionist':
        html = row_to_html(title, nutritionist_columns, data)
        print(html)
        return html
    elif title.lower() == 'fitness_data':
        html = row_to_html(title, fitness_data_columns, data)
        print(html)
        return html
    else:
        print('SOMETHING WENT WRONG - maybe wrong table name is being passed')


def row_to_html(title, columns, data):
    form_html = f'<form action="/update_{title}" method="post">'
    for col, value in zip(columns, data[0]):
        form_html += f'<label for="{col}">{col.capitalize()}:</label><br>'
        form_html += f'<input type="text" id="{col}" name="{col}" value="{value}"><br><br>'
    form_html += '<input type="submit" value="Submit">'
    form_html += "</form>"
    return form_html


def generate_html_table_from_data(title, columns, data):
    if not data:
        return "<p>No data available</p>"

    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title} Table</title>
        <style>
            table {{
                width: 100%;
                border-collapse: collapse;
                border: 1px solid #ddd;
            }}
            th, td {{
                padding: 8px;
                text-align: left;
                border-bottom: 1px solid #ddd;
            }}
            th {{
                background-color: #f2f2f2;
            }}
        </style>
    </head>
    <body>
    
    """

    html += f"""
    </table>
    
    <h2>{title} Data</h2>
    
    <table>
        <tr>
    """

    for column in columns:
        html += f"<th>{column}</th>"
    html += "</tr>"

    for row in data:
        html += "<tr>"
        for value in row:
            if isinstance(value, datetime.datetime):
                value = value.strftime("%Y-%m-%d %H:%M:%S")
            html += f"<td>{value}</td>"
        html += "</tr>"

    html += """
    </table>
    
    </body>
    </html>
    """
    return html
