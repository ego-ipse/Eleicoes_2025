""" FOO """
from typing import Dict
from res import HistoricData

class ElectCalculator:
    def __init__(self, path):
        self.data = HistoricData(path)

    def hondt(self, res: Dict, mand) -> Dict[str, int]:
        """ Metodo de hondt """
        vals = []
        res.pop("Brancos", None)
        res.pop("Nulos", None)
        for k,v in res.items():
            vals += [(part:=[v/i for i in range(1,mand)])]
            #print(f"{k} -> {part}")
            res[k] = 0

        # Transpose & flatten.
        vals=sum(list(map(list, zip(*vals))), [])

        for i in range(1, mand+1):
            vals[(ind:=vals.index(max(vals)))] = -1
            res[(part:=[*res][ind % len(res)])] += 1
            #print(f"Mand {i} goes to {part}")

        #print(res)
        return res


    def adjust_res(self, district: str, model:Dict) -> Dict[str, int]:
        """ TST """
        gener = self.data.general(district)
        previ = self.data[district]

        first_pass = {k:v*previ[k]/gener[k] for k,v in model.items()}

        big_prev = [v for k,v in previ.items() if k in model]
        big_gen = [v for k,v in gener.items() if k in model]
        adj_big = (sum_sond:=sum(model.values()))*sum(big_prev)/sum(big_gen)

        second_pass = {k:v*adj_big/sum(first_pass.values()) for k,v in first_pass.items()}
        sum_sp = sum(second_pass.values())
        #print(f"Adj, known : {second_pass}, sum: {sum_sp}")

        m_p = {k:v*(100-sum_sp)/(100-sum_sond) for k,v in previ.items() if k not in model}
        #print(f"Adj, min : {m_p}, sum: {sum(m_p.values())}")

        second_pass.update(m_p)
        return second_pass

    def print_data(self, dt: Dict):
        """ """
        print("\n".join([f"{k:<3} -> {v}"
                         for k, v in sorted(dt.items(), key=lambda item: -item[1])
                         if v > 0]))


    def elect(self, model):
        """" FOO """
        man = 0
        fin = {}
        for district in self.data.districts:
            print(f"Resultados para : {district}")
            dt = self.hondt(self.adjust_res(district, model),
                            self.data.mandates(district))
            self.print_data(dt)
            man += self.data.mandates(district)
            for a,b in dt.items():
                fin[a] = fin[a] + b if a in fin else b

        print(f"Totais para {man} mandatos")
        self.print_data(fin)
        return fin
