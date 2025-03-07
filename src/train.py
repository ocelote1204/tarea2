def train_model(model, x_train, y_train):
    model.fit(x_train, y_train, epochs=5, batch_size=128)
