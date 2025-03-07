from src.data import load_data
from src.model import build_model
from src.train import train_model

def main():
    # Cargar datos
    x_train, y_train, x_test, y_test = load_data()

    # Construir modelo
    model = build_model()

    # Mostrar resumen del modelo
    model.summary()

    # Entrenar modelo
    train_model(model, x_train, y_train)

if __name__ == "__main__":
    main()
