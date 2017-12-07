import Preprocessing as OCR
import URL as url

#Train the URL Detector
#Create classifier
URL_detector = url.URL_Detector()

#Train the classifier
URL_detector.perform_training('training_text/urls.txt', 'training_text/non_urls.txt')



print(URL_detector.classify_array(OCR.OCR('images/testImage1.png')))
