from imageai.Classification import ImageClassification
import os

def predict(dsp):
    execution_path = os.getcwd()
    
    if dsp == "MobileNetV2":
        prediction = ImageClassification()
        prediction.setModelTypeAsMobileNetV2()  # Choose your desired algorithm here
        prediction.setModelPath(os.path.join(execution_path+"/ia_pretrained_files/", "mobilenet_v2-b0353104.pth"))  # Path to the model file
        prediction.loadModel()
        
        predictions, probabilities = prediction.classifyImage(os.path.join(execution_path+"/temp/", "image.jpg"), result_count=5)
        for eachPrediction, eachProbability in zip(predictions, probabilities):
            data = (str(eachPrediction) + " : " + str(eachProbability))
            
            with open('temp/prediction_data.txt', 'a+') as data_file:
                data_file.write(data + "\n\n")
        
            
    if dsp == "InceptionV3":
        prediction = ImageClassification()
        prediction.setModelTypeAsInceptionV3()  # Choose your desired algorithm here
        prediction.setModelPath(os.path.join(execution_path+"/ia_pretrained_files/", "inception_v3_google-1a9a5a14.pth"))  # Path to the model file
        prediction.loadModel()
        
        predictions, probabilities = prediction.classifyImage(os.path.join(execution_path+"/temp/", "image.jpg"), result_count=5)
        for eachPrediction, eachProbability in zip(predictions, probabilities):
            data = (str(eachPrediction) + " : " + str(eachProbability))
            
            with open('temp/prediction_data.txt', 'a+') as data_file:
                data_file.write(data + "\n\n")

    if dsp == "DenseNet121":
        prediction = ImageClassification()
        prediction.setModelTypeAsDenseNet121()  # Choose your desired algorithm here
        prediction.setModelPath(os.path.join(execution_path+"/ia_pretrained_files/", "densenet121-a639ec97.pth"))  # Path to the model file
        prediction.loadModel()
        
        predictions, probabilities = prediction.classifyImage(os.path.join(execution_path+"/temp/", "image.jpg"), result_count=5)
        for eachPrediction, eachProbability in zip(predictions, probabilities):
            data = (str(eachPrediction) + " : " + str(eachProbability))
            
            with open('temp/prediction_data.txt', 'a+') as data_file:
                data_file.write(data + "\n\n")