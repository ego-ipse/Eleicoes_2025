from elect_calc import ElectCalculator

# Meta renascença
SOND = {"AD":32.3,
        "PS":26.6,
        "CH":17.4,
        "IL":6.1,
        "L":3.9,
        "BE":2.8,
        "CDU":2.9,
        "PAN":1.3}

# Latest JN
SOND_2 = {"AD":31.1,
          "PS":24.4,
          "CH":17.8,
          "IL":6.3,
          "L":5.3,
          "BE":3.2,
          "CDU":3.2,
          "PAN":1.1}
Calc = ElectCalculator('2024_res_pd.csv')
Calc.elect(SOND_2)
