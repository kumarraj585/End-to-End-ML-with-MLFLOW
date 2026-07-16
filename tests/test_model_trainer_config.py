import unittest

from mlProject.config.configuration import ConfigurationManager


class ModelTrainerConfigTest(unittest.TestCase):
    def test_model_trainer_config_reads_elasticnet_params(self):
        config = ConfigurationManager()
        model_config = config.get_model_trainer_config()

        self.assertEqual(model_config.alpha, 0.2)
        self.assertEqual(model_config.l1_ratio, 0.1)
        self.assertEqual(model_config.target_column, "quality")


if __name__ == "__main__":
    unittest.main()
