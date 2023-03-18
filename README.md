# Drag Dash: 

## Drag Queen Performance by Season

- Link to group repo: https://github.com/UBC-MDS/dragracerviz
- Link to group Proposal: https://github.com/UBC-MDS/dragracerviz/blob/main/reports/proposal.md

## Introduction

This dashboard was created using Dash, a Python framework for building web applications. The purpose of this dashboard is to display a comparison of contestant performance by season for the show RuPaul's Drag Race using a dataset from the R package dragracer. 

## Dataset

The dataset used in this dashboard is from the R package dragracer. The data contains information on contestant performance by season for RuPaul's Drag Race. The dataset for this project can be found [here](https://cran.r-project.org/web/packages/dragracer/index.html).


## Features

This dashboard displays a bar chart that shows the performance of each queen in a given season. Users can select a season from a dropdown menu to update the graph. The colors of the bars indicate the performance of the queen in each episode:

- WIN (blue)
- HIGH (pink)
- SAFE (green)
- LOW (orange)
- BOTTOM (yellow)
- OUT (grey)

## Initial Sketch

![sketch](https://github.com/dhruvinishar/dragdash/blob/master/assets/sketch.png)

## Installation and Setup

- Clone this repository to your local machine using 

```bash
git clone https://github.com/username/repository.git.
```

- Install the necessary libraries using 

```bash
pip install -r requirements.txt.
```

- Run the application using 

```bash
python app.py.
```

## Usage

Once the application is running, open a web browser and navigate to the local browser port. The dashboard should appear. Select a season from the dropdown menu to update the graph interactively.

### Run the app locally

To run this app using Docker write the following commands after cloning the repo:

```bash
cd 532-ia1-flordandrea
docker-compose up
```

Finally, open the app in the followin URL http://localhost:8000/

## Contributors

This dashboard was created by Dhruvi Nishar. If you would like to contribute to this project, please submit a pull request and follow the contributing guidelines from the group repo.

## License

This project is licensed under the MIT License.