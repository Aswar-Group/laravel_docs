# Swagger UI Generator

This tool generates a Swagger UI HTML page from an API specification defined in a JSON/YAML file. It allows you to visualize and interact with the API's resources without implementing the logic behind it.

## Requirements

- Python 3
- PyYAML
- A YAML file containing your API specification following the OpenAPI Specification (OAS).

## Installation

Before running the script, you need to ensure that Python 3 is installed on your system. You also need to install the requirements:

```
pip install -r requirments.txt
```

## Usage

To use the script, you need to provide two arguments:
- The path to the input YAML file containing your API specification.
- The path to the output HTML file where the Swagger UI will be generated. (Should be in the same root folder as the [swagger_libs](swagger_libs))

The command format is:
```
python swagger_ui_gen.py swagger.json index.html
```

This command reads the API specification from `swagger.json` and generates a Swagger UI HTML page in `index.html`.

##  Workflow Configuration
The workflow is defined in .github/workflows/scheduled_get_request.yml. No further action is required unless you wish to change the schedule or the scripts being run.

## Customization

The Swagger UI can be customized by modifying the `TEMPLATE` string within the script. You can adjust the HTML, CSS, and JavaScript according to your needs.

This current one is based on
on [Swagger API Source code](https://github.com/swagger-api/swagger-ui/blob/4f1772f6544699bc748299bd65f7ae2112777abc/dist/index.html)


## Contributing

Contributions to this project are welcome. You can contribute by improving the script, adding more features, or reporting bugs.


