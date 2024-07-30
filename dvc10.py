import pandas as pd
import os


def run_command(command):
    result = os.system(command)
    if result != 0:
        print(f"Error running command: {command}")
    return result


run_command('rmdir /S /Q .git')
run_command('rmdir /S /Q .dvc')

data = pd.read_csv('InternationalSales.csv')

run_command('git init')
run_command('dvc init -f')

run_command('dvc add InternationalSales.csv')
run_command('git add InternationalSales.csv.dvc .gitignore')
run_command('git commit -m "Add original dataset"')




data = data.dropna()

data = data.drop_duplicates()


data.to_csv('InternationalSales.csv')

run_command('dvc add InternationalSales.csv')
run_command('git add InternationalSales.csv.dvc .gitignore')
run_command('git commit -m "Add Preprocessed dataset"')


data = data.drop(columns = ['Region'])

data.to_csv('InternationalSales.csv')

run_command('dvc add InternationalSales.csv')
run_command('git add InternationalSales.csv.dvc .gitignore')
run_command('git commit -m "Dataset without Region and Sales Channel " ')


## And finally if I want to return to a specific version
## we can use git checkout <commit nb> and dvc checkout



