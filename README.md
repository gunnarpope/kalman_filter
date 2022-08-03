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
| Position   | $p_t$ | $p$ | $\delta p$ | $p_t = p + \delta p$ | | |
| Velocity | $v_t$ | $v$ | $\delta v$ | $v_t = v + \delta v$ | | |
| Quaternion | $q_t$ | $q$ | $\delta q$ | $q_t = q \bigotimes \delta q$ | | |
| Rotation Matrix | $R_t$ | $R$ | $\delta R$ | $R_t = R \delta R$ | | |
| Angles Vector | | | $\delta \theta$  | $dq = e^{\delta \theta/ 2}$ | | |
| Angles Vector | | | $\delta \theta$  | $dR = e^{\|{\delta \theta}\|}\times$ | | |
| Accel. Bias| $a_{bt}$ | $a_b$ | $\delta a_b$ | $a_{bt}=a_b + \delta a_b$ | | $a_w$ |
| Gyro.  Bias| $\omega_{bt}$ | $\omega_b$ | $\delta \omega_b$ | $\omega_{bt} =\omega_b + \delta \omega_b$ | | $\omega_w$ |
| Gravity Vector | $g_{t}$ | $g$ | $\delta g$ | $g_{t}=g + \delta g$ | | |
| Acceleration   | $a_t$ | | |  | $a_m$| $a_n$ |
| Angular Rate   | $\omega_t$ | | |  | $\omega_m$| $\omega_n$ |
