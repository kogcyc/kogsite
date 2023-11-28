
from jinja2 import Template
import json

# Your JSON data
json_data = '''
{
  "groups": [
    {
      "name": "Role",
      "options": [
        {"value": "commuting", "label": "Commuting"},
        {"value": "road", "label": "Road"},
        {"value": "gravel", "label": "Gravel"}
      ]
    },
    {
      "name": "Material",
      "options": [
        {"value": "steel-tig", "label": "Steel, TIG'd"},
        {"value": "steel-fillet", "label": "Steel, fillet brazed"},
        {"value": "steel-lugged", "label": "Steel, lugged"},
        {"value": "aluminum", "label": "Aluminum, TIG'd"}
      ]
    }
  ]
}
'''



# Load JSON data
data = json.loads(json_data)

# Jinja2 template
template_str = '''
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Radio Buttons Example</title>
</head>
<body>

<form action="http://localhost:5000" method="post" id="myForm">

  {% for group in groups %}
    <fieldset>
      <legend>{{ group.name }}</legend>
      {% for option in group.options %}
        <label>
          <input type="radio" name="{{ group.name }}" value="{{ option.value }}">
          {{ option.label }}
        </label><br>
      {% endfor %}
    </fieldset>
  {% endfor %}
  <input type="submit" value="Submit">

</form>

</body>
</html>
'''

# Create a Jinja2 template
template = Template(template_str)

# Render the template with the JSON data
html_output = template.render(groups=data['groups'])

# Output the HTML
print(html_output)
