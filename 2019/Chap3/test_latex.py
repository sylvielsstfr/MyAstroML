import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['text.usetex'] = True

plt.figure()
ax = plt.subplot(111, polar=True)


plt.savefig('foo.png')  # Works
plt.savefig('foo.jpg')  # Works
plt.savefig('foo.tif')  # Works
# plt.savefig('foo.pdf')  # Fails
# plt.savefig('foo.svg')  # Fails
plt.show()