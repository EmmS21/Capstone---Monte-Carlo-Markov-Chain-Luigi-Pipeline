import pandas as pd
import luigi
import glob
import state_to_state_machine as ssm
class wrapper(luigi.WrapperTask):
    source = luigi.Parameter()
    def requires(self):
        size = 10000
        return[ssm.state_machine(size=size,obs_nums=i,source=self.source)for i in range(0, size)]
    def run(self):
        full_mc_sim = pd.concat([pd.read_csv(f, index_col=0) for f in glob.glob('C:\\Users\\User\\Documents\\GitHub\\Springboard-DSC\\AttributionModel\\Data\\sims\\*statemachine.csv')])
        full_mc_sim.to_csv('C:\\Users\\User\\Documents\\GitHub\\Springboard-DSC\\AttributionModel\\Data\\ModelData\\fullmcsims.csv')
        # pd.DataFrame().to_csv('/Users/emmanuels/Documents/AttributionData/Data/datawranglerwrapper3.csv') #never returns anything
    def output(self):
        return luigi.LocalTarget('C:\\Users\\User\\Documents\\GitHub\\Springboard-DSC\\AttributionModel\\Data\\ModelData\\fullmcsims.csv')
if __name__ == '__main__':
    luigi.build([wrapper(source = 'tizen')],workers=8,local_scheduler=True)

