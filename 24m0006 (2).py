import numpy as np 
import matplotlib.pyplot as plt
  

xi=np.linspace(0,1,101) # 101 grid points in xi-direction  
eta=np.linspace(0,1,81)  # 81 grid points in eta-direction 
XI, ETA=np.meshgrid(xi,eta) # Generating the computational grid 

# Transfinite Interpolation mapping
X=(1+19*ETA)*(np.cos(2*(np.pi)*XI))
Y=(0.5*(1-ETA)+20*ETA)*np.sin(2*(np.pi)*XI)

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(X,Y, 'b', linewidth=0.5)
plt.plot(X.T,Y.T, 'b-', linewidth=0.5)
plt.title("Physical  Domain (X, Y)")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.axis("equal")

plt.subplot(1, 2, 2)
plt.plot(XI,ETA, 'b-', linewidth=0.5)
plt.plot(XI.T,ETA.T, 'b-', linewidth=0.5)
plt.title("Computational Domain (ξ, η)")
plt.xlabel("ξ")
plt.ylabel("η")
plt.grid(True)
plt.show()
