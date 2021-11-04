# FEATURE EXTRACTION OF TRAINING ARRAYS
AUTO = tf.data.experimental.AUTOTUNE
def get_features(model_name, data_preprocessor, data):
    '''
    1- Create a feature extractor to extract features from the data.
    2- Returns the extracted features and the feature extractor.

    '''
    dataset = tf.data.Dataset.from_tensor_slices(data)

    # data augmentation
    def preprocess(x):
        x = tf.image.random_flip_left_right(x) 
        return x

    ds = dataset.map(preprocess, num_parallel_calls=AUTO).batch(bath_size)

    input_size = data.shape[1:]
    
    # Prepare pipeline.
    input_layer = Input(input_size)
    preprocessor = Lambda(data_preprocessor)(input_layer)

    base_model = model_name(weights='imagenet', include_top=False,
                 input_shape=input_size)(preprocessor)

    avg = GlobalAveragePooling2D()(base_model)
    feature_extractor = Model(inputs = input_layer, outputs = avg)


    # Extract feature.
    feature_maps = feature_extractor.predict(ds, verbose=1)
    print('Feature maps shape: ', feature_maps.shape)
    
    # deleting variables
    del(feature_extractor, base_model, preprocessor, dataset)
    gc.collect()
    return feature_maps

# FEATURE EXTRACTION OF VALIDAION AND TESTING ARRAYS
def get_valfeatures(model_name, data_preprocessor, data):
    '''
    Same as above except not image augmentations applied.
    Used for feature extraction of validation and testing.
    '''
    dataset = tf.data.Dataset.from_tensor_slices(data)

    ds = dataset.batch(bath_size)

    input_size = data.shape[1:]

    # Prepare pipeline.
    input_layer = Input(input_size)

    preprocessor = Lambda(data_preprocessor)(input_layer)

    base_model = model_name(weights = 'imagenet', include_top = False,
                input_shape = input_size)(preprocessor)
                
    avg = GlobalAveragePooling2D()(base_model)
    feature_extractor = Model(inputs = input_layer, outputs = avg)

    # Extract feature.
    feature_maps = feature_extractor.predict(ds, verbose=1)
    print('Feature maps shape: ', feature_maps.shape)
    return feature_maps

# RETURNING CONCATENATED FEATURES USING MODELS AND PREPROCESSORS
def get_concat_features(feat_func, models, preprocs, array):

    print(f"Beggining extraction with {feat_func.__name__}\n")
    feats_list = []

    for i in range(len(models)):
        
        print(f"\nStarting feature extraction with {models[i].__name__} using {preprocs[i].__name__}\n")
        
        # applying the above function and storing in list
        feats_list.append(feat_func(models[i], preprocs[i], array))

    # features concatenating
    final_feats = np.concatenate(feats_list, axis=-1)
    
    # memory saving
    del(feats_list, array)
    gc.collect()

    return final_feats


# DEFINING models and preprocessors imports 
from keras.applications.xception import Xception, preprocess_input #0.57
xception_preprocessor = preprocess_input

from keras.applications.resnet_v2 import ResNet152V2, preprocess_input 
resnext_preprocessor = preprocess_input


models = [ResNet152V2, Xception]   
preprocs = [resnext_preprocessor, xception_preprocessor] 
# calculating features of the train data
final_train_features = get_concat_features(get_features, models, preprocs, Xarr)
print('Final feature maps shape', final_train_features.shape)

# calculating features of the test data
test_features = get_concat_features(get_valfeatures, models, preprocs, Xtesarr)
print('Final feature maps shape', test_features.shape)
