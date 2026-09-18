import numpy as np
import matplotlib.pyplot as plt

class LinearRegressionGD():
    def __init__(self , learning_rate , n_iters):
        self.learning_rate = learning_rate
        self.n_iters = n_iters
        self.theta_0 = 0.0
        self.theta_1 = 0.0
        self.SSE_history = []
        
    def fit(self , x , y):
        n = len(x)
        for _ in range(self.n_iters):
            y_hat = self.theta_0 + self.theta_1*x
            
            error = y_hat - y
            sse = np.sum(error**2)
            self.SSE_history.append(sse)
            
            grad_theta_0 = (2/n)*np.sum(error)
            grad_theta_1 = (2/n)*np.sum(error*x)
            
            self.theta_0 -= self.learning_rate*grad_theta_0
            self.theta_1 -= self.learning_rate*grad_theta_1
            
    def predict(self , x):
        return self.theta_0 + self.theta_1*x    
    
    def plot_training(self , x , y):
        plt.figure(figsize = (12,5))
        plt.subplot(1 , 2 , 1)
        plt.scatter(x, y)              
        y_pred = self.predict(x)      
        plt.plot(x, y_pred)            
        plt.xlabel("Size")
        plt.ylabel("Price")
        
        plt.subplot(1 , 2 , 2)
        plt.plot(range(len(self.SSE_history)) , self.SSE_history)
        plt.xlabel("Iteration")
        plt.ylabel("SSE")
        plt.tight_layout()
        plt.show()
        