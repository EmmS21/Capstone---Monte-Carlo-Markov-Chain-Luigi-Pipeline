import luigi
import pandas as pd
class data_filter(luigi.Task):
    file = luigi.Parameter()
    source = luigi.Parameter()
    def run(self):
        file_pd = pd.read_csv(self.file)
        # file_pd = file_pd[file_pd['device_used']==self.source]
        actions = file_pd.state.unique()
        for current in actions:
            filter_file = file_pd.loc[file_pd.state.str.contains(current,na=False)]
            filter_file.to_csv('C:\\Users\\User\\Documents\\GitHub\\Springboard-DSC\\AttributionModel\\Data\\ModelData\\'+str(current)+'.csv')
    def requires(self):
        return []
    def output(self):
        return luigi.LocalTarget(r'C:\Users\User\Documents\GitHub\Springboard-DSC\AttributionModel\Data\ModelData\complete.csv')

