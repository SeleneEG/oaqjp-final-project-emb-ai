import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test1(self):
        text = "I am glad this happened"
        result = emotion_detector(text)
        self.assertEqual(result["dominant_emotion"], "joy")

    def test2(self):
        text = "I am really mad about this"
        result = emotion_detector(text)
        self.assertEqual(result["dominant_emotion"], "anger")

    def test3(self):
        text = "I feel disgusted just hearing about this"
        result = emotion_detector(text)
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test4(self):
        text = "I am so sad about this"
        result = emotion_detector(text)
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test5(self):
        text = "I am really afraid that this will happen"
        result = emotion_detector(text)
        self.assertEqual(result["dominant_emotion"], "fear")

if __name__ == "__main__":
    unittest.main()
