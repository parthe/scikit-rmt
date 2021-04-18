import numpy as np

class SampleEstimator:

    def estimate(self, X, k=None):
        n, p = X.shape

        if k is None:
            # demean data matrix
            X = X - X.mean(axis=0)
            # subtract one degree of freedom 
            k=1
        # effective sample size
        n=n-k
        # get sample covariance estimator
        self.sigma_tilde = np.matmul(X.T, X)/n
        return self.sigma_tilde



class FSOptEstimator:

    def __init__(self, Sigma):
        self.Sigma = Sigma
        self.sample_est = SampleEstimator()
    
    def estimate(self, X):
        n, p = X.shape

        sample = self.sample_est.estimate(X)

        eigvals, eigvects = np.linalg.eig(sample)
        order = np.argsort(eigvals)
        eigvals = eigvals[order]
        eigvects = eigvects[:,order]

        d_star = np.array([np.matmul(np.matmul(vec, self.Sigma), vec.T) for vec in eigvects.T])

        # compute finite-sample optimal (FSOpt) nonlinear shrinkage estimator
        self.sigma_tilde = np.matmul(np.matmul(eigvects, np.diag(d_star)), eigvects.T)
        return self.sigma_tilde






