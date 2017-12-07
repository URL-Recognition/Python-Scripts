# Read input file to get list of strings
def readInput(fileName):
    with open(fileName) as f:
        content = f.readlines()
        f.close()
    content = [x.strip() for x in content]

    return content


# The histogram of letters in a string
def getHistogram(input_str):
    count = len(input_str)
    hist = [0 for i in range(95)]

    # Count char occurrences
    for c in input_str:
        hist[ord(c) - 32] += 1

    return hist


# Get histogram of training set fileName
def trainingHist(fileName):
    data = readInput(fileName)

    hist = [0 for i in range(95)]

    for val in data:
        h = getHistogram(val);
        # Add values from histograms together
        hist = [x + y for x, y in zip(h, hist)]

    return hist


def getSmoothProbabilities(histogram):
    total = sum(histogram) + len(histogram)
    probs = [(i + 1) / total for i in histogram]
    return probs


class URL_Classifier:
    URL_prob = []
    URL_hist = [0 for i in range(95)]
    NonURL_prob = []
    NonURL_hist = [0 for i in range(95)]

    def trainClassifier(self, fileName, isURL):

        training = trainingHist(fileName)
        if isURL:
            self.URL_hist = [x + y for x, y in zip(self.URL_hist, training)]
        else:
            self.NonURL_hist = [x + y for x, y in zip(self.NonURL_hist, training)]

    def setProbabilities(self):
        self.URL_prob = getSmoothProbabilities(self.URL_hist)
        self.NonURL_prob = getSmoothProbabilities(self.NonURL_hist)

    def classify(self, string):

        if (len(self.URL_prob) < 1 or len(self.NonURL_prob) < 1):
            print('The classifier must be trained first!')

        # Calculate probabilities
        url_prob = .5
        not_prob = .5
        for c in string:
            url_prob *= self.URL_prob[ord(c) - 32]
            not_prob *= self.NonURL_prob[ord(c) - 32]

        if (url_prob > not_prob):
            return True
        return False

    def classifyArray(self,stringArray):

        URLS = []
        for string in stringArray:
            isURL = self.classify(string)
            if isURL:
                URLS.append(string)

        return URLS