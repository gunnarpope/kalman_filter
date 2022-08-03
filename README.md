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
| Quaternion | $q_t$ | $q$ | $\delta q$ | $q_t = q \otimes \delta q$ | | |
| Rotation Matrix | $R_t$ | $R$ | $\delta R$ | $R_t = R \delta R$ | | |
| Angles Vector | | | $\delta \theta$  | $dq = e^{\delta \theta/ 2}$ | | |
| Angles Vector | | | $\delta \theta$  | $dR = e^{\|{\delta \theta}\|}\times$ | | |
| Accel. Bias| $a_{bt}$ | $a_b$ | $\delta a_b$ | $a_{bt}=a_b + \delta a_b$ | | $a_w$ |
| Gyro.  Bias| $\omega_{bt}$ | $\omega_b$ | $\delta \omega_b$ | $\omega_{bt} =\omega_b + \delta \omega_b$ | | $\omega_w$ |
| Gravity Vector | $g_{t}$ | $g$ | $\delta g$ | $g_{t}=g + \delta g$ | | |
| Acceleration   | $a_t$ | | |  | $a_m$| $a_n$ |
| Angular Rate   | $\omega_t$ | | |  | $\omega_m$| $\omega_n$ |

# Kinematic Equations
$$\dot{p}_t = v_t$$
$$\dot{v}_t = a_t$$
$$\dot{q}_t = \frac{1}{2} q_t \otimes \omega_t$$
$$\dot{a}_{bt} = a_w$$
$$\dot{\omega}_{bt} = \omega_w$$
$$\dot{g}_t = 0$$

The noise in measurments of accel and gyro can be modeled as:
$$ a_m = R^{\intercal}_{t}(a_t - g_t) + a_{bt} + a_n$$
$$ \omega_m = \omega_t + \omega_{bt} + \omega_n$$

After inverting the measurement equation...
$$ a_t = R_t(a_m - a_{bt} - a_n) + g_t$$
$$ \omega_t = \omega_m - \omega_{bt} - \omega_n$$

The final substitution reveals the final kinematic system:
$$\dot{p}_t = v_t$$
$$\dot{v}_t = R_t(a_m - a_{bt} - a_n) + g_t$$
$$\dot{q}_t = \frac{1}{2} q_t \otimes (\omega_m - \omega_{bt} - \omega_n)$$
$$\dot{a}_{bt} = a_w$$
$$\dot{\omega}_{bt} = \omega_w$$
$$\dot{g}_t = 0$$

The final system state, $x_t$ becomes:
$$x_t = 
\begin{bmatrix}
p_t \\
v_t \\
q_t \\
a_{bt} \\
\omega_{bt} \\
g_t 
\end{bmatrix}
$$

IMU noise readings, $u_m$, are:
$$ u = 
\begin{bmatrix}
a_m - a_n \\
\omega_m - \omega_n
\end{bmatrix}
$$

The white Gaussian noise, $w$ is:
$$w=
\begin{bmatrix}
a_w \\
\omega_w
\end{bmatrix}
$$

## Discrete time kinematics

$$ p \leftarrow p + v \Delta t + \frac{1}{2}(R(a_m - a_b)+g) \Delta t^2$$
$$ v \leftarrow v + (R(a_m - a_b)+g) \Delta t$$
$$ q \leftarrow q \otimes q{(\omega_m - \omega_b)\delta t}$$
$$ a_b \leftarrow a_b$$
$$ w_b \leftarrow w_b$$
$$ g   \leftarrow g$$

where $\leftarrow$ is the time update $x_{k+1} = f(x_k)$


