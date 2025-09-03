import datetime
import matplotlib.pyplot as plt

class PlantioGirassolAI:
    def __init__(self, temperatura, umidade_solo, chuva_prevista, data_plantio):
        self.temperatura = temperatura  # em °C
        self.umidade_solo = umidade_solo  # em %
        self.chuva_prevista = chuva_prevista  # em mm
        self.data_plantio = data_plantio  # string 'YYYY-MM-DD'

    def dias_desde_plantio(self):
        data_plantio = datetime.datetime.strptime(self.data_plantio, "%Y-%m-%d").date()
        hoje = datetime.date.today()
        return (hoje - data_plantio).days

    def tamanho_estimado(self):
        dias = self.dias_desde_plantio()
        # Estimativa: até 100 dias, crescimento linear até 180cm (média para girassol)
        max_dias = 100
        max_tamanho = 180  # cm
        tamanho = min((dias / max_dias) * max_tamanho, max_tamanho)
        return tamanho

    def verificar_periodo_ideal(self):
        if 20 <= self.temperatura <= 30:
            return "Período ideal para o plantio."
        else:
            return "Fora do período ideal. Aguarde temperaturas entre 20°C e 30°C."

    def recomendar_espacamento(self):
        return "Espaçamento recomendado: 30cm entre plantas e 70cm entre linhas."

    def verificar_irrigacao(self):
        if self.umidade_solo < 60 and self.chuva_prevista < 10:
            return "Irrigação recomendada nos próximos dias."
        else:
            return "Solo adequado, irrigação não necessária."

    def relatorio(self):
        return {
            "periodo_ideal": self.verificar_periodo_ideal(),
            "espacamento": self.recomendar_espacamento(),
            "irrigacao": self.verificar_irrigacao(),
            "dias_desde_plantio": self.dias_desde_plantio(),
            "tamanho_estimado_cm": round(self.tamanho_estimado(), 1),
            "data_recomendacao": datetime.date.today().isoformat()
        }

    def gerar_imagem_girassol(self, path="girassol.png"):
        tamanho = self.tamanho_estimado()  # cm
        altura = tamanho / 10  # escala para imagem (max 18)
        fig, ax = plt.subplots(figsize=(3, 6))
        ax.set_xlim(-2, 2)
        ax.set_ylim(0, 20)
        # Talo
        ax.plot([0, 0], [0, altura], lw=8, color="green")
        # Folhas
        ax.plot([0, -1], [altura*0.4, altura*0.6], lw=6, color="lime")
        ax.plot([0, 1], [altura*0.5, altura*0.7], lw=6, color="lime")
        # Flor (cabeça)
        girassol_center = (0, altura)
        flor = plt.Circle(girassol_center, 1, color="yellow", zorder=2)
        centro = plt.Circle(girassol_center, 0.5, color="saddlebrown", zorder=3)
        ax.add_patch(flor)
        ax.add_patch(centro)
        # Texto tamanho
        ax.text(0, altura + 2, f"Tamanho estimado: {round(tamanho,1)} cm", ha='center', fontsize=12)
        ax.axis('off')
        plt.savefig(path, bbox_inches='tight')
        plt.close(fig)
        print(f"Imagem gerada: {path}")

# Exemplo de uso
if __name__ == "__main__":
    temperatura = 25
    umidade_solo = 55
    chuva_prevista = 5
    data_plantio = "2025-06-01"

    ia_girassol = PlantioGirassolAI(temperatura, umidade_solo, chuva_prevista, data_plantio)
    relatorio = ia_girassol.relatorio()

    for chave, valor in relatorio.items():
        print(f"{chave}: {valor}")

    ia_girassol.gerar_imagem_girassol()
