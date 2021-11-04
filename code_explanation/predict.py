
def predict(models, test_fea):
  y_pred_norm = models[0].predict(test_fea, batch_size = bath_size)/3
  for dnn in models[1:]:
      y_pred_norm += dnn.predict(test_fea, batch_size = bath_size)/3
  
  dict2 = {value:key for key, value in class_to_num.items()}
  pred_codes = np.argmax(y_pred_norm, axis = 1)
  result = pd.Series(pred_codes).map(dict2)
  return result

answer = predict(trained_models, test_features)
print(answer)

submission = np.array(pd.concat([pd.Series(test_images), answer], axis=1))
np.savetxt(data_dir+'/answer.txt', submission, fmt='%s')



