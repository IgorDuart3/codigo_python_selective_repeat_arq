import random


class SelectiveRepeatSim:
    def __init__(self, total_pacotes, tamanho_janela, prob_perda):
        self.total_pacotes = total_pacotes
        self.tamanho_janela = tamanho_janela
        self.prob_perda = prob_perda
        self.pacotes_confirmados = [False] * total_pacotes
        self.tentativas_totais = 0

    def enviar(self):
        base = 0

        while base < self.total_pacotes:
            for i in range(base, min(base + self.tamanho_janela, self.total_pacotes)):
                if not self.pacotes_confirmados[i]:
                    self.tentativas_totais += 1
                    print(f"Transmitindo Pacote {i}...", end=" ")

                    if random.random() > self.prob_perda:
                        print("Recibo (ACK) recebido!")
                        self.pacotes_confirmados[i] = True
                    else:
                        print("FALHA (Pacote perdido/corrompido)")

            while base < self.total_pacotes and self.pacotes_confirmados[base]:
                base += 1
                print(f"Janela deslizou para a posição {base}")

            print("-" * 30)

        print(f"\nSucesso! Todos os {self.total_pacotes} pacotes entregues.")
        print(f"Total de transmissões realizadas: {self.tentativas_totais}")


if __name__ == "__main__":
    # Configuração: 10 pacotes, janela de tamanho 4, 30% de chance de perda
    simulacao = SelectiveRepeatSim(total_pacotes=10, tamanho_janela=4, prob_perda=0.3)
    print(f"Transmitindo {simulacao.total_pacotes} pacotes\n")
    print(f"Janela inicia na posição 0")
    simulacao.enviar()
