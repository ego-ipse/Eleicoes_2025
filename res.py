""" """
import pandas as pd

class HistoricData:
    """"""
    def __init__(self, path):
        """"""
        self.all_data = self.get_elect_data(pd.read_csv(path, sep=";"))
        self.metadata = pd.read_csv('metadata.csv', sep=";")


    def __getitem__(self, key):
        """ """
        return self.all_data[key]

    @property
    def districts(self):
        """ """
        return self.metadata.columns.values


    def general(self, district):
        """ """
        return self[self.metadata.loc[1,district]]


    def mandates(self, district):
        """ """
        return int(self.metadata.loc[0,district])

    def get_elect_data(self, data):
        """ """
        members = {}
        for x in data.columns.values[1:]:
                members[x] = {part: data.loc[idx,x]
                              for idx, part in enumerate(data.iloc[:,0].to_list())}
        return members
