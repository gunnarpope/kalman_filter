# kalman_filter
A library of applications of the Kalman filter

# Definitions

| Variable | Description                                 |   
| ---------|-------------------------------------------- | 
| z  |  (mx1), the input measurement matrix              |
| x  |  (nx1), the output (estimate) of the KF           | 
| xp |  (nx1), the prediction of the output              | 
| P  |  (nxn), the error covariance                      |  
| Pp |  (nxn), the prediction of the error covariance    | 
| A  |  (nxn), state transition matrix                   | 
| H  |  (mxn), state-to-measurement matrix               | 
| K  |  (mx1), the kalman filter gain                    |
| w  |  (nx1), state transition noise                    |
| Q  |  (nxn), covariance matrix of w, the process noise | 
| v  |  (mx1), measurement noise                         |  
| R  |  (mxm), covariance matrix of v                    |

Refer to [Quaternion Kinematics](https://www.iri.upc.edu/people/jsola/JoanSola/objectes/notes/kinematics.pdf) for an excellent outline of variable descriptions.

| Magnitude | True | Nominal | Error | Composition | Measured | Noise | 
| --------- |  --- | ------- | ----- | ----------- | -------- | ----- |
| Full State | $x_t$ | $x$ | $\delta x$ | $x_t = x + \delta x$ | | |
| Position   |  | |  |  | | |
| Velocity   |  | |  |  | | |
| Quaternion |  | |  |  | | |
| Angles     |  | |  |  | | |
| Accel. Bias|  | |  |  | | |
| Gyro.  Bias|  | |  |  | | |
| Gravity Vector|  | |  |  | | |
| Acceleration |  | |  |  | | |
| Angular Rate |  | |  |  | | |

$z=[x, y, a]$ 
