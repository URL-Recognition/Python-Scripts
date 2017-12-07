class URL_Detector:

    CHARACTER_RANGE = [0,255]
    BIN_SIZE = CHARACTER_RANGE[1]-CHARACTER_RANGE[0]
    URL_prob = []
    URL_hist = [0 for i in range(BIN_SIZE)]
    NonURL_prob = []
    NonURL_hist = [0 for i in range(BIN_SIZE)]

    # Read input file to get list of strings
    def read_input(self, filename):
        with open(filename) as f:
            content = f.readlines()
            f.close()
        content = [x.strip() for x in content]

        return content

    # The histogram of letters in a string
    def get_histogram(self, input_str):
        hist = [0 for i in range(self.BIN_SIZE)]

        # Count char occurrences
        for c in input_str:
            hist[ord(c)] += 1

        return hist

    # Get histogram of training set fileName
    def training_hist(self, filename):
        data = self.read_input(filename)

        hist = [0 for i in range(self.BIN_SIZE)]

        for val in data:
            h = self.get_histogram(val)
            # Add values from ›
            hist = [x + y for x, y in zip(h, hist)]

        return hist

    def calc_probabilities(self, histogram):
        total = sum(histogram) + len(histogram)
        probs = [(i + 1) / total for i in histogram]
        return probs

    def train_classifier(self, filename, is_url):

        training = self.training_hist(filename)
        if is_url:
            self.URL_hist = [x + y for x, y in zip(self.URL_hist, training)]
        else:
            self.NonURL_hist = [x + y for x, y in zip(self.NonURL_hist, training)]

    def set_probabilities(self):
        self.URL_prob = self.calc_probabilities(self.URL_hist)
        self.NonURL_prob = self.calc_probabilities(self.NonURL_hist)

    def perform_training(self,url_file,non_url_file):
        self.train_classifier(url_file,True)
        self.train_classifier(non_url_file,False)
        self.set_probabilities()

    def classify(self, string):

        if len(self.URL_prob) < 1 or len(self.NonURL_prob) < 1:
            print('The classifier must be trained first!')

        # Calculate probabilities
        url_prob = .5
        not_prob = .5
        for c in string:
            url_prob *= self.URL_prob[ord(c) - self.CHARACTER_RANGE[0]]
            not_prob *= self.NonURL_prob[ord(c) - self.CHARACTER_RANGE[0]]

        return url_prob - not_prob
        
    def classify_array(self,strings):
        
        urls = []
        
        for string in strings:
            prob = self.classify(string)
            if prob > 0:
                urls.append(string)
        
        return urls
