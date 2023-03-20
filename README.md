# Drag Dash: 

## Drag Queen Performance by Season

- Link to group repo: https://github.com/UBC-MDS/dragracerviz
- Link to group Proposal: https://github.com/UBC-MDS/dragracerviz/blob/main/reports/proposal.md
- Link where the Dash app is deployed: https://dragdash.onrender.com 

## Introduction

This dashboard was created using Dash, a Python framework for building web applications. The purpose of this dashboard is to display a comparison of contestant performance by season for the show RuPaul's Drag Race using a dataset from the R package dragracer. To read more about the proposal follow [this](https://github.com/UBC-MDS/dragracerviz/blob/main/reports/proposal.md) link.

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

It also has a Overall comparison of all the winners as a bar graph with the same colors that represent the performance of the winners in every episode throughout their respective seasons.

## Initial Sketch

This is what the initial sketch of the app looks like, the dashboard however does have updated layouts.

![sketch](https://github.com/dhruvinishar/dragdash/blob/master/assets/sketch.png)

## Installation and Setup to Run App Locally

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

- Or run the Jupyter Notebook file `app.ipynb` that uses JupyterDash to display the dashboard inline for easier access.

- Otherwise, if you choose not to runt the app locally, check out the deployed app using `render` at [this](https://dragdash.onrender.com/) URL to check out the dashboard.

## Usage

Once the application is running, open a web browser and navigate to the local browser port that the terminal prompts. The dashboard should appear with all the graphs and the interactive filters and legends. Select a season from the dropdown menu to update the graph interactively. You can also select the particular category in the legend of the graphs to look at specific categories for the Queens.

## Contributors

This dashboard was created by **Dhruvi Nishar**. If you would like to contribute to this project, please submit a pull request and follow the [Contributing guidelines](https://github.com/UBC-MDS/dragracerviz/blob/main/CONTRIBUTING.md) from the group repo.

If you are interested in contributing to this project, please follow these steps:

- Fork the repository and clone it to your local machine.
- Create a new branch for your work.
- Make your changes and commit them with clear commit messages.
- Push your changes to your fork.
- Submit a pull request with a clear description of your changes.

Contributors are welcome to work on any part of the dashboard, including adding new features, improving the user interface, or fixing bugs. If you are looking for ideas for how to contribute, please see the issues section of the repository for a list of current issues that need attention. 
Note that all contributions must abide by our [guidelines](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md).

## License

This project is licensed under the MIT License.