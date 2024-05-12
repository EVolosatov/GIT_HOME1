import numpy as np
import matplotlib.pyplot as plt

# Создание изображения
img = np.zeros((500, 500, 3), dtype=np.uint8)
for i in range(10):
 img = add_noise(img)

# Отображение изображения жохлых кошек
plt.imshow(img)
plt.axis('off')
plt.title('Котики')
plt.show()
