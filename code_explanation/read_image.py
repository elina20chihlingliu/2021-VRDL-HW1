# set training images labels
def set_labeldf():
  header_list = ["img", "breed"]
  labels_df  = pd.read_csv(data_dir + train_txt, sep = " ",names = header_list)  # all the testing images
  train_dir = 'training_images/'
  bird_breeds = sorted(list(set(labels_df['breed'])))
  n_classes = len(bird_breeds)

  class_dict = dict(zip(bird_breeds, range(n_classes)))
  labels_df['file_path'] = labels_df['img'].apply(lambda x:train_dir+f"{x}")
  labels_df['breed'] = labels_df.breed.map(class_dict)
  return labels_df, class_dict
labels_dataframe, class_to_num = set_labeldf()

# function define
def read_trainimg(data):
  X_list = []
  for image in tqdm.tqdm(data):
      # Reading RGB Images
      image_path = data_dir+'/'+image
      print(image_path)
      orig_image = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)
      res_image = cv2.resize(orig_image,(img_size, img_size))
      X_list.append(res_image)
  return X_list


# TEST IMAGES
def read_testimg():
  test_dir = 'testing_images/'
  f.close()
  X_tsls = [] 
  for image in tqdm.tqdm(np.array(test_images)):
    image_path = data_dir+'/'+test_dir+image
    orig_image = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)
    res_image = cv2.resize(orig_image,(img_size, img_size))
    X_tsls.append(res_image)
  return X_tsls


with open(data_dir + test_txt) as f:
      test_images = [x.strip() for x in f.readlines()]  # all the testing images


X_ls = read_trainimg(labels_dataframe['file_path'])
X_test = read_testimg()

# Converting to arrays
Xarr = np.array(X_ls)
Xtesarr = np.array(X_test)

y_train = to_categorical(labels_dataframe.breed)
Y = list(labels_dataframe.breed)


del(X_ls)
gc.collect()
print(Xarr.shape, y_train.shape)

del(X_test)
gc.collect()
print(Xtesarr.shape)
