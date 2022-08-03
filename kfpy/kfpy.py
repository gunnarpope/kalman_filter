""" @brief A linear Kalman Filter (KF) implementation
    @author gunnar pope
    @date   2022-08-02
"""
import numpy as np

class KF():
    def __init__(self, A, H, K, w, Q, v, R, x0, P0):
        self.z       = None  # (mx1), the input measurement matrix
        self.x       = x0    # (nx1), the output (estimate) of the KF
        self.xp      = None  # (nx1), the prediction of the output 
        self.P       = P0    # (nxn), the error covariance
        self.Pp      = None  # (nxn), the prediction of the error covariance
        self.A       = None  # (nxn), state transition matrix 
        self.H       = None  # (mxn), state-to-measurement matrix
        self.K       = None  # (mx1), the kalman filter gain 
        self.w       = None  # (nx1), state transition noise
        self.Q       = None  # (nxn), covariance matrix of w, the process uncertainty/noise
        self.v       = None  # (mx1), measurement noise
        self.R       = None  # (mxm), covariance matrix of v

        # validate the initialization
        self.N       = len(self.z)     # the number of columns of z 
        self.M       = len(self.x)     # the number of columns of x 

        self.is_init = False # set to True if all matrix dimmensions are legit.

    def predict(self):
        pass

    def compute_gain(self):
        pass
    
    def compute_estimate(self):
        pass

    def compute_error_cov(self):
        pass
    

if __name__ == '__main__':
    import unittest

    class TestKF(unittest.TestCase):

        def test_init(self):
            kf = KF()
            self.assertEquals(True, kf.is_init, 'ERROR: Failed to init the KF.')

    unittest.main()    

    

