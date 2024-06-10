def format_data_as_html_table(data):
    html_table = "<table border='1'><tr><th>ID</th><th>Name</th><th>Age</th><th>Gender</th><th>Email</th></tr>"
    
    for row in data:
        html_table += "<tr>"
        for item in row:
            html_table += "<td>{}</td>".format(item)
        html_table += "</tr>"
    
    html_table += "</table>"
    
    return html_table