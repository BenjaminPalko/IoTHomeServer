import unittest
#
import scripts.devices as devices


class TestPublish(unittest.TestCase):

    def test_rgbled(self):
        # RGBLED Topic
        topic = "nodemcu/rgbled"
        # Create listener client
        # Create rgbled device object
        rgbled = devices.RGBLED(topic)
        # Test Red
        rgbled.update_state(255, 0, 0)
        # Test Green
        rgbled.update_state(0, 255, 0)
        # Test Blue
        rgbled.update_state(0, 0, 255)


if __name__ == '__main__':
    unittest.main()
