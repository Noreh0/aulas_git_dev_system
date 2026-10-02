from models.hotel import Hotel

hotel01 = Hotel("Pousada Bonito", "Rua dos Bobos, N°0")
hotel01.receber_avaliacao("Heronzinho Lindo", 4.8)
hotel01.receber_avaliacao("Claudinei do GTA5", 3.4)
hotel01.receber_avaliacao("Jorgin do Grau", 4.9)
hotel01.receber_avaliacao("Nego Drama", 2.4)

def main():
    print(hotel01)

if __name__ == "__main__":
    main()