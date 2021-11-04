EarlyStop_callback = keras.callbacks.EarlyStopping(monitor='val_accuracy', 
                                patience = 10, 
                                restore_best_weights=True,
                                verbose = 0)

my_callback=[EarlyStop_callback]

splits = list(StratifiedKFold(n_splits = 5, shuffle=True, random_state=10).split(final_train_features, Y))

# set lists of trained_models, accuracy, losses
trained_models = []
accuracy = []
losses = []

# Prepare And Train DNN model
for i, (train_idx, valid_idx) in enumerate(splits): 

    print(f"\nStarting fold {i+1}\n")
    x_train_fold = final_train_features[train_idx, :]
    y_train_fold = y_train[train_idx, :]
    x_val_fold = final_train_features[valid_idx]
    y_val_fold = y_train[valid_idx, :]

    dnn = keras.models.Sequential([
        InputLayer(final_train_features.shape[1:]),
        Dropout(0.7),
        Dense(200, activation='softmax')
    ])
    
    optimizer = tf.keras.optimizers.Adam(lr = 0.001) # 0.001
    dnn.compile(optimizer = optimizer, #'adam'
                loss = 'categorical_crossentropy',
                metrics = ['accuracy'])
    print("Training...")
    
    #Train simple DNN on extracted features.
    h = dnn.fit(x_train_fold, y_train_fold,
                batch_size = bath_size, #64
                epochs = 80,
                verbose = 2,
                validation_data = (x_val_fold, y_val_fold),
                callbacks = my_callback)  

    print("Evaluating model ...")
    model_res = dnn.evaluate(x_val_fold, y_val_fold)

    accuracy.append(model_res[1])
    losses.append(model_res[0])
    trained_models.append(dnn)

print('\n CV Score -')
print(f"\nAccuracy - {sum(accuracy)/len(accuracy)}")
print(f"\nLoss - {sum(losses)/len(losses)}")
