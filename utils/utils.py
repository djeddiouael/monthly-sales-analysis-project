import numpy as np

def generate_random_sales(min_val, max_val, size):
    """
    Génère des nombres aléatoires pour les ventes
    """
    return np.random.randint(min_val, max_val + 1, size)