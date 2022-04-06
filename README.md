# snakedev_de_loka
To run this the first time simply open a terminal inside the snakedev_de_loka folder and run

```bash
just default
```
this assumes you have just installed, more info here: https://github.com/casey/just

To check out the results of the final step (Business Intelligence), check out these visualizations built using Falcon, hosted on plotly. Here you will see 2 visualizations protraying the average trip duration per day of the week:

Pie Chart
https://plotly.com/datacache/Zmum3JrStP1aM7wZZK55

Bar Chart
https://plotly.com/datacache/NHJOorXyTAkYN7OA4xIO


In the folder you will notice a file called flow.svg. This is a diagram depicting the end to end pipeline process using a DAG like format. This file can be generated automatically using the following steps:
- make sure the justfile is working properly and that there is a recipe called "default" which executes the individual recipe steps in the desired order
- run the parse_just.py - this will generate the DAG file with the logic required to create the visualization. It will be called flow.dot
- run the command:
```bash
 dot flow.dot -Tpng > flow.png
```

This will generate the visualization entitled flow.svg
This does not need to be run on a recurring basis, only when a step of the workflow is modified