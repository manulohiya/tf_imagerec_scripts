# These are the commands needed to train and test your dataset	

# Run Docker (your path may vary)
# docker run -it -v $HOME/tf_files:/tf_files  gcr.io/tensorflow/tensorflow:latest-devel

# Navigate to tensorflow
# cd /tensorflow

# Retrain your dataset (this may take a few minutes)
# python tensorflow/examples/image_retraining/retrain.py 
# --bottleneck_dir=/tf_files/bottlenecks 
# --how_many_training_steps 500 
# --model_dir=/tf_files/inception 
# --output_graph=/tf_files/retrained_graph.pb 
# --output_labels=/tf_files/retrained_labels.txt 
# --image_dir /tf_files/training_photos/flower_photos

# Test your data set against a new image that the algorithm hasnt seen before
# python /tf_files/scripts/label_image.py /tf_files/testing_photos/flowers/daffodil.jpg


