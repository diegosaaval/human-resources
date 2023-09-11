##############################ENTRAR MODELOS CON CV Y METRICA################################################################
# Cargar librerías
from sklearn.model_selection import cross_validate  # Validación cruzada


def train_models_cv(models, X_train, y_train, cv, metric):
    for model in models:
        models[model].fit(X_train, y_train)

    for model in models:
        cv_results = cross_validate(
            models[model],
            X_train,
            y_train,
            cv=cv,
            n_jobs=-1,
            scoring=metric,
            return_train_score=True,
        )
        print(
            f"{model}\n{metric} mean train: {cv_results['train_score'].mean():.3f} +/- {cv_results['train_score'].std():.3f}\n{metric} mean test: {cv_results['test_score'].mean():.3f} +/- {cv_results['test_score'].std():.3f}\n"
        )


##############################################CURVA DE APRENDIZAJE################################################################
from sklearn.model_selection import learning_curve


# Función para gráfica la curva de aprendizaje
def plot_learning_curve(
    estimator, title, X, y, ylim=None, cv=None, n_jobs=-1, score=None
):
    """
    Genera una gráfica de la curva de aprendizaje de un estimador dado

    Parámetros
    ----------
    estimator : object
        Estimador a utilizar
    title : string
        Título del gráfico
    X : array-like, shape (n_samples, n_features)
        Conjunto de entrenamiento
    y : array-like, shape (n_samples) or (n_samples, n_features), optional
        Etiquetas
    ylim : tuple, shape (ymin, ymax), optional
        Rango del eje y
    cv : int, cross-validation generator or an iterable, optional
        Estrategia de validación cruzada
    n_jobs : int, optional
        Número de trabajos paralelos a ejecutar (-1 usa todos los procesadores)
    score : string, callable or None, optional, default: None

    Returns
    -------
    train_scores_mean : array-like, shape (n_ticks,)
        Puntajes de entrenamiento promedio
    test_scores_mean : array-like, shape (n_ticks,)
        Puntajes de validación cruzada promedio
    """
    import matplotlib.pyplot as plt
    import numpy as np

    plt.figure()
    plt.title(title)
    if ylim is not None:
        plt.ylim(*ylim)
    plt.xlabel("Training examples")
    plt.ylabel(score)
    train_sizes, train_scores, test_scores = learning_curve(
        estimator, X, y, cv=cv, n_jobs=n_jobs
    )
    train_scores_mean = np.mean(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    plt.grid()

    plt.plot(
        train_sizes,
        train_scores_mean,
        "o-",
        color="r",
        label="Training score",
        lw=2,
        alpha=0.8,
    )
    plt.plot(
        train_sizes,
        test_scores_mean,
        "o-",
        color="g",
        label="Cross-validation score",
        lw=2,
        alpha=0.8,
    )

    plt.legend(loc="best")
    return train_scores_mean, test_scores_mean
