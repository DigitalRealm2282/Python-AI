import tensorflow as tf


X1 = tf.constant([1, 3, 5, 9])
Y1 = tf.constant([4, 3, 5, 10])

SS= tf.add(X1, Y1)

tf.function(print(SS))


