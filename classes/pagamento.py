class Pagamento():
    def __str__(self):
        string = f"{self.nomeFavorecido} | {self.data} | {self.valor} | {self.numero} | {self.forma}"
        return string
