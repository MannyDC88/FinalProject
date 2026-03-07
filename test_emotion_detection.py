import unittest
from EmotionDetection.emotion_detection import emotion_pred

class Test_Emotion_Analyze(unittest.TestCase):

    def test_emotion(self):

        result_1 = emotion_pred("I am glad this happened")
        self.assertEqual(result_1['dominant_emotion'], 'joy')

        result_2 = emotion_pred("I am really mad about this")
        self.assertEqual(result_2['dominant_emotion'], 'anger')

        result_3 = emotion_pred("I feel disgusted just hearing about this")
        self.assertEqual(result_3['dominant_emotion'], 'disgust')

        result_4 = emotion_pred("I am so sad about this")
        self.assertEqual(result_4['dominant_emotion'], 'sadness')

        result_5 = emotion_pred("I am really afraid that this will happen")
        self.assertEqual(result_5['dominant_emotion'], 'fear')


if __name__ == '__main__':
    unittest.main()