import datetime


class DadosIniciais:
    def __init__(self, capital_inicial: float, taxa_juros: float, periodizacao,
                 ano_final: int, mes_final: int, dia_final: int):
        self.capital_inicial = capital_inicial
        self.taxa_juros = taxa_juros
        self.periodizacao = periodizacao
        self.data_final = f"{ano_final}-{mes_final}-{dia_final}"
        self.dia_hoje = datetime.datetime.today()
        self.prazo = (datetime.datetime.fromisoformat(self.data_final) - self.dia_hoje).days


class JurosCompostos(DadosIniciais):
    def __init__(self, capital_inicial: float, taxa_juros: float, periodizacao, ano_final: int, mes_final: int,
                 dia_final: int):
        super().__init__(capital_inicial, taxa_juros, periodizacao, ano_final, mes_final, dia_final)
        self.ano_final = ano_final
        self.mes_final = mes_final
        self.dia_final = dia_final
        try:
            if ".".find(periodizacao):
                ".".removesuffix(".")
            if periodizacao == "am":
                self.periodizacao = 30
            elif periodizacao == "aa":
                self.periodizacao = 365
            elif periodizacao == "as":
                self.periodizacao = 180
        except ValueError:
            raise ValueError

    def juros_compostos(self):
        montante = self.capital_inicial * (1 + (self.taxa_juros / 100)) ** (self.prazo / self.periodizacao)
        print(f"Na data {self.dia_final}/{self.mes_final}/{self.ano_final} o valor inicial de R$ "
              f"{self.capital_inicial:_.2f} terá rendido há uma taxa de {self.taxa_juros:.2f}% R$ "
              f"{montante:_.2f}".replace(".", ",").replace("_", "."))


# ----------------- Exemplo de uso ----------------------#
operacao = JurosCompostos(30000, 10.5, "aa", 2026, 12, 31)
operacao.juros_compostos()
