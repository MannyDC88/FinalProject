from EmotionDetection.emotion_detection import emotion_detection
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        text = "I am glad this happened"
        expected_dominant_emotion = "joy"
        response = emotion_detection(text)
        self.assertEqual(response["dominant_emotion"], expected_dominant_emotion)

unittest.main()